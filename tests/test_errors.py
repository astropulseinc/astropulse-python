"""Every error the package raises is an AstroPulseError.

The API's refusals are generated exceptions and the waiting errors are
hand-written, but a caller catches all of them with one class, as with most API
SDKs. The generated hierarchy underneath is unchanged, so code that catches
``ApiException`` or ``OpenApiException`` keeps working.
"""

from __future__ import annotations

import pytest

import astropulse
from astropulse import (
    ApiAttributeError,
    ApiException,
    ApiKeyError,
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
