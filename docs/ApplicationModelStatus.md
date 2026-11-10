# ApplicationModelStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accelerator** | **str** | The GPUs each replica uses, such as \&quot;1× L4\&quot;; absent for a model without one. | [optional] 
**access_policy** | **str** | The access policy that guards the model&#39;s endpoint; absent when it has none. | [optional] 
**endpoint_phase** | [**EndpointPhase**](EndpointPhase.md) | The phase of the model&#39;s access-controlled endpoint, as the cluster last reported it; absent when it has none. | [optional] 
**external_endpoint** | **str** | The address the model is configured to answer from outside the cluster, in every phase: the exposed hostname over https, with the path its runtime serves. It does not mean the address answers yet; for an endpoint protected by an access policy, the endpoint&#39;s url and message say more. Empty when the application is not exposed. | [optional] 
**internal_endpoint** | **str** | Where the same model answers from inside the cluster, over plain http. Always present, because a workload on this cluster should call it here rather than leaving and coming back. | [optional] 
**scaling** | [**ModelScalingRule**](ModelScalingRule.md) | How the model&#39;s replicas scale, as last deployed; absent until then. | [optional] 
**served_model_name** | **str** | The model id to put in a request&#39;s &#x60;model&#x60; field; responses name the model by its generated name. | [optional] 
**task** | [**ModelTask**](ModelTask.md) | What the running model serves: Generate for chat and completions, Embed for embeddings. Absent when it isn&#39;t known. | [optional] 
**task_message** | **str** | Says why task is absent or, for an embedding model, that it does not answer chat requests. Absent for a Generate model. | [optional] 

## Example

```python
from astropulse._generated.models.application_model_status import ApplicationModelStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationModelStatus from a JSON string
application_model_status_instance = ApplicationModelStatus.from_json(json)
# print the JSON string representation of the object
print(ApplicationModelStatus.to_json())

# convert the object into a dict
application_model_status_dict = application_model_status_instance.to_dict()
# create an instance of ApplicationModelStatus from a dict
application_model_status_from_dict = ApplicationModelStatus.from_dict(application_model_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


