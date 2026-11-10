# ClusterAccessTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClusterAccessToken**](ClusterAccessToken.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_access_token_response import ClusterAccessTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAccessTokenResponse from a JSON string
cluster_access_token_response_instance = ClusterAccessTokenResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterAccessTokenResponse.to_json())

# convert the object into a dict
cluster_access_token_response_dict = cluster_access_token_response_instance.to_dict()
# create an instance of ClusterAccessTokenResponse from a dict
cluster_access_token_response_from_dict = ClusterAccessTokenResponse.from_dict(cluster_access_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


