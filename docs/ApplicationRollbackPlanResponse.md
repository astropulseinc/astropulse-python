# ApplicationRollbackPlanResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ApplicationRollbackPlan**](ApplicationRollbackPlan.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.application_rollback_plan_response import ApplicationRollbackPlanResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationRollbackPlanResponse from a JSON string
application_rollback_plan_response_instance = ApplicationRollbackPlanResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationRollbackPlanResponse.to_json())

# convert the object into a dict
application_rollback_plan_response_dict = application_rollback_plan_response_instance.to_dict()
# create an instance of ApplicationRollbackPlanResponse from a dict
application_rollback_plan_response_from_dict = ApplicationRollbackPlanResponse.from_dict(application_rollback_plan_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


