# Provisioner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aks** | [**AKSClusterSpec**](AKSClusterSpec.md) | The specification for an Azure AKS cluster (required when type is aks) | [optional] 
**eks** | [**EKSClusterSpec**](EKSClusterSpec.md) | The specification for an Amazon EKS cluster (required when type is eks) | [optional] 
**gke** | [**GKEClusterSpec**](GKEClusterSpec.md) | The specification for a Google GKE cluster (required when type is gke) | [optional] 
**self_hosted** | [**SelfHostedSpec**](SelfHostedSpec.md) | The specification for a platform-managed self-hosted cluster (required when type is selfHosted) | [optional] 
**type** | [**ProvisionerType**](ProvisionerType.md) | The provisioner that creates the cluster; the provider-specific field of the same name holds its settings. | 

## Example

```python
from astropulse._generated.models.provisioner import Provisioner

# TODO update the JSON string below
json = "{}"
# create an instance of Provisioner from a JSON string
provisioner_instance = Provisioner.from_json(json)
# print the JSON string representation of the object
print(Provisioner.to_json())

# convert the object into a dict
provisioner_dict = provisioner_instance.to_dict()
# create an instance of Provisioner from a dict
provisioner_from_dict = Provisioner.from_dict(provisioner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


