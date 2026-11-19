# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class NodeGroupChangeType(str, Enum):
    """
    NodeGroupChangeType
    """

    """
    allowed enum values
    """
    Unspecified = 'Unspecified'
    Scale = 'Scale'
    UpdateLabels = 'UpdateLabels'
    UpgradeVersion = 'UpgradeVersion'
    Recreate = 'Recreate'
    Create = 'Create'
    Rollback = 'Rollback'
    Remove = 'Remove'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of NodeGroupChangeType from a JSON string"""
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
    [member._value_ for member in NodeGroupChangeType],
    [
        "No change",
        "Scale",
        "Labels and taints",
        "Version upgrade",
        "Replace",
        "Create",
        "Roll back",
        "Remove",
    ],
))
_DESCRIPTIONS: dict[str, str] = dict(zip(
    [member._value_ for member in NodeGroupChangeType],
    [
        "Nothing about the node group changes.",
        "The node group's node count changes.",
        "The node labels or taints change.",
        "The nodes move to a newer Kubernetes version.",
        "The node group is replaced, because a setting that cannot change in place changes.",
        "A new node group is created.",
        "The nodes return to an earlier Kubernetes version.",
        "The node group's nodes are drained, then the group is deleted.",
    ],
))

