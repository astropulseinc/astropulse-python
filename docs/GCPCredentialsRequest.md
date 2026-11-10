# GCPCredentialsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_name** | **str** | The name of the cluster | 
**duration** | **str** | The duration for which the credentials are valid | [optional] 
**target_project_id** | **str** | The ID of the target GCP project Optional - looked up from cluster if not provided | [optional] 
**target_region** | **str** | The GCP region Optional - looked up from cluster if not provided | [optional] 

## Example

```python
from astropulse._generated.models.gcp_credentials_request import GCPCredentialsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GCPCredentialsRequest from a JSON string
gcp_credentials_request_instance = GCPCredentialsRequest.from_json(json)
# print the JSON string representation of the object
print(GCPCredentialsRequest.to_json())

# convert the object into a dict
gcp_credentials_request_dict = gcp_credentials_request_instance.to_dict()
# create an instance of GCPCredentialsRequest from a dict
gcp_credentials_request_from_dict = GCPCredentialsRequest.from_dict(gcp_credentials_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


