# ApplicationHistoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ApplicationHistory**](ApplicationHistory.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.application_history_response import ApplicationHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationHistoryResponse from a JSON string
application_history_response_instance = ApplicationHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationHistoryResponse.to_json())

# convert the object into a dict
application_history_response_dict = application_history_response_instance.to_dict()
# create an instance of ApplicationHistoryResponse from a dict
application_history_response_from_dict = ApplicationHistoryResponse.from_dict(application_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


