# ControlPlaneNodeGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **Dict[str, str]** | Kubernetes labels applied to control plane nodes (optional). Keys are Kubernetes label keys, not under kubernetes.io or k8s.io; values are 1-63 letters, digits, &#39;-&#39;, &#39;_&#39; and &#39;.&#39;, starting and ending with a letter or digit. | [optional] 
**machine_types** | **List[str]** | The list of machine types for control plane nodes (required, minimum 1 item). Provider-specific formats: eks (e.g. \&quot;t3.medium\&quot;), gke (e.g. \&quot;n1-standard-1\&quot;), aks (e.g. \&quot;Standard_D2s_v3\&quot;). | 
**max_node** | **int** | The maximum number of control plane nodes (optional, default: 1). Should be an odd number (1, 3, 5) for quorum. Must be &gt;&#x3D; MinNode. | [optional] 
**min_node** | **int** | The minimum number of control plane nodes (optional, default: 1). Should be an odd number (1, 3, 5) for quorum. Nodes are distributed across availability zones. | [optional] 
**name** | **str** | The control plane node group name (required, 1-50 characters, valid DNS name) | 

## Example

```python
from astropulse._generated.models.control_plane_node_group import ControlPlaneNodeGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ControlPlaneNodeGroup from a JSON string
control_plane_node_group_instance = ControlPlaneNodeGroup.from_json(json)
# print the JSON string representation of the object
print(ControlPlaneNodeGroup.to_json())

# convert the object into a dict
control_plane_node_group_dict = control_plane_node_group_instance.to_dict()
# create an instance of ControlPlaneNodeGroup from a dict
control_plane_node_group_from_dict = ControlPlaneNodeGroup.from_dict(control_plane_node_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


