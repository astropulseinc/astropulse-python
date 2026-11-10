# ApplicationMetricsSeriesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ApplicationMetricsSeries**](ApplicationMetricsSeries.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.application_metrics_series_response import ApplicationMetricsSeriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationMetricsSeriesResponse from a JSON string
application_metrics_series_response_instance = ApplicationMetricsSeriesResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationMetricsSeriesResponse.to_json())

# convert the object into a dict
application_metrics_series_response_dict = application_metrics_series_response_instance.to_dict()
# create an instance of ApplicationMetricsSeriesResponse from a dict
application_metrics_series_response_from_dict = ApplicationMetricsSeriesResponse.from_dict(application_metrics_series_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


