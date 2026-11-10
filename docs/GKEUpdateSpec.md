# GKEUpdateSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorized_networks** | **List[str]** | CIDR blocks allowed to access the Kubernetes API server (optional, max 50 entries). Each entry must be a valid CIDR block. Pass empty array to allow unrestricted access. | [optional] 
**credentials** | [**Credentials**](Credentials.md) | Replaces the cluster&#39;s stored static credentials when it carries data; omitted, or with the type and no data, it keeps them. | [optional] 
**image_type** | [**GKEImageType**](GKEImageType.md) | The operating system image of the node pools. Omitted keeps it; changing it replaces the nodes. | [optional] 
**maintenance_window** | [**MaintenanceWindow**](MaintenanceWindow.md) | The daily window GKE runs automatic maintenance in. Omitted keeps it. | [optional] 
**release_channel** | [**GKEReleaseChannel**](GKEReleaseChannel.md) | The release channel the cluster takes its Kubernetes versions from. Omitted keeps it. | [optional] 

## Example

```python
from astropulse._generated.models.gke_update_spec import GKEUpdateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of GKEUpdateSpec from a JSON string
gke_update_spec_instance = GKEUpdateSpec.from_json(json)
# print the JSON string representation of the object
print(GKEUpdateSpec.to_json())

# convert the object into a dict
gke_update_spec_dict = gke_update_spec_instance.to_dict()
# create an instance of GKEUpdateSpec from a dict
gke_update_spec_from_dict = GKEUpdateSpec.from_dict(gke_update_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


