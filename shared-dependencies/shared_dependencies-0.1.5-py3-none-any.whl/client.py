import contextlib
import os
from httpx import AsyncClient, Timeout, HTTPStatusError, HTTPError, Response, NetworkError
import json
from sentry_sdk import capture_message
from http.client import HTTPException
from sentry_sdk import init, capture_exception
from sentry_sdk.integrations.pure_eval import PureEvalIntegration


# SENTRY_DSN, SENTRY_ENVIRONMENT are caught in parent app variables when not specified
# Must be init in the parent app
def init_sentry(sentry_integrations: list, traces_sample_rate: float, sample_rate: float):
    return init(
        integrations=sentry_integrations,
        traces_sample_rate=traces_sample_rate,
        sample_rate=sample_rate
    )

class CustomHttpRequest:
    def __init__(self, url, timeout = 60.0, *args, **kwargs):
        self.url = url
        self.timeout = timeout
        self.client = self.get_client(*args, **kwargs)


    @contextlib.asynccontextmanager
    async def get_client(self, *args, **kwargs):
        async with AsyncClient(
                *args, timeout=Timeout(self.timeout, connect=self.timeout), **kwargs
        ) as client:
            yield client


    async def request_url(self) -> Response:
        async with self.client as client:
            status_code = 500
            try:
                res = await client.get(url=self.url)
                res.raise_for_status()

            except HTTPStatusError as e:
                status_code = e.response.status_code
                res = self.create_error_response(status_code, e.response.text, "no_id")

            except HTTPError as e:
                event_id = str(capture_exception(e))
                print(f"event_id : {event_id}")
                message = str(e)
                res = self.create_error_response(status_code, message, event_id)

            return res


    @staticmethod
    def create_error_response(status_code: int, message: str, event_id: str) -> Response:
        return Response(
            status_code=status_code,
            json={"message": message, "sentry_event_id": event_id},
        )
