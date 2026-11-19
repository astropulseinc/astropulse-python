# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AddonConfigurationFormat(str, Enum):
    """
    AddonConfigurationFormat
    """

    """
    allowed enum values
    """
    Quantity = 'Quantity'
    Duration = 'Duration'
    Email = 'Email'
    URL = 'URL'
    DNSLabel = 'DNSLabel'
    DNSSubdomain = 'DNSSubdomain'
    KeyValue = 'KeyValue'
    Decimal = 'Decimal'
    Currency = 'Currency'
    IAMRoleARN = 'IAMRoleARN'
    CapacityReservationID = 'CapacityReservationID'
    GCPServiceAccount = 'GCPServiceAccount'
    UUID = 'UUID'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AddonConfigurationFormat from a JSON string"""
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
    [member._value_ for member in AddonConfigurationFormat],
    [
        "Quantity",
        "Duration",
        "Email address",
        "URL",
        "DNS label",
        "DNS subdomain",
        "Key and value",
        "Decimal",
        "Currency code",
        "IAM role ARN",
        "Capacity reservation ID",
        "Google service account",
        "UUID",
    ],
))
_DESCRIPTIONS: dict[str, str] = dict(zip(
    [member._value_ for member in AddonConfigurationFormat],
    [
        "A Kubernetes resource quantity, such as 250m or 512Mi.",
        "A length of time in hours, minutes and seconds, such as 90s, 10m or 1h30m.",
        "An email address.",
        "An absolute http or https URL.",
        "A name of lowercase letters, digits and '-', at most 63 characters, such as team-a.",
        "A name of lowercase letters, digits, '-' and '.', at most 253 characters.",
        "A key and a value written key=value, such as team=ml.",
        "A non-negative decimal number, such as 0.035.",
        "A three-letter ISO 4217 currency code, such as USD.",
        "The ARN of an AWS IAM role, such as `arn:aws:iam::123456789012:role/name`.",
        "An EC2 capacity reservation ID, such as cr-0123456789abcdef0.",
        "A Google service account's email, such as dns@my-project.iam.gserviceaccount.com.",
        "A UUID, such as 11111111-2222-3333-4444-555555555555.",
    ],
))

