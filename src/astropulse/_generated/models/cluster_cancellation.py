# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.cancel_cleanup_item import CancelCleanupItem
from astropulse._generated.models.cluster_cancellation_status import ClusterCancellationStatus
from astropulse._generated.models.cluster_operation_kind import ClusterOperationKind
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterCancellation(BaseModel):
    """
    ClusterCancellation
    """ # noqa: E501
    ended_at: Optional[datetime] = Field(default=None, description="When the cancel finished. Omitted while Cancelling.", alias="endedAt")
    operation: Optional[ClusterOperationKind] = Field(default=None, description="The kind of operation that was cancelled: Update, Upgrade or Rollback.")
    removed: Optional[List[CancelCleanupItem]] = Field(default=None, description="Says, for each node group the operation was adding, whether it was removed.")
    requested_at: Optional[datetime] = Field(default=None, description="When the cancel reached the operation.", alias="requestedAt")
    status: Optional[ClusterCancellationStatus] = Field(default=None, description="Where the cancel has got to: Cancelling while the operation stops and cleans up, then Cancelled.")
    __properties: ClassVar[List[str]] = ["endedAt", "operation", "removed", "requestedAt", "status"]

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
        """Create an instance of ClusterCancellation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in removed (list)
        _items = []
        if self.removed:
            for _item_removed in self.removed:
                if _item_removed:
                    _items.append(_item_removed.to_dict())
            _dict['removed'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterCancellation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "endedAt": obj.get("endedAt"),
            "operation": obj.get("operation"),
            "removed": [CancelCleanupItem.from_dict(_item) for _item in obj["removed"]] if obj.get("removed") is not None else None,
            "requestedAt": obj.get("requestedAt"),
            "status": obj.get("status")
        })
        return _obj


