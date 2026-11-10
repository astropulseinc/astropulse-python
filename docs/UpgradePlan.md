# UpgradePlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_name** | **str** | The name of the cluster being upgraded | [optional] 
**current_version** | **str** | The current Kubernetes version | [optional] 
**phases** | [**List[UpgradePlanPhase]**](UpgradePlanPhase.md) | Lists the upgrade phases in execution order | [optional] 
**preflight_checks** | [**List[PreflightCheck]**](PreflightCheck.md) | Contains automated validation checks run before the upgrade | [optional] 
**provider** | [**Provider**](Provider.md) | The cloud the cluster runs in. | [optional] 
**provisioner_type** | [**ProvisionerType**](ProvisionerType.md) | What created and manages the cluster. | [optional] 
**region** | **str** | The cloud provider region | [optional] 
**rolling_strategy** | [**RollingUpdateStrategy**](RollingUpdateStrategy.md) | Describes how existing nodes are replaced; absent when the update only creates node groups. | [optional] 
**target_version** | **str** | The target Kubernetes version | [optional] 
**unfinished_checks** | **List[str]** | Names the checks that did not finish, so they neither passed nor failed; run the dry run again. | [optional] 

## Example

```python
from astropulse._generated.models.upgrade_plan import UpgradePlan

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradePlan from a JSON string
upgrade_plan_instance = UpgradePlan.from_json(json)
# print the JSON string representation of the object
print(UpgradePlan.to_json())

# convert the object into a dict
upgrade_plan_dict = upgrade_plan_instance.to_dict()
# create an instance of UpgradePlan from a dict
upgrade_plan_from_dict = UpgradePlan.from_dict(upgrade_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


