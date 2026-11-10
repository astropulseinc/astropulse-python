# AuditEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**AuditAction**](AuditAction.md) | What was done to the resource, or for a dry run what was checked. | [optional] 
**actor_type** | [**AuditActorType**](AuditActorType.md) | How the actor signed in. | [optional] 
**api_key_id** | **str** | The API key the actor used, when one was used | [optional] 
**details** | **Dict[str, object]** | Contains additional event-specific information | [optional] 
**dry_run** | **bool** | True when the request only checked the action and changed nothing | [optional] 
**event_type** | [**AuditEventType**](AuditEventType.md) | The kind of resource the event is about, such as Cluster or Addon; Request when the request named none. | [optional] 
**id** | **str** | The unique identifier for the audit event | [optional] 
**ip_address** | **str** | Of the user who performed the action | [optional] 
**method** | **str** | The HTTP method of the request that made the change, such as POST or DELETE | [optional] 
**org_id** | **str** | The organization ID where the event occurred | [optional] 
**reason** | **str** | The message a failed action answered with; omitted when the action succeeded or no message was recorded | [optional] 
**request_id** | **str** | The trace/request ID for correlation | [optional] 
**resource** | [**AuditEventType**](AuditEventType.md) | The kind of resource acted upon, the same as eventType. | [optional] 
**resource_id** | **str** | Names the resource, after the resources it belongs to, such as prod-01/nginx-ingress for an add-on of cluster prod-01 | [optional] 
**resource_ids** | **Dict[str, str]** | The route&#39;s parameters and their values, such as appName and clusterName | [optional] 
**resource_name** | **str** | The name of the resource, such as a cluster, application or API key name; omitted when the event did not record one | [optional] 
**route** | **str** | The API route of that request, with its parameters named, such as /api/v1/applications/:appName | [optional] 
**source** | [**AuditSource**](AuditSource.md) | The channel the action came through; absent when none was recorded. | [optional] 
**status_code** | **int** | The HTTP status the action answered with; 0 when none was recorded | [optional] 
**success** | **bool** | Indicates whether the action was successful | [optional] 
**summary** | **str** | One readable line describing the event, such as \&quot;Started upgrading cluster prod-01 to 1.31\&quot;; it never contains the actor&#39;s name, email or IP address | [optional] 
**timestamp** | **datetime** | When the event occurred | [optional] 
**user_agent** | **str** | Of the client that performed the action | [optional] 
**user_id** | **str** | The ID of the user who performed the action | [optional] 
**user_profile** | **Dict[str, object]** | The actor (name, email, roles) when they acted. Name and email are in full for org owners and admins, masked for everyone else and in exports. | [optional] 

## Example

```python
from astropulse._generated.models.audit_event import AuditEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AuditEvent from a JSON string
audit_event_instance = AuditEvent.from_json(json)
# print the JSON string representation of the object
print(AuditEvent.to_json())

# convert the object into a dict
audit_event_dict = audit_event_instance.to_dict()
# create an instance of AuditEvent from a dict
audit_event_from_dict = AuditEvent.from_dict(audit_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


