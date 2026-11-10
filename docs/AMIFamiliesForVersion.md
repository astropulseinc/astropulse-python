# AMIFamiliesForVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**families** | [**List[AMIFamilyOffer]**](AMIFamilyOffer.md) | The AMI families offered at this version. | [optional] 
**kubernetes_version** | **str** | The Kubernetes minor version, for example \&quot;1.36\&quot;. | [optional] 

## Example

```python
from astropulse._generated.models.ami_families_for_version import AMIFamiliesForVersion

# TODO update the JSON string below
json = "{}"
# create an instance of AMIFamiliesForVersion from a JSON string
ami_families_for_version_instance = AMIFamiliesForVersion.from_json(json)
# print the JSON string representation of the object
print(AMIFamiliesForVersion.to_json())

# convert the object into a dict
ami_families_for_version_dict = ami_families_for_version_instance.to_dict()
# create an instance of AMIFamiliesForVersion from a dict
ami_families_for_version_from_dict = AMIFamiliesForVersion.from_dict(ami_families_for_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


