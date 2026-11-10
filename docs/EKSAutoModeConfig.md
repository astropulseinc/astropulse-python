# EKSAutoModeConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_gpu_node_pool** | **bool** | Lets EKS Auto Mode provision GPU instances (optional, default false). AWS owns the NVIDIA driver and device plugin on these nodes; AstroPulse renders only the NodePool. Nodes are tainted nvidia.com/gpu:NoSchedule, so pods need a matching toleration. | [optional] 
**gpu_capacity_types** | [**List[InstanceType]**](InstanceType.md) | The purchase options the GPU pool may buy: &#x60;OnDemand&#x60;, &#x60;Spot&#x60; or both. A new cluster&#39;s pool buys &#x60;OnDemand&#x60;, and an existing one keeps what it buys unless this is set. | [optional] 
**gpu_limit** | **int** | The maximum number of GPUs the GPU node pool may provision, counted across the pool (optional, 1-1000, default 10). Ignored unless the GPU node pool is enabled. | [optional] 

## Example

```python
from astropulse._generated.models.eks_auto_mode_config import EKSAutoModeConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EKSAutoModeConfig from a JSON string
eks_auto_mode_config_instance = EKSAutoModeConfig.from_json(json)
# print the JSON string representation of the object
print(EKSAutoModeConfig.to_json())

# convert the object into a dict
eks_auto_mode_config_dict = eks_auto_mode_config_instance.to_dict()
# create an instance of EKSAutoModeConfig from a dict
eks_auto_mode_config_from_dict = EKSAutoModeConfig.from_dict(eks_auto_mode_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


