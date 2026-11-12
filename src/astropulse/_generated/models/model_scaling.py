# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.model_scaling_metric import ModelScalingMetric
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ModelScaling(BaseModel):
    """
    ModelScaling
    """ # noqa: E501
    max_replicas: Optional[StrictInt] = Field(default=None, description="The ceiling. Defaults to minReplicas, or 1. Equal to minReplicas, the model runs at that fixed count with no autoscaler.", alias="maxReplicas")
    metric: Optional[ModelScalingMetric] = Field(default=None, description="The signal replicas follow, and needs maxReplicas above minReplicas. Left unset, AstroPulse chooses the one that suits the model.")
    min_replicas: Optional[StrictInt] = Field(default=None, description="The floor, at least 1. Scaling to zero is not supported: it needs a request-driven wake-up path in front of the predictor, and without one a model at zero replicas never comes back.", alias="minReplicas")
    __properties: ClassVar[List[str]] = ["maxReplicas", "metric", "minReplicas"]

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
        """Create an instance of ModelScaling from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of metric
        if self.metric:
            _dict['metric'] = self.metric.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ModelScaling from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "maxReplicas": obj.get("maxReplicas"),
            "metric": ModelScalingMetric.from_dict(obj["metric"]) if obj.get("metric") is not None else None,
            "minReplicas": obj.get("minReplicas")
        })
        return _obj


