# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.endpoint_exposure import EndpointExposure
from astropulse._generated.models.gateway_auto_scaling_config import GatewayAutoScalingConfig
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class GatewayAddonConfiguration(BaseModel):
    """
    GatewayAddonConfiguration
    """ # noqa: E501
    auto_scaling: Optional[GatewayAutoScalingConfig] = Field(default=None, description="Adds and removes gateway proxy copies as load changes. Left out or off, one copy runs.", alias="autoScaling")
    enable_node_port: Optional[StrictBool] = Field(default=None, description="Serves the gateway on a port of every node instead of a cloud load balancer; turn it on for a cluster that cannot create one.", alias="enableNodePort")
    exposure: Optional[EndpointExposure] = Field(default=None, description="Who can reach the shared gateway, and the default for model endpoints that name none.")
    __properties: ClassVar[List[str]] = ["autoScaling", "enableNodePort", "exposure"]

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
        """Create an instance of GatewayAddonConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of auto_scaling
        if self.auto_scaling:
            _dict['autoScaling'] = self.auto_scaling.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GatewayAddonConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "autoScaling": GatewayAutoScalingConfig.from_dict(obj["autoScaling"]) if obj.get("autoScaling") is not None else None,
            "enableNodePort": obj.get("enableNodePort"),
            "exposure": obj.get("exposure")
        })
        return _obj


