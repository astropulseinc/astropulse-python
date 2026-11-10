# StringListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[str]** |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.string_list_response import StringListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StringListResponse from a JSON string
string_list_response_instance = StringListResponse.from_json(json)
# print the JSON string representation of the object
print(StringListResponse.to_json())

# convert the object into a dict
string_list_response_dict = string_list_response_instance.to_dict()
# create an instance of StringListResponse from a dict
string_list_response_from_dict = StringListResponse.from_dict(string_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


