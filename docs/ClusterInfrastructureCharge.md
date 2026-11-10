# ClusterInfrastructureCharge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | The ISO 4217 code &#x60;hourlyRate&#x60; and &#x60;monthlyRate&#x60; are in. | [optional] 
**hourly_rate** | **str** | The price of one for an hour, a decimal in &#x60;currency&#x60;; absent when the charge has no price. | [optional] 
**item** | [**ClusterInfrastructureItem**](ClusterInfrastructureItem.md) | What is charged for. | [optional] 
**monthly_rate** | **str** | The price of one for a month, a decimal in &#x60;currency&#x60;, at 730 hours a month; absent when the charge has no price. | [optional] 
**quantity** | **int** | How many a new cluster gets, each charged at &#x60;hourlyRate&#x60;; absent when it depends on the cluster. | [optional] 
**read_time** | **str** | When &#x60;hourlyRate&#x60; was read from &#x60;source&#x60;. | [optional] 
**source** | [**ClusterPriceSource**](ClusterPriceSource.md) | Where &#x60;hourlyRate&#x60; was read. | [optional] 
**unpriced** | [**ClusterInfrastructureUnpriced**](ClusterInfrastructureUnpriced.md) | Why the charge has no &#x60;hourlyRate&#x60;. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_infrastructure_charge import ClusterInfrastructureCharge

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterInfrastructureCharge from a JSON string
cluster_infrastructure_charge_instance = ClusterInfrastructureCharge.from_json(json)
# print the JSON string representation of the object
print(ClusterInfrastructureCharge.to_json())

# convert the object into a dict
cluster_infrastructure_charge_dict = cluster_infrastructure_charge_instance.to_dict()
# create an instance of ClusterInfrastructureCharge from a dict
cluster_infrastructure_charge_from_dict = ClusterInfrastructureCharge.from_dict(cluster_infrastructure_charge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


