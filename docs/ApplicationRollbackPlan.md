# ApplicationRollbackPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_name** | **str** | The user-facing application name. | [optional] 
**applied_version** | **str** | The newest version applied, set only when it did not finish deploying. | [optional] 
**current_version** | **str** | The version last confirmed running, as listed in the application&#39;s history. | [optional] 
**diff** | [**List[DeploymentDiffItem]**](DeploymentDiffItem.md) | The sanitized current→target change summary. | [optional] 
**eligible** | **bool** | Indicates the rollback can proceed. | [optional] 
**next_actions** | **List[str]** | Concrete follow-up commands for humans/automation. | [optional] 
**pinned_after_rollback** | **bool** | Indicates the rollback will leave the application in RollbackPinned until it is resumed. | [optional] 
**requires_confirmation** | **bool** | Indicates a mutating apply needs confirmation (or --yes). | [optional] 
**target_source_identity** | [**SourceIdentity**](SourceIdentity.md) | The immutable identity that would be deployed. | [optional] 
**target_version** | **str** | The Astro version that would be rolled back to. | [optional] 
**title** | **str** | The plan&#39;s verdict as a headline to show. | [optional] 
**unavailable_reason** | **str** | Explains why an ineligible rollback cannot proceed. | [optional] 
**warnings** | **List[str]** | Carries non-fatal advisories (e.g. profile drift, current sync OutOfSync). | [optional] 

## Example

```python
from astropulse._generated.models.application_rollback_plan import ApplicationRollbackPlan

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationRollbackPlan from a JSON string
application_rollback_plan_instance = ApplicationRollbackPlan.from_json(json)
# print the JSON string representation of the object
print(ApplicationRollbackPlan.to_json())

# convert the object into a dict
application_rollback_plan_dict = application_rollback_plan_instance.to_dict()
# create an instance of ApplicationRollbackPlan from a dict
application_rollback_plan_from_dict = ApplicationRollbackPlan.from_dict(application_rollback_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


