# ClusterAddonTLSChallenges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns01** | [**ClusterAddonTLSChallenge**](ClusterAddonTLSChallenge.md) | The challenge answered by writing a DNS record, which is what a certificate behind a gateway needs. | [optional] 
**http01** | [**ClusterAddonTLSChallenge**](ClusterAddonTLSChallenge.md) | The challenge served over the cluster&#39;s ingress. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_tls_challenges import ClusterAddonTLSChallenges

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonTLSChallenges from a JSON string
cluster_addon_tls_challenges_instance = ClusterAddonTLSChallenges.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonTLSChallenges.to_json())

# convert the object into a dict
cluster_addon_tls_challenges_dict = cluster_addon_tls_challenges_instance.to_dict()
# create an instance of ClusterAddonTLSChallenges from a dict
cluster_addon_tls_challenges_from_dict = ClusterAddonTLSChallenges.from_dict(cluster_addon_tls_challenges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


