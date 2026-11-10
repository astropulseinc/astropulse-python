# GKESubnetConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The subnet name (required). Format: 1-63 lowercase letters, digits, or hyphens; must start with a letter and end with letter or digit. | 
**pods_range** | **str** | The name of the secondary IP range for pods (required). Format: 1-63 lowercase letters, digits, or hyphens. Must match a secondary range on your subnet. | 
**services_range** | **str** | The name of the secondary IP range for services (required). Format: 1-63 lowercase letters, digits, or hyphens. Must match a secondary range on your subnet. | 

## Example

```python
from astropulse._generated.models.gke_subnet_config import GKESubnetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GKESubnetConfig from a JSON string
gke_subnet_config_instance = GKESubnetConfig.from_json(json)
# print the JSON string representation of the object
print(GKESubnetConfig.to_json())

# convert the object into a dict
gke_subnet_config_dict = gke_subnet_config_instance.to_dict()
# create an instance of GKESubnetConfig from a dict
gke_subnet_config_from_dict = GKESubnetConfig.from_dict(gke_subnet_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


