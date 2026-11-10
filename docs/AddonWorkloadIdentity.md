# AddonWorkloadIdentity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_role_arn** | **str** | The IAM role the add-on runs as in Amazon Web Services, such as &#x60;arn:aws:iam::123456789012:role/dns&#x60;. AstroPulse writes the annotation Amazon EKS reads. | [optional] 
**azure_client_id** | **str** | The client ID of the managed identity the add-on runs as on Azure. AstroPulse writes the annotation and the label AKS reads. | [optional] 
**cloud** | [**WorkloadIdentityCloud**](WorkloadIdentityCloud.md) | The cloud the identity belongs to, which names the field it is set in. Left out, it is the cloud of the field that is set, or Other when only annotations or labels are; a read returns the one in use. | [optional] 
**gcp_service_account** | **str** | The Google service account the add-on runs as on Google Cloud, such as &#x60;dns@my-project.iam.gserviceaccount.com&#x60;. AstroPulse writes the annotation GKE reads. | [optional] 
**service_account_annotations** | **Dict[str, str]** | Provider-required annotations applied to the managed add-on&#39;s service account. | [optional] 
**service_account_labels** | **Dict[str, str]** | Provider-required labels applied to the managed add-on&#39;s workload identity resources. | [optional] 

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


