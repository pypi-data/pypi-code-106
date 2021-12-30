import contextlib
import os
from httpx import AsyncClient, Timeout, HTTPStatusError, HTTPError, Response, NetworkError
import json
from sentry_sdk import capture_message
from http.client import HTTPException
from sentry_sdk import capture_exception


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
            try:
                res = await client.get(url=self.url)
                res.raise_for_status()

            except HTTPError as e:
                res = self.create_error_response(e)

            return res


    @staticmethod
    def create_error_response(e: any) -> Response:
        status_code = 500
        if hasattr(e, "response"):
            message = e.response.text
            status_code = e.response.status_code
            if status_code <= 500:
                event_id = "no_id"
            else:
                event_id = capture_exception(e)
        else:
            event_id = capture_exception(e)
            message = str(e)

        return Response(
            status_code=status_code,
            json={"message": message, "sentry_event_id": event_id},
        )
