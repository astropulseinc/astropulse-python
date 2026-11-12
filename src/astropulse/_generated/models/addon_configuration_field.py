# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from astropulse._generated.models.addon_configuration_format import AddonConfigurationFormat
from astropulse._generated.models.addon_field_condition import AddonFieldCondition
from astropulse._generated.models.addon_field_type import AddonFieldType
from astropulse._generated.models.addon_unavailable_value import AddonUnavailableValue
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class AddonConfigurationField(BaseModel):
    """
    AddonConfigurationField
    """ # noqa: E501
    advanced: Optional[StrictBool] = Field(default=None, description="Marks a setting most users leave at its default; clients show it in an advanced section.")
    default: Optional[StrictStr] = Field(default=None, description="The value a new add-on gets when the setting is left out, written as it is in the configuration. In a cluster's catalog it is the value that cluster uses; empty when there is none.")
    description: Optional[StrictStr] = Field(default=None, description="Says what the setting does, from the field's own contract.")
    enum: Optional[List[StrictStr]] = Field(default=None, description="The complete set of values the setting accepts, empty for a setting that accepts any value of its type. For an array it is what one element accepts. Published so a client offers the choice instead of a free-text box the API then refuses, and so the list cannot drift from the one validation reads.")
    enum_schema: Optional[StrictStr] = Field(default=None, description="Names the schema in this API's document that lists the setting's values with each one's display name and meaning, such as `InstanceType`.", alias="enumSchema")
    format: Optional[AddonConfigurationFormat] = Field(default=None, description="The form a text setting's value takes, empty for text of any form. For an array it is the form of one element.")
    label: Optional[StrictStr] = Field(default=None, description="This field's name for display, such as CPU for resources.cpu.")
    leaf: Optional[StrictBool] = Field(default=None, description="True for a field that takes a value and false for the objects that only give structure: render leaves as inputs and the rest as headings.")
    max_items: Optional[StrictInt] = Field(default=None, description="The most entries a list setting accepts, absent when it has no limit.", alias="maxItems")
    maximum: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The largest value a number setting accepts, absent when it has no upper bound.")
    minimum: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The smallest value a number setting accepts, absent when it has no lower bound.")
    path: Optional[StrictStr] = Field(default=None, description="The setting's dotted path within the add-on's configuration.")
    placeholder: Optional[StrictStr] = Field(default=None, description="A hint for an empty field: an example value such as 250m, or false, 0, [] or {} for its type, and empty for text with no example.")
    read_only: Optional[StrictBool] = Field(default=None, description="Shown for reference; clients don't offer to change it.", alias="readOnly")
    required: Optional[StrictBool] = Field(default=None, description="Marks a setting the add-on refuses a configuration without, wherever the setting applies (visibleWhen).")
    section: Optional[StrictStr] = Field(default=None, description="The heading this field belongs under, empty for a top-level one. It is the parent object's label, not its path.")
    suggested: Optional[StrictStr] = Field(default=None, description="A value AstroPulse knows would work on this cluster, empty when it knows of none. It is never applied for you.")
    suggested_from: Optional[StrictStr] = Field(default=None, description="Says where the suggestion came from, so it reads as a proposal with a reason rather than a value that appeared.", alias="suggestedFrom")
    type: Optional[AddonFieldType] = Field(default=None, description="The kind of value the setting takes.")
    unavailable: Optional[List[AddonUnavailableValue]] = Field(default=None, description="Values in enum this cluster does not offer, each with why; absent when it offers every one.")
    visible_when: Optional[AddonFieldCondition] = Field(default=None, description="When the setting applies: while the other setting it names, itself applying, holds one of `values`. A client shows the setting only then; absent when it always applies.", alias="visibleWhen")
    __properties: ClassVar[List[str]] = ["advanced", "default", "description", "enum", "enumSchema", "format", "label", "leaf", "maxItems", "maximum", "minimum", "path", "placeholder", "readOnly", "required", "section", "suggested", "suggestedFrom", "type", "unavailable", "visibleWhen"]

    model_config = ConfigDict(
        validate_by_name=True,
        validate_by_alias=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(to_jsonable_python(self.to_dict()))

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AddonConfigurationField from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in unavailable (list)
        _items = []
        if self.unavailable:
            for _item_unavailable in self.unavailable:
                if _item_unavailable:
                    _items.append(_item_unavailable.to_dict())
            _dict['unavailable'] = _items
        # override the default output from pydantic by calling `to_dict()` of visible_when
        if self.visible_when:
            _dict['visibleWhen'] = self.visible_when.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AddonConfigurationField from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "advanced": obj.get("advanced"),
            "default": obj.get("default"),
            "description": obj.get("description"),
            "enum": obj.get("enum"),
            "enumSchema": obj.get("enumSchema"),
            "format": obj.get("format"),
            "label": obj.get("label"),
            "leaf": obj.get("leaf"),
            "maxItems": obj.get("maxItems"),
            "maximum": obj.get("maximum"),
            "minimum": obj.get("minimum"),
            "path": obj.get("path"),
            "placeholder": obj.get("placeholder"),
            "readOnly": obj.get("readOnly"),
            "required": obj.get("required"),
            "section": obj.get("section"),
            "suggested": obj.get("suggested"),
            "suggestedFrom": obj.get("suggestedFrom"),
            "type": obj.get("type"),
            "unavailable": [AddonUnavailableValue.from_dict(_item) for _item in obj["unavailable"]] if obj.get("unavailable") is not None else None,
            "visibleWhen": AddonFieldCondition.from_dict(obj["visibleWhen"]) if obj.get("visibleWhen") is not None else None
        })
        return _obj


