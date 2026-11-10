# ApplicationCostSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ApplicationCostSummary**](ApplicationCostSummary.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.application_cost_summary_response import ApplicationCostSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCostSummaryResponse from a JSON string
application_cost_summary_response_instance = ApplicationCostSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationCostSummaryResponse.to_json())

# convert the object into a dict
application_cost_summary_response_dict = application_cost_summary_response_instance.to_dict()
# create an instance of ApplicationCostSummaryResponse from a dict
application_cost_summary_response_from_dict = ApplicationCostSummaryResponse.from_dict(application_cost_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


