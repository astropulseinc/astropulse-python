# UpdateConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_downgrade** | **bool** | Permits rollback to an older Kubernetes version. Required when target version is older than current version. Default: false (downgrades rejected for safety). | [optional] 
**dry_run** | **bool** | Validates the update without executing it. Returns the execution plan with preflight results, selected strategy, estimated duration, and any blocking issues. Default: false. | [optional] 
**generate_report** | **bool** | Produces a comprehensive readiness report including the execution plan, strategy selection rationale, risk assessment, and provider-specific recommendations. Default: false. | [optional] 
**max_surge** | **str** | How many extra nodes may be added above the desired count during the update, as a count (\&quot;1\&quot;) or a percentage (\&quot;25%\&quot;). When omitted, each node group keeps its own setting. | [optional] 
**max_unavailable** | **str** | How many nodes may be unavailable at once during the update, as a count (\&quot;2\&quot;) or a percentage (\&quot;25%\&quot;). When omitted, each node group keeps its own setting. | [optional] 
**reapply** | **bool** | Applies the named node groups even when they are unchanged, which replaces their nodes on a self-hosted cluster. Default: false. | [optional] 
**replace_running** | **bool** | Cancels the update that is running on the cluster and starts this one once it has stopped. Without it, an update sent while another runs is refused. Default: false. | [optional] 

## Example

```python
from astropulse._generated.models.update_config import UpdateConfig

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateConfig from a JSON string
update_config_instance = UpdateConfig.from_json(json)
# print the JSON string representation of the object
print(UpdateConfig.to_json())

# convert the object into a dict
update_config_dict = update_config_instance.to_dict()
# create an instance of UpdateConfig from a dict
update_config_from_dict = UpdateConfig.from_dict(update_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


