"""ASGI interface for electrostatic

Provides an ASGI implementation of electrostatic.
The implementation is designed to be used either as a standalone application,
or as a "middleware" (wrapping another ASGI application).
"""

import asyncio
import logging
from os.path import normpath
from typing import Any, Dict, Iterable, List, Optional, Tuple, cast

from asgiref.compatibility import guarantee_single_callable
from asgiref.typing import (
    ASGI3Application,
    ASGIApplication,
    ASGIReceiveCallable,
    ASGISendCallable,
    HTTPResponseBodyEvent,
    HTTPResponseStartEvent,
    HTTPScope,
    Scope,
)

from .assets import BaseAsset, BaseAssetFinder
from .utils import PrefixMatcher

logger = logging.getLogger(__name__)


class NotHandledError(NotImplementedError):
    """An ASGI request was not able to be handled by our application"""

    pass


def normalize_prefix(prefix: str) -> str:
    """Normalize a url prefix so it matches correctly"""

    if prefix.endswith("/"):
        prefix = "/".join(x for x in prefix.split("/") if x) + "/"
    else:
        prefix = "/".join(x for x in prefix.split("/") if x)

    if prefix == "/":
        return ""

    return "/" + prefix


class Electrostatic:
    """Electrostatic

    ASGI application or middleware to serve static files
    """

    _wrapped_app: Optional[ASGI3Application]
    finders: PrefixMatcher[BaseAssetFinder]
    not_found_asset: Optional[BaseAsset]

    def __init__(
        self,
        application: Optional[ASGIApplication] = None,
        *,
        finders: Optional[Dict[str, BaseAssetFinder]] = None,
        finder: Optional[BaseAssetFinder] = None,
        prefix: str = "/",
        not_found: Optional[str] = None,
        pass_through_not_found: bool = False,
    ) -> None:
        """Create an ASGI application or middleware to serve static files

        Args:
            application:    if specified, act as a middleware and pass requests through if no file is found
            finders:        a dictionary of prefixes and Finders for each prefix
            finder:         a Finder for the default prefix; can be used in combination with or instead of finders
            prefix:         the default prefix, used mostly with the finder parameter as a shorthand form
            not_found:      the asset path of a 404 page to use
            pass_through_not_found: if an asset is not found on a matched prefix, pass through to the wrapped app

        For example, a common way to use with Django would be:

            django_app = get_asgi_application()
            app = Electrostatic(django_app, finder=DjangoAssetFinder())
        """

        logger.debug("Instantiating Electrostatic application")

        if finders is None:
            finders = {}
        if finder is not None:
            finders[prefix] = finder

        if len(finders) == 0:
            raise RuntimeError(
                "Electrostatic requires an asset finder passed via finder or finders parameter"
            )

        # Convert the finders to a PrefixMatcher
        self.finders = PrefixMatcher(
            [(normalize_prefix(k), v) for k, v in finders.items()]
        )

        self.ready = asyncio.Event()
        self.stopping = asyncio.Event()

        # We have two "modes":
        # 1. as a middleware, passing unhandled requests to another application
        # 2. as an application, returning 404 or raising an exception for handled requests
        if application:
            # Makes sure an ASGI2 app is converted to ASGI3 protocol first
            self._wrapped_app = guarantee_single_callable(application)
        else:
            self._wrapped_app = None

        if self._wrapped_app and pass_through_not_found:
            # Pass through to the wrapped application for not-found assets
            # This lets you do things like serve static assets from /, and pass through to the
            # API backend on any requests to /api, for example.
            self.not_found_asset = None
        else:
            self.not_found_asset = self.find_asset(not_found) if not_found else None

    def find_asset(self, url) -> Optional[BaseAsset]:
        """Use the PrefixMatcher to determine the Finders to call, and look for an asset"""

        # Iterate through matching Finders, longest prefix first. Each finder will either:
        # 1. Find an asset and return it
        # 2. Fail to find an asset, but return a 404 asset instead.
        # 3. Return None, in which case move on to the next finder.
        for prefix, finder in reversed(list(self.finders.prefix_matches(url))):
            # Call the finder, passing in the url (minus the prefix)
            # Pass the prefix as a kwarg; finders will generally ignore but might
            # be useful to them sometimes.
            asset = finder(url[len(prefix) :], prefix=prefix)
            if asset is not None:
                return asset

        return None

    async def send_zerocopy(
        self,
        send: ASGISendCallable,
        *,
        status: int,
        fd: int,
        headers: Optional[Iterable[Tuple[bytes, bytes]]] = None,
    ) -> None:
        if headers is None:
            headers = []
        # cast() because of https://github.com/python/mypy/issues/8533:
        await send(
            cast(
                HTTPResponseStartEvent,
                {"type": "http.response.start", "status": status, "headers": headers},
            )
        )

        # We assume here that scope['extensions']['http.response.zerocopysend'] is present
        # IOW don't call send_response with a 'fd' parameter unless you know zerocopysend is supported
        # This is an ASGI extension, and it is not compliant to any asgiref event types, hence the typing ignore
        await send(
            {  # type: ignore
                "type": "http.response.zerocopysend",
                "file": fd,
                "more_body": False,
            }
        )

    async def send_response(
        self,
        send: ASGISendCallable,
        *,
        status: int,
        body: Iterable[bytes],
        headers: Optional[List[Tuple[bytes, bytes]]] = None,
    ) -> None:
        if headers is None:
            headers = []
        # cast() because of https://github.com/python/mypy/issues/8533:
        await send(
            cast(
                HTTPResponseStartEvent,
                {"type": "http.response.start", "status": status, "headers": headers},
            )
        )

        # Iterate through chunks; doing it this way makes sure that even if we're reading in and sending
        # a huge file, we won't stop the async world (event loop) while we process it.
        for chunk in body:
            # cast() because of https://github.com/python/mypy/issues/8533:
            await send(
                cast(
                    HTTPResponseBodyEvent,
                    {
                        "type": "http.response.body",
                        "body": chunk,
                        "more_body": True,
                    },
                )
            )
        # cast() because of https://github.com/python/mypy/issues/8533:
        await send(
            cast(
                HTTPResponseBodyEvent,
                {
                    "type": "http.response.body",
                    "more_body": False,
                },
            )
        )

    async def send_asset(
        self,
        send: ASGISendCallable,
        *,
        asset: BaseAsset,
        status: Optional[int] = None,
        zero_copy: bool = False,
    ):
        if status is None:
            status = asset.status
        if zero_copy and asset.fd is not None:
            # use context manager so that (as per ASGI spec) the file descriptor
            # is closed after zerocopy is done with it and we're returning
            with asset.fd as fd:
                return await self.send_zerocopy(
                    send, status=status, fd=fd.fileno(), headers=asset.headers
                )
        else:
            return await self.send_response(
                send, status=status, body=asset.body(), headers=asset.headers
            )

    async def receive_request(self, receive: ASGIReceiveCallable):
        body = b""
        while True:
            message = await receive()
            if message["type"] != "http.request":
                raise ValueError(f"Unexpected http event '{message['type']}'")
            body += message.get("body", b"")
            if not message.get("more_body", False):
                return body

    async def send_not_found(
        self, scope, receive: ASGIReceiveCallable, send: ASGISendCallable
    ) -> None:
        # Receive (and ignore) any body
        await self.receive_request(receive)
        if scope["method"] not in {"GET", "HEAD"}:
            # Nothing fancy here; just flat out reject non-GET requests
            return await self.send_response(
                send,
                status=405,
                body=[b"Method not allowed"],
                headers=[
                    (b"Accept", b"GET,HEAD"),
                ],
            )
        if self.not_found_asset is not None:
            # If there is a 404.html file, return that
            return await self.send_asset(
                send,
                asset=self.not_found_asset,
                status=404,
            )
        elif self._wrapped_app:
            raise NotHandledError("Passing through to wrapped application")
        else:
            # otherwise, just send a plain 404
            return await self.send_response(send, status=404, body=[b"Page not found"])

    async def handle_http(
        self, scope: HTTPScope, receive: ASGIReceiveCallable, send: ASGISendCallable
    ) -> None:
        try:
            asset = self.find_asset(normpath(scope["path"]))
        except KeyError:
            asset = None
            # No matching prefix; if there is a wrapped app, pass the whole request to it
            if self._wrapped_app is not None:
                raise NotHandledError("Passing through to wrapped application")
        if asset is not None:
            # Receive any request body, even though only an empty one is intended to
            # be sent with a GET. In any case, we'll just throw it away.
            await self.receive_request(receive)
            if scope["method"] not in {"GET", "HEAD"}:
                # Nothing fancy here; just flat out reject non-GET requests
                return await self.send_response(
                    send,
                    status=405,
                    body=[b"Method not allowed"],
                    headers=[
                        (b"Accept", b"GET,HEAD"),
                    ],
                )
            else:
                # Serve the actual file.
                # First, check if we support zerocopysend; if so, and the asset has a fd, send it.
                # Otherwise just send the asset as chunks (an iterable of bytes)
                # Note: typing cast() due to extensions having weird type of Dict[object, object] (wtf)
                can_zero_copy = "http.response.zerocopysend" in cast(
                    Dict[str, Any], scope.get("extensions", {})
                )
                return await self.send_asset(
                    send,
                    asset=asset,
                    zero_copy=can_zero_copy,
                )

        # If we get here, we had a matching prefix, but no asset was found.
        # Should probably make the behaviour configurable, but right now we send the configured
        # not-found asset (or just a simple 404 message if none configured)
        return await self.send_not_found(scope, receive, send)

    async def handle_lifespan(
        self, scope: Scope, receive: ASGIReceiveCallable, send: ASGISendCallable
    ) -> None:
        # Would be good to support this later, so that we can run startup() here...but
        # it is complicated, as we would want to transparently pass through to the wrapped_app
        # as well, and this is a little complicated to implement
        raise NotHandledError("Lifespan support not currently implemented")

    async def startup(self):
        """Run startup, mostly involves initializing any asset finders we have attached"""
        for finder in self.finders.values():
            finder.startup()
        self.ready.set()

    async def __call__(
        self, scope: Scope, receive: ASGIReceiveCallable, send: ASGISendCallable
    ) -> None:
        logger.debug("Received connection open: %r", scope)

        # If we were using lifespan protocol, we'd do this as part of the lifespan startup
        # Instead, we just do it the first time we get called. That's possibly sub-optimal;
        # it'll slow down our first request...
        if not self.ready.is_set():
            await self.startup()

        try:
            if scope["type"] == "http":
                return await self.handle_http(scope, receive, send)
            elif scope["type"] == "lifespan":
                return await self.handle_lifespan(scope, receive, send)
            else:
                raise NotHandledError(f"Scope type '{scope['type']} not supported.")
        except NotHandledError:
            # If any of our code raises a NotHandled error, attempt to pass through to the wrapped application if
            #  it exists, otherwise just raise the exception so that the ASGI server calling us knows.
            if self._wrapped_app is not None:
                return await self._wrapped_app(scope, receive, send)
            else:
                raise
