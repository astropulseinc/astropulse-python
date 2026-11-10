# ApplyDryRunResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**ApplyDryRunAction**](ApplyDryRunAction.md) | What applying would do: Create when the resource does not exist yet, Update when it does. | [optional] 
**message** | **str** | What applying the request would do, in one sentence. | [optional] 
**title** | **str** | The verdict as a headline to show. | [optional] 
**verdict** | [**DryRunVerdict**](DryRunVerdict.md) | How the dry run ended: always Passed, since a request that fails a check is refused with the error an apply would return. | [optional] 

## Example

```python
from astropulse._generated.models.apply_dry_run_result import ApplyDryRunResult

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyDryRunResult from a JSON string
apply_dry_run_result_instance = ApplyDryRunResult.from_json(json)
# print the JSON string representation of the object
print(ApplyDryRunResult.to_json())

# convert the object into a dict
apply_dry_run_result_dict = apply_dry_run_result_instance.to_dict()
# create an instance of ApplyDryRunResult from a dict
apply_dry_run_result_from_dict = ApplyDryRunResult.from_dict(apply_dry_run_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


