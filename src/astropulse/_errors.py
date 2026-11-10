"""What this package raises on its own behalf.

Everything the API itself refuses raises a generated exception --
:class:`astropulse.NotFoundException` and its siblings, all of them
:class:`astropulse.ApiException`. These are the two situations the API cannot
report, because they are about waiting rather than about a request: a deploy
that ended somewhere it cannot serve from, and one that never settled.

They are ``TimeoutError`` and ``RuntimeError`` underneath, so code written
against the previous release keeps catching them.
"""

from __future__ import annotations

from ._generated.models.application_status import ApplicationStatus


class AstroPulseError(Exception):
    """Anything this package raises that the API did not."""


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


__all__ = ["AstroPulseError", "DeploymentFailed", "WaitTimeout"]
