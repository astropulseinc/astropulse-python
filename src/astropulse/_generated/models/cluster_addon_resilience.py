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
from astropulse._generated.models.addon_availability import AddonAvailability
from astropulse._generated.models.addon_resources import AddonResources
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterAddonResilience(BaseModel):
    """
    ClusterAddonResilience
    """ # noqa: E501
    availability: Optional[AddonAvailability] = Field(default=None, description="The effective setting: Standard when none was applied.")
    per_node: Optional[StrictStr] = Field(default=None, description="Names the nodes the main component runs one copy on, such as \"GPU node\"; Replicas is then how many run now, 0 when not yet known.", alias="perNode")
    reason: Optional[StrictStr] = Field(default=None, description="Says why that many copies run, such as \"1 replica: the cluster has fewer than two nodes it can run on\".")
    replicas: Optional[StrictInt] = Field(default=None, description="How many copies of the add-on's most available component run.")
    resources: Optional[AddonResources] = Field(default=None, description="The main component's effective sizing.")
    __properties: ClassVar[List[str]] = ["availability", "perNode", "reason", "replicas", "resources"]

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
        """Create an instance of ClusterAddonResilience from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of resources
        if self.resources:
            _dict['resources'] = self.resources.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterAddonResilience from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "availability": obj.get("availability"),
            "perNode": obj.get("perNode"),
            "reason": obj.get("reason"),
            "replicas": obj.get("replicas"),
            "resources": AddonResources.from_dict(obj["resources"]) if obj.get("resources") is not None else None
        })
        return _obj


