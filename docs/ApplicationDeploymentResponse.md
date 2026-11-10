# ApplicationDeploymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ApplicationDeployment**](ApplicationDeployment.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.application_deployment_response import ApplicationDeploymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationDeploymentResponse from a JSON string
application_deployment_response_instance = ApplicationDeploymentResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationDeploymentResponse.to_json())

# convert the object into a dict
application_deployment_response_dict = application_deployment_response_instance.to_dict()
# create an instance of ApplicationDeploymentResponse from a dict
application_deployment_response_from_dict = ApplicationDeploymentResponse.from_dict(application_deployment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


