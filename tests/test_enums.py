"""A value the API adds to an enum must not break a response.

The API document promises that new values can appear in enum-like fields at any
time. A client that rejects one stops being able to read the resource at all, so
every generated enum accepts a value it does not list, keeps the string it was
given, and sends that string back unchanged.

Each member also carries the display name and meaning the API document gives it
(``label``, ``description``); a value it does not list has neither.
"""

from __future__ import annotations

import json
from enum import Enum
from typing import Any

import pytest

from astropulse import models
from astropulse.models import (
    AgentCapabilityStatus,
    AKSNetworkPlugin,
    Application,
    ApplicationStatus,
    ModelAPIFormat,
    NotificationChannelType,
    NotificationSubscription,
)

UNKNOWN = "HIBERNATING"


def test_enum_parses_a_value_it_does_not_list() -> None:
    status = ApplicationStatus(UNKNOWN)

    assert isinstance(status, ApplicationStatus)
    assert status.value == UNKNOWN
    assert status == UNKNOWN
    assert all(status is not member for member in ApplicationStatus)


def test_enum_from_json_parses_a_value_it_does_not_list() -> None:
    status = ApplicationStatus.from_json(json.dumps(UNKNOWN))

    assert status.value == UNKNOWN


def test_enum_still_maps_a_known_value_to_its_member() -> None:
    assert ApplicationStatus("Running") is ApplicationStatus.Running
    assert ApplicationStatus.from_json('"Failed"') is ApplicationStatus.Failed


def test_enum_lists_only_its_own_members() -> None:
    ApplicationStatus(UNKNOWN)

    assert UNKNOWN not in [member.value for member in ApplicationStatus]


def test_enum_still_rejects_a_value_of_the_wrong_type() -> None:
    with pytest.raises(ValueError):
        ApplicationStatus(5)


def test_model_with_an_unknown_enum_value_round_trips() -> None:
    body = {"appName": "qwen-chat", "status": UNKNOWN, "phase": "Running"}

    app = Application.from_dict(body)

    assert app is not None
    assert app.status is not None and app.status.value == UNKNOWN
    assert app.phase is ApplicationStatus.Running
    assert json.loads(app.to_json()) == body
    assert app.to_dict()["status"] == UNKNOWN


def test_model_from_json_with_an_unknown_enum_value() -> None:
    app = Application.from_json(json.dumps({"status": UNKNOWN}))

    assert app is not None and app.status is not None
    assert app.status.value == UNKNOWN


def test_list_of_enums_keeps_an_unknown_item() -> None:
    body = {"channels": ["email", "pagerduty"], "topic": "deploys"}

    subscription = NotificationSubscription.from_dict(body)

    assert subscription is not None and subscription.channels is not None
    assert subscription.channels[0] is NotificationChannelType.Email
    assert subscription.channels[1].value == "pagerduty"
    assert json.loads(subscription.to_json()) == body


def test_inline_enum_field_keeps_a_value_it_does_not_list() -> None:
    body = {"name": "tunnel-v1", "state": "draining"}

    capability = AgentCapabilityStatus.from_dict(body)

    assert capability is not None
    assert capability.state == "draining"
    assert json.loads(capability.to_json()) == body


def test_inline_enum_field_still_takes_a_known_value() -> None:
    capability = AgentCapabilityStatus.from_dict({"state": "ready"})

    assert capability is not None and capability.state == "ready"


def test_assigning_an_unknown_value_is_accepted() -> None:
    app = Application()

    app.status = UNKNOWN  # type: ignore[assignment]

    assert app.status is not None and app.status.value == UNKNOWN


# Any: each generated enum has label and description; the Enum base does not.
ENUMS: list[Any] = [
    item
    for item in (getattr(models, name) for name in models.__all__)
    if isinstance(item, type) and issubclass(item, Enum)
]


def test_a_member_carries_the_label_and_description_from_the_document() -> None:
    assert AKSNetworkPlugin.Azure.label == "Azure CNI"
    assert AKSNetworkPlugin.Azure.description == (
        "Pods get addresses from Azure's container networking."
    )
    assert AKSNetworkPlugin.None_.label == "None"
    assert ApplicationStatus.DeleteFailed.label == "Delete failed"


def test_a_label_is_looked_up_by_value() -> None:
    assert ApplicationStatus.label_for("DeleteFailed") == "Delete failed"
    assert ApplicationStatus.description_for("Running") == ApplicationStatus.Running.description
    assert ApplicationStatus.label_for(UNKNOWN) is None
    assert ApplicationStatus.description_for(UNKNOWN) is None


def test_a_value_it_does_not_list_has_no_label_or_description() -> None:
    status = ApplicationStatus(UNKNOWN)

    assert status.label is None
    assert status.description is None
    assert status.value == UNKNOWN


def test_the_label_tables_add_no_members() -> None:
    assert [member.name for member in AKSNetworkPlugin] == ["Azure", "Kubenet", "None_"]


def test_a_text_with_quotes_and_braces_survives_generation() -> None:
    assert ModelAPIFormat.V2.description is not None
    assert "`/v2/models/{name}/infer`" in ModelAPIFormat.V2.description
    assert AKSNetworkPlugin.Azure.description is not None
    assert "Azure's" in AKSNetworkPlugin.Azure.description


def test_every_listed_member_has_a_label_and_a_description() -> None:
    assert ENUMS
    for enum in ENUMS:
        for member in enum:
            # Every enum in the document publishes both today; a gap shows up
            # here, on the regeneration PR that brings it in.
            assert member.label, f"{enum.__name__}.{member.name} has no label"
            assert member.description, f"{enum.__name__}.{member.name} has no meaning"
