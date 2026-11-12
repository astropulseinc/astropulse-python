# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class SelfHostedCredentialState(str, Enum):
    """
    SelfHostedCredentialState
    """

    """
    allowed enum values
    """
    Active = 'Active'
    NotFound = 'NotFound'
    Unreadable = 'Unreadable'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SelfHostedCredentialState from a JSON string"""
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


