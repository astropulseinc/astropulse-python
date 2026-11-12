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
from astropulse._generated.models.model_cache import ModelCache
from astropulse._generated.models.model_format import ModelFormat
from astropulse._generated.models.model_queue import ModelQueue
from astropulse._generated.models.model_resources import ModelResources
from astropulse._generated.models.model_runtime import ModelRuntime
from astropulse._generated.models.model_scaling import ModelScaling
from astropulse._generated.models.model_serving import ModelServing
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class Model(BaseModel):
    """
    Model
    """ # noqa: E501
    cache: Optional[ModelCache] = Field(default=None, description="Serves the artifact from the node's own disk instead of downloading it on every replica start. The target cluster's model-serving add-on must have its modelCache enabled.")
    format: Optional[ModelFormat] = Field(default=None, description="The model format the serving runtime is selected from. Defaults to vLLM for hf:// artifacts, which is where the weights come from rather than what runs them; required otherwise. Like uri, it is fixed once the application has served.")
    queue: Optional[ModelQueue] = Field(default=None, description="Admits the predictor's replicas through a workload queue: a ClusterQueue the target cluster's workload-queueing add-on declares. AstroPulse stamps Kueue's queue-name label on the predictor pods and renders a LocalQueue this application owns in its namespace; Kueue admits the replicas against the queue's quota. Whether a serving workload belongs in a queue is the builder's call.")
    resources: Optional[ModelResources] = Field(default=None, description="Declares the hardware one replica needs.")
    runtime: Optional[ModelRuntime] = Field(default=None, description="Pins the serving runtime instead of letting the format choose. Like uri, it is fixed once the application has served.")
    scaling: Optional[ModelScaling] = Field(default=None, description="Bounds the replica count.")
    serving: Optional[ModelServing] = Field(default=None, description="Configures the inference API the model is served with.")
    uri: Optional[StrictStr] = Field(default=None, description="The model artifact. It can be corrected until the application has served, and is fixed after that.  Point it at bytes that cannot change underneath it. AstroPulse caches what it downloads and shares that copy between applications using the same artifact, so an artifact that moves is served from the copy taken the first time, and rolling back restores the spec rather than the same model. These forms name one exact artifact:  hf://<org>/<repo>:<40-character commit sha> oci://<registry>/<repository>@sha256:<64 hex digits> s3://<bucket>/<object>?versionId=<version id> gs://<bucket>/<object>?generation=<generation>  A Hugging Face branch or tag, an image tag, or a bucket key with no version names whatever was last written there.  pvc://<claim>/<path> is an existing volume, mounted as it is, with whatever guarantee its owner provides. Azure Blob Storage is accepted as https://<account>.blob.core.windows.net/<container>/<path>. Neither is copied by AstroPulse.  The only query parameters accepted are the two above, each on its own scheme. No credentials may appear in the URI: how a private artifact is read is set on the cluster.")
    __properties: ClassVar[List[str]] = ["cache", "format", "queue", "resources", "runtime", "scaling", "serving", "uri"]

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
        """Create an instance of Model from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cache
        if self.cache:
            _dict['cache'] = self.cache.to_dict()
        # override the default output from pydantic by calling `to_dict()` of queue
        if self.queue:
            _dict['queue'] = self.queue.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resources
        if self.resources:
            _dict['resources'] = self.resources.to_dict()
        # override the default output from pydantic by calling `to_dict()` of runtime
        if self.runtime:
            _dict['runtime'] = self.runtime.to_dict()
        # override the default output from pydantic by calling `to_dict()` of scaling
        if self.scaling:
            _dict['scaling'] = self.scaling.to_dict()
        # override the default output from pydantic by calling `to_dict()` of serving
        if self.serving:
            _dict['serving'] = self.serving.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Model from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cache": ModelCache.from_dict(obj["cache"]) if obj.get("cache") is not None else None,
            "format": obj.get("format"),
            "queue": ModelQueue.from_dict(obj["queue"]) if obj.get("queue") is not None else None,
            "resources": ModelResources.from_dict(obj["resources"]) if obj.get("resources") is not None else None,
            "runtime": ModelRuntime.from_dict(obj["runtime"]) if obj.get("runtime") is not None else None,
            "scaling": ModelScaling.from_dict(obj["scaling"]) if obj.get("scaling") is not None else None,
            "serving": ModelServing.from_dict(obj["serving"]) if obj.get("serving") is not None else None,
            "uri": obj.get("uri")
        })
        return _obj


