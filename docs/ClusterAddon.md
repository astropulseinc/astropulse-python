# ClusterAddon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accelerator** | [**ClusterAddonAcceleratorReadiness**](ClusterAddonAcceleratorReadiness.md) | Reported for the accelerator-metrics add-on only: what this cluster has for the exporter to measure. See ClusterAddonAcceleratorReadiness. | [optional] 
**available_upgrades** | **List[str]** | The versions it can move to, ordered oldest to newest: the last one is the newest release on offer. | [optional] 
**configurable** | **bool** | Reports whether this add-on accepts a configuration. False means it installs with no settings of its own. | [optional] 
**configuration** | [**ClusterAddonConfiguration**](ClusterAddonConfiguration.md) | The settings it is running with, as they were applied. | [optional] 
**current_version** | **str** | The Astro chart version installed -- what &#x60;apply --version&#x60; and rollback take. See UpstreamVersion for the release inside. | [optional] 
**deployed_at** | **str** | When the add-on was first installed, RFC 3339. | [optional] 
**display_name** | **str** | The add-on&#39;s name in front of a person. | [optional] 
**endpoint_authentication** | **List[str]** | Lists the access-policy mechanisms (jwt, apiKeys) the installed release enforces on model endpoints. Absent when the add-on cannot enforce any: an exposure add-on that only routes, or a release the catalog does not declare. | [optional] 
**exposure** | [**ClusterAddonExposure**](ClusterAddonExposure.md) | How the add-on can be reached, for the exposure add-ons (gateway, nginx-ingress) only, as the cluster agent last observed it. Absent on every other add-on. | [optional] 
**findings_policy** | **str** | Says which findings the vulnerability-scanning add-on leaves out of its results. Absent on every other add-on. | [optional] 
**health** | [**ClusterAddonHealth**](ClusterAddonHealth.md) | What the cluster reports about the add-on&#39;s own workload. | [optional] 
**ingress_tls** | [**ClusterAddonIngressTLS**](ClusterAddonIngressTLS.md) | Reported for the nginx-ingress add-on only: the TLS modes it offers applications. | [optional] 
**last_updated_at** | **str** | When it was last changed, RFC 3339. | [optional] 
**model_cache** | [**ClusterAddonModelCacheReadiness**](ClusterAddonModelCacheReadiness.md) | Reported for the model-serving add-on only: what its weight cache holds on this cluster, and how the cluster&#39;s models read private artifacts. See ClusterAddonModelCacheReadiness. | [optional] 
**name** | **str** | The name of the Application serving this add-on on the cluster. | [optional] 
**pricing** | [**ClusterAddonCostPricing**](ClusterAddonCostPricing.md) | Reported for the cost-visibility add-on only: the price-sheet rates its configuration sets that this cluster does not apply yet. Absent when every rate applies. | [optional] 
**queue_namespaces** | [**ClusterAddonQueueNamespaces**](ClusterAddonQueueNamespaces.md) | Is, for the workload-queueing add-on, where the namespaces it gives a queue differ from those of the queued applications; absent when they agree. | [optional] 
**resilience** | [**ClusterAddonResilience**](ClusterAddonResilience.md) | How the add-on runs on this cluster: its effective availability, how many copies run and why, and its main component&#39;s sizing. | [optional] 
**status** | [**ClusterAddonStatus**](ClusterAddonStatus.md) | The lifecycle answer: is this add-on installed and working? A resync or upgrade of a working add-on leaves it &#x60;Deployed&#x60;, because it is still installed and still serving. | [optional] 
**status_notice** | [**Notice**](Notice.md) | Says what a failed or unhealthy status, or an unfinished rollback, means and the one step that resolves it; absent otherwise. | [optional] 
**status_reason** | **str** | A sentence explaining the add-on&#39;s status, such as why it failed or why no upgrade is offered. Empty when there is nothing to explain. | [optional] 
**support** | [**ClusterAddonSupport**](ClusterAddonSupport.md) | Says whether the installed version is supported and until when. Absent when the installed version is not known. | [optional] 
**syncing** | **bool** | The operation answer: is deployment work in flight right now? &#x60;status&#x60; stays &#x60;Deployed&#x60; while a working add-on is resynced or upgraded. | [optional] 
**tls** | [**ClusterAddonTLSReadiness**](ClusterAddonTLSReadiness.md) | Reported for the cert-manager add-on only: what its configuration can mint on this cluster. See ClusterAddonTLSReadiness. | [optional] 
**type** | [**ClusterAddonType**](ClusterAddonType.md) | The add-on&#39;s public name, and what every add-on command takes. | [optional] 
**upstream_version** | **str** | The third-party release the installed version runs, such as \&quot;cert-manager v1.21.2\&quot; or \&quot;KServe v0.20.0\&quot;. Empty when there is none. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon import ClusterAddon

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddon from a JSON string
cluster_addon_instance = ClusterAddon.from_json(json)
# print the JSON string representation of the object
print(ClusterAddon.to_json())

# convert the object into a dict
cluster_addon_dict = cluster_addon_instance.to_dict()
# create an instance of ClusterAddon from a dict
cluster_addon_from_dict = ClusterAddon.from_dict(cluster_addon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


