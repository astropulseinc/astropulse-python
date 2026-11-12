# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from astropulse._generated.models.inference_runtime import InferenceRuntime
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class InferenceMetrics(BaseModel):
    """
    InferenceMetrics
    """ # noqa: E501
    generation_tokens_per_second: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="How many output tokens were produced each second -- what an accelerator-hour buys. Generative runtimes only.", alias="generationTokensPerSecond")
    kv_cache_utilization: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The fraction (0..1) of the accelerator's KV cache in use -- the pressure that precedes queueing. Generative runtimes only.", alias="kvCacheUtilization")
    prompt_tokens_per_second: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="How many input tokens were consumed each second. Generative runtimes only.", alias="promptTokensPerSecond")
    request_count: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="How many observations the percentiles above rest on.", alias="requestCount")
    request_latency_mean_seconds: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The mean end-to-end request latency.", alias="requestLatencyMeanSeconds")
    request_latency_p50_seconds: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The median end-to-end request latency.", alias="requestLatencyP50Seconds")
    request_latency_p95_seconds: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The 95th-percentile end-to-end request latency.", alias="requestLatencyP95Seconds")
    request_latency_p99_seconds: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The 99th-percentile end-to-end request latency.", alias="requestLatencyP99Seconds")
    requests_per_second: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="How many requests the model served each second.", alias="requestsPerSecond")
    requests_running: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The mean number of requests executing at once.", alias="requestsRunning")
    requests_waiting: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The mean number of requests queued for execution, and the signal queue-depth autoscaling follows. Rising while RequestsRunning is flat means too few replicas.", alias="requestsWaiting")
    runtime: Optional[InferenceRuntime] = Field(default=None, description="The serving runtime family the numbers came from, which says which of the fields below to expect.")
    runtime_name: Optional[StrictStr] = Field(default=None, description="The serving runtime by name -- \"sklearnserver\", \"vLLM\". Absent when the image names nothing recognisable.", alias="runtimeName")
    time_per_output_token_p50_seconds: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The median gap between output tokens once the stream has started. Generative runtimes only.", alias="timePerOutputTokenP50Seconds")
    time_per_output_token_p95_seconds: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The 95th-percentile gap between output tokens. Generative runtimes only.", alias="timePerOutputTokenP95Seconds")
    time_to_first_token_p50_seconds: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The median wait for the first token. Generative runtimes only.", alias="timeToFirstTokenP50Seconds")
    time_to_first_token_p95_seconds: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The 95th-percentile wait for the first token. Generative runtimes only.", alias="timeToFirstTokenP95Seconds")
    time_to_first_token_p99_seconds: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The 99th-percentile wait for the first token. Generative runtimes only.", alias="timeToFirstTokenP99Seconds")
    __properties: ClassVar[List[str]] = ["generationTokensPerSecond", "kvCacheUtilization", "promptTokensPerSecond", "requestCount", "requestLatencyMeanSeconds", "requestLatencyP50Seconds", "requestLatencyP95Seconds", "requestLatencyP99Seconds", "requestsPerSecond", "requestsRunning", "requestsWaiting", "runtime", "runtimeName", "timePerOutputTokenP50Seconds", "timePerOutputTokenP95Seconds", "timeToFirstTokenP50Seconds", "timeToFirstTokenP95Seconds", "timeToFirstTokenP99Seconds"]

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
        """Create an instance of InferenceMetrics from a JSON string"""
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
        """Create an instance of InferenceMetrics from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "generationTokensPerSecond": obj.get("generationTokensPerSecond"),
            "kvCacheUtilization": obj.get("kvCacheUtilization"),
            "promptTokensPerSecond": obj.get("promptTokensPerSecond"),
            "requestCount": obj.get("requestCount"),
            "requestLatencyMeanSeconds": obj.get("requestLatencyMeanSeconds"),
            "requestLatencyP50Seconds": obj.get("requestLatencyP50Seconds"),
            "requestLatencyP95Seconds": obj.get("requestLatencyP95Seconds"),
            "requestLatencyP99Seconds": obj.get("requestLatencyP99Seconds"),
            "requestsPerSecond": obj.get("requestsPerSecond"),
            "requestsRunning": obj.get("requestsRunning"),
            "requestsWaiting": obj.get("requestsWaiting"),
            "runtime": obj.get("runtime"),
            "runtimeName": obj.get("runtimeName"),
            "timePerOutputTokenP50Seconds": obj.get("timePerOutputTokenP50Seconds"),
            "timePerOutputTokenP95Seconds": obj.get("timePerOutputTokenP95Seconds"),
            "timeToFirstTokenP50Seconds": obj.get("timeToFirstTokenP50Seconds"),
            "timeToFirstTokenP95Seconds": obj.get("timeToFirstTokenP95Seconds"),
            "timeToFirstTokenP99Seconds": obj.get("timeToFirstTokenP99Seconds")
        })
        return _obj


