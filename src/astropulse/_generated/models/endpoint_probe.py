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
from astropulse._generated.models.endpoint_probe_reach import EndpointProbeReach
from astropulse._generated.models.endpoint_probe_result import EndpointProbeResult
from astropulse._generated.models.endpoint_probe_vantage import EndpointProbeVantage
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class EndpointProbe(BaseModel):
    """
    EndpointProbe
    """ # noqa: E501
    message: Optional[StrictStr] = None
    method: Optional[StrictStr] = None
    path: Optional[StrictStr] = None
    reach: Optional[EndpointProbeReach] = Field(default=None, description="What the endpoint's hostname did when tried from inside the cluster.")
    result: Optional[EndpointProbeResult] = Field(default=None, description="What the probe found.")
    vantage: Optional[EndpointProbeVantage] = Field(default=None, description="Where the probe was sent from.")
    __properties: ClassVar[List[str]] = ["message", "method", "path", "reach", "result", "vantage"]

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
        """Create an instance of EndpointProbe from a JSON string"""
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
        """Create an instance of EndpointProbe from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "message": obj.get("message"),
            "method": obj.get("method"),
            "path": obj.get("path"),
            "reach": obj.get("reach"),
            "result": obj.get("result"),
            "vantage": obj.get("vantage")
        })
        return _obj


