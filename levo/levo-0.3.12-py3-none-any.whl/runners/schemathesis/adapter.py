from typing import Dict, List

from levo_commons import events
from levo_commons.models import Interaction, Request, Response, Status
from schemathesis.failures import RequestTimeout
from schemathesis.models import Status as SeStatus
from schemathesis.runner import events as se

from .models import (
    AfterExecutionPayload,
    BeforeExecutionPayload,
    FinishedPayload,
    InitializedPayload,
    SerializedCheck,
    SerializedError,
    SerializedTestResult,
)

STATUS_MAP = {
    SeStatus.success: Status.success,
    SeStatus.error: Status.error,
    SeStatus.failure: Status.failure,
}


def _convert_status(status: SeStatus) -> Status:
    if STATUS_MAP[status]:
        return STATUS_MAP[status]
    return Status.error


def _convert_initialized(
    event: se.Initialized,
) -> events.Initialized[InitializedPayload]:
    return events.Initialized(
        start_time=event.start_time,
        payload=InitializedPayload(
            operations_count=event.operations_count,
            location=event.location,
            base_url=event.base_url,
            specification_name=event.specification_name,
        ),
    )


def _convert_before_execution(
    event: se.BeforeExecution,
) -> events.BeforeTestCaseExecution[BeforeExecutionPayload]:
    return events.BeforeTestCaseExecution(
        payload=BeforeExecutionPayload(
            correlation_id=event.correlation_id,
            method=event.method,
            relative_path=event.relative_path,
            verbose_name=event.verbose_name,
            recursion_level=event.recursion_level,
        ),
    )


def _get_duration(check) -> int:
    if isinstance(check.context, RequestTimeout):
        return check.context.timeout
    if check.response is not None:
        return int(check.response.elapsed * 1000)
    # Practically not possible as the request timeout is the only case when response is absent
    raise ValueError("Can not detect check duration")


def _convert_after_execution(
    event: se.AfterExecution,
) -> events.AfterTestCaseExecution[AfterExecutionPayload]:
    checks_by_name: Dict[str, List[SerializedCheck]] = {}
    for interaction in event.result.interactions:
        for check in interaction.checks:
            container = checks_by_name.setdefault(check.name, [])
            container.append(_convert_check(check, interaction))
    return events.AfterTestCaseExecution(
        payload=AfterExecutionPayload(
            method=event.method,
            relative_path=event.relative_path,
            status=_convert_status(event.status),
            elapsed_time=event.elapsed_time,
            correlation_id=event.correlation_id,
            result=SerializedTestResult(
                verbose_name=event.result.verbose_name,
                has_failures=event.result.has_failures,
                has_errors=event.result.has_errors,
                is_errored=event.result.is_errored,
                seed=event.result.seed,
                data_generation_method=event.result.data_generation_method,
                checks_by_name=checks_by_name,
                checks=[
                    SerializedCheck(
                        name=check.name,
                        value=check.value,
                        response=Response(
                            method=check.request.method,
                            uri=check.request.uri,
                            body=check.response.body,
                            encoding=check.response.encoding,
                            status_code=check.response.status_code,
                            http_version=check.response.http_version,
                            message=check.response.message,
                            headers=check.response.headers,
                        )
                        if check.response is not None
                        else None,
                        request=Request(
                            body=check.request.body,
                            method=check.request.method,
                            uri=check.request.uri,
                            headers=check.request.headers,
                        )
                        if check.request is not None
                        else None,
                        example=check.example,
                        message=check.message,
                        duration=_get_duration(check),
                    )
                    for check in event.result.checks
                ],
                errors=[
                    SerializedError(
                        exception=error.exception,
                        exception_with_traceback=error.exception_with_traceback,
                        example=error.example,
                        title=error.title,
                    )
                    for error in event.result.errors
                ],
                interactions=[
                    Interaction(
                        request=Request(
                            method=interaction.request.method,
                            uri=interaction.request.uri,
                            body=interaction.request.body,
                            headers=interaction.request.headers,
                        ),
                        response=Response(
                            method=check.request.method,
                            uri=check.request.uri,
                            body=interaction.response.body,
                            status_code=interaction.response.status_code,
                            message=interaction.response.message,
                            headers=interaction.response.headers,
                            http_version=interaction.response.http_version,
                            encoding=interaction.response.encoding,
                        ),
                        elapsed=interaction.response.elapsed,
                        status=_convert_status(interaction.status),
                        recorded_at=interaction.recorded_at,
                    )
                    for interaction in event.result.interactions
                ],
            ),
            hypothesis_output=event.hypothesis_output,
        ),
    )


def _convert_check(check, interaction) -> SerializedCheck:
    return SerializedCheck(
        name=check.name,
        value=_convert_status(check.value),
        recorded_at=interaction.recorded_at,
        response=Response(
            method=check.request.method,
            uri=check.request.uri,
            body=check.response.body,
            encoding=check.response.encoding,
            status_code=check.response.status_code,
            http_version=check.response.http_version,
            message=check.response.message,
            headers=check.response.headers,
        )
        if check.response is not None
        else None,
        request=Request(
            body=check.request.body,
            method=check.request.method,
            uri=check.request.uri,
            headers=check.request.headers,
        )
        if check.request is not None
        else None,
        # TODO: Convert this into a serializable object
        example=check.example,
        message=check.message,
        duration=_get_duration(check),
    )


def _convert_internal_error(event: se.InternalError) -> events.InternalError:
    return events.InternalError(
        message=event.message,
        exception_type=event.exception_type,
        exception=event.exception,
        exception_with_traceback=event.exception_with_traceback,
    )


def _convert_finished(event: se.Finished) -> events.Finished[FinishedPayload]:
    # Convert the Schemathesis Status enum to levo-commons Status enum.
    total = {}
    if event.total:
        for key, value in event.total.items():
            inner_dict = {}
            for k, v in value.items():
                if type(k) == str:
                    inner_dict[k] = v
                else:
                    inner_dict[_convert_status(k)] = v
            total[key] = inner_dict

    return events.Finished(
        running_time=event.running_time,
        payload=FinishedPayload(
            has_failures=event.has_failures,
            has_errors=event.has_errors,
            is_empty=event.is_empty,
            total=total,
            generic_errors=[
                SerializedError(
                    exception=error.exception,
                    exception_with_traceback=error.exception_with_traceback,
                    example=error.example,
                    title=error.title,
                )
                for error in event.generic_errors
            ],
        ),
    )


def convert_event(event: se.ExecutionEvent) -> events.Event:
    """Convert Schemathesis events to Levo events."""
    handler = {
        se.Initialized: _convert_initialized,
        se.BeforeExecution: _convert_before_execution,
        se.AfterExecution: _convert_after_execution,
        se.Interrupted: lambda e: events.Interrupted(),
        se.InternalError: _convert_internal_error,
        se.Finished: _convert_finished,
    }[event.__class__]
    return handler(event)
