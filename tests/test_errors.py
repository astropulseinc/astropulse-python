"""Every error the package raises is an AstroPulseError.

The API's refusals are generated exceptions and the waiting errors are
hand-written, but a caller catches all of them with one class, as with most API
SDKs. The generated hierarchy underneath is unchanged, so code that catches
``ApiException`` or ``OpenApiException`` keeps working.
"""

from __future__ import annotations

import socket

import pytest
import urllib3

import astropulse
from astropulse import (
    ApiAttributeError,
    ApiConnectionError,
    ApiException,
    ApiKeyError,
    ApiTimeoutError,
    ApiTypeError,
    ApiValueError,
    AstroPulseError,
    BadRequestException,
    ConflictException,
    DeploymentFailed,
    ForbiddenException,
    NotFoundException,
    OpenApiException,
    ServiceException,
    UnauthorizedException,
    UnprocessableEntityException,
    WaitTimeout,
)
from astropulse._errors import connection_error
from astropulse._generated.rest import RESTResponse
from astropulse.models import ApplicationStatus

API_ERRORS = [
    ApiException,
    BadRequestException,
    UnauthorizedException,
    ForbiddenException,
    NotFoundException,
    ConflictException,
    UnprocessableEntityException,
    ServiceException,
]
ARGUMENT_ERRORS = [ApiTypeError, ApiValueError, ApiAttributeError, ApiKeyError]


def test_every_exported_exception_is_an_astropulse_error() -> None:
    exported = [getattr(astropulse, name) for name in astropulse.__all__]
    exceptions = [
        item for item in exported if isinstance(item, type) and issubclass(item, BaseException)
    ]

    assert exceptions
    for exception in exceptions:
        assert issubclass(exception, AstroPulseError), exception.__name__


@pytest.mark.parametrize("error", API_ERRORS)
def test_an_api_error_is_caught_as_an_astropulse_error(error: type[ApiException]) -> None:
    with pytest.raises(AstroPulseError):
        raise error(status=404, reason="Not Found")


@pytest.mark.parametrize("error", API_ERRORS)
def test_an_api_error_is_still_caught_as_an_api_exception(error: type[ApiException]) -> None:
    with pytest.raises(ApiException):
        raise error(status=404, reason="Not Found")
    with pytest.raises(OpenApiException):
        raise error(status=404, reason="Not Found")


@pytest.mark.parametrize("error", ARGUMENT_ERRORS)
def test_an_argument_error_is_caught_as_an_astropulse_error(error: type[OpenApiException]) -> None:
    with pytest.raises(AstroPulseError):
        raise error("bad argument")


def test_argument_errors_keep_their_builtin_bases() -> None:
    assert issubclass(ApiTypeError, TypeError)
    assert issubclass(ApiValueError, ValueError)
    assert issubclass(ApiAttributeError, AttributeError)
    assert issubclass(ApiKeyError, KeyError)


def test_waiting_errors_are_astropulse_errors_and_keep_their_builtin_bases() -> None:
    failed = DeploymentFailed("qwen-chat", ApplicationStatus.Failed, "image pull")
    timeout = WaitTimeout("qwen-chat", ApplicationStatus.InProgress, 30)

    assert isinstance(failed, AstroPulseError) and isinstance(failed, RuntimeError)
    assert isinstance(timeout, AstroPulseError) and isinstance(timeout, TimeoutError)
    assert not isinstance(failed, OpenApiException)
    assert str(failed) == "qwen-chat is Failed: image pull"


_POOL = urllib3.HTTPConnectionPool("127.0.0.1", 9)
_CONNECTION = urllib3.connection.HTTPConnection("127.0.0.1", 9)
_REFUSED = urllib3.exceptions.NewConnectionError(_CONNECTION, "Connection refused")
_UNRESOLVED = urllib3.exceptions.NameResolutionError(
    "nowhere.invalid", _CONNECTION, socket.gaierror("no host")
)
_CONNECT_TIMEOUT = urllib3.exceptions.ConnectTimeoutError(_POOL, "timed out connecting")
_READ_TIMEOUT = urllib3.exceptions.ReadTimeoutError(_POOL, "/", "timed out reading")
_RESET = urllib3.exceptions.ProtocolError("Connection aborted.", ConnectionResetError())


@pytest.mark.parametrize(
    ("error", "expected"),
    [
        (_REFUSED, ApiConnectionError),
        (_UNRESOLVED, ApiConnectionError),
        (_RESET, ApiConnectionError),
        (_CONNECT_TIMEOUT, ApiTimeoutError),
        (_READ_TIMEOUT, ApiTimeoutError),
        (urllib3.exceptions.MaxRetryError(_POOL, "/", _REFUSED), ApiConnectionError),
        (urllib3.exceptions.MaxRetryError(_POOL, "/", _READ_TIMEOUT), ApiTimeoutError),
        (urllib3.exceptions.MaxRetryError(_POOL, "/", None), ApiConnectionError),
    ],
)
def test_a_transport_error_is_classified_by_what_went_wrong(
    error: urllib3.exceptions.HTTPError, expected: type[ApiConnectionError]
) -> None:
    """A refused or unresolvable host is not a timeout, although urllib3 derives
    those errors from ConnectTimeoutError; after retries, the reason decides."""
    converted = connection_error(error)

    assert type(converted) is expected
    assert str(error) in str(converted)


def test_connection_errors_keep_the_bases_callers_already_catch() -> None:
    assert issubclass(ApiConnectionError, AstroPulseError)
    assert issubclass(ApiConnectionError, urllib3.exceptions.HTTPError)
    assert issubclass(ApiTimeoutError, ApiConnectionError)
    assert issubclass(ApiTimeoutError, TimeoutError)
    assert not issubclass(ApiConnectionError, OpenApiException)


def test_a_body_that_breaks_off_while_reading_is_a_connection_error() -> None:
    """The body is read after request() returns, so it is wrapped there too."""

    class _BrokenResponse:
        status = 200
        reason = "OK"

        @property
        def data(self) -> bytes:
            raise _READ_TIMEOUT

    with pytest.raises(ApiTimeoutError) as raised:
        RESTResponse(_BrokenResponse()).read()  # type: ignore[no-untyped-call]
    assert raised.value.__cause__ is _READ_TIMEOUT
