# Application


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** | The name of the application. | [optional] 
**app_profile_name** | **str** | The name of the application profile. | [optional] 
**applied_version** | **str** | The version created by the most recent apply or rollback, such as \&quot;v7\&quot;. Present only on a single-application read, and absent when no version is recorded. | [optional] 
**cluster_name** | **str** | The name of the cluster where the application is deployed. | [optional] 
**created_timestamp** | **datetime** | When the application was created. | [optional] 
**current_version** | **str** | The version last confirmed running, as listed in the application&#39;s history. It differs from appliedVersion while a newer version deploys or after it failed, and is absent until a version has run or when appliedVersion is absent. | [optional] 
**desired_replicas** | **int** | How many replicas the application&#39;s Deployments want, present whenever readyReplicas is. | [optional] 
**display_status** | **str** | The short text to show for this application in a list when its notice changes what to show; absent otherwise, when its status&#39;s display name applies. | [optional] 
**effective_spec** | **str** | The source as AstroPulse resolved it: every field the caller left unset filled in with what was actually chosen, in the same shape as the document they applied. | [optional] 
**endpoint** | **str** | The endpoint of the application. | [optional] 
**endpoint_dns** | [**EndpointDNSObservation**](EndpointDNSObservation.md) | What AstroPulse observed of the exposed hostname&#39;s DNS: whether it resolves, to what, and whether that is the address the cluster&#39;s gateway or ingress publishes. Present only on a single-application read of an exposed application. | [optional] 
**exposure** | [**EndpointExposureStatus**](EndpointExposureStatus.md) | Who can reach the application&#39;s endpoint and whether the application or the cluster chose it. Present only on a single-application read of an exposed application. | [optional] 
**id** | **str** | The unique identifier of the application. | [optional] 
**last_termination** | [**ApplicationContainerTermination**](ApplicationContainerTermination.md) | How the application&#39;s container last exited: its exit code, reason and restart count. Present only on a single-application read of an application that is not healthy and has a recorded exit. | [optional] 
**last_updated_timestamp** | **datetime** | When the application was last changed. | [optional] 
**model** | [**ApplicationModelStatus**](ApplicationModelStatus.md) | What a model source reports, absent for every other source type. | [optional] 
**namespace** | **str** | The namespace where platform creates the application. | [optional] 
**notices** | [**List[Notice]**](Notice.md) | What to know about the application and what to do about it; absent when there is nothing to say. | [optional] 
**org_id** | **str** | The organization ID where the application is created. | [optional] 
**pending_version** | [**ApplicationVersionEntry**](ApplicationVersionEntry.md) | The version applied that has not finished deploying, as its history entry; absent when none is waiting. | [optional] 
**phase** | [**ApplicationStatus**](ApplicationStatus.md) | The operation view: is deployment work in flight right now? Provisioning or InProgress here alongside a Running status means \&quot;serving, and syncing\&quot;. | [optional] 
**ready_replicas** | **int** | How many replicas of the application&#39;s Deployments are ready. Present only on a single-application read, and absent when they could not be read or the application has no Deployment. | [optional] 
**serving_note** | **str** | One sentence naming the version that serves and why, when it is not the version last requested: a deploy in flight, or an update that was refused or failed. Empty otherwise, and present only on a single-application read. | [optional] 
**slug** | **str** | The unique identifier of the application. | [optional] 
**source_type** | [**SourceType**](SourceType.md) | The kind of source the application is deployed from. | [optional] 
**status** | [**ApplicationStatus**](ApplicationStatus.md) | The lifecycle status of the application: is it serving? A resync or a rolling update of an application that is already serving leaves this on Running, because the application keeps serving its current revision throughout. | [optional] 
**status_notice** | [**Notice**](Notice.md) | Says what a failed, waiting or held-back status means and the one step that resolves it; absent when there is nothing to do. | [optional] 
**status_reason** | **str** | Names the resource holding the application back and what it reported, when status alone does not explain it -- \&quot;the image cannot be pulled\&quot;, not \&quot;Provisioning\&quot;. On a Running application it names instead the custom resources AstroPulse could not health-assess, when there are any: those were confirmed applied, not confirmed serving. Empty when the application is healthy and every resource was judged, or when nothing unhealthy carried a message. Safe to display verbatim. | [optional] 
**target_namespace** | **str** | The target namespace where the application is deployed. | [optional] 

## Example

```python
from astropulse._generated.models.application import Application

# TODO update the JSON string below
json = "{}"
# create an instance of Application from a JSON string
application_instance = Application.from_json(json)
# print the JSON string representation of the object
print(Application.to_json())

# convert the object into a dict
application_dict = application_instance.to_dict()
# create an instance of Application from a dict
application_from_dict = Application.from_dict(application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


