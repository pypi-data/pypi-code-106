import sys
from functools import wraps
from typing import Callable

import faust
import sentry_sdk
from faust.types import AgentT
from mode.utils.times import Seconds

__all__ = ['FaustIntegration', ]


def reraise(err_value, traceback=None):
    if err_value.__traceback__ is not traceback:
        raise err_value.with_traceback(traceback)
    raise err_value


def patch_crash():
    old_crash = faust.App.crash

    async def sentry_patched_crash(
        self,
        reason: BaseException
    ) -> None:
        sentry_sdk.capture_exception(reason)
        return await old_crash(self, reason)

    faust.App.crash = sentry_patched_crash


def patch_agent():
    old_on_agent_error = faust.App._on_agent_error  # noqa

    async def sentry_patched_on_agent_error(
        self,
        agent: AgentT,
        exc: BaseException
    ) -> None:
        sentry_sdk.capture_exception(exc)
        return await old_on_agent_error(self, agent, exc)

    faust.App._on_agent_error = sentry_patched_on_agent_error


def patch_timer():
    old_timer = faust.App.timer

    def sentry_patched_timer(
        self,
        interval: Seconds,
        on_leader: bool = False,
        traced: bool = True,
        name: str = None,
        max_drift_correction: float = 0.1
    ) -> Callable:

        def _inner(fun):
            @wraps(fun)
            async def around_timer(*args):
                try:
                    await fun(*args)
                except Exception as e:
                    sentry_sdk.capture_exception(e)
                    _, exc_value, traceback = sys.exc_info()
                    reraise(exc_value, traceback)

            return old_timer(self, interval, on_leader, traced, name, max_drift_correction)(around_timer)
        return _inner

    faust.App.timer = sentry_patched_timer


class FaustIntegration(sentry_sdk.integrations.Integration):
    identifier = "faust"

    @staticmethod
    def setup_once():
        patch_timer()
        patch_agent()
        patch_crash()
