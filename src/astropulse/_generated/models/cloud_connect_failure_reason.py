# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class CloudConnectFailureReason(str, Enum):
    """
    CloudConnectFailureReason
    """

    """
    allowed enum values
    """
    PlatformSignInUnavailable = 'PlatformSignInUnavailable'
    IdentityPoolNotFound = 'IdentityPoolNotFound'
    IdentityPoolDisabled = 'IdentityPoolDisabled'
    IdentityPoolDeleted = 'IdentityPoolDeleted'
    ServiceAccountNotFound = 'ServiceAccountNotFound'
    ApplicationNotInTenant = 'ApplicationNotInTenant'
    SignInRefused = 'SignInRefused'
    AccessNotGranted = 'AccessNotGranted'
    TargetNotFound = 'TargetNotFound'
    CloudUnavailable = 'CloudUnavailable'
    Unknown = 'Unknown'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CloudConnectFailureReason from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value: object) -> Self | None:
        """Accept a value this version does not know, keeping it as given.

        The API may add values to this enum at any time. One this version does
        not list parses to a member whose ``value`` is the string received, so
        it is never lost and is sent back unchanged; it equals no listed member.
        """
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = str(value)
        member._value_ = value
        return member

    @property
    def label(self) -> str | None:
        """The display name the API document gives this value.

        ``None`` for a value this version of the package does not list.
        """
        return _LABELS.get(self._value_)

    @property
    def description(self) -> str | None:
        """What this value means, as the API document describes it.

        ``None`` for a value this version of the package does not list.
        """
        return _DESCRIPTIONS.get(self._value_)

    @classmethod
    def label_for(cls, value: str) -> str | None:
        """The display name of a value, or ``None`` for one this version does not list."""
        return _LABELS.get(value)

    @classmethod
    def description_for(cls, value: str) -> str | None:
        """What a value means, or ``None`` for one this version does not list."""
        return _DESCRIPTIONS.get(value)



# The API document lists the labels and descriptions in the order of the values,
# which is also the order of the members above.
_LABELS: dict[str, str] = dict(zip(
    [member._value_ for member in CloudConnectFailureReason],
    [
        "AstroPulse sign-in unavailable",
        "Identity pool not found",
        "Identity pool disabled",
        "Identity pool deleted",
        "Service account not found",
        "Application not in tenant",
        "Sign-in refused",
        "Access not granted",
        "Target not found",
        "Cloud unavailable",
        "Unknown",
    ],
))
_DESCRIPTIONS: dict[str, str] = dict(zip(
    [member._value_ for member in CloudConnectFailureReason],
    [
        "AstroPulse could not sign in to your cloud with its own identity.",
        "The project has no usable workload identity pool or provider for AstroPulse.",
        "The workload identity pool or provider for AstroPulse is disabled.",
        "The workload identity pool or provider for AstroPulse was deleted.",
        "The service account the setup creates is not in the project.",
        "The AstroPulse application is not in your Microsoft Entra tenant.",
        "Your cloud refused AstroPulse's sign-in.",
        "AstroPulse signed in, but the access the setup grants is missing or still taking effect.",
        "The subscription or resource group named for the connection does not exist.",
        "The cloud could not be reached, limited the check, or failed it.",
        "The check failed for another reason; the message says what happened.",
    ],
))

