# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AddonFieldType(str, Enum):
    """
    AddonFieldType
    """

    """
    allowed enum values
    """
    String = 'String'
    Boolean = 'Boolean'
    Integer = 'Integer'
    Number = 'Number'
    Object = 'Object'
    StringList = 'StringList'
    IntegerList = 'IntegerList'
    NumberList = 'NumberList'
    BooleanList = 'BooleanList'
    ObjectList = 'ObjectList'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AddonFieldType from a JSON string"""
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
    [member._value_ for member in AddonFieldType],
    [
        "Text",
        "Switch",
        "Whole number",
        "Number",
        "Object",
        "List of text values",
        "List of whole numbers",
        "List of numbers",
        "List of switches",
        "List of blocks",
    ],
))
_DESCRIPTIONS: dict[str, str] = dict(zip(
    [member._value_ for member in AddonFieldType],
    [
        "A text value.",
        "true or false.",
        "A whole number.",
        "A number that may have a fractional part.",
        "A block of settings, or a map of keys to values when it is a leaf.",
        "A list whose entries are text.",
        "A list whose entries are whole numbers.",
        "A list whose entries are numbers.",
        "A list whose entries are true or false.",
        "A list whose entries are blocks of settings.",
    ],
))

