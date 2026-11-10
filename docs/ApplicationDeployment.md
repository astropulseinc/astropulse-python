# ApplicationDeployment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **bool** | False when the deploy updated an application that already existed. | [optional] 
**name** | **str** | The application, and what every other endpoint takes. | [optional] 
**notices** | [**List[Notice]**](Notice.md) | Say what the deploy did differently from what the request asked; absent when there is nothing to say. | [optional] 
**outcome** | [**Outcome**](Outcome.md) | Proceed: the deploy went ahead. | [optional] 
**profile_name** | **str** | The profile the application deployed onto. | [optional] 
**version** | **int** | The application version this deploy recorded, and what a rollback returns to. | [optional] 

## Example

```python
from astropulse._generated.models.application_deployment import ApplicationDeployment

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationDeployment from a JSON string
application_deployment_instance = ApplicationDeployment.from_json(json)
# print the JSON string representation of the object
print(ApplicationDeployment.to_json())

# convert the object into a dict
application_deployment_dict = application_deployment_instance.to_dict()
# create an instance of ApplicationDeployment from a dict
application_deployment_from_dict = ApplicationDeployment.from_dict(application_deployment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


