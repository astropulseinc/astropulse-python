# SelfHostedSetupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_hint** | **str** | The email address of the Google account that owns the project (GCP only). When set, Cloud Shell opens as that account if it is signed in to the browser, and the setup commands stop if they run as another. | [optional] 
**account_id** | **str** | The AWS account ID (12 digits) or GCP project ID (required). | 
**cluster_name** | **str** | The cluster the resources are for (required). | 
**region** | **str** | Where the resources are created (required). | 

## Example

```python
from astropulse._generated.models.self_hosted_setup_request import SelfHostedSetupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SelfHostedSetupRequest from a JSON string
self_hosted_setup_request_instance = SelfHostedSetupRequest.from_json(json)
# print the JSON string representation of the object
print(SelfHostedSetupRequest.to_json())

# convert the object into a dict
self_hosted_setup_request_dict = self_hosted_setup_request_instance.to_dict()
# create an instance of SelfHostedSetupRequest from a dict
self_hosted_setup_request_from_dict = SelfHostedSetupRequest.from_dict(self_hosted_setup_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


