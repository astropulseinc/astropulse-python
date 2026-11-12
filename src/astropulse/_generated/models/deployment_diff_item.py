# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class DeploymentDiffItem(BaseModel):
    """
    DeploymentDiffItem
    """ # noqa: E501
    after: Optional[Any] = Field(default=None, description="The sanitized new value (omitted/redacted for secrets).")
    before: Optional[Any] = Field(default=None, description="The sanitized prior value (omitted/redacted for secrets).")
    description: Optional[StrictStr] = Field(default=None, description="An optional human explanation of the change.")
    path: Optional[StrictStr] = Field(default=None, description="The changed field's path in the application request, as this API's document names it, such as `source.helm.repo.chartVersion`. Below `values.object` it continues with the chart's own value keys.")
    redacted: Optional[StrictBool] = Field(default=None, description="Indicates the value was hidden: before and after are left out. The text ***REDACTED*** stands for a hidden value and is never accepted as a value when applying.")
    secret: Optional[StrictBool] = Field(default=None, description="Indicates the field is classified as secret-bearing.")
    __properties: ClassVar[List[str]] = ["after", "before", "description", "path", "redacted", "secret"]

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
        """Create an instance of DeploymentDiffItem from a JSON string"""
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
        # set to None if after (nullable) is None
        # and model_fields_set contains the field
        if self.after is None and "after" in self.model_fields_set:
            _dict['after'] = None

        # set to None if before (nullable) is None
        # and model_fields_set contains the field
        if self.before is None and "before" in self.model_fields_set:
            _dict['before'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeploymentDiffItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "after": obj.get("after"),
            "before": obj.get("before"),
            "description": obj.get("description"),
            "path": obj.get("path"),
            "redacted": obj.get("redacted"),
            "secret": obj.get("secret")
        })
        return _obj


