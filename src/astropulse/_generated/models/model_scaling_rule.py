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
from astropulse._generated.models.model_scaling_signal import ModelScalingSignal
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ModelScalingRule(BaseModel):
    """
    ModelScalingRule
    """ # noqa: E501
    metric: Optional[ModelScalingSignal] = Field(default=None, description="What the replica count follows.")
    metric_label: Optional[StrictStr] = Field(default=None, description="The rule in a few words, such as \"CPU above 80%\" or \"Fixed at 1 replica\".", alias="metricLabel")
    target: Optional[StrictStr] = Field(default=None, description="The value the metric is held at; absent for fixed.")
    __properties: ClassVar[List[str]] = ["metric", "metricLabel", "target"]

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
        """Create an instance of ModelScalingRule from a JSON string"""
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
        """Create an instance of ModelScalingRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "metric": obj.get("metric"),
            "metricLabel": obj.get("metricLabel"),
            "target": obj.get("target")
        })
        return _obj


