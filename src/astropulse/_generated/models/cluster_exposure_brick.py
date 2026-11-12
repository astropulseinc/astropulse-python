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
from astropulse._generated.models.cluster_exposure_owner import ClusterExposureOwner
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterExposureBrick(BaseModel):
    """
    ClusterExposureBrick
    """ # noqa: E501
    gateway_routes: Optional[StrictBool] = Field(default=None, description="(external-dns only) reports whether HTTPRoute hostnames get a DNS record: the add-on applied with gatewayRoutes, or an observed controller running the gateway-httproute source.", alias="gatewayRoutes")
    message: Optional[StrictStr] = Field(default=None, description="One sentence about the brick. On externalDNS it says who writes the DNS record for an application's hostname: AstroPulse, a DNS controller you run, or you.")
    name: Optional[StrictStr] = None
    namespace: Optional[StrictStr] = Field(default=None, description="The namespace and name locate the observed controller.")
    observed: Optional[StrictBool] = Field(default=None, description="Reports whether the agent saw a running controller.")
    owner: Optional[ClusterExposureOwner] = Field(default=None, description="Who runs the brick on the cluster.")
    __properties: ClassVar[List[str]] = ["gatewayRoutes", "message", "name", "namespace", "observed", "owner"]

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
        """Create an instance of ClusterExposureBrick from a JSON string"""
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
        """Create an instance of ClusterExposureBrick from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "gatewayRoutes": obj.get("gatewayRoutes"),
            "message": obj.get("message"),
            "name": obj.get("name"),
            "namespace": obj.get("namespace"),
            "observed": obj.get("observed"),
            "owner": obj.get("owner")
        })
        return _obj


