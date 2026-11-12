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
from astropulse._generated.models.model_accelerator import ModelAccelerator
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ModelResources(BaseModel):
    """
    ModelResources
    """ # noqa: E501
    accelerator: Optional[ModelAccelerator] = Field(default=None, description="The accelerator one replica needs, in AstroPulse's normalized vocabulary (the same identity the cluster's node groups declare with countPerNode).")
    cpu: Optional[StrictStr] = Field(default=None, description="The CPU budget for one replica, as a Kubernetes quantity (\"2\", \"500m\"). Left unset, a generative model on GPUs gets 3 per GPU and any other model takes KServe's default. It matters most for CPU inference, where the runtime's throughput is the core count.")
    memory: Optional[StrictStr] = Field(default=None, description="The memory limit for one replica, as a Kubernetes quantity (\"4Gi\"). Defaults to 4Gi for a generative model on CPU and 8Gi on a GPU; raise it when a replica runs out of memory.")
    __properties: ClassVar[List[str]] = ["accelerator", "cpu", "memory"]

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
        """Create an instance of ModelResources from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of accelerator
        if self.accelerator:
            _dict['accelerator'] = self.accelerator.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ModelResources from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accelerator": ModelAccelerator.from_dict(obj["accelerator"]) if obj.get("accelerator") is not None else None,
            "cpu": obj.get("cpu"),
            "memory": obj.get("memory")
        })
        return _obj


