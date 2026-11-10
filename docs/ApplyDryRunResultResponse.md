# ApplyDryRunResultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ApplyDryRunResult**](ApplyDryRunResult.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.apply_dry_run_result_response import ApplyDryRunResultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyDryRunResultResponse from a JSON string
apply_dry_run_result_response_instance = ApplyDryRunResultResponse.from_json(json)
# print the JSON string representation of the object
print(ApplyDryRunResultResponse.to_json())

# convert the object into a dict
apply_dry_run_result_response_dict = apply_dry_run_result_response_instance.to_dict()
# create an instance of ApplyDryRunResultResponse from a dict
apply_dry_run_result_response_from_dict = ApplyDryRunResultResponse.from_dict(apply_dry_run_result_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


