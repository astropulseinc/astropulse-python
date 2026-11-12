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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class AWSConnectRequest(BaseModel):
    """
    AWSConnectRequest
    """ # noqa: E501
    cluster_name: Annotated[str, Field(min_length=1, strict=True, max_length=50)] = Field(description="The cluster name (required, 1-50 characters, valid DNS name)", alias="clusterName")
    destination_account_id: Optional[StrictStr] = Field(default=None, description="The target AWS account ID (optional, 12-digit numeric string). Auto-detected from cluster metadata if not provided.", alias="destinationAccountId")
    duration: Optional[StrictStr] = Field(default=None, description="The validity period for credentials (optional, Go duration format e.g. \"1h\", \"30m\")", json_schema_extra={"examples": ["1h"]})
    force_update: Optional[StrictBool] = Field(default=None, description="Bypasses cluster existence checks and forces resource updates (optional, default: false)", alias="forceUpdate")
    target_region: Optional[StrictStr] = Field(default=None, description="The AWS region for resource creation (optional, e.g. \"us-west-2\"). Auto-detected from cluster metadata if not provided.", alias="targetRegion")
    __properties: ClassVar[List[str]] = ["clusterName", "destinationAccountId", "duration", "forceUpdate", "targetRegion"]

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
        """Create an instance of AWSConnectRequest from a JSON string"""
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
        """Create an instance of AWSConnectRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusterName": obj.get("clusterName"),
            "destinationAccountId": obj.get("destinationAccountId"),
            "duration": obj.get("duration"),
            "forceUpdate": obj.get("forceUpdate"),
            "targetRegion": obj.get("targetRegion")
        })
        return _obj


