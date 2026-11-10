# ClusterAccessToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **str** | When the token stops being accepted, in RFC 3339. | [optional] 
**kubeconfig_expires_at** | **str** | When the kubeconfig stops getting tokens, in RFC 3339; no token is reported to last past it. | [optional] 
**token** | **str** | The credential. Send it as the bearer token on requests to the cluster address in the kubeconfig. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_access_token import ClusterAccessToken

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAccessToken from a JSON string
cluster_access_token_instance = ClusterAccessToken.from_json(json)
# print the JSON string representation of the object
print(ClusterAccessToken.to_json())

# convert the object into a dict
cluster_access_token_dict = cluster_access_token_instance.to_dict()
# create an instance of ClusterAccessToken from a dict
cluster_access_token_from_dict = ClusterAccessToken.from_dict(cluster_access_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


