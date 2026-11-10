# DeployValidationResultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeployValidationResult**](DeployValidationResult.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.deploy_validation_result_response import DeployValidationResultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeployValidationResultResponse from a JSON string
deploy_validation_result_response_instance = DeployValidationResultResponse.from_json(json)
# print the JSON string representation of the object
print(DeployValidationResultResponse.to_json())

# convert the object into a dict
deploy_validation_result_response_dict = deploy_validation_result_response_instance.to_dict()
# create an instance of DeployValidationResultResponse from a dict
deploy_validation_result_response_from_dict = DeployValidationResultResponse.from_dict(deploy_validation_result_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


