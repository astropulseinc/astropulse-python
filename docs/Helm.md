# Helm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repo** | [**HelmRepo**](HelmRepo.md) | Contains repository details for the Helm chart | [optional] 
**values** | [**Values**](Values.md) | Defines the values for the Helm chart | [optional] 

## Example

```python
from astropulse._generated.models.helm import Helm

# TODO update the JSON string below
json = "{}"
# create an instance of Helm from a JSON string
helm_instance = Helm.from_json(json)
# print the JSON string representation of the object
print(Helm.to_json())

# convert the object into a dict
helm_dict = helm_instance.to_dict()
# create an instance of Helm from a dict
helm_from_dict = Helm.from_dict(helm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


