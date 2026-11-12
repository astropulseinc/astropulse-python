# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from astropulse._generated.models.k8s_cluster_spec import K8sClusterSpec
from astropulse._generated.models.provider import Provider
from astropulse._generated.models.provisioner import Provisioner
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class K8sClusterRequest(BaseModel):
    """
    K8sClusterRequest
    """ # noqa: E501
    cluster_name: Annotated[str, Field(min_length=1, strict=True, max_length=50)] = Field(description="The cluster name (required, 1-50 characters, valid DNS name). Format: lowercase alphanumeric and hyphens, must start with a letter.", alias="clusterName")
    cluster_spec: K8sClusterSpec = Field(description="The cluster specification containing control plane and data plane configuration (required)", alias="clusterSpec")
    provider: Provider = Field(description="The cloud provider (required). One of: aws, azure, gcp.")
    provisioner: Provisioner = Field(description="The provisioner configuration specifying which cloud provider and settings to use (required)")
    region: Annotated[str, Field(min_length=1, strict=True)] = Field(description="The cloud provider region (required, minimum 1 character). Provider-specific format: AWS (e.g. \"us-west-2\"), GCP (e.g. \"us-central1\"), Azure (e.g. \"eastus\").")
    __properties: ClassVar[List[str]] = ["clusterName", "clusterSpec", "provider", "provisioner", "region"]

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
        """Create an instance of K8sClusterRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cluster_spec
        if self.cluster_spec:
            _dict['clusterSpec'] = self.cluster_spec.to_dict()
        # override the default output from pydantic by calling `to_dict()` of provisioner
        if self.provisioner:
            _dict['provisioner'] = self.provisioner.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of K8sClusterRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusterName": obj.get("clusterName"),
            "clusterSpec": K8sClusterSpec.from_dict(obj["clusterSpec"]) if obj.get("clusterSpec") is not None else None,
            "provider": obj.get("provider"),
            "provisioner": Provisioner.from_dict(obj["provisioner"]) if obj.get("provisioner") is not None else None,
            "region": obj.get("region")
        })
        return _obj


