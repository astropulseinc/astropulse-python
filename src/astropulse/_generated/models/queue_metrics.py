# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class QueueMetrics(BaseModel):
    """
    QueueMetrics
    """ # noqa: E501
    admission_count: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="How many replicas were admitted during the window, the denominator behind the percentiles above.", alias="admissionCount")
    admission_wait_mean_seconds: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The mean wait for quota.", alias="admissionWaitMeanSeconds")
    admission_wait_p50_seconds: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The median wait for quota among replicas admitted during the window.", alias="admissionWaitP50Seconds")
    admission_wait_p95_seconds: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The 95th-percentile wait for quota.", alias="admissionWaitP95Seconds")
    cluster_queue: Optional[StrictStr] = Field(default=None, description="The queue the replicas are admitted through.", alias="clusterQueue")
    local_queue: Optional[StrictStr] = Field(default=None, description="The application's own LocalQueue in its namespace.", alias="localQueue")
    queue_admitted_workloads: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The ClusterQueue's admitted total across every tenant, averaged over the window: how busy the shared queue is.", alias="queueAdmittedWorkloads")
    queue_pending_workloads: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The ClusterQueue's pending total across every tenant, averaged over the window.", alias="queuePendingWorkloads")
    replicas_admitted: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The mean number of replicas holding admitted quota over the window.", alias="replicasAdmitted")
    replicas_waiting: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The mean number of replicas waiting for quota. Above zero while the queue is at its quota means the queue is full, not the model slow.", alias="replicasWaiting")
    __properties: ClassVar[List[str]] = ["admissionCount", "admissionWaitMeanSeconds", "admissionWaitP50Seconds", "admissionWaitP95Seconds", "clusterQueue", "localQueue", "queueAdmittedWorkloads", "queuePendingWorkloads", "replicasAdmitted", "replicasWaiting"]

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
        """Create an instance of QueueMetrics from a JSON string"""
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
        """Create an instance of QueueMetrics from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "admissionCount": obj.get("admissionCount"),
            "admissionWaitMeanSeconds": obj.get("admissionWaitMeanSeconds"),
            "admissionWaitP50Seconds": obj.get("admissionWaitP50Seconds"),
            "admissionWaitP95Seconds": obj.get("admissionWaitP95Seconds"),
            "clusterQueue": obj.get("clusterQueue"),
            "localQueue": obj.get("localQueue"),
            "queueAdmittedWorkloads": obj.get("queueAdmittedWorkloads"),
            "queuePendingWorkloads": obj.get("queuePendingWorkloads"),
            "replicasAdmitted": obj.get("replicasAdmitted"),
            "replicasWaiting": obj.get("replicasWaiting")
        })
        return _obj


