# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.cluster_addon_model_cache_node_group import ClusterAddonModelCacheNodeGroup
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterAddonModelCacheReadiness(BaseModel):
    """
    ClusterAddonModelCacheReadiness
    """ # noqa: E501
    cache_trust_subject: Optional[StrictStr] = Field(default=None, description="The Kubernetes service account the weight cache downloads as, to grant access to in your cloud IAM.", alias="cacheTrustSubject")
    credential_secret_name: Optional[StrictStr] = Field(default=None, description="The Secret the cluster's models read private artifacts with.", alias="credentialSecretName")
    credential_secret_namespace: Optional[StrictStr] = Field(default=None, description="The namespace that Secret must exist in.", alias="credentialSecretNamespace")
    enabled: Optional[StrictBool] = Field(default=None, description="Whether the cache is turned on at all.")
    identity_annotations: Optional[Dict[str, StrictStr]] = Field(default=None, description="The cloud workload-identity annotations the add-on binds its models, and its cache's downloads, to. Absent when the add-on has no identity.", alias="identityAnnotations")
    models_trust_subject: Optional[StrictStr] = Field(default=None, description="The Kubernetes service account pattern to grant access to in your cloud IAM, covering every model on this cluster.", alias="modelsTrustSubject")
    node_groups: Optional[List[ClusterAddonModelCacheNodeGroup]] = Field(default=None, description="The node groups holding the cache: each node group whose disk is known, and the cluster's GPU node pool when it has one.", alias="nodeGroups")
    node_storage_path: Optional[StrictStr] = Field(default=None, description="The directory on each cached node the weights are held in, the same path serving containers read them from.", alias="nodeStoragePath")
    summary: Optional[StrictStr] = Field(default=None, description="Says in plain words where the cache holds the weights. Empty when the cache is off.")
    warning: Optional[StrictStr] = Field(default=None, description="Says what the cache cannot do here. Empty when nothing is wrong.")
    __properties: ClassVar[List[str]] = ["cacheTrustSubject", "credentialSecretName", "credentialSecretNamespace", "enabled", "identityAnnotations", "modelsTrustSubject", "nodeGroups", "nodeStoragePath", "summary", "warning"]

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
        """Create an instance of ClusterAddonModelCacheReadiness from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in node_groups (list)
        _items = []
        if self.node_groups:
            for _item_node_groups in self.node_groups:
                if _item_node_groups:
                    _items.append(_item_node_groups.to_dict())
            _dict['nodeGroups'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterAddonModelCacheReadiness from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cacheTrustSubject": obj.get("cacheTrustSubject"),
            "credentialSecretName": obj.get("credentialSecretName"),
            "credentialSecretNamespace": obj.get("credentialSecretNamespace"),
            "enabled": obj.get("enabled"),
            "identityAnnotations": obj.get("identityAnnotations"),
            "modelsTrustSubject": obj.get("modelsTrustSubject"),
            "nodeGroups": [ClusterAddonModelCacheNodeGroup.from_dict(_item) for _item in obj["nodeGroups"]] if obj.get("nodeGroups") is not None else None,
            "nodeStoragePath": obj.get("nodeStoragePath"),
            "summary": obj.get("summary"),
            "warning": obj.get("warning")
        })
        return _obj


