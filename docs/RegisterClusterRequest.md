# RegisterClusterRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_namespace** | **str** | Where the Astro agent is installed. It is persisted so agent-driven add-ons can place their local control ConfigMaps correctly. | [optional] 
**agent_update** | **bool** | Returns the manifest that upgrades the agent of a cluster that is already registered, keeping its identity. It requires dryRun. | [optional] 
**architecture** | [**CPUArchitecture**](CPUArchitecture.md) | The CPU architecture the cluster&#39;s nodes run. | [optional] 
**cluster_name** | **str** | The cluster name. Set from the URL path param — ignored if provided in body. | [optional] 
**dry_run** | **bool** | Generates the agent manifest without persisting the cluster or waiting for agent connection. | [optional] 
**kubernetes_version** | **str** | Optional. If omitted, it is detected from the cluster. | [optional] 
**labels** | **Dict[str, str]** | Key/value pairs stored on the cluster, following the Kubernetes label rules. Keys are Kubernetes label keys, not under kubernetes.io or k8s.io; values are 1-63 letters, digits, &#39;-&#39;, &#39;_&#39; and &#39;.&#39;, starting and ending with a letter or digit. | [optional] 
**provisioner** | **str** | Set automatically by the server — ignored if provided in the request body. | [optional] 
**provisioner_config** | **Dict[str, str]** | What is known about the cluster: \&quot;provider\&quot;, detected from the kubeconfig, and on EKS \&quot;eksComputeMode\&quot; when it is known. | [optional] 
**region** | **str** | The cloud region or zone the cluster runs in, such as us-east-1, or local for a cluster outside a cloud. Defaults to local. | [optional] 

## Example

```python
from astropulse._generated.models.register_cluster_request import RegisterClusterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterClusterRequest from a JSON string
register_cluster_request_instance = RegisterClusterRequest.from_json(json)
# print the JSON string representation of the object
print(RegisterClusterRequest.to_json())

# convert the object into a dict
register_cluster_request_dict = register_cluster_request_instance.to_dict()
# create an instance of RegisterClusterRequest from a dict
register_cluster_request_from_dict = RegisterClusterRequest.from_dict(register_cluster_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


