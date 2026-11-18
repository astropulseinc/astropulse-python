# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AuditEventType(str, Enum):
    """
    AuditEventType
    """

    """
    allowed enum values
    """
    APIKey = 'APIKey'
    Cluster = 'Cluster'
    Application = 'Application'
    AppProfile = 'AppProfile'
    Organization = 'Organization'
    User = 'User'
    Provider = 'Provider'
    Audit = 'Audit'
    Notification = 'Notification'
    Credential = 'Credential'
    Domain = 'Domain'
    Platform = 'Platform'
    Request = 'Request'
    Addon = 'Addon'
    AccessPolicy = 'AccessPolicy'
    Exposure = 'Exposure'
    Storage = 'Storage'
    Member = 'Member'
    ServiceAccount = 'ServiceAccount'
    Integration = 'Integration'
    DomainBinding = 'DomainBinding'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AuditEventType from a JSON string"""
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
    [member._value_ for member in AuditEventType],
    [
        "API key",
        "Cluster",
        "Application",
        "Application profile",
        "Organization",
        "User",
        "Cloud provider",
        "Audit log",
        "Notification",
        "Credential",
        "Domain",
        "Platform",
        "Request",
        "Add-on",
        "Access policy",
        "Exposure",
        "Storage",
        "Member",
        "Service account",
        "Integration",
        "Domain binding",
    ],
))
_DESCRIPTIONS: dict[str, str] = dict(zip(
    [member._value_ for member in AuditEventType],
    [
        "A personal or service account API key.",
        "A Kubernetes cluster.",
        "An application deployed to a cluster.",
        "A reusable application profile.",
        "The organization itself.",
        "A user account.",
        "A cloud provider connection.",
        "The audit log, read or exported.",
        "A notification subscription or integration.",
        "A stored credential.",
        "A domain the organization owns.",
        "An AstroPulse-wide setting.",
        "A request that named no resource.",
        "An add-on of a cluster.",
        "An access policy for model endpoints.",
        "Who can reach a cluster's endpoints.",
        "A cluster's storage.",
        "A member of the organization.",
        "A service account of the organization.",
        "A connected service, such as GitHub or Hugging Face.",
        "A domain bound to a cluster.",
    ],
))

