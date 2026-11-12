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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.application_container_termination import ApplicationContainerTermination
from astropulse._generated.models.application_model_status import ApplicationModelStatus
from astropulse._generated.models.application_status import ApplicationStatus
from astropulse._generated.models.application_version_entry import ApplicationVersionEntry
from astropulse._generated.models.endpoint_dns_observation import EndpointDNSObservation
from astropulse._generated.models.endpoint_exposure_status import EndpointExposureStatus
from astropulse._generated.models.notice import Notice
from astropulse._generated.models.source_type import SourceType
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class Application(BaseModel):
    """
    Application
    """ # noqa: E501
    app_name: Optional[StrictStr] = Field(default=None, description="The name of the application.", alias="appName")
    app_profile_name: Optional[StrictStr] = Field(default=None, description="The name of the application profile.", alias="appProfileName")
    applied_version: Optional[StrictStr] = Field(default=None, description="The version created by the most recent apply or rollback, such as \"v7\". Present only on a single-application read, and absent when no version is recorded.", alias="appliedVersion")
    cluster_name: Optional[StrictStr] = Field(default=None, description="The name of the cluster where the application is deployed.", alias="clusterName")
    created_timestamp: Optional[datetime] = Field(default=None, description="When the application was created.", alias="createdTimestamp")
    current_version: Optional[StrictStr] = Field(default=None, description="The version last confirmed running, as listed in the application's history. It differs from appliedVersion while a newer version deploys or after it failed, and is absent until a version has run or when appliedVersion is absent.", alias="currentVersion")
    desired_replicas: Optional[StrictInt] = Field(default=None, description="How many replicas the application's Deployments want, present whenever readyReplicas is.", alias="desiredReplicas")
    display_status: Optional[StrictStr] = Field(default=None, description="The short text to show for this application in a list when its notice changes what to show; absent otherwise, when its status's display name applies.", alias="displayStatus")
    effective_spec: Optional[StrictStr] = Field(default=None, description="The source as AstroPulse resolved it: every field the caller left unset filled in with what was actually chosen, in the same shape as the document they applied.", alias="effectiveSpec")
    endpoint: Optional[StrictStr] = Field(default=None, description="The endpoint of the application.")
    endpoint_dns: Optional[EndpointDNSObservation] = Field(default=None, description="What AstroPulse observed of the exposed hostname's DNS: whether it resolves, to what, and whether that is the address the cluster's gateway or ingress publishes. Present only on a single-application read of an exposed application.", alias="endpointDns")
    exposure: Optional[EndpointExposureStatus] = Field(default=None, description="Who can reach the application's endpoint and whether the application or the cluster chose it. Present only on a single-application read of an exposed application.")
    id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the application.")
    last_termination: Optional[ApplicationContainerTermination] = Field(default=None, description="How the application's container last exited: its exit code, reason and restart count. Present only on a single-application read of an application that is not healthy and has a recorded exit.", alias="lastTermination")
    last_updated_timestamp: Optional[datetime] = Field(default=None, description="When the application was last changed.", alias="lastUpdatedTimestamp")
    model: Optional[ApplicationModelStatus] = Field(default=None, description="What a model source reports, absent for every other source type.")
    namespace: Optional[StrictStr] = Field(default=None, description="The namespace where platform creates the application.")
    notices: Optional[List[Notice]] = Field(default=None, description="What to know about the application and what to do about it; absent when there is nothing to say.")
    org_id: Optional[StrictStr] = Field(default=None, description="The organization ID where the application is created.", alias="orgId")
    pending_version: Optional[ApplicationVersionEntry] = Field(default=None, description="The version applied that has not finished deploying, as its history entry; absent when none is waiting.", alias="pendingVersion")
    phase: Optional[ApplicationStatus] = Field(default=None, description="The operation view: is deployment work in flight right now? Provisioning or InProgress here alongside a Running status means \"serving, and syncing\".")
    ready_replicas: Optional[StrictInt] = Field(default=None, description="How many replicas of the application's Deployments are ready. Present only on a single-application read, and absent when they could not be read or the application has no Deployment.", alias="readyReplicas")
    serving_note: Optional[StrictStr] = Field(default=None, description="One sentence naming the version that serves and why, when it is not the version last requested: a deploy in flight, or an update that was refused or failed. Empty otherwise, and present only on a single-application read.", alias="servingNote")
    slug: Optional[StrictStr] = Field(default=None, description="The unique identifier of the application.")
    source_type: Optional[SourceType] = Field(default=None, description="The kind of source the application is deployed from.", alias="sourceType")
    status: Optional[ApplicationStatus] = Field(default=None, description="The lifecycle status of the application: is it serving? A resync or a rolling update of an application that is already serving leaves this on Running, because the application keeps serving its current revision throughout.")
    status_notice: Optional[Notice] = Field(default=None, description="Says what a failed, waiting or held-back status means and the one step that resolves it; absent when there is nothing to do.", alias="statusNotice")
    status_reason: Optional[StrictStr] = Field(default=None, description="Names the resource holding the application back and what it reported, when status alone does not explain it -- \"the image cannot be pulled\", not \"Provisioning\". On a Running application it names instead the custom resources AstroPulse could not health-assess, when there are any: those were confirmed applied, not confirmed serving. Empty when the application is healthy and every resource was judged, or when nothing unhealthy carried a message. Safe to display verbatim.", alias="statusReason")
    target_namespace: Optional[StrictStr] = Field(default=None, description="The target namespace where the application is deployed.", alias="targetNamespace")
    __properties: ClassVar[List[str]] = ["appName", "appProfileName", "appliedVersion", "clusterName", "createdTimestamp", "currentVersion", "desiredReplicas", "displayStatus", "effectiveSpec", "endpoint", "endpointDns", "exposure", "id", "lastTermination", "lastUpdatedTimestamp", "model", "namespace", "notices", "orgId", "pendingVersion", "phase", "readyReplicas", "servingNote", "slug", "sourceType", "status", "statusNotice", "statusReason", "targetNamespace"]

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
        """Create an instance of Application from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of endpoint_dns
        if self.endpoint_dns:
            _dict['endpointDns'] = self.endpoint_dns.to_dict()
        # override the default output from pydantic by calling `to_dict()` of exposure
        if self.exposure:
            _dict['exposure'] = self.exposure.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_termination
        if self.last_termination:
            _dict['lastTermination'] = self.last_termination.to_dict()
        # override the default output from pydantic by calling `to_dict()` of model
        if self.model:
            _dict['model'] = self.model.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in notices (list)
        _items = []
        if self.notices:
            for _item_notices in self.notices:
                if _item_notices:
                    _items.append(_item_notices.to_dict())
            _dict['notices'] = _items
        # override the default output from pydantic by calling `to_dict()` of pending_version
        if self.pending_version:
            _dict['pendingVersion'] = self.pending_version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status_notice
        if self.status_notice:
            _dict['statusNotice'] = self.status_notice.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Application from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "appName": obj.get("appName"),
            "appProfileName": obj.get("appProfileName"),
            "appliedVersion": obj.get("appliedVersion"),
            "clusterName": obj.get("clusterName"),
            "createdTimestamp": obj.get("createdTimestamp"),
            "currentVersion": obj.get("currentVersion"),
            "desiredReplicas": obj.get("desiredReplicas"),
            "displayStatus": obj.get("displayStatus"),
            "effectiveSpec": obj.get("effectiveSpec"),
            "endpoint": obj.get("endpoint"),
            "endpointDns": EndpointDNSObservation.from_dict(obj["endpointDns"]) if obj.get("endpointDns") is not None else None,
            "exposure": EndpointExposureStatus.from_dict(obj["exposure"]) if obj.get("exposure") is not None else None,
            "id": obj.get("id"),
            "lastTermination": ApplicationContainerTermination.from_dict(obj["lastTermination"]) if obj.get("lastTermination") is not None else None,
            "lastUpdatedTimestamp": obj.get("lastUpdatedTimestamp"),
            "model": ApplicationModelStatus.from_dict(obj["model"]) if obj.get("model") is not None else None,
            "namespace": obj.get("namespace"),
            "notices": [Notice.from_dict(_item) for _item in obj["notices"]] if obj.get("notices") is not None else None,
            "orgId": obj.get("orgId"),
            "pendingVersion": ApplicationVersionEntry.from_dict(obj["pendingVersion"]) if obj.get("pendingVersion") is not None else None,
            "phase": obj.get("phase"),
            "readyReplicas": obj.get("readyReplicas"),
            "servingNote": obj.get("servingNote"),
            "slug": obj.get("slug"),
            "sourceType": obj.get("sourceType"),
            "status": obj.get("status"),
            "statusNotice": Notice.from_dict(obj["statusNotice"]) if obj.get("statusNotice") is not None else None,
            "statusReason": obj.get("statusReason"),
            "targetNamespace": obj.get("targetNamespace")
        })
        return _obj


