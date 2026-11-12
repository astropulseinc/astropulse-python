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
from astropulse._generated.models.cluster_selection import ClusterSelection
from astropulse._generated.models.constraints import Constraints
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ApplicationProfile(BaseModel):
    """
    ApplicationProfile
    """ # noqa: E501
    cluster_name: Optional[StrictStr] = Field(default=None, description="The name of the cluster.", alias="clusterName")
    cluster_selection: Optional[ClusterSelection] = Field(default=None, alias="clusterSelection")
    constraints: Optional[Constraints] = Field(default=None, description="Specifies different constraint that the underlying infrastructe has to adhere to run the application.")
    id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the application profile.")
    name: Optional[StrictStr] = Field(default=None, description="The name of the application profile.")
    namespace: Optional[StrictStr] = Field(default=None, description="The Kubernetes namespace where the profile resides.")
    org_id: Optional[StrictStr] = Field(default=None, description="The organization ID.", alias="orgId")
    slug: Optional[StrictStr] = Field(default=None, description="The unique identifier of the application profile.")
    __properties: ClassVar[List[str]] = ["clusterName", "clusterSelection", "constraints", "id", "name", "namespace", "orgId", "slug"]

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
        """Create an instance of ApplicationProfile from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cluster_selection
        if self.cluster_selection:
            _dict['clusterSelection'] = self.cluster_selection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of constraints
        if self.constraints:
            _dict['constraints'] = self.constraints.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApplicationProfile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusterName": obj.get("clusterName"),
            "clusterSelection": ClusterSelection.from_dict(obj["clusterSelection"]) if obj.get("clusterSelection") is not None else None,
            "constraints": Constraints.from_dict(obj["constraints"]) if obj.get("constraints") is not None else None,
            "id": obj.get("id"),
            "name": obj.get("name"),
            "namespace": obj.get("namespace"),
            "orgId": obj.get("orgId"),
            "slug": obj.get("slug")
        })
        return _obj


