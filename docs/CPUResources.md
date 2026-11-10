# CPUResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maximum** | **str** | The maximum CPU allocation (required, must be &gt;&#x3D; Minimum): a Kubernetes CPU quantity such as 500m or 2, stored in millicores. | 
**minimum** | **str** | The minimum CPU allocation (required): a Kubernetes CPU quantity such as 500m or 2, stored in millicores. | 

## Example

```python
from astropulse._generated.models.cpu_resources import CPUResources

# TODO update the JSON string below
json = "{}"
# create an instance of CPUResources from a JSON string
cpu_resources_instance = CPUResources.from_json(json)
# print the JSON string representation of the object
print(CPUResources.to_json())

# convert the object into a dict
cpu_resources_dict = cpu_resources_instance.to_dict()
# create an instance of CPUResources from a dict
cpu_resources_from_dict = CPUResources.from_dict(cpu_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


