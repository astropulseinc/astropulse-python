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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.audit_action import AuditAction
from astropulse._generated.models.audit_actor_type import AuditActorType
from astropulse._generated.models.audit_event_type import AuditEventType
from astropulse._generated.models.audit_source import AuditSource
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class AuditEvent(BaseModel):
    """
    AuditEvent
    """ # noqa: E501
    action: Optional[AuditAction] = Field(default=None, description="What was done to the resource, or for a dry run what was checked.")
    actor_type: Optional[AuditActorType] = Field(default=None, description="How the actor signed in.", alias="actorType")
    api_key_id: Optional[StrictStr] = Field(default=None, description="The API key the actor used, when one was used", alias="apiKeyId")
    details: Optional[Dict[str, Any]] = Field(default=None, description="Contains additional event-specific information")
    dry_run: Optional[StrictBool] = Field(default=None, description="True when the request only checked the action and changed nothing", alias="dryRun")
    event_type: Optional[AuditEventType] = Field(default=None, description="The kind of resource the event is about, such as Cluster or Addon; Request when the request named none.", alias="eventType")
    id: Optional[StrictStr] = Field(default=None, description="The unique identifier for the audit event")
    ip_address: Optional[StrictStr] = Field(default=None, description="Of the user who performed the action", alias="ipAddress")
    method: Optional[StrictStr] = Field(default=None, description="The HTTP method of the request that made the change, such as POST or DELETE")
    org_id: Optional[StrictStr] = Field(default=None, description="The organization ID where the event occurred", alias="orgId")
    reason: Optional[StrictStr] = Field(default=None, description="The message a failed action answered with; omitted when the action succeeded or no message was recorded")
    request_id: Optional[StrictStr] = Field(default=None, description="The trace/request ID for correlation", alias="requestId")
    resource: Optional[AuditEventType] = Field(default=None, description="The kind of resource acted upon, the same as eventType.")
    resource_id: Optional[StrictStr] = Field(default=None, description="Names the resource, after the resources it belongs to, such as prod-01/nginx-ingress for an add-on of cluster prod-01", alias="resourceId")
    resource_ids: Optional[Dict[str, StrictStr]] = Field(default=None, description="The route's parameters and their values, such as appName and clusterName", alias="resourceIds")
    resource_name: Optional[StrictStr] = Field(default=None, description="The name of the resource, such as a cluster, application or API key name; omitted when the event did not record one", alias="resourceName")
    route: Optional[StrictStr] = Field(default=None, description="The API route of that request, with its parameters named, such as /api/v1/applications/:appName")
    source: Optional[AuditSource] = Field(default=None, description="The channel the action came through; absent when none was recorded.")
    status_code: Optional[StrictInt] = Field(default=None, description="The HTTP status the action answered with; 0 when none was recorded", alias="statusCode")
    success: Optional[StrictBool] = Field(default=None, description="Indicates whether the action was successful")
    summary: Optional[StrictStr] = Field(default=None, description="One readable line describing the event, such as \"Started upgrading cluster prod-01 to 1.31\"; it never contains the actor's name, email or IP address")
    timestamp: Optional[datetime] = Field(default=None, description="When the event occurred")
    user_agent: Optional[StrictStr] = Field(default=None, description="Of the client that performed the action", alias="userAgent")
    user_id: Optional[StrictStr] = Field(default=None, description="The ID of the user who performed the action", alias="userId")
    user_profile: Optional[Dict[str, Any]] = Field(default=None, description="The actor (name, email, roles) when they acted. Name and email are in full for org owners and admins, masked for everyone else and in exports.", alias="userProfile")
    __properties: ClassVar[List[str]] = ["action", "actorType", "apiKeyId", "details", "dryRun", "eventType", "id", "ipAddress", "method", "orgId", "reason", "requestId", "resource", "resourceId", "resourceIds", "resourceName", "route", "source", "statusCode", "success", "summary", "timestamp", "userAgent", "userId", "userProfile"]

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
        """Create an instance of AuditEvent from a JSON string"""
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
        """Create an instance of AuditEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "action": obj.get("action"),
            "actorType": obj.get("actorType"),
            "apiKeyId": obj.get("apiKeyId"),
            "details": obj.get("details"),
            "dryRun": obj.get("dryRun"),
            "eventType": obj.get("eventType"),
            "id": obj.get("id"),
            "ipAddress": obj.get("ipAddress"),
            "method": obj.get("method"),
            "orgId": obj.get("orgId"),
            "reason": obj.get("reason"),
            "requestId": obj.get("requestId"),
            "resource": obj.get("resource"),
            "resourceId": obj.get("resourceId"),
            "resourceIds": obj.get("resourceIds"),
            "resourceName": obj.get("resourceName"),
            "route": obj.get("route"),
            "source": obj.get("source"),
            "statusCode": obj.get("statusCode"),
            "success": obj.get("success"),
            "summary": obj.get("summary"),
            "timestamp": obj.get("timestamp"),
            "userAgent": obj.get("userAgent"),
            "userId": obj.get("userId"),
            "userProfile": obj.get("userProfile")
        })
        return _obj


