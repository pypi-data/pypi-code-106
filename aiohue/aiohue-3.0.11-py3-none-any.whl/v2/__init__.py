"""Control a Philips Hue bridge with V2 API."""
from __future__ import annotations

import asyncio
import logging
import time
from contextlib import asynccontextmanager
from types import TracebackType
from typing import Callable, Generator, List, Optional, Type

import aiohttp
from aiohttp import ClientResponse
from aiohue.v2.models.clip import LOGGER, CLIPResource
from asyncio_throttle import Throttler

from ..errors import BridgeBusy, Unauthorized, raise_from_error
from .controllers.config import ConfigController
from .controllers.devices import DevicesController
from .controllers.events import EventCallBackType, EventStream, EventType
from .controllers.groups import GroupsController
from .controllers.lights import LightsController
from .controllers.scenes import ScenesController
from .controllers.sensors import SensorsController

MAX_RETRIES = 25  # how many times do we retry on a 503 (bridge overload/rate limit)
THROTTLE_CONCURRENT_REQUESTS = 2  # how many concurrent requests to the bridge
THROTTLE_TIMESPAN = 0.25  # timespan/period (in seconds) for the rate limiting


class HueBridgeV2:
    """Control a Philips Hue bridge with V2 API."""

    def __init__(
        self,
        host: str,
        app_key: str,
        websession: aiohttp.ClientSession | None = None,
    ) -> None:
        """
        Initialize the Bridge instance.

        Parameters:
            `host`: the hostname or IP-address of the bridge as string.
            `app_key`: provide the hue appkey/username for authentication.
            `websession`: optionally provide a aiohttp ClientSession.
        """
        self._host = host
        self._app_key = app_key
        self._websession = websession
        self._websession_provided = websession is not None

        self.logger = logging.getLogger(f"{__package__}[{host}]")
        self._events = EventStream(self)
        # all resource controllers
        self._config = ConfigController(self)
        self._devices = DevicesController(self)
        self._lights = LightsController(self)
        self._scenes = ScenesController(self)
        self._groups = GroupsController(self)
        self._sensors = SensorsController(self)
        # Setup the Throttler/rate limiter for requests to the bridge.
        # NOTE: The EventStream also counts for 1 connection to the bridge.
        self._throttler = Throttler(
            rate_limit=THROTTLE_CONCURRENT_REQUESTS, period=THROTTLE_TIMESPAN
        )
        self._disconnect_timestamp = 0

    @property
    def bridge_id(self) -> str | None:
        """Return the ID of the bridge we're currently connected to."""
        return self._config.bridge_id

    @property
    def host(self) -> str:
        """Return the hostname of the bridge."""
        return self._host

    @property
    def events(self) -> EventStream:
        """Return the EventStream controller."""
        return self._events

    @property
    def config(self) -> ConfigController:
        """Get the Config Controller with config-like resources."""
        return self._config

    @property
    def devices(self) -> DevicesController:
        """Get the Devices Controller for managing all device resources."""
        return self._devices

    @property
    def lights(self) -> LightsController:
        """Get the Lights Controller for managing all light resources."""
        return self._lights

    @property
    def scenes(self) -> ScenesController:
        """Get the Scenes Controller for managing all scene resources."""
        return self._scenes

    @property
    def groups(self) -> GroupsController:
        """Get the Groups Controller for managing all group resources."""
        return self._groups

    @property
    def sensors(self) -> SensorsController:
        """Get the Sensors Controller for managing all sensor resources."""
        return self._sensors

    async def initialize(self) -> None:
        """Initialize the connection to the bridge and fetch all data."""
        # Initialize all HUE resource controllers
        # fetch complete full state once and distribute to controllers
        await self.fetch_full_state()
        # start event listener
        await self._events.initialize()
        # subscribe to reconnect event
        self._events.subscribe(
            self._handle_connect_event, (EventType.RECONNECTED, EventType.DISCONNECTED)
        )

    async def close(self) -> None:
        """Close connection and cleanup."""
        await self.events.stop()
        if not self._websession_provided:
            await self._websession.close()
        self.logger.info("Connection to bridge closed.")

    def subscribe(
        self,
        callback: EventCallBackType,
    ) -> Callable:
        """
        Subscribe to status changes for all resources.

        Returns:
            function to unsubscribe.
        """
        unsubscribes = [
            self.config.subscribe(callback),
            self.devices.subscribe(callback),
            self.groups.subscribe(callback),
            self.lights.subscribe(callback),
            self.scenes.subscribe(callback),
            self.sensors.subscribe(callback),
        ]

        def unsubscribe():
            for unsub in unsubscribes:
                unsub()

        return unsubscribe

    async def request(self, method: str, path: str, **kwargs) -> dict | List[dict]:
        """Make request on the api and return response data."""
        # The bridge will rate limit if we send more requests than about 2-5 per second
        # we guard ourselves from hitting the rate limit by using a throttler
        # but others apps/services are hitting the Hue bridge too so we still
        # might hit the rate limit/overload at some point so we also retry if this happens.
        retries = 0

        while retries < MAX_RETRIES:
            retries += 1

            if retries > 1:
                retry_wait = 0.25 * retries
                LOGGER.debug(
                    "Got 503 error from Hue bridge, retry request in %s seconds",
                    retry_wait,
                )
                await asyncio.sleep(retry_wait)

            async with self._throttler, self.create_request(
                method, path, **kwargs
            ) as resp:
                # 503 means the bridge is rate limiting/overloaded, we should back off a bit.
                if resp.status == 503:
                    continue
                if resp.status == 403:
                    raise Unauthorized
                # raise on all other error status codes
                resp.raise_for_status()
                result = await resp.json()
                if result.get("errors"):
                    raise_from_error(result["errors"][0])
                return result["data"]

        raise BridgeBusy(
            f"{retries} requests to the bridge failed, "
            "its probably overloaded. Giving up."
        )

    @asynccontextmanager
    async def create_request(
        self, method: str, path: str, **kwargs
    ) -> Generator[ClientResponse, None, None]:
        """
        Make a request to any path with V2 request method (auth in header).

        Returns a generator with aiohttp ClientResponse.
        """
        if self._websession is None:
            self._websession = aiohttp.ClientSession()

        url = f"https://{self._host}/{path}"

        kwargs["ssl"] = False

        if "headers" not in kwargs:
            kwargs["headers"] = {}

        kwargs["headers"]["hue-application-key"] = self._app_key

        async with self._websession.request(method, url, **kwargs) as res:
            yield res

    async def __aenter__(self) -> "HueBridgeV2":
        """Return Context manager."""
        await self.initialize()
        return self

    async def __aexit__(
        self,
        exc_type: Type[BaseException],
        exc_val: BaseException,
        exc_tb: TracebackType,
    ) -> Optional[bool]:
        """Exit context manager."""
        await self.close()
        if exc_val:
            raise exc_val
        return exc_type

    async def _handle_connect_event(
        self, type: EventType, item: CLIPResource | None
    ) -> None:
        """Handle (disconnect) event from the EventStream."""
        if type == EventType.DISCONNECTED:
            # If we receive a disconnect event, we store the timestamp
            self._disconnect_timestamp = time.time()
        elif type == EventType.RECONNECTED:
            # if the time between the disconnect and reconnect is more than 1 minute,
            # we fetch the full state.
            if (time.time() - self._disconnect_timestamp) > 60:
                await self.fetch_full_state()

    async def fetch_full_state(self) -> None:
        """Fetch state on all controllers."""
        full_state = await self.request("get", "clip/v2/resource")
        await asyncio.gather(
            self._config.initialize(full_state),
            self._devices.initialize(full_state),
            self._lights.initialize(full_state),
            self._scenes.initialize(full_state),
            self._sensors.initialize(full_state),
            self._groups.initialize(full_state),
        )
