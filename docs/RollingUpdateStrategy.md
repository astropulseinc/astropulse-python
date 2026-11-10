# RollingUpdateStrategy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Says what this strategy trades off, in words to show. | [optional] 
**max_surge** | **str** | How many nodes may be added above the desired count while the update runs, as a count or a percentage; absent when each node group keeps its own. | [optional] 
**max_unavailable** | **str** | How many may be unavailable at once, as a count or a percentage; absent when each node group keeps its own. | [optional] 

## Example

```python
from astropulse._generated.models.rolling_update_strategy import RollingUpdateStrategy

# TODO update the JSON string below
json = "{}"
# create an instance of RollingUpdateStrategy from a JSON string
rolling_update_strategy_instance = RollingUpdateStrategy.from_json(json)
# print the JSON string representation of the object
print(RollingUpdateStrategy.to_json())

# convert the object into a dict
rolling_update_strategy_dict = rolling_update_strategy_instance.to_dict()
# create an instance of RollingUpdateStrategy from a dict
rolling_update_strategy_from_dict = RollingUpdateStrategy.from_dict(rolling_update_strategy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


