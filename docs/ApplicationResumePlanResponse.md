# ApplicationResumePlanResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ApplicationResumePlan**](ApplicationResumePlan.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.application_resume_plan_response import ApplicationResumePlanResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationResumePlanResponse from a JSON string
application_resume_plan_response_instance = ApplicationResumePlanResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationResumePlanResponse.to_json())

# convert the object into a dict
application_resume_plan_response_dict = application_resume_plan_response_instance.to_dict()
# create an instance of ApplicationResumePlanResponse from a dict
application_resume_plan_response_from_dict = ApplicationResumePlanResponse.from_dict(application_resume_plan_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


