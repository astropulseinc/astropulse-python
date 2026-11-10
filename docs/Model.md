# Model


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache** | [**ModelCache**](ModelCache.md) | Serves the artifact from the node&#39;s own disk instead of downloading it on every replica start. The target cluster&#39;s model-serving add-on must have its modelCache enabled. | [optional] 
**format** | [**ModelFormat**](ModelFormat.md) | The model format the serving runtime is selected from. Defaults to vLLM for hf:// artifacts, which is where the weights come from rather than what runs them; required otherwise. Like uri, it is fixed once the application has served. | [optional] 
**queue** | [**ModelQueue**](ModelQueue.md) | Admits the predictor&#39;s replicas through a workload queue: a ClusterQueue the target cluster&#39;s workload-queueing add-on declares. AstroPulse stamps Kueue&#39;s queue-name label on the predictor pods and renders a LocalQueue this application owns in its namespace; Kueue admits the replicas against the queue&#39;s quota. Whether a serving workload belongs in a queue is the builder&#39;s call. | [optional] 
**resources** | [**ModelResources**](ModelResources.md) | Declares the hardware one replica needs. | [optional] 
**runtime** | [**ModelRuntime**](ModelRuntime.md) | Pins the serving runtime instead of letting the format choose. Like uri, it is fixed once the application has served. | [optional] 
**scaling** | [**ModelScaling**](ModelScaling.md) | Bounds the replica count. | [optional] 
**serving** | [**ModelServing**](ModelServing.md) | Configures the inference API the model is served with. | [optional] 
**uri** | **str** | The model artifact. It can be corrected until the application has served, and is fixed after that.  Point it at bytes that cannot change underneath it. AstroPulse caches what it downloads and shares that copy between applications using the same artifact, so an artifact that moves is served from the copy taken the first time, and rolling back restores the spec rather than the same model. These forms name one exact artifact:  hf://&lt;org&gt;/&lt;repo&gt;:&lt;40-character commit sha&gt; oci://&lt;registry&gt;/&lt;repository&gt;@sha256:&lt;64 hex digits&gt; s3://&lt;bucket&gt;/&lt;object&gt;?versionId&#x3D;&lt;version id&gt; gs://&lt;bucket&gt;/&lt;object&gt;?generation&#x3D;&lt;generation&gt;  A Hugging Face branch or tag, an image tag, or a bucket key with no version names whatever was last written there.  pvc://&lt;claim&gt;/&lt;path&gt; is an existing volume, mounted as it is, with whatever guarantee its owner provides. Azure Blob Storage is accepted as https://&lt;account&gt;.blob.core.windows.net/&lt;container&gt;/&lt;path&gt;. Neither is copied by AstroPulse.  The only query parameters accepted are the two above, each on its own scheme. No credentials may appear in the URI: how a private artifact is read is set on the cluster. | [optional] 

## Example

```python
from astropulse._generated.models.model import Model

# TODO update the JSON string below
json = "{}"
# create an instance of Model from a JSON string
model_instance = Model.from_json(json)
# print the JSON string representation of the object
print(Model.to_json())

# convert the object into a dict
model_dict = model_instance.to_dict()
# create an instance of Model from a dict
model_from_dict = Model.from_dict(model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


