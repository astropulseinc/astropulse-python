"""The official Python SDK for the AstroPulse Platform API.

The resources on :class:`Client` are generated from the platform's OpenAPI
document. The exceptions come from two places: the generated client raises one
per status -- :class:`NotFoundException` and its siblings, all of them
:class:`ApiException` -- and this package raises :class:`DeploymentFailed` and
:class:`WaitTimeout` while waiting for work the platform does asynchronously.

Catch :class:`OpenApiException` to catch everything the client can raise,
including the argument errors it checks before sending anything.

``__version__`` is this package's own; ``__api_version__`` is the platform
build whose API document it was generated from. They move independently: a
client fix ships without an API change, and an API change reaches callers only
when the SDK is regenerated and released.
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
from ._errors import AstroPulseError, DeploymentFailed, WaitTimeout
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
    # raised by this package, while waiting
    "AstroPulseError",
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
