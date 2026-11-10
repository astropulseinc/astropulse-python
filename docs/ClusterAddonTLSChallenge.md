# ClusterAddonTLSChallenge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** | Reports whether this challenge type can issue on the cluster. | [optional] 
**needs** | **str** | Names what is missing when the challenge is unavailable. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_tls_challenge import ClusterAddonTLSChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonTLSChallenge from a JSON string
cluster_addon_tls_challenge_instance = ClusterAddonTLSChallenge.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonTLSChallenge.to_json())

# convert the object into a dict
cluster_addon_tls_challenge_dict = cluster_addon_tls_challenge_instance.to_dict()
# create an instance of ClusterAddonTLSChallenge from a dict
cluster_addon_tls_challenge_from_dict = ClusterAddonTLSChallenge.from_dict(cluster_addon_tls_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


