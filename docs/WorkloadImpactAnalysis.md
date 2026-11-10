# WorkloadImpactAnalysis


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**critical_workloads** | **List[str]** |  | [optional] 
**daemon_sets** | **int** |  | [optional] 
**impact_summary** | **str** |  | [optional] 
**single_replicas** | **int** |  | [optional] 
**stateful_sets** | **int** |  | [optional] 
**total_deployments** | **int** |  | [optional] 
**without_pdb** | **int** |  | [optional] 

## Example

```python
from astropulse._generated.models.workload_impact_analysis import WorkloadImpactAnalysis

# TODO update the JSON string below
json = "{}"
# create an instance of WorkloadImpactAnalysis from a JSON string
workload_impact_analysis_instance = WorkloadImpactAnalysis.from_json(json)
# print the JSON string representation of the object
print(WorkloadImpactAnalysis.to_json())

# convert the object into a dict
workload_impact_analysis_dict = workload_impact_analysis_instance.to_dict()
# create an instance of WorkloadImpactAnalysis from a dict
workload_impact_analysis_from_dict = WorkloadImpactAnalysis.from_dict(workload_impact_analysis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


