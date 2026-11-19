# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class PreflightReasonCode(str, Enum):
    """
    PreflightReasonCode
    """

    """
    allowed enum values
    """
    QuotaExceeded = 'QuotaExceeded'
    MachineTypeUnavailable = 'MachineTypeUnavailable'
    ReservedCapacityUnavailable = 'ReservedCapacityUnavailable'
    ReservedCapacityUncovered = 'ReservedCapacityUncovered'
    CapacityBlockUnavailable = 'CapacityBlockUnavailable'
    CapacityBlockEnded = 'CapacityBlockEnded'
    AcceleratorQuotaExceeded = 'AcceleratorQuotaExceeded'
    AcceleratorUnavailable = 'AcceleratorUnavailable'
    DriverOwnerMissing = 'DriverOwnerMissing'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PreflightReasonCode from a JSON string"""
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
    [member._value_ for member in PreflightReasonCode],
    [
        "Quota exceeded",
        "Machine type unavailable",
        "No usable reservation",
        "Reservation too small",
        "No usable Capacity Block",
        "Capacity Block ended",
        "GPU quota exceeded",
        "GPU unavailable",
        "GPU driver missing",
    ],
))
_DESCRIPTIONS: dict[str, str] = dict(zip(
    [member._value_ for member in PreflightReasonCode],
    [
        "The cloud account's quota has no room for the nodes.",
        "The machine type is not offered in the zones the node group uses.",
        "The account holds no capacity reservation the node group can use.",
        "The account's reservations cover fewer nodes than the node group can run; the rest are On-Demand.",
        "The account holds no active Capacity Block for ML that fits the node group.",
        "The Capacity Block the node group runs on has ended.",
        "The cloud account's GPU quota has no room for the nodes.",
        "The GPU is not offered in the zones the node group uses.",
        "Nothing on the cluster installs the GPU driver the node group needs.",
    ],
))

