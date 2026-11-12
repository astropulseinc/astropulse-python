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
from astropulse._generated.models.endpoint_phase import EndpointPhase
from astropulse._generated.models.model_scaling_rule import ModelScalingRule
from astropulse._generated.models.model_task import ModelTask
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ApplicationModelStatus(BaseModel):
    """
    ApplicationModelStatus
    """ # noqa: E501
    accelerator: Optional[StrictStr] = Field(default=None, description="The GPUs each replica uses, such as \"1× L4\"; absent for a model without one.")
    access_policy: Optional[StrictStr] = Field(default=None, description="The access policy that guards the model's endpoint; absent when it has none.", alias="accessPolicy")
    endpoint_phase: Optional[EndpointPhase] = Field(default=None, description="The phase of the model's access-controlled endpoint, as the cluster last reported it; absent when it has none.", alias="endpointPhase")
    external_endpoint: Optional[StrictStr] = Field(default=None, description="The address the model is configured to answer from outside the cluster, in every phase: the exposed hostname over https, with the path its runtime serves. It does not mean the address answers yet; for an endpoint protected by an access policy, the endpoint's url and message say more. Empty when the application is not exposed.", alias="externalEndpoint")
    internal_endpoint: Optional[StrictStr] = Field(default=None, description="Where the same model answers from inside the cluster, over plain http. Always present, because a workload on this cluster should call it here rather than leaving and coming back.", alias="internalEndpoint")
    scaling: Optional[ModelScalingRule] = Field(default=None, description="How the model's replicas scale, as last deployed; absent until then.")
    served_model_name: Optional[StrictStr] = Field(default=None, description="The model id to put in a request's `model` field; responses name the model by its generated name.", alias="servedModelName")
    task: Optional[ModelTask] = Field(default=None, description="What the running model serves: Generate for chat and completions, Embed for embeddings. Absent when it isn't known.")
    task_message: Optional[StrictStr] = Field(default=None, description="Says why task is absent or, for an embedding model, that it does not answer chat requests. Absent for a Generate model.", alias="taskMessage")
    __properties: ClassVar[List[str]] = ["accelerator", "accessPolicy", "endpointPhase", "externalEndpoint", "internalEndpoint", "scaling", "servedModelName", "task", "taskMessage"]

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
        """Create an instance of ApplicationModelStatus from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of scaling
        if self.scaling:
            _dict['scaling'] = self.scaling.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApplicationModelStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accelerator": obj.get("accelerator"),
            "accessPolicy": obj.get("accessPolicy"),
            "endpointPhase": obj.get("endpointPhase"),
            "externalEndpoint": obj.get("externalEndpoint"),
            "internalEndpoint": obj.get("internalEndpoint"),
            "scaling": ModelScalingRule.from_dict(obj["scaling"]) if obj.get("scaling") is not None else None,
            "servedModelName": obj.get("servedModelName"),
            "task": obj.get("task"),
            "taskMessage": obj.get("taskMessage")
        })
        return _obj


