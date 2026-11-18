# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AuditAction(str, Enum):
    """
    AuditAction
    """

    """
    allowed enum values
    """
    Create = 'Create'
    Update = 'Update'
    Delete = 'Delete'
    Revoke = 'Revoke'
    Upgrade = 'Upgrade'
    Read = 'Read'
    Resync = 'Resync'
    Register = 'Register'
    Unregister = 'Unregister'
    Connect = 'Connect'
    Disconnect = 'Disconnect'
    Approve = 'Approve'
    Reject = 'Reject'
    Rollback = 'Rollback'
    RollbackResume = 'RollbackResume'
    DriftDetected = 'DriftDetected'
    SelfHealed = 'SelfHealed'
    Issue = 'Issue'
    SignIn = 'SignIn'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AuditAction from a JSON string"""
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
    [member._value_ for member in AuditAction],
    [
        "Create",
        "Update",
        "Delete",
        "Revoke",
        "Upgrade",
        "Read",
        "Resync",
        "Register",
        "Unregister",
        "Connect",
        "Disconnect",
        "Approve",
        "Reject",
        "Roll back",
        "Resume after rollback",
        "Drift detected",
        "Self-healed",
        "Issue",
        "Sign in",
    ],
))
_DESCRIPTIONS: dict[str, str] = dict(zip(
    [member._value_ for member in AuditAction],
    [
        "The resource was created.",
        "The resource was changed.",
        "The resource was deleted.",
        "The credential was revoked.",
        "The cluster was upgraded to a newer Kubernetes version.",
        "Sensitive data, such as the audit log, was read.",
        "The application was deployed again from its source.",
        "The cluster was registered.",
        "The cluster was unregistered.",
        "A credential or service was connected.",
        "A credential or service was disconnected.",
        "The organization owner approved the change.",
        "The organization owner rejected the change.",
        "The application was rolled back to an earlier version.",
        "The application resumed following its configured source.",
        "What runs on the cluster no longer matches what was deployed.",
        "The drift was corrected automatically.",
        "A credential was issued, such as an agent certificate.",
        "The person signed in.",
    ],
))

