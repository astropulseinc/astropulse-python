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
from astropulse._generated.models.affinity_type import AffinityType
from astropulse._generated.models.container import Container
from astropulse._generated.models.hpa import HPA
from astropulse._generated.models.priority_class_type import PriorityClassType
from astropulse._generated.models.resource_requirements import ResourceRequirements
from astropulse._generated.models.vpa import VPA
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class TierConfig(BaseModel):
    """
    TierConfig
    """ # noqa: E501
    container: Optional[Container] = None
    horizontal_auto_scaling: Optional[HPA] = Field(default=None, alias="horizontalAutoScaling")
    id: Optional[StrictStr] = None
    multi_zone_deployment: Optional[StrictBool] = Field(default=None, alias="multiZoneDeployment")
    name: Optional[StrictStr] = None
    org_id: Optional[StrictStr] = Field(default=None, alias="orgId")
    placement_preference: Optional[AffinityType] = Field(default=None, alias="placementPreference")
    priority_level: Optional[PriorityClassType] = Field(default=None, alias="priorityLevel")
    resources: Optional[ResourceRequirements] = None
    vertical_auto_scaling: Optional[VPA] = Field(default=None, alias="verticalAutoScaling")
    __properties: ClassVar[List[str]] = ["container", "horizontalAutoScaling", "id", "multiZoneDeployment", "name", "orgId", "placementPreference", "priorityLevel", "resources", "verticalAutoScaling"]

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
        """Create an instance of TierConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of container
        if self.container:
            _dict['container'] = self.container.to_dict()
        # override the default output from pydantic by calling `to_dict()` of horizontal_auto_scaling
        if self.horizontal_auto_scaling:
            _dict['horizontalAutoScaling'] = self.horizontal_auto_scaling.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resources
        if self.resources:
            _dict['resources'] = self.resources.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vertical_auto_scaling
        if self.vertical_auto_scaling:
            _dict['verticalAutoScaling'] = self.vertical_auto_scaling.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TierConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "container": Container.from_dict(obj["container"]) if obj.get("container") is not None else None,
            "horizontalAutoScaling": HPA.from_dict(obj["horizontalAutoScaling"]) if obj.get("horizontalAutoScaling") is not None else None,
            "id": obj.get("id"),
            "multiZoneDeployment": obj.get("multiZoneDeployment"),
            "name": obj.get("name"),
            "orgId": obj.get("orgId"),
            "placementPreference": obj.get("placementPreference"),
            "priorityLevel": obj.get("priorityLevel"),
            "resources": ResourceRequirements.from_dict(obj["resources"]) if obj.get("resources") is not None else None,
            "verticalAutoScaling": VPA.from_dict(obj["verticalAutoScaling"]) if obj.get("verticalAutoScaling") is not None else None
        })
        return _obj


