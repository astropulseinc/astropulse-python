# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from astropulse._generated.models.accelerator_metrics import AcceleratorMetrics
from astropulse._generated.models.inference_metrics import InferenceMetrics
from astropulse._generated.models.queue_metrics import QueueMetrics
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class MetricsSeriesPoint(BaseModel):
    """
    MetricsSeriesPoint
    """ # noqa: E501
    accelerator: Optional[AcceleratorMetrics] = Field(default=None, description="What the accelerators the application's pods hold did over the window, present only for an application actually holding a device while the accelerator-metrics add-on is installed.")
    average_cpu_cores_used: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The CPU the application used across the window.", alias="averageCpuCoresUsed")
    complete: Optional[StrictBool] = Field(default=None, description="False when the collector could not obtain a measurement for every workload instance it expected this window. Render as partial, never averaged in as if whole.")
    inference: Optional[InferenceMetrics] = Field(default=None, description="What the serving runtime measured, present only for an application that serves a model.")
    memory_working_set_bytes: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The memory it held.", alias="memoryWorkingSetBytes")
    network_receive_bytes_per_second: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The network receive and transmit rates are absent (not zero) whenever the active source cannot observe network — never present when Source is \"metrics-api\". A zero here would render as \"this application sent no traffic,\" which looks exactly like an outage on a usage graph.", alias="networkReceiveBytesPerSecond")
    network_transmit_bytes_per_second: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="networkTransmitBytesPerSecond")
    queue: Optional[QueueMetrics] = Field(default=None, description="What the cluster's workload queue did with the application's replicas, present only for an application whose pods name a queue while the workload-queueing add-on is installed.")
    source: Optional[StrictStr] = Field(default=None, description="Names which Kubernetes-native tier produced this point: kubelet-summary, metrics-api, or prometheus. Only kubelet-summary ever carries network.")
    window_end: Optional[StrictStr] = Field(default=None, description="When it closed.", alias="windowEnd")
    window_start: Optional[StrictStr] = Field(default=None, description="When this sample's window opened.", alias="windowStart")
    __properties: ClassVar[List[str]] = ["accelerator", "averageCpuCoresUsed", "complete", "inference", "memoryWorkingSetBytes", "networkReceiveBytesPerSecond", "networkTransmitBytesPerSecond", "queue", "source", "windowEnd", "windowStart"]

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
        """Create an instance of MetricsSeriesPoint from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of inference
        if self.inference:
            _dict['inference'] = self.inference.to_dict()
        # override the default output from pydantic by calling `to_dict()` of queue
        if self.queue:
            _dict['queue'] = self.queue.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MetricsSeriesPoint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accelerator": AcceleratorMetrics.from_dict(obj["accelerator"]) if obj.get("accelerator") is not None else None,
            "averageCpuCoresUsed": obj.get("averageCpuCoresUsed"),
            "complete": obj.get("complete"),
            "inference": InferenceMetrics.from_dict(obj["inference"]) if obj.get("inference") is not None else None,
            "memoryWorkingSetBytes": obj.get("memoryWorkingSetBytes"),
            "networkReceiveBytesPerSecond": obj.get("networkReceiveBytesPerSecond"),
            "networkTransmitBytesPerSecond": obj.get("networkTransmitBytesPerSecond"),
            "queue": QueueMetrics.from_dict(obj["queue"]) if obj.get("queue") is not None else None,
            "source": obj.get("source"),
            "windowEnd": obj.get("windowEnd"),
            "windowStart": obj.get("windowStart")
        })
        return _obj


