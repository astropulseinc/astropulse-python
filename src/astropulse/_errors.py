"""The errors this package raises, under one base class.

:class:`AstroPulseError` is the base of everything the package raises. What the
API refuses raises a generated exception -- :class:`astropulse.NotFoundException`
and its siblings, all of them :class:`astropulse.ApiException` -- and those
derive from it too, through the generator's exception template. The ones
defined here are the situations the API cannot report:

- a request that got no answer at all -- :class:`ApiConnectionError`, and
  :class:`ApiTimeoutError` when the platform did not answer in time;
- a deploy that ended somewhere it cannot serve from -- :class:`DeploymentFailed`;
- a deploy that never settled -- :class:`WaitTimeout`.

Each keeps the base an earlier release raised in its place (urllib3's
``HTTPError``, ``TimeoutError``, ``RuntimeError``), so code written against it
keeps catching them.

The generated exceptions import this module while the package is still being
imported, so it imports nothing from the generated code at run time.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import urllib3

if TYPE_CHECKING:
    from ._generated.models.application_status import ApplicationStatus


class AstroPulseError(Exception):
    """Anything this package raises: the base of every error below and of the API's."""


class ApiConnectionError(AstroPulseError, urllib3.exceptions.HTTPError):
    """A request got no answer: the connection failed or broke off.

    Nothing the platform said is available, so unlike :class:`ApiException`
    there is no status or body. The urllib3 error is the ``__cause__``.
    """


class ApiTimeoutError(ApiConnectionError, TimeoutError):
    """A request got no answer in time: connecting or reading ran out."""


def connection_error(error: urllib3.exceptions.HTTPError) -> ApiConnectionError:
    """The error to raise, from ``error``, for a request that got no answer.

    The generated transport calls this for every urllib3 error it catches.
    When urllib3 has retried and given up, the error is a ``MaxRetryError``
    and what went wrong is its ``reason``.
    """
    cause: BaseException | None = error
    if isinstance(error, urllib3.exceptions.MaxRetryError) and error.reason is not None:
        cause = error.reason
    # urllib3 derives NewConnectionError, and so a refused or unresolvable
    # host, from ConnectTimeoutError: rule it out before asking about time.
    timed_out = isinstance(cause, urllib3.exceptions.TimeoutError) and not isinstance(
        cause, urllib3.exceptions.NewConnectionError
    )
    kind = ApiTimeoutError if timed_out else ApiConnectionError
    return kind(str(error))


class DeploymentFailed(AstroPulseError, RuntimeError):
    """An application reached a state it cannot serve from."""

    def __init__(
        self, application: str, status: ApplicationStatus | None, reason: str = ""
    ) -> None:
        self.application = application
        self.status = status
        self.reason = reason
        state = status.value if status is not None else "unknown"
        super().__init__(f"{application} is {state}{f': {reason}' if reason else ''}")


class WaitTimeout(AstroPulseError, TimeoutError):
    """An application had not settled before the wait ran out."""

    def __init__(self, application: str, status: ApplicationStatus | None, timeout: float) -> None:
        self.application = application
        self.status = status
        self.timeout = timeout
        state = status.value if status is not None else "unknown"
        super().__init__(f"{application} was still {state} after {timeout:g}s")


__all__ = [
    "ApiConnectionError",
    "ApiTimeoutError",
    "AstroPulseError",
    "DeploymentFailed",
    "WaitTimeout",
]
