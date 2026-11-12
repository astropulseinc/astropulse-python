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
from astropulse._generated.models.failure import Failure
from astropulse._generated.models.kubeconfig import Kubeconfig
from astropulse._generated.models.kubeconfig_state import KubeconfigState
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class KubeconfigGeneration(BaseModel):
    """
    KubeconfigGeneration
    """ # noqa: E501
    cluster_id: Optional[StrictStr] = Field(default=None, description="The cluster the kubeconfig is for.", alias="clusterId")
    error: Optional[Failure] = Field(default=None, description="Says why generation failed, when it did.")
    kubeconfig: Optional[Kubeconfig] = Field(default=None, description="Present once there is one.")
    status: Optional[KubeconfigState] = Field(default=None, description="How far generation has got. Poll the GET endpoint until it is Provisioned.")
    __properties: ClassVar[List[str]] = ["clusterId", "error", "kubeconfig", "status"]

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
        """Create an instance of KubeconfigGeneration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict['error'] = self.error.to_dict()
        # override the default output from pydantic by calling `to_dict()` of kubeconfig
        if self.kubeconfig:
            _dict['kubeconfig'] = self.kubeconfig.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of KubeconfigGeneration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusterId": obj.get("clusterId"),
            "error": Failure.from_dict(obj["error"]) if obj.get("error") is not None else None,
            "kubeconfig": Kubeconfig.from_dict(obj["kubeconfig"]) if obj.get("kubeconfig") is not None else None,
            "status": obj.get("status")
        })
        return _obj


