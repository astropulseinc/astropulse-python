# ApplicationContainerTermination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container** | **str** | The container&#39;s name. | [optional] 
**exit_code** | **int** | The exit code of the container&#39;s last run. | [optional] 
**finished_at** | **datetime** | When that run ended. | [optional] 
**pod** | **str** | The pod the container runs in. | [optional] 
**reason** | **str** | Why that run ended, as Kubernetes reports it: Error, OOMKilled, Completed. | [optional] 
**restart_count** | **int** | How many times the container has restarted. | [optional] 

## Example

```python
from astropulse._generated.models.application_container_termination import ApplicationContainerTermination

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationContainerTermination from a JSON string
application_container_termination_instance = ApplicationContainerTermination.from_json(json)
# print the JSON string representation of the object
print(ApplicationContainerTermination.to_json())

# convert the object into a dict
application_container_termination_dict = application_container_termination_instance.to_dict()
# create an instance of ApplicationContainerTermination from a dict
application_container_termination_from_dict = ApplicationContainerTermination.from_dict(application_container_termination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


