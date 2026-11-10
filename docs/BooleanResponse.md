# BooleanResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.boolean_response import BooleanResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BooleanResponse from a JSON string
boolean_response_instance = BooleanResponse.from_json(json)
# print the JSON string representation of the object
print(BooleanResponse.to_json())

# convert the object into a dict
boolean_response_dict = boolean_response_instance.to_dict()
# create an instance of BooleanResponse from a dict
boolean_response_from_dict = BooleanResponse.from_dict(boolean_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


