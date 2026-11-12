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
from astropulse._generated.models.preflight_category import PreflightCategory
from astropulse._generated.models.preflight_reason_code import PreflightReasonCode
from astropulse._generated.models.preflight_status import PreflightStatus
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class PreflightCheck(BaseModel):
    """
    PreflightCheck
    """ # noqa: E501
    category: Optional[PreflightCategory] = Field(default=None, description="Classifies the check type")
    description: Optional[StrictStr] = Field(default=None, description="Explains what was checked and the result")
    development_credentials: Optional[StrictBool] = Field(default=None, description="True on the Account Connection check when a local development platform creates the cluster with its own credentials instead of a connection.", alias="developmentCredentials")
    name: Optional[StrictStr] = Field(default=None, description="The check name (e.g. \"Version Compatibility\", \"Cloud Provider Capacity\")")
    reason_code: Optional[PreflightReasonCode] = Field(default=None, description="Why the check did not pass. Empty when the check has none.", alias="reasonCode")
    remediation: Optional[StrictStr] = Field(default=None, description="Provides actionable steps when status is `Fail`")
    requires_connection: Optional[StrictBool] = Field(default=None, description="True when the check is answered by reaching the cluster's connected cloud account, so it cannot pass until a real account is connected.", alias="requiresConnection")
    status: Optional[PreflightStatus] = Field(default=None, description="The check result")
    __properties: ClassVar[List[str]] = ["category", "description", "developmentCredentials", "name", "reasonCode", "remediation", "requiresConnection", "status"]

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
        """Create an instance of PreflightCheck from a JSON string"""
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
        """Create an instance of PreflightCheck from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "category": obj.get("category"),
            "description": obj.get("description"),
            "developmentCredentials": obj.get("developmentCredentials"),
            "name": obj.get("name"),
            "reasonCode": obj.get("reasonCode"),
            "remediation": obj.get("remediation"),
            "requiresConnection": obj.get("requiresConnection"),
            "status": obj.get("status")
        })
        return _obj


