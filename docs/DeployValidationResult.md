# DeployValidationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**List[DeploymentDiffItem]**](DeploymentDiffItem.md) | The fields an apply would change from the application&#39;s newest version; absent for a new application or when nothing changes. | [optional] 
**message** | **str** | Describes the outcome; it names any check that did not finish. | [optional] 
**notices** | [**List[Notice]**](Notice.md) | Say what the deploy would do differently from what the request asked; absent when there is nothing to say. | [optional] 
**outcome** | [**Outcome**](Outcome.md) | Proceed when the application would deploy as submitted, and Blocked when a notice stops it. | [optional] 
**placement** | [**ModelPlacement**](ModelPlacement.md) | Says where a model&#39;s GPU replicas would run when a GPU node pool launches their nodes; absent otherwise. | [optional] 
**runtime** | [**ModelRuntimeChoice**](ModelRuntimeChoice.md) | The serving runtime a model would run on and the format it is served as; absent for an application that is not a model or a format no supported runtime serves. | [optional] 
**scaling** | [**ModelScalingRule**](ModelScalingRule.md) | How a model&#39;s replicas would scale; absent for other source types. | [optional] 
**title** | **str** | The verdict as a headline to show. | [optional] 
**unfinished_checks** | **List[str]** | Names the checks that did not finish, so they neither passed nor failed. | [optional] 
**verdict** | [**DryRunVerdict**](DryRunVerdict.md) | How the dry run ended: Passed, Failed, or Unfinished when some checks did not finish and none failed. | [optional] 

## Example

```python
from astropulse._generated.models.deploy_validation_result import DeployValidationResult

# TODO update the JSON string below
json = "{}"
# create an instance of DeployValidationResult from a JSON string
deploy_validation_result_instance = DeployValidationResult.from_json(json)
# print the JSON string representation of the object
print(DeployValidationResult.to_json())

# convert the object into a dict
deploy_validation_result_dict = deploy_validation_result_instance.to_dict()
# create an instance of DeployValidationResult from a dict
deploy_validation_result_from_dict = DeployValidationResult.from_dict(deploy_validation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


