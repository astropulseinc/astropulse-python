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
from astropulse._generated.models.endpoint_access_policy_none import EndpointAccessPolicyNone
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class EndpointAccessPolicyReference(BaseModel):
    """
    EndpointAccessPolicyReference
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="Of the organization's access policy to enforce on the endpoint.")
    var_none: Optional[EndpointAccessPolicyNone] = Field(default=None, description="Opts the endpoint out of caller authentication: anyone who reaches the hostname can call it. Compared exactly; applying it needs organization owner authority and is audited.", alias="none")
    revision: Optional[StrictInt] = Field(default=None, description="Of the named policy this deployment is bound to. Resolved by the API at apply (omit it to take the latest) and preserved in deployment and rollback snapshots, so a policy update reaches an application on its next deploy, never silently.")
    __properties: ClassVar[List[str]] = ["name", "none", "revision"]

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
        """Create an instance of EndpointAccessPolicyReference from a JSON string"""
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
        """Create an instance of EndpointAccessPolicyReference from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "none": obj.get("none"),
            "revision": obj.get("revision")
        })
        return _obj


