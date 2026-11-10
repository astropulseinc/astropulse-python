# Values


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | **List[str]** | The files containing the values, used when type is &#x60;Files&#x60;; for a &#x60;Repository&#x60; source they are relative to the repository path. | [optional] 
**object** | **object** | The values as key-value pairs, used when type is &#x60;Object&#x60;. | [optional] 
**type** | [**HelmValueType**](HelmValueType.md) | Where the values are written. | [optional] 

## Example

```python
from astropulse._generated.models.values import Values

# TODO update the JSON string below
json = "{}"
# create an instance of Values from a JSON string
values_instance = Values.from_json(json)
# print the JSON string representation of the object
print(Values.to_json())

# convert the object into a dict
values_dict = values_instance.to_dict()
# create an instance of Values from a dict
values_from_dict = Values.from_dict(values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


