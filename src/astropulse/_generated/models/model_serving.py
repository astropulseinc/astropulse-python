# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.model_api_format import ModelAPIFormat
from astropulse._generated.models.model_multimodal import ModelMultimodal
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ModelServing(BaseModel):
    """
    ModelServing
    """ # noqa: E501
    api_format: Optional[ModelAPIFormat] = Field(default=None, description="The API the endpoint speaks. Omitted, a generative runtime serves its OpenAI-compatible API and any other runtime its own prediction API.", alias="apiFormat")
    kv_cache_size: Optional[StrictStr] = Field(default=None, description="The memory the generative runtime reserves for its KV cache, as a Kubernetes quantity (\"2Gi\"): out of resources.memory on CPU, device memory per GPU on a GPU. Defaults to a quarter of resources.memory on CPU and to what the runtime works out from the device on a GPU; an embedding model ignores it.", alias="kvCacheSize")
    max_concurrent_requests: Optional[StrictInt] = Field(default=None, description="The most requests one replica serves at once; further requests wait, where scaling.metric.requestsWaiting counts them. Defaults to two per CPU core on CPU and to the runtime's own limit on a GPU.", alias="maxConcurrentRequests")
    max_context_tokens: Optional[StrictInt] = Field(default=None, description="Caps the context window the runtime allocates for.", alias="maxContextTokens")
    multimodal: Optional[ModelMultimodal] = Field(default=None, description="Caps how many media items one request may carry, for a vision, video or audio model. Such a model is one model, not a pipeline: the generative runtime loads the encoder in the same process and accepts image, video and audio parts on the same chat-completions endpoint the text-only model answers on.  These are per-request limits the runtime allocates for, not quotas applied after the fact. The engine reserves memory against them when it starts, so raising a limit costs memory on every replica whether or not a caller ever sends that many items, and a request carrying more than the limit is refused rather than queued. Leaving a modality unset keeps the runtime's own limit for it.  Generative runtimes only, and refused behind a serving runtime AstroPulse did not install: the limit resolves into that runtime's own flag, and AstroPulse renders flags only for the runtimes it installs.")
    __properties: ClassVar[List[str]] = ["apiFormat", "kvCacheSize", "maxConcurrentRequests", "maxContextTokens", "multimodal"]

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
        """Create an instance of ModelServing from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of multimodal
        if self.multimodal:
            _dict['multimodal'] = self.multimodal.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ModelServing from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "apiFormat": obj.get("apiFormat"),
            "kvCacheSize": obj.get("kvCacheSize"),
            "maxConcurrentRequests": obj.get("maxConcurrentRequests"),
            "maxContextTokens": obj.get("maxContextTokens"),
            "multimodal": ModelMultimodal.from_dict(obj["multimodal"]) if obj.get("multimodal") is not None else None
        })
        return _obj


