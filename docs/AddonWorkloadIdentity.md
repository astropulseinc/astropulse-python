# AddonWorkloadIdentity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_role_arn** | **str** | The AWS IAM role the add-on runs as, such as &#x60;arn:aws:iam::123456789012:role/dns&#x60;. | [optional] 
**azure_client_id** | **str** | The client ID of the Azure managed identity the add-on runs as. | [optional] 
**cloud** | [**WorkloadIdentityCloud**](WorkloadIdentityCloud.md) | The cloud the identity belongs to, which decides the field it is set in. Left out, it is the cloud of the field that is set, or &#x60;Other&#x60; when only annotations or labels are. | [optional] 
**gcp_service_account** | **str** | The Google service account the add-on runs as, such as &#x60;dns@my-project.iam.gserviceaccount.com&#x60;. | [optional] 
**service_account_annotations** | **Dict[str, str]** | Annotations your cloud needs on the add-on&#39;s service account, when &#x60;cloud&#x60; is &#x60;Other&#x60;. | [optional] 
**service_account_labels** | **Dict[str, str]** | Labels your cloud needs on the add-on&#39;s workload identity, when &#x60;cloud&#x60; is &#x60;Other&#x60;. | [optional] 

## Example

```python
from astropulse._generated.models.addon_workload_identity import AddonWorkloadIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of AddonWorkloadIdentity from a JSON string
addon_workload_identity_instance = AddonWorkloadIdentity.from_json(json)
# print the JSON string representation of the object
print(AddonWorkloadIdentity.to_json())

# convert the object into a dict
addon_workload_identity_dict = addon_workload_identity_instance.to_dict()
# create an instance of AddonWorkloadIdentity from a dict
addon_workload_identity_from_dict = AddonWorkloadIdentity.from_dict(addon_workload_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


