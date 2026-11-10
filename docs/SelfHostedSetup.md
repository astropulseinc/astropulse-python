# SelfHostedSetup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_hint** | **str** | The email address of the Google account the setup was started for; omitted when none was given. | [optional] 
**account_id** | **str** | The AWS account or GCP project. | [optional] 
**bucket_name** | **str** | The bucket that holds the cluster&#39;s state, the one to name when creating the cluster. | [optional] 
**cleanup_commands** | **List[str]** | The shell commands that remove what the setup creates once no cluster uses it, in order. On GCP they keep a service account or bucket the setup did not create. | [optional] 
**cluster_name** | **str** | The cluster the resources are for. | [optional] 
**commands** | **List[str]** | The shell commands that create the resources, in order (GCP). | [optional] 
**connect** | [**SelfHostedConnectStep**](SelfHostedConnectStep.md) | The command that sends the setup&#39;s credentials to the vault, or replaces the stored ones once they are there; omitted before the resources can exist. | [optional] 
**credential_status** | [**SelfHostedCredentialStatus**](SelfHostedCredentialStatus.md) | How the cluster&#39;s credentials stored in AstroPulse stand; omitted when credential storage is not configured. | [optional] 
**note** | **str** | Says what the setup creates, what it costs and how to remove it. | [optional] 
**notice** | [**Notice**](Notice.md) | Says where the setup stands and the next step to take. | [optional] 
**outcome** | [**Outcome**](Outcome.md) | Blocked when the setup failed, and proceed otherwise. | [optional] 
**provider** | [**Provider**](Provider.md) | The cloud the resources are in. | [optional] 
**region** | **str** | Where the resources are created. | [optional] 
**resources** | **Dict[str, str]** | Names what setup creates, by kind (stack, user, bucket, serviceAccount, ...). | [optional] 
**shell** | **str** | Where to run &#x60;commands&#x60; and &#x60;cleanupCommands&#x60;, such as Cloud Shell. | [optional] 
**stack_name** | **str** | The CloudFormation stack the setup creates (AWS). | [optional] 
**state** | [**SelfHostedSetupState**](SelfHostedSetupState.md) | Where the setup stands as a whole. | [optional] 
**steps** | [**List[SetupStep]**](SetupStep.md) | The recorded steps, in order. | [optional] 
**summary** | **str** | Says in one sentence where the setup stands now. | [optional] 

## Example

```python
from astropulse._generated.models.self_hosted_setup import SelfHostedSetup

# TODO update the JSON string below
json = "{}"
# create an instance of SelfHostedSetup from a JSON string
self_hosted_setup_instance = SelfHostedSetup.from_json(json)
# print the JSON string representation of the object
print(SelfHostedSetup.to_json())

# convert the object into a dict
self_hosted_setup_dict = self_hosted_setup_instance.to_dict()
# create an instance of SelfHostedSetup from a dict
self_hosted_setup_from_dict = SelfHostedSetup.from_dict(self_hosted_setup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


