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
from astropulse._generated.models.workload_cluster_queue import WorkloadClusterQueue
from astropulse._generated.models.workload_local_queue import WorkloadLocalQueue
from astropulse._generated.models.workload_queueing_gang_scheduling import WorkloadQueueingGangScheduling
from astropulse._generated.models.workload_queueing_integration import WorkloadQueueingIntegration
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class WorkloadQueueingAddonConfiguration(BaseModel):
    """
    WorkloadQueueingAddonConfiguration
    """ # noqa: E501
    cluster_queues: Optional[List[WorkloadClusterQueue]] = Field(default=None, description="The queues that share the cluster's capacity; a model application picks one in `model.queue.name`. Left out, one queue named `default` gets the cluster's whole GPU capacity.", alias="clusterQueues")
    gang_scheduling: Optional[WorkloadQueueingGangScheduling] = Field(default=None, description="Starts a workload only when all its pods can run: if they aren't all ready within the timeout, it is stopped and queued again.", alias="gangScheduling")
    integrations: Optional[List[WorkloadQueueingIntegration]] = Field(default=None, description="The kinds of workload the queues accept; a kind other than batch/job needs its own controller on the cluster. Left out, only batch/job is accepted.")
    local_queues: Optional[List[WorkloadLocalQueue]] = Field(default=None, description="Connects namespaces of yours to a queue. An application that names a queue gets its own connection without one here.", alias="localQueues")
    __properties: ClassVar[List[str]] = ["clusterQueues", "gangScheduling", "integrations", "localQueues"]

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
        """Create an instance of WorkloadQueueingAddonConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in cluster_queues (list)
        _items = []
        if self.cluster_queues:
            for _item_cluster_queues in self.cluster_queues:
                if _item_cluster_queues:
                    _items.append(_item_cluster_queues.to_dict())
            _dict['clusterQueues'] = _items
        # override the default output from pydantic by calling `to_dict()` of gang_scheduling
        if self.gang_scheduling:
            _dict['gangScheduling'] = self.gang_scheduling.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in local_queues (list)
        _items = []
        if self.local_queues:
            for _item_local_queues in self.local_queues:
                if _item_local_queues:
                    _items.append(_item_local_queues.to_dict())
            _dict['localQueues'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WorkloadQueueingAddonConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusterQueues": [WorkloadClusterQueue.from_dict(_item) for _item in obj["clusterQueues"]] if obj.get("clusterQueues") is not None else None,
            "gangScheduling": WorkloadQueueingGangScheduling.from_dict(obj["gangScheduling"]) if obj.get("gangScheduling") is not None else None,
            "integrations": obj.get("integrations"),
            "localQueues": [WorkloadLocalQueue.from_dict(_item) for _item in obj["localQueues"]] if obj.get("localQueues") is not None else None
        })
        return _obj


