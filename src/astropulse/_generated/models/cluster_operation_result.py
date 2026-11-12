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
from astropulse._generated.models.cluster_status import ClusterStatus
from astropulse._generated.models.failure import Failure
from astropulse._generated.models.notice import Notice
from astropulse._generated.models.outcome import Outcome
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterOperationResult(BaseModel):
    """
    ClusterOperationResult
    """ # noqa: E501
    cluster_id: Optional[StrictStr] = Field(default=None, description="The cluster the operation acted on.", alias="clusterId")
    error: Optional[Failure] = Field(default=None, description="Contains failure details when the operation failed.")
    message: Optional[StrictStr] = Field(default=None, description="Provides human-readable details.")
    notices: Optional[List[Notice]] = Field(default=None, description="Say what the request did and the one next step.")
    outcome: Optional[Outcome] = Field(default=None, description="Whether the request goes ahead, when it answers with notices.")
    status: Optional[ClusterStatus] = Field(default=None, description="The cluster's status once the operation returned.")
    __properties: ClassVar[List[str]] = ["clusterId", "error", "message", "notices", "outcome", "status"]

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
        """Create an instance of ClusterOperationResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict['error'] = self.error.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in notices (list)
        _items = []
        if self.notices:
            for _item_notices in self.notices:
                if _item_notices:
                    _items.append(_item_notices.to_dict())
            _dict['notices'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterOperationResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusterId": obj.get("clusterId"),
            "error": Failure.from_dict(obj["error"]) if obj.get("error") is not None else None,
            "message": obj.get("message"),
            "notices": [Notice.from_dict(_item) for _item in obj["notices"]] if obj.get("notices") is not None else None,
            "outcome": obj.get("outcome"),
            "status": obj.get("status")
        })
        return _obj


