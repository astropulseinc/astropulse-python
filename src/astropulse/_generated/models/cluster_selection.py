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
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.cloud_provider_config import CloudProviderConfig
from astropulse._generated.models.cluster import Cluster
from astropulse._generated.models.cluster_selection_type import ClusterSelectionType
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterSelection(BaseModel):
    """
    ClusterSelection
    """ # noqa: E501
    cloud_provider: Optional[CloudProviderConfig] = Field(default=None, description="Specifies the cloud provider and region where the application will be deployed.", alias="cloudProvider")
    cluster: Optional[Cluster] = Field(default=None, description="Specifies the cluster name where the application will be deployed.")
    type: Optional[ClusterSelectionType] = Field(default=None, description="Of cluster selection")
    __properties: ClassVar[List[str]] = ["cloudProvider", "cluster", "type"]

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
        """Create an instance of ClusterSelection from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cloud_provider
        if self.cloud_provider:
            _dict['cloudProvider'] = self.cloud_provider.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cluster
        if self.cluster:
            _dict['cluster'] = self.cluster.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterSelection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cloudProvider": CloudProviderConfig.from_dict(obj["cloudProvider"]) if obj.get("cloudProvider") is not None else None,
            "cluster": Cluster.from_dict(obj["cluster"]) if obj.get("cluster") is not None else None,
            "type": obj.get("type")
        })
        return _obj


