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
from astropulse._generated.models.cluster_status import ClusterStatus
from astropulse._generated.models.provisioner_type import ProvisionerType
from astropulse._generated.models.state_tone import StateTone
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class CloudAccountCluster(BaseModel):
    """
    CloudAccountCluster
    """ # noqa: E501
    message: Optional[StrictStr] = Field(default=None, description="Says in one sentence what your team must do before AstroPulse can manage the cluster; empty when nothing.")
    name: Optional[StrictStr] = Field(default=None, description="The cluster's name.")
    provisioner: Optional[ProvisionerType] = Field(default=None, description="How the cluster is managed; omitted when AstroPulse does not know.")
    state: Optional[ClusterStatus] = Field(default=None, description="The cluster's state.")
    state_tone: Optional[StateTone] = Field(default=None, description="How the state reads at a glance.", alias="stateTone")
    __properties: ClassVar[List[str]] = ["message", "name", "provisioner", "state", "stateTone"]

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
        """Create an instance of CloudAccountCluster from a JSON string"""
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
        """Create an instance of CloudAccountCluster from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "message": obj.get("message"),
            "name": obj.get("name"),
            "provisioner": obj.get("provisioner"),
            "state": obj.get("state"),
            "stateTone": obj.get("stateTone")
        })
        return _obj


