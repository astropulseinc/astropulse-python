# EKSUpdateSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ami_family** | [**AMIFamily**](AMIFamily.md) | The operating system image of the cluster&#39;s nodes. Omitted keeps it; changing it replaces the nodes. | [optional] 
**auto_mode** | [**EKSAutoModeConfig**](EKSAutoModeConfig.md) | Updates the EKS Auto Mode GPU NodePool switch (optional). Valid only on clusters provisioned with computeMode &#x60;AutoMode&#x60;; flipping it renders or removes the pool. | [optional] 
**credentials** | [**Credentials**](Credentials.md) | Replaces the cluster&#39;s stored static credentials when it carries data; omitted, or with the type and no data, it keeps them. | [optional] 
**ecr_account_ids** | **List[str]** | Replaces the other AWS accounts whose ECR the nodes pull from (optional, max 20); omit to keep them, send [] to clear them. | [optional] 

## Example

```python
from astropulse._generated.models.eks_update_spec import EKSUpdateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of EKSUpdateSpec from a JSON string
eks_update_spec_instance = EKSUpdateSpec.from_json(json)
# print the JSON string representation of the object
print(EKSUpdateSpec.to_json())

# convert the object into a dict
eks_update_spec_dict = eks_update_spec_instance.to_dict()
# create an instance of EKSUpdateSpec from a dict
eks_update_spec_from_dict = EKSUpdateSpec.from_dict(eks_update_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


