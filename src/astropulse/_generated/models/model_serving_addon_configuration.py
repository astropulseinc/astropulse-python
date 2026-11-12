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
from astropulse._generated.models.addon_workload_identity import AddonWorkloadIdentity
from astropulse._generated.models.cloud_access_mode import CloudAccessMode
from astropulse._generated.models.model_serving_cache_configuration import ModelServingCacheConfiguration
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ModelServingAddonConfiguration(BaseModel):
    """
    ModelServingAddonConfiguration
    """ # noqa: E501
    cloud_access: Optional[CloudAccessMode] = Field(default=None, description="How models sign in to private model storage. Left out, it is `Identity` when `identity` is set, `Secret` when `secretRef` is set, and `None` otherwise.", alias="cloudAccess")
    identity: Optional[AddonWorkloadIdentity] = Field(default=None, description="The cloud identity models and the weight cache run as to read private model files.")
    model_cache: Optional[ModelServingCacheConfiguration] = Field(default=None, description="Keeps model weights on the cluster, so a replica starting where they are held reads them instead of downloading them. Left out, every replica downloads its own weights.", alias="modelCache")
    secret_ref: Optional[StrictStr] = Field(default=None, description="The name of a Secret in the add-on's namespace that models read private model files with. Use it only where a cloud identity can't be used; it can't be combined with `identity`.", alias="secretRef")
    __properties: ClassVar[List[str]] = ["cloudAccess", "identity", "modelCache", "secretRef"]

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
        """Create an instance of ModelServingAddonConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of identity
        if self.identity:
            _dict['identity'] = self.identity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of model_cache
        if self.model_cache:
            _dict['modelCache'] = self.model_cache.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ModelServingAddonConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cloudAccess": obj.get("cloudAccess"),
            "identity": AddonWorkloadIdentity.from_dict(obj["identity"]) if obj.get("identity") is not None else None,
            "modelCache": ModelServingCacheConfiguration.from_dict(obj["modelCache"]) if obj.get("modelCache") is not None else None,
            "secretRef": obj.get("secretRef")
        })
        return _obj


