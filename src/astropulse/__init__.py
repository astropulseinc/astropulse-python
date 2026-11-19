"""The official Python SDK for the AstroPulse Platform API.

The resources on :class:`Client` are generated from the platform's OpenAPI
document. Every error the platform, the network or the SDK's own setup causes
is an :class:`AstroPulseError`: the generated client raises one per
status -- :class:`NotFoundException` and its siblings, all of them
:class:`ApiException` -- or :class:`ApiConnectionError` (and
:class:`ApiTimeoutError`) when a request gets no answer, and this package raises
:class:`DeploymentFailed` and :class:`WaitTimeout` while waiting for work the
platform does asynchronously.

Catch :class:`AstroPulseError` to handle all of them. A programming error is not
one of these, so that clause never hides a bug: conflicting or out-of-range
arguments raise the builtin ``TypeError`` or ``ValueError``, and the generated
methods raise :class:`pydantic.ValidationError` (a ``ValueError``) for an
argument of the wrong type.

``__api_version__`` is the platform API version the package was generated
from, and ``__version__`` follows it: 1.0.5 is generated from API v1.0.5, and
a fix to this package alone, against the same API, is 1.0.5.post1.
"""

from ._api_version import __api_version__
from ._client import (
    DEFAULT_RETRIES,
    DEFAULT_TIMEOUT,
    IN_FLIGHT,
    NOT_SERVING,
    SERVING,
    Client,
)
from ._errors import (
    ApiConnectionError,
    ApiTimeoutError,
    AstroPulseError,
    DeploymentFailed,
    WaitTimeout,
)
from ._generated.exceptions import (  # noqa: F401
    ApiAttributeError,
    ApiException,
    ApiKeyError,
    ApiTypeError,
    ApiValueError,
    BadRequestException,
    ConflictException,
    ForbiddenException,
    NotFoundException,
    OpenApiException,
    ServiceException,
    UnauthorizedException,
    UnprocessableEntityException,
)
from ._version import __version__

__all__ = [
    "Client",
    "SERVING",
    "NOT_SERVING",
    "IN_FLIGHT",
    "DEFAULT_RETRIES",
    "DEFAULT_TIMEOUT",
    # the base of every error below
    "AstroPulseError",
    # raised when a request gets no answer
    "ApiConnectionError",
    "ApiTimeoutError",
    # raised by this package, while waiting
    "DeploymentFailed",
    "WaitTimeout",
    # raised by the generated client, per status
    "OpenApiException",
    "ApiException",
    "BadRequestException",
    "UnauthorizedException",
    "ForbiddenException",
    "NotFoundException",
    "ConflictException",
    "UnprocessableEntityException",
    "ServiceException",
    # raised by the generated client before a request is sent
    "ApiTypeError",
    "ApiValueError",
    "ApiAttributeError",
    "ApiKeyError",
    "__version__",
    "__api_version__",
]
