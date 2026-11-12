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
from astropulse._generated.models.cluster_addon_node_address import ClusterAddonNodeAddress
from astropulse._generated.models.gateway_programmed_state import GatewayProgrammedState
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterAddonExposure(BaseModel):
    """
    ClusterAddonExposure
    """ # noqa: E501
    addresses: Optional[List[StrictStr]] = Field(default=None, description="The load balancer IPs or hostnames (for the gateway, the addresses its implementation published). Empty on NodePort and until the cloud provisions the balancer.")
    message: Optional[StrictStr] = Field(default=None, description="Explains an empty or partial exposure (balancer still being provisioned, agent not connected, the Gateway's own condition message).")
    node_addresses: Optional[List[ClusterAddonNodeAddress]] = Field(default=None, description="A few node addresses to dial a NodePort on; only set when Type is NodePort.", alias="nodeAddresses")
    note: Optional[StrictStr] = Field(default=None, description="Says what is not open yet and when it opens, for example that HTTPS (443) opens when the first model endpoint is exposed through the gateway.")
    ports: Optional[Dict[str, StrictInt]] = Field(default=None, description="Maps a port role (http, https) to the port to dial: the node port on NodePort, the Service port otherwise.")
    programmed: Optional[StrictStr] = Field(default=None, description="The Gateway's Programmed condition (True, False, Unknown); gateway only.")
    programmed_state: Optional[GatewayProgrammedState] = Field(default=None, description="Whether the gateway is ready for traffic, read from programmed; Unknown while it has not said. Gateway only.", alias="programmedState")
    type: Optional[StrictStr] = Field(default=None, description="The exposing Service's type: LoadBalancer, NodePort or ClusterIP. Empty until the Service has been observed.")
    __properties: ClassVar[List[str]] = ["addresses", "message", "nodeAddresses", "note", "ports", "programmed", "programmedState", "type"]

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
        """Create an instance of ClusterAddonExposure from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in node_addresses (list)
        _items = []
        if self.node_addresses:
            for _item_node_addresses in self.node_addresses:
                if _item_node_addresses:
                    _items.append(_item_node_addresses.to_dict())
            _dict['nodeAddresses'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterAddonExposure from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addresses": obj.get("addresses"),
            "message": obj.get("message"),
            "nodeAddresses": [ClusterAddonNodeAddress.from_dict(_item) for _item in obj["nodeAddresses"]] if obj.get("nodeAddresses") is not None else None,
            "note": obj.get("note"),
            "ports": obj.get("ports"),
            "programmed": obj.get("programmed"),
            "programmedState": obj.get("programmedState"),
            "type": obj.get("type")
        })
        return _obj


