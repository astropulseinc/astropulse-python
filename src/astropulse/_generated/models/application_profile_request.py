# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from astropulse._generated.models.cloud_provider import CloudProvider
from astropulse._generated.models.resource_requirement import ResourceRequirement
from astropulse._generated.models.tier_type import TierType
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ApplicationProfileRequest(BaseModel):
    """
    Application profile creation request.
    """ # noqa: E501
    availability_tier: Optional[TierType] = Field(default=None, description="The availability tier applications on this profile run at.", alias="availabilityTier")
    cloud_provider: Optional[CloudProvider] = Field(default=None, description="Specifies the cloud provider and region for deployment (optional). If omitted, cluster selection is determined by ClusterName or platform defaults.", alias="cloudProvider")
    cluster_name: Optional[StrictStr] = Field(default=None, description="The target cluster name (optional). Takes precedence over CloudProvider when both are set.", alias="clusterName")
    profile_name: Annotated[str, Field(min_length=1, strict=True, max_length=50)] = Field(description="The profile name (required, 1-50 characters, valid DNS name). Format: lowercase alphanumeric and hyphens, must start with a letter. Example: \"example-profile\"", alias="profileName")
    resources: Optional[ResourceRequirement] = Field(default=None, description="Specifies resource requirements for the application. example: {\"memory\":{\"minimum\":\"1Gi\",\"maximum\":\"2Gi\"}}")
    __properties: ClassVar[List[str]] = ["availabilityTier", "cloudProvider", "clusterName", "profileName", "resources"]

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
        """Create an instance of ApplicationProfileRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cloud_provider
        if self.cloud_provider:
            _dict['cloudProvider'] = self.cloud_provider.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resources
        if self.resources:
            _dict['resources'] = self.resources.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApplicationProfileRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "availabilityTier": obj.get("availabilityTier"),
            "cloudProvider": CloudProvider.from_dict(obj["cloudProvider"]) if obj.get("cloudProvider") is not None else None,
            "clusterName": obj.get("clusterName"),
            "profileName": obj.get("profileName"),
            "resources": ResourceRequirement.from_dict(obj["resources"]) if obj.get("resources") is not None else None
        })
        return _obj


