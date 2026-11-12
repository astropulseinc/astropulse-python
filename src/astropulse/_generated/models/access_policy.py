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
from astropulse._generated.models.access_policy_spec import AccessPolicySpec
from astropulse._generated.models.object_meta import ObjectMeta
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class AccessPolicy(BaseModel):
    """
    AccessPolicy
    """ # noqa: E501
    api_version: Optional[StrictStr] = Field(default=None, alias="apiVersion")
    kind: Optional[StrictStr] = None
    metadata: Optional[ObjectMeta] = None
    open_endpoints: Optional[List[StrictStr]] = Field(default=None, description="Names the applications whose open endpoint this policy currently protects. Set by AstroPulse; ignored on apply.", alias="openEndpoints")
    references: Optional[List[StrictStr]] = None
    revision: Optional[StrictInt] = None
    spec: Optional[AccessPolicySpec] = None
    updated_at: Optional[StrictStr] = Field(default=None, alias="updatedAt")
    __properties: ClassVar[List[str]] = ["apiVersion", "kind", "metadata", "openEndpoints", "references", "revision", "spec", "updatedAt"]

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
        """Create an instance of AccessPolicy from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of spec
        if self.spec:
            _dict['spec'] = self.spec.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AccessPolicy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "apiVersion": obj.get("apiVersion"),
            "kind": obj.get("kind"),
            "metadata": ObjectMeta.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None,
            "openEndpoints": obj.get("openEndpoints"),
            "references": obj.get("references"),
            "revision": obj.get("revision"),
            "spec": AccessPolicySpec.from_dict(obj["spec"]) if obj.get("spec") is not None else None,
            "updatedAt": obj.get("updatedAt")
        })
        return _obj


