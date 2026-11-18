# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class PlanResource(str, Enum):
    """
    PlanResource
    """

    """
    allowed enum values
    """
    Applications = 'Applications'
    Clusters = 'Clusters'
    RegisteredClusters = 'RegisteredClusters'
    ApplicationProfiles = 'ApplicationProfiles'
    ServiceAccounts = 'ServiceAccounts'
    APIKeys = 'APIKeys'
    NotificationSubscriptions = 'NotificationSubscriptions'
    NotificationProviders = 'NotificationProviders'
    Organizations = 'Organizations'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PlanResource from a JSON string"""
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
    [member._value_ for member in PlanResource],
    [
        "Applications",
        "Clusters",
        "Registered clusters",
        "Application profiles",
        "Service accounts",
        "API keys",
        "Notification subscriptions",
        "Notification providers",
        "Organizations",
    ],
))
_DESCRIPTIONS: dict[str, str] = dict(zip(
    [member._value_ for member in PlanResource],
    [
        "Applications and models deployed in the organization.",
        "Clusters AstroPulse created for the organization.",
        "Clusters the organization registered with the AstroPulse agent.",
        "Application profiles in the organization.",
        "Active service accounts in the organization.",
        "Active API keys in the organization.",
        "Notification subscriptions in the organization.",
        "Notification channels connected to the organization.",
        "Organizations the caller belongs to.",
    ],
))

