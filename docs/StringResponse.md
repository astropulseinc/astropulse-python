# StringResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.string_response import StringResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StringResponse from a JSON string
string_response_instance = StringResponse.from_json(json)
# print the JSON string representation of the object
print(StringResponse.to_json())

# convert the object into a dict
string_response_dict = string_response_instance.to_dict()
# create an instance of StringResponse from a dict
string_response_from_dict = StringResponse.from_dict(string_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


