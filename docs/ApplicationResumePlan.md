# ApplicationResumePlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_name** | **str** | The user-facing application name. | [optional] 
**configured_ref** | **str** | The branch/tag the app would resume tracking (e.g. \&quot;main\&quot;). | [optional] 
**current_resolved_ref** | **str** | The configured ref resolved to its current immutable revision. | [optional] 
**diff** | [**List[DeploymentDiffItem]**](DeploymentDiffItem.md) | The sanitized pinned→current change summary. | [optional] 
**next_actions** | **List[str]** | Concrete follow-up commands for humans/automation. | [optional] 
**pinned_revision** | **str** | The immutable revision the app is pinned to. | [optional] 
**pinned_version** | **str** | The Astro version currently pinned by rollback. | [optional] 
**requires_confirmation** | **bool** | Indicates a mutating apply needs confirmation (or --yes). | [optional] 
**summary** | **str** | Says in plain words what resuming does: the ref the application tracks again and the version it is pinned at. Empty when there is nothing to resume. | [optional] 
**warnings** | **List[str]** | Carries non-fatal advisories. | [optional] 

## Example

```python
from astropulse._generated.models.application_resume_plan import ApplicationResumePlan

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationResumePlan from a JSON string
application_resume_plan_instance = ApplicationResumePlan.from_json(json)
# print the JSON string representation of the object
print(ApplicationResumePlan.to_json())

# convert the object into a dict
application_resume_plan_dict = application_resume_plan_instance.to_dict()
# create an instance of ApplicationResumePlan from a dict
application_resume_plan_from_dict = ApplicationResumePlan.from_dict(application_resume_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


