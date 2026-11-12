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
from astropulse._generated.models.cluster_addon_configuration import ClusterAddonConfiguration
from astropulse._generated.models.cluster_addon_update_options import ClusterAddonUpdateOptions
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class UpdateClusterAddonRequest(BaseModel):
    """
    UpdateClusterAddonRequest
    """ # noqa: E501
    configuration: Optional[ClusterAddonConfiguration] = Field(default=None, description="Replaces the add-on's settings; omitted keeps the stored ones, and with only availability or resources those change and the stored add-on block stays. At most one add-on block may be set, the one belonging to the add-on being updated.")
    options: Optional[ClusterAddonUpdateOptions] = Field(default=None, description="Control how the update is carried out.")
    target_version: Optional[StrictStr] = Field(default=None, description="The add-on version to move to. Left out, the add-on keeps its current version and only its configuration changes.", alias="targetVersion")
    __properties: ClassVar[List[str]] = ["configuration", "options", "targetVersion"]

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
        """Create an instance of UpdateClusterAddonRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of configuration
        if self.configuration:
            _dict['configuration'] = self.configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of options
        if self.options:
            _dict['options'] = self.options.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateClusterAddonRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "configuration": ClusterAddonConfiguration.from_dict(obj["configuration"]) if obj.get("configuration") is not None else None,
            "options": ClusterAddonUpdateOptions.from_dict(obj["options"]) if obj.get("options") is not None else None,
            "targetVersion": obj.get("targetVersion")
        })
        return _obj


