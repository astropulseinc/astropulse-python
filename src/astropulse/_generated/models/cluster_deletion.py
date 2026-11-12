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
from astropulse._generated.models.cluster_delete_dry_run import ClusterDeleteDryRun
from astropulse._generated.models.cluster_status import ClusterStatus
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterDeletion(BaseModel):
    """
    ClusterDeletion
    """ # noqa: E501
    already_running: Optional[StrictBool] = Field(default=None, description="True when the cluster was already being deleted, so nothing new was started.", alias="alreadyRunning")
    cluster_id: Optional[StrictStr] = Field(default=None, description="The id of the cluster's delete operation; empty on a dry run.", alias="clusterId")
    dry_run: Optional[ClusterDeleteDryRun] = Field(default=None, description="Present only on a dry run, and says what the delete would leave in your cloud account. Nothing was deleted.", alias="dryRun")
    message: Optional[StrictStr] = Field(default=None, description="Says what happened; with recordOnly, it lists what is left in your cloud account.")
    status: Optional[ClusterStatus] = Field(default=None, description="The cluster's state once the delete was accepted; empty on a dry run.")
    __properties: ClassVar[List[str]] = ["alreadyRunning", "clusterId", "dryRun", "message", "status"]

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
        """Create an instance of ClusterDeletion from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of dry_run
        if self.dry_run:
            _dict['dryRun'] = self.dry_run.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterDeletion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alreadyRunning": obj.get("alreadyRunning"),
            "clusterId": obj.get("clusterId"),
            "dryRun": ClusterDeleteDryRun.from_dict(obj["dryRun"]) if obj.get("dryRun") is not None else None,
            "message": obj.get("message"),
            "status": obj.get("status")
        })
        return _obj


