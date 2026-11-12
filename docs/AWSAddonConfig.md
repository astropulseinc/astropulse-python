# AWSAddonConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iam_role_arn** | **str** | The role Node Autoscaling runs as in your AWS account, from the prerequisites stack AstroPulse generates, for a registered EKS cluster. Leave it empty on a cluster AstroPulse created. | [optional] 
**instance_profile** | **str** | The instance profile given to the nodes Node Autoscaling starts. | [optional] 
**security_group_tags** | **List[str]** | Tags, written key&#x3D;value, that pick the security groups for new nodes. | [optional] 
**subnet_tags** | **List[str]** | Tags, written key&#x3D;value, that pick the subnets for new nodes. | [optional] 

## Example

```python
from astropulse._generated.models.aws_addon_config import AWSAddonConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AWSAddonConfig from a JSON string
aws_addon_config_instance = AWSAddonConfig.from_json(json)
# print the JSON string representation of the object
print(AWSAddonConfig.to_json())

# convert the object into a dict
aws_addon_config_dict = aws_addon_config_instance.to_dict()
# create an instance of AWSAddonConfig from a dict
aws_addon_config_from_dict = AWSAddonConfig.from_dict(aws_addon_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


