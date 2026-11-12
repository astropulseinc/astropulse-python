# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.cluster_addon_support_status import ClusterAddonSupportStatus
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterAddonSupport(BaseModel):
    """
    ClusterAddonSupport
    """ # noqa: E501
    deprecated_on: Optional[date] = Field(default=None, description="The date this version was deprecated, as YYYY-MM-DD.", alias="deprecatedOn")
    end_of_support: Optional[date] = Field(default=None, description="The date this version is retired, as YYYY-MM-DD.", alias="endOfSupport")
    recommended: Optional[StrictStr] = Field(default=None, description="The version to move to. Empty when this is the recommended version.")
    status: Optional[ClusterAddonSupportStatus] = Field(default=None, description="Where the version is in its support lifecycle.")
    __properties: ClassVar[List[str]] = ["deprecatedOn", "endOfSupport", "recommended", "status"]

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
        """Create an instance of ClusterAddonSupport from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterAddonSupport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "deprecatedOn": obj.get("deprecatedOn"),
            "endOfSupport": obj.get("endOfSupport"),
            "recommended": obj.get("recommended"),
            "status": obj.get("status")
        })
        return _obj


