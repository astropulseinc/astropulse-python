# ClusterAddonConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability** | [**AddonAvailability**](AddonAvailability.md) | How many copies of the add-on&#39;s components run. Left out, an update keeps the current one and a new add-on runs Standard. | [optional] 
**cert_manager** | [**CertManagerAddonConfiguration**](CertManagerAddonConfiguration.md) | Configures the cert-manager add-on. | [optional] 
**cost_visibility** | [**CostVisibilityAddonConfiguration**](CostVisibilityAddonConfiguration.md) | Configures the cost-visibility add-on. | [optional] 
**external_dns** | [**ExternalDNSAddonConfiguration**](ExternalDNSAddonConfiguration.md) | Configures the external-dns add-on. | [optional] 
**gateway** | [**GatewayAddonConfiguration**](GatewayAddonConfiguration.md) | Configures the gateway add-on. | [optional] 
**karpenter** | [**KarpenterAddonConfiguration**](KarpenterAddonConfiguration.md) | Configures the Node Autoscaling add-on. | [optional] 
**model_serving** | [**ModelServingAddonConfiguration**](ModelServingAddonConfiguration.md) | Configures the model-serving add-on. | [optional] 
**nginx** | [**NginxAddonConfiguration**](NginxAddonConfiguration.md) | Configures the nginx-ingress add-on. | [optional] 
**resources** | [**AddonResources**](AddonResources.md) | Sizes the add-on&#39;s main component. Fields you omit keep their current value; an empty object returns to AstroPulse&#39;s sizing. | [optional] 
**vulnerability_scanning** | [**VulnerabilityScanningAddonConfiguration**](VulnerabilityScanningAddonConfiguration.md) | Configures the vulnerability-scanning add-on. | [optional] 
**workload_autoscaling** | [**WorkloadAutoscalingAddonConfiguration**](WorkloadAutoscalingAddonConfiguration.md) | Configures the workload-autoscaling add-on. | [optional] 
**workload_queueing** | [**WorkloadQueueingAddonConfiguration**](WorkloadQueueingAddonConfiguration.md) | Configures the workload-queueing add-on. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_configuration import ClusterAddonConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonConfiguration from a JSON string
cluster_addon_configuration_instance = ClusterAddonConfiguration.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonConfiguration.to_json())

# convert the object into a dict
cluster_addon_configuration_dict = cluster_addon_configuration_instance.to_dict()
# create an instance of ClusterAddonConfiguration from a dict
cluster_addon_configuration_from_dict = ClusterAddonConfiguration.from_dict(cluster_addon_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


