# SelfHostedSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The cloud provider account identifier (required, minimum 1 character). For AWS: 12-digit account ID. For GCP: project ID (6-30 lowercase letters/digits/hyphens). | 
**bucket_name** | **str** | The bucket that holds the cluster&#39;s state, in the cluster&#39;s account and region (S3 on AWS, Cloud Storage on GCP). Required with &#x60;Static&#x60; or &#x60;Dynamic&#x60; credentials; with &#x60;Vault&#x60; credentials it defaults to the bucket setup creates. | [optional] 
**credentials** | [**Credentials**](Credentials.md) | The cloud provider authentication credentials (required) | 
**kubernetes_version** | **str** | The target Kubernetes version (optional, format: semver e.g. \&quot;1.30.14\&quot;). Only full semantic version is accepted (major.minor.patch). Major.minor format is not supported. If omitted, AstroPulse uses the default version. | [optional] 
**network_id** | **str** | The cloud provider network identifier (optional). For AWS: VPC ID. For GCP: VPC network name. If omitted, a new network is created. | [optional] 

## Example

```python
from astropulse._generated.models.self_hosted_spec import SelfHostedSpec

# TODO update the JSON string below
json = "{}"
# create an instance of SelfHostedSpec from a JSON string
self_hosted_spec_instance = SelfHostedSpec.from_json(json)
# print the JSON string representation of the object
print(SelfHostedSpec.to_json())

# convert the object into a dict
self_hosted_spec_dict = self_hosted_spec_instance.to_dict()
# create an instance of SelfHostedSpec from a dict
self_hosted_spec_from_dict = SelfHostedSpec.from_dict(self_hosted_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


