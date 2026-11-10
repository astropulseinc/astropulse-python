# VPA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | The flag to enable or disable the vertical pod autoscaler. | 

## Example

```python
from astropulse._generated.models.vpa import VPA

# TODO update the JSON string below
json = "{}"
# create an instance of VPA from a JSON string
vpa_instance = VPA.from_json(json)
# print the JSON string representation of the object
print(VPA.to_json())

# convert the object into a dict
vpa_dict = vpa_instance.to_dict()
# create an instance of VPA from a dict
vpa_from_dict = VPA.from_dict(vpa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


