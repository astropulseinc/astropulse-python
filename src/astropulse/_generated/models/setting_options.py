# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.setting_format import SettingFormat
from astropulse._generated.models.setting_value_requirement import SettingValueRequirement
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class SettingOptions(BaseModel):
    """
    SettingOptions
    """ # noqa: E501
    default: Optional[StrictStr] = Field(default=None, description="The value used when the field is omitted; absent when there is none.")
    default_reason: Optional[StrictStr] = Field(default=None, description="Why `default` is the value used, in one sentence; absent when there is no default.", alias="defaultReason")
    description: Optional[StrictStr] = Field(default=None, description="What the setting controls, in one sentence.")
    enum: Optional[List[StrictStr]] = Field(default=None, description="The accepted values, in the order to offer them; absent for a text setting, which has a `format`.")
    var_field: Optional[StrictStr] = Field(default=None, description="The request field the values are for, such as `releaseChannel`.", alias="field")
    format: Optional[SettingFormat] = Field(default=None, description="The form a text setting's value takes; for a list, the form of each entry. Absent for a setting with `enum`.")
    label: Optional[StrictStr] = Field(default=None, description="The setting's name for people, such as Release channel.")
    max_items: Optional[StrictInt] = Field(default=None, description="The most entries a list setting accepts; absent when the setting is not a list or has no limit.", alias="maxItems")
    requirements: Optional[List[SettingValueRequirement]] = Field(default=None, description="Values in `enum` that run only on capacity the cloud account already holds, which no request field can supply, each with what that capacity must be. Absent when no value needs held capacity.")
    __properties: ClassVar[List[str]] = ["default", "defaultReason", "description", "enum", "field", "format", "label", "maxItems", "requirements"]

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
        """Create an instance of SettingOptions from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in requirements (list)
        _items = []
        if self.requirements:
            for _item_requirements in self.requirements:
                if _item_requirements:
                    _items.append(_item_requirements.to_dict())
            _dict['requirements'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SettingOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "default": obj.get("default"),
            "defaultReason": obj.get("defaultReason"),
            "description": obj.get("description"),
            "enum": obj.get("enum"),
            "field": obj.get("field"),
            "format": obj.get("format"),
            "label": obj.get("label"),
            "maxItems": obj.get("maxItems"),
            "requirements": [SettingValueRequirement.from_dict(_item) for _item in obj["requirements"]] if obj.get("requirements") is not None else None
        })
        return _obj


