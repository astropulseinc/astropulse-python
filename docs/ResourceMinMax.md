# ResourceMinMax


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maximum** | [**Quantity**](Quantity.md) |  | [optional] 
**minimum** | [**Quantity**](Quantity.md) |  | [optional] 

## Example

```python
from astropulse._generated.models.resource_min_max import ResourceMinMax

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceMinMax from a JSON string
resource_min_max_instance = ResourceMinMax.from_json(json)
# print the JSON string representation of the object
print(ResourceMinMax.to_json())

# convert the object into a dict
resource_min_max_dict = resource_min_max_instance.to_dict()
# create an instance of ResourceMinMax from a dict
resource_min_max_from_dict = ResourceMinMax.from_dict(resource_min_max_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


