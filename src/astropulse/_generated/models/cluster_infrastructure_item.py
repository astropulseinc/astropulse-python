# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ClusterInfrastructureItem(str, Enum):
    """
    ClusterInfrastructureItem
    """

    """
    allowed enum values
    """
    ControlPlane = 'ControlPlane'
    NATGateway = 'NATGateway'
    NATDataProcessing = 'NATDataProcessing'
    PublicIPv4 = 'PublicIPv4'
    LoadBalancer = 'LoadBalancer'
    AutoModeManagement = 'AutoModeManagement'
    DataTransfer = 'DataTransfer'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ClusterInfrastructureItem from a JSON string"""
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
    [member._value_ for member in ClusterInfrastructureItem],
    [
        "Control plane",
        "NAT gateway",
        "NAT data processing",
        "Public IPv4 address",
        "Load balancer",
        "EKS Auto Mode management",
        "Data transfer",
    ],
))
_DESCRIPTIONS: dict[str, str] = dict(zip(
    [member._value_ for member in ClusterInfrastructureItem],
    [
        "The cloud's hourly fee for the managed control plane.",
        "A gateway that lets nodes on private subnets reach the internet, charged by the hour.",
        "The charge per gigabyte of traffic the NAT gateways carry.",
        "A public address the cluster's network holds, charged by the hour.",
        "A load balancer in front of the control plane or the cluster's outbound traffic.",
        "The fee EKS Auto Mode charges for each instance it runs.",
        "Traffic out to the internet and between zones, charged per gigabyte.",
    ],
))

