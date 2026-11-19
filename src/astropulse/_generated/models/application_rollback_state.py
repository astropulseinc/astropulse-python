# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ApplicationRollbackState(str, Enum):
    """
    ApplicationRollbackState
    """

    """
    allowed enum values
    """
    Active = 'Active'
    RollbackInProgress = 'RollbackInProgress'
    RollbackPinned = 'RollbackPinned'
    ResumeInProgress = 'ResumeInProgress'
    ProtectionDegraded = 'ProtectionDegraded'
    RollbackFailed = 'RollbackFailed'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ApplicationRollbackState from a JSON string"""
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
    [member._value_ for member in ApplicationRollbackState],
    [
        "Active",
        "Rollback in progress",
        "Pinned by rollback",
        "Resume in progress",
        "Rolled back; restoring protection",
        "Rollback failed",
    ],
))
_DESCRIPTIONS: dict[str, str] = dict(zip(
    [member._value_ for member in ApplicationRollbackState],
    [
        "The application follows its spec, with automatic sync and repair on.",
        "A rollback is running.",
        "A rollback pinned the application to an earlier revision until you resume it.",
        "A resume is running.",
        "The application is on the rollback target, and AstroPulse is still turning automatic sync and repair back on.",
        "The rollback could not complete and needs your attention.",
    ],
))

