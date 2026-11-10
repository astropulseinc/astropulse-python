# MemResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maximum** | **str** | The maximum memory allocation (required, must be &gt;&#x3D; Minimum). Format: Kubernetes memory quantity with suffix (e.g. \&quot;512Mi\&quot;, \&quot;1Gi\&quot;, \&quot;2G\&quot;). | 
**minimum** | **str** | The minimum memory allocation (required). Format: Kubernetes memory quantity with suffix (e.g. \&quot;512Mi\&quot;, \&quot;1Gi\&quot;, \&quot;2G\&quot;). | 

## Example

```python
from astropulse._generated.models.mem_resources import MemResources

# TODO update the JSON string below
json = "{}"
# create an instance of MemResources from a JSON string
mem_resources_instance = MemResources.from_json(json)
# print the JSON string representation of the object
print(MemResources.to_json())

# convert the object into a dict
mem_resources_dict = mem_resources_instance.to_dict()
# create an instance of MemResources from a dict
mem_resources_from_dict = MemResources.from_dict(mem_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


