# K8sClusterSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | [**CPUArchitecture**](CPUArchitecture.md) | The CPU architecture this cluster runs. Usually there is nothing to write here — the platform derives it from the machine types the node groups pin, since every provider picks the node image from the instance type, so pinning m7g.large (or a c4a-* on GCP, a Dpls_v6 on Azure) is already asking for arm64. Declare it when nothing is pinned to derive from: an accelerator-only node group whose machine AstroPulse resolves, or provider-managed compute (EKS Auto Mode, GKE Autopilot). When declared alongside pinned machine types it is checked against them, and a contradiction is refused. Immutable after create. | [optional] 
**control_plane** | [**ControlPlaneNode**](ControlPlaneNode.md) | The configuration for the control plane | [optional] 
**data_plane** | [**DataPlane**](DataPlane.md) | The configuration for the data plane. It is required for normal clusters and must be omitted when the provider owns worker compute: EKS Auto Mode (provisioner.eks.computeMode &#x3D; &#x60;AutoMode&#x60;) or GKE Autopilot (provisioner.gke.autopilot &#x3D; true). | [optional] 

## Example

```python
from astropulse._generated.models.k8s_cluster_spec import K8sClusterSpec

# TODO update the JSON string below
json = "{}"
# create an instance of K8sClusterSpec from a JSON string
k8s_cluster_spec_instance = K8sClusterSpec.from_json(json)
# print the JSON string representation of the object
print(K8sClusterSpec.to_json())

# convert the object into a dict
k8s_cluster_spec_dict = k8s_cluster_spec_instance.to_dict()
# create an instance of K8sClusterSpec from a dict
k8s_cluster_spec_from_dict = K8sClusterSpec.from_dict(k8s_cluster_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


