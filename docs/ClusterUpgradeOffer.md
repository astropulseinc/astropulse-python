# ClusterUpgradeOffer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** | True when the cluster can be upgraded to nextVersion. | [optional] 
**in_extended_support** | **bool** | True when the cluster&#39;s version is past standard support and in the provider&#39;s extended support. | [optional] 
**label** | **str** | A few words for a list cell, such as \&quot;1.37 available\&quot;. | [optional] 
**latest_version** | **str** | The newest Kubernetes version AstroPulse supports for this cluster. | [optional] 
**message** | **str** | Explains the offer in one or two sentences, such as \&quot;Kubernetes 1.37 is available; 1.38 is 2 upgrades away.\&quot; | [optional] 
**next_version** | **str** | The version the next upgrade moves the cluster to, one minor version at a time. | [optional] 
**standard_support_ends_at** | **date** | The date the provider ends standard support of the cluster&#39;s version. Omitted when the provider publishes none. | [optional] 
**steps_to_latest** | **int** | How many upgrades, one minor version each, reach latestVersion. | [optional] 
**support_ending** | **bool** | True when standard support of the cluster&#39;s version ends within 90 days or has ended. | [optional] 
**support_message** | **str** | Says when support ends, in one sentence. Present when supportEnding is true. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_upgrade_offer import ClusterUpgradeOffer

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterUpgradeOffer from a JSON string
cluster_upgrade_offer_instance = ClusterUpgradeOffer.from_json(json)
# print the JSON string representation of the object
print(ClusterUpgradeOffer.to_json())

# convert the object into a dict
cluster_upgrade_offer_dict = cluster_upgrade_offer_instance.to_dict()
# create an instance of ClusterUpgradeOffer from a dict
cluster_upgrade_offer_from_dict = ClusterUpgradeOffer.from_dict(cluster_upgrade_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


