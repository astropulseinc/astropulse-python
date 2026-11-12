# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.cluster_operation_kind import ClusterOperationKind
from astropulse._generated.models.cluster_operation_step import ClusterOperationStep
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterOperation(BaseModel):
    """
    ClusterOperation
    """ # noqa: E501
    added_node_groups: Optional[List[StrictStr]] = Field(default=None, description="The node groups the operation adds, which the cluster does not have yet; they are in nodeGroups too.", alias="addedNodeGroups")
    attempt: Optional[StrictInt] = Field(default=None, description="The attempt number of the step running now. Omitted when unknown.")
    involves_control_plane: Optional[StrictBool] = Field(default=None, description="True when the operation changes the control plane.", alias="involvesControlPlane")
    kind: Optional[ClusterOperationKind] = Field(default=None, description="The operation running on the cluster.")
    node_groups: Optional[List[StrictStr]] = Field(default=None, description="The node groups the operation adds, changes or removes.", alias="nodeGroups")
    phase_label: Optional[StrictStr] = Field(default=None, description="The step the operation is on in words, such as Creating node groups. Omitted when the operation names no step.", alias="phaseLabel")
    started_at: Optional[datetime] = Field(default=None, description="When the operation started.", alias="startedAt")
    step: Optional[ClusterOperationStep] = Field(default=None, description="The step the operation is on. Omitted before its first step.")
    __properties: ClassVar[List[str]] = ["addedNodeGroups", "attempt", "involvesControlPlane", "kind", "nodeGroups", "phaseLabel", "startedAt", "step"]

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
        """Create an instance of ClusterOperation from a JSON string"""
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
        """Create an instance of ClusterOperation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addedNodeGroups": obj.get("addedNodeGroups"),
            "attempt": obj.get("attempt"),
            "involvesControlPlane": obj.get("involvesControlPlane"),
            "kind": obj.get("kind"),
            "nodeGroups": obj.get("nodeGroups"),
            "phaseLabel": obj.get("phaseLabel"),
            "startedAt": obj.get("startedAt"),
            "step": obj.get("step")
        })
        return _obj


