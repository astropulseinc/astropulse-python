# InferenceMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generation_tokens_per_second** | **float** | How many output tokens were produced each second -- what an accelerator-hour buys. Generative runtimes only. | [optional] 
**kv_cache_utilization** | **float** | The fraction (0..1) of the accelerator&#39;s KV cache in use -- the pressure that precedes queueing. Generative runtimes only. | [optional] 
**prompt_tokens_per_second** | **float** | How many input tokens were consumed each second. Generative runtimes only. | [optional] 
**request_count** | **float** | How many observations the percentiles above rest on. | [optional] 
**request_latency_mean_seconds** | **float** | The mean end-to-end request latency. | [optional] 
**request_latency_p50_seconds** | **float** | The median end-to-end request latency. | [optional] 
**request_latency_p95_seconds** | **float** | The 95th-percentile end-to-end request latency. | [optional] 
**request_latency_p99_seconds** | **float** | The 99th-percentile end-to-end request latency. | [optional] 
**requests_per_second** | **float** | How many requests the model served each second. | [optional] 
**requests_running** | **float** | The mean number of requests executing at once. | [optional] 
**requests_waiting** | **float** | The mean number of requests queued for execution, and the signal queue-depth autoscaling follows. Rising while RequestsRunning is flat means too few replicas. | [optional] 
**runtime** | [**InferenceRuntime**](InferenceRuntime.md) | The serving runtime family the numbers came from, which says which of the fields below to expect. | [optional] 
**runtime_name** | **str** | The serving runtime by name -- \&quot;sklearnserver\&quot;, \&quot;vLLM\&quot;. Absent when the image names nothing recognisable. | [optional] 
**time_per_output_token_p50_seconds** | **float** | The median gap between output tokens once the stream has started. Generative runtimes only. | [optional] 
**time_per_output_token_p95_seconds** | **float** | The 95th-percentile gap between output tokens. Generative runtimes only. | [optional] 
**time_to_first_token_p50_seconds** | **float** | The median wait for the first token. Generative runtimes only. | [optional] 
**time_to_first_token_p95_seconds** | **float** | The 95th-percentile wait for the first token. Generative runtimes only. | [optional] 
**time_to_first_token_p99_seconds** | **float** | The 99th-percentile wait for the first token. Generative runtimes only. | [optional] 

## Example

```python
from astropulse._generated.models.inference_metrics import InferenceMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of InferenceMetrics from a JSON string
inference_metrics_instance = InferenceMetrics.from_json(json)
# print the JSON string representation of the object
print(InferenceMetrics.to_json())

# convert the object into a dict
inference_metrics_dict = inference_metrics_instance.to_dict()
# create an instance of InferenceMetrics from a dict
inference_metrics_from_dict = InferenceMetrics.from_dict(inference_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


