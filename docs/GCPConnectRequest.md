# GCPConnectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_hint** | **str** | The email address of the Google account that owns the project. When set, Cloud Shell opens as that account if it is signed in to the browser, and the setup script stops if it runs as another. | [optional] 
**cluster_name** | **str** | The name of the cluster | 
**duration** | **str** | The duration for which the credentials are valid | [optional] 
**force_update** | **bool** | Bypasses cluster existence checks and forces resource updates | [optional] 
**target_project_id** | **str** | The ID of the target GCP project (your project) Optional for credentials - looked up from cluster if not provided Format: 6-30 lowercase letters, digits, hyphens; must start with letter | [optional] 
**target_project_number** | **str** | The numeric GCP project number (required for cloud connect) Retrieve via: gcloud projects describe PROJECT_ID --format&#x3D;\&quot;value(projectNumber)\&quot; | [optional] 
**target_region** | **str** | The GCP region where resources should be created Optional for credentials - looked up from cluster if not provided Format: location-direction-number (e.g., us-central1) | [optional] 

## Example

```python
from astropulse._generated.models.gcp_connect_request import GCPConnectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GCPConnectRequest from a JSON string
gcp_connect_request_instance = GCPConnectRequest.from_json(json)
# print the JSON string representation of the object
print(GCPConnectRequest.to_json())

# convert the object into a dict
gcp_connect_request_dict = gcp_connect_request_instance.to_dict()
# create an instance of GCPConnectRequest from a dict
gcp_connect_request_from_dict = GCPConnectRequest.from_dict(gcp_connect_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


