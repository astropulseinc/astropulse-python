# EKSClusterSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The AWS account ID (required, 12-digit numeric string, e.g. \&quot;123456789012\&quot;) | 
**ami_family** | [**AMIFamily**](AMIFamily.md) | The operating system image of the cluster&#39;s nodes. Defaults to &#x60;AmazonLinux2023&#x60;. | [optional] 
**auto_mode** | [**EKSAutoModeConfig**](EKSAutoModeConfig.md) | Configures EKS Auto Mode extensions (optional). Valid only when computeMode is AutoMode; on ManagedNodeGroups, provision GPU capacity through the self-managed Karpenter add-on instead. | [optional] 
**compute_mode** | [**EKSComputeMode**](EKSComputeMode.md) | Who creates and manages the worker nodes. &#x60;AutoMode&#x60; cannot be used with the Karpenter add-on. | [optional] 
**credentials** | [**Credentials**](Credentials.md) | The AWS credentials the cluster is created and managed with; required for a new cluster. Applying an existing cluster again without them, or with the type and no data, keeps the stored ones. | [optional] 
**ecr_account_ids** | **List[str]** | Other AWS accounts whose ECR the nodes pull from (optional, max 20). Their repository policies must allow the cluster&#39;s node roles, which the cluster reports. | [optional] 
**kubernetes_version** | **str** | The target Kubernetes version (optional). Accepts major.minor (e.g. \&quot;1.30\&quot;) or major.minor.patch (e.g. \&quot;1.30.14\&quot;) format. If omitted, AstroPulse uses the latest default version. | [optional] 
**subnets** | **Dict[str, List[SubnetSpec]]** | Maps availability zone names to subnet specifications for BYOVPC (optional). Required when VPCId is provided. Key is the zone name (e.g. \&quot;us-west-2a\&quot;), value is a list of SubnetSpec. | [optional] 
**tags** | **Dict[str, str]** | AWS tags applied to the cluster&#39;s node groups (optional, at most 40). Keys are 1-128 and values at most 256 letters, digits, spaces and _ . : / &#x3D; + - @; keys may not start with aws:, platform.astropulse.io/, alpha.eksctl.io/, eksctl.cluster.k8s.io/ or karpenter.sh/. | [optional] 
**vpc_cidr** | **str** | The VPC&#39;s IPv4 range: required with vpcId, where it must equal the existing VPC&#39;s CIDR, and optional without it, where it sets the new VPC&#39;s range (e.g. \&quot;10.0.0.0/16\&quot;). It must be a /16 to /24 inside 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16, 100.64.0.0/10 or 198.19.0.0/16. | [optional] 
**vpc_id** | **str** | The existing AWS VPC ID (optional, format: vpc-xxxxxxxx). If omitted, a new VPC is created. Provide for BYOVPC deployments. | [optional] 

## Example

```python
from astropulse._generated.models.eks_cluster_spec import EKSClusterSpec

# TODO update the JSON string below
json = "{}"
# create an instance of EKSClusterSpec from a JSON string
eks_cluster_spec_instance = EKSClusterSpec.from_json(json)
# print the JSON string representation of the object
print(EKSClusterSpec.to_json())

# convert the object into a dict
eks_cluster_spec_dict = eks_cluster_spec_instance.to_dict()
# create an instance of EKSClusterSpec from a dict
eks_cluster_spec_from_dict = EKSClusterSpec.from_dict(eks_cluster_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


