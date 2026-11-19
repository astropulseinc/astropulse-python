# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class EndpointProbeReach(str, Enum):
    """
    EndpointProbeReach
    """

    """
    allowed enum values
    """
    Answered = 'Answered'
    NoLoadBalancer = 'NoLoadBalancer'
    NoDNS = 'NoDNS'
    NoAnswer = 'NoAnswer'
    WrongCertificate = 'WrongCertificate'
    NotChecked = 'NotChecked'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EndpointProbeReach from a JSON string"""
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
    [member._value_ for member in EndpointProbeReach],
    [
        "Answered",
        "No load balancer yet",
        "Hostname doesn't resolve",
        "No answer",
        "Wrong certificate",
        "Not checked",
    ],
))
_DESCRIPTIONS: dict[str, str] = dict(zip(
    [member._value_ for member in EndpointProbeReach],
    [
        "The hostname resolved and the endpoint answered with its certificate.",
        "The gateway's load balancer has no address yet.",
        "The hostname does not resolve yet.",
        "The hostname resolved but nothing answered in time.",
        "Something answered with a different certificate.",
        "The gateway has no load balancer, so there is no address to try.",
    ],
))

