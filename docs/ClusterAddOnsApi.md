# astropulse._generated.ClusterAddOnsApi

All URIs are relative to *https://api.astropulse.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_cluster_addon**](ClusterAddOnsApi.md#delete_cluster_addon) | **DELETE** /api/v1/clusters/{clusterName}/addons/{addonType} | Delete a managed cluster add-on
[**deploy_cluster_addon**](ClusterAddOnsApi.md#deploy_cluster_addon) | **POST** /api/v1/clusters/{clusterName}/addons/{addonType}/deploy | Deploy a managed cluster add-on
[**get_cluster_addon**](ClusterAddOnsApi.md#get_cluster_addon) | **GET** /api/v1/clusters/{clusterName}/addons/{addonType} | Get a managed cluster add-on
[**get_cluster_addon_catalog**](ClusterAddOnsApi.md#get_cluster_addon_catalog) | **GET** /api/v1/clusters/{clusterName}/addons/catalog | Get the add-on catalog for a cluster
[**get_cluster_addon_cost_series**](ClusterAddOnsApi.md#get_cluster_addon_cost_series) | **GET** /api/v1/clusters/{clusterName}/addons/{addonType}/cost/series | Get managed cluster add-on cost over time
[**get_cluster_addon_cost_summary**](ClusterAddOnsApi.md#get_cluster_addon_cost_summary) | **GET** /api/v1/clusters/{clusterName}/addons/{addonType}/cost/summary | Get managed cluster add-on cost summary
[**get_cluster_addon_finding_detail**](ClusterAddOnsApi.md#get_cluster_addon_finding_detail) | **GET** /api/v1/clusters/{clusterName}/addons/{addonType}/findings/detail | Get live per-CVE detail for one scanned workload
[**get_cluster_addon_findings**](ClusterAddOnsApi.md#get_cluster_addon_findings) | **GET** /api/v1/clusters/{clusterName}/addons/{addonType}/findings | Get the latest vulnerability scan findings for a cluster
[**get_cluster_addon_metrics_series**](ClusterAddOnsApi.md#get_cluster_addon_metrics_series) | **GET** /api/v1/clusters/{clusterName}/addons/{addonType}/metrics/series | Get managed cluster add-on resource usage
[**get_cluster_addon_spec**](ClusterAddOnsApi.md#get_cluster_addon_spec) | **GET** /api/v1/clusters/{clusterName}/addons/{addonType}/spec | Get a managed cluster add-on&#39;s manifest
[**get_cluster_exposure**](ClusterAddOnsApi.md#get_cluster_exposure) | **GET** /api/v1/clusters/{clusterName}/exposure | Get a cluster&#39;s exposure
[**list_cluster_addon_history**](ClusterAddOnsApi.md#list_cluster_addon_history) | **GET** /api/v1/clusters/{clusterName}/addons/{addonType}/history | Get managed cluster add-on deployment history
[**list_cluster_addon_versions**](ClusterAddOnsApi.md#list_cluster_addon_versions) | **GET** /api/v1/clusters/{clusterName}/addons/{addonType}/versions | List supported versions for a managed cluster add-on
[**list_cluster_addons**](ClusterAddOnsApi.md#list_cluster_addons) | **GET** /api/v1/clusters/{clusterName}/addons | List managed add-ons for a cluster
[**resync_cluster_addon**](ClusterAddOnsApi.md#resync_cluster_addon) | **POST** /api/v1/clusters/{clusterName}/addons/{addonType}/resync | Resync a managed cluster add-on
[**rollback_cluster_addon**](ClusterAddOnsApi.md#rollback_cluster_addon) | **POST** /api/v1/clusters/{clusterName}/addons/{addonType}/rollback | Roll back a managed cluster add-on
[**update_cluster_addon**](ClusterAddOnsApi.md#update_cluster_addon) | **PUT** /api/v1/clusters/{clusterName}/addons/{addonType} | Update a managed cluster add-on
[**update_cluster_exposure**](ClusterAddOnsApi.md#update_cluster_exposure) | **PUT** /api/v1/clusters/{clusterName}/exposure | Set a cluster&#39;s exposure settings


# **delete_cluster_addon**
> ClusterAddonOperationResponse delete_cluster_addon(cluster_name, addon_type, force=force, timeout=timeout)

Delete a managed cluster add-on

Removes the managed add-on from the cluster. The astro-agent add-on cannot be deleted; it is removed when a registered cluster is unregistered or a provisioned cluster is deleted.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_addon_operation_response import ClusterAddonOperationResponse
from astropulse._generated.models.cluster_addon_type import ClusterAddonType
from astropulse._generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astropulse.io
# See configuration.py for a list of all supported configuration parameters.
configuration = astropulse._generated.Configuration(
    host = "https://api.astropulse.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = astropulse._generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with astropulse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astropulse._generated.ClusterAddOnsApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    addon_type = astropulse._generated.ClusterAddonType() # ClusterAddonType | Add-on type
    force = True # bool | Delete even when another installed add-on depends on this add-on (optional)
    timeout = 'timeout_example' # str | Deletion timeout (for example 10m) (optional)

    try:
        # Delete a managed cluster add-on
        api_response = api_instance.delete_cluster_addon(cluster_name, addon_type, force=force, timeout=timeout)
        print("The response of ClusterAddOnsApi->delete_cluster_addon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterAddOnsApi->delete_cluster_addon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **addon_type** | [**ClusterAddonType**](.md)| Add-on type | 
 **force** | **bool**| Delete even when another installed add-on depends on this add-on | [optional] 
 **timeout** | **str**| Deletion timeout (for example 10m) | [optional] 

### Return type

[**ClusterAddonOperationResponse**](ClusterAddonOperationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | The delete was refused: the cluster is not ready, something still depends on the add-on, or the add-on can never be deleted on its own (reason AddonClusterManaged) |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy_cluster_addon**
> ClusterAddonOperationResponse deploy_cluster_addon(cluster_name, addon_type, deploy_cluster_addon_request)

Deploy a managed cluster add-on

Validates the requested configuration and deploys the managed add-on. Applying the configuration the add-on already runs changes nothing. A configuration whose last deployment failed is refused with 409; fix the cause, then resync the add-on to retry it.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_addon_operation_response import ClusterAddonOperationResponse
from astropulse._generated.models.cluster_addon_type import ClusterAddonType
from astropulse._generated.models.deploy_cluster_addon_request import DeployClusterAddonRequest
from astropulse._generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astropulse.io
# See configuration.py for a list of all supported configuration parameters.
configuration = astropulse._generated.Configuration(
    host = "https://api.astropulse.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = astropulse._generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with astropulse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astropulse._generated.ClusterAddOnsApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    addon_type = astropulse._generated.ClusterAddonType() # ClusterAddonType | Add-on type
    deploy_cluster_addon_request = astropulse._generated.DeployClusterAddonRequest() # DeployClusterAddonRequest | Deployment request

    try:
        # Deploy a managed cluster add-on
        api_response = api_instance.deploy_cluster_addon(cluster_name, addon_type, deploy_cluster_addon_request)
        print("The response of ClusterAddOnsApi->deploy_cluster_addon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterAddOnsApi->deploy_cluster_addon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **addon_type** | [**ClusterAddonType**](.md)| Add-on type | 
 **deploy_cluster_addon_request** | [**DeployClusterAddonRequest**](DeployClusterAddonRequest.md)| Deployment request | 

### Return type

[**ClusterAddonOperationResponse**](ClusterAddonOperationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dry-run validation succeeded, or nothing was started and a notice says why |  -  |
**202** | Deployment initiated |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_addon**
> ClusterAddonResponse get_cluster_addon(cluster_name, addon_type)

Get a managed cluster add-on

Returns one platform-managed add-on and its lifecycle state.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_addon_response import ClusterAddonResponse
from astropulse._generated.models.cluster_addon_type import ClusterAddonType
from astropulse._generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astropulse.io
# See configuration.py for a list of all supported configuration parameters.
configuration = astropulse._generated.Configuration(
    host = "https://api.astropulse.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = astropulse._generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with astropulse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astropulse._generated.ClusterAddOnsApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    addon_type = astropulse._generated.ClusterAddonType() # ClusterAddonType | Add-on type

    try:
        # Get a managed cluster add-on
        api_response = api_instance.get_cluster_addon(cluster_name, addon_type)
        print("The response of ClusterAddOnsApi->get_cluster_addon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterAddOnsApi->get_cluster_addon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **addon_type** | [**ClusterAddonType**](.md)| Add-on type | 

### Return type

[**ClusterAddonResponse**](ClusterAddonResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_addon_catalog**
> ClusterAddonCatalogEntryListResponse get_cluster_addon_catalog(cluster_name)

Get the add-on catalog for a cluster

Returns AstroPulse's add-on catalog with compatibility evaluated for this cluster by the same rules that gate deployment.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_addon_catalog_entry_list_response import ClusterAddonCatalogEntryListResponse
from astropulse._generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astropulse.io
# See configuration.py for a list of all supported configuration parameters.
configuration = astropulse._generated.Configuration(
    host = "https://api.astropulse.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = astropulse._generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with astropulse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astropulse._generated.ClusterAddOnsApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name

    try:
        # Get the add-on catalog for a cluster
        api_response = api_instance.get_cluster_addon_catalog(cluster_name)
        print("The response of ClusterAddOnsApi->get_cluster_addon_catalog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterAddOnsApi->get_cluster_addon_catalog: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 

### Return type

[**ClusterAddonCatalogEntryListResponse**](ClusterAddonCatalogEntryListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_addon_cost_series**
> ClusterAddonCostSeriesResponse get_cluster_addon_cost_series(cluster_name, addon_type, window=window, interval=interval)

Get managed cluster add-on cost over time

Returns the add-on's cost over time. Missing intervals are never converted to zero spend; an astro-agent not yet recorded as the cluster's add-on has no points.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_addon_cost_series_response import ClusterAddonCostSeriesResponse
from astropulse._generated.models.cluster_addon_type import ClusterAddonType
from astropulse._generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astropulse.io
# See configuration.py for a list of all supported configuration parameters.
configuration = astropulse._generated.Configuration(
    host = "https://api.astropulse.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = astropulse._generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with astropulse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astropulse._generated.ClusterAddOnsApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    addon_type = astropulse._generated.ClusterAddonType() # ClusterAddonType | Add-on type
    window = '24h' # str | Window duration (for example 24h, 7d, 30d) (optional) (default to '24h')
    interval = 'auto' # str | Bucket interval, or auto (optional) (default to 'auto')

    try:
        # Get managed cluster add-on cost over time
        api_response = api_instance.get_cluster_addon_cost_series(cluster_name, addon_type, window=window, interval=interval)
        print("The response of ClusterAddOnsApi->get_cluster_addon_cost_series:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterAddOnsApi->get_cluster_addon_cost_series: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **addon_type** | [**ClusterAddonType**](.md)| Add-on type | 
 **window** | **str**| Window duration (for example 24h, 7d, 30d) | [optional] [default to &#39;24h&#39;]
 **interval** | **str**| Bucket interval, or auto | [optional] [default to &#39;auto&#39;]

### Return type

[**ClusterAddonCostSeriesResponse**](ClusterAddonCostSeriesResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_addon_cost_summary**
> ClusterAddonCostSummaryResponse get_cluster_addon_cost_summary(cluster_name, addon_type, window=window)

Get managed cluster add-on cost summary

Returns the add-on's cost summary. Coverage says how completely the cluster reported; no reported allocation is not zero spend. An astro-agent not yet recorded as the cluster's add-on reports none.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_addon_cost_summary_response import ClusterAddonCostSummaryResponse
from astropulse._generated.models.cluster_addon_type import ClusterAddonType
from astropulse._generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astropulse.io
# See configuration.py for a list of all supported configuration parameters.
configuration = astropulse._generated.Configuration(
    host = "https://api.astropulse.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = astropulse._generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with astropulse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astropulse._generated.ClusterAddOnsApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    addon_type = astropulse._generated.ClusterAddonType() # ClusterAddonType | Add-on type
    window = '24h' # str | Window duration (for example 24h, 7d, 30d) (optional) (default to '24h')

    try:
        # Get managed cluster add-on cost summary
        api_response = api_instance.get_cluster_addon_cost_summary(cluster_name, addon_type, window=window)
        print("The response of ClusterAddOnsApi->get_cluster_addon_cost_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterAddOnsApi->get_cluster_addon_cost_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **addon_type** | [**ClusterAddonType**](.md)| Add-on type | 
 **window** | **str**| Window duration (for example 24h, 7d, 30d) | [optional] [default to &#39;24h&#39;]

### Return type

[**ClusterAddonCostSummaryResponse**](ClusterAddonCostSummaryResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_addon_finding_detail**
> VulnerabilityFindingDetailResponse get_cluster_addon_finding_detail(cluster_name, addon_type, namespace, kind, name)

Get live per-CVE detail for one scanned workload

Returns normalized per-vulnerability details for one workload. Detail is read from the cluster on demand and is not persisted by AstroPulse.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_addon_type import ClusterAddonType
from astropulse._generated.models.vulnerability_finding_detail_response import VulnerabilityFindingDetailResponse
from astropulse._generated.models.workload_kind import WorkloadKind
from astropulse._generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astropulse.io
# See configuration.py for a list of all supported configuration parameters.
configuration = astropulse._generated.Configuration(
    host = "https://api.astropulse.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = astropulse._generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with astropulse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astropulse._generated.ClusterAddOnsApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    addon_type = astropulse._generated.ClusterAddonType() # ClusterAddonType | Add-on type. Takes only `vulnerability-scanning`.
    namespace = 'namespace_example' # str | Workload namespace
    kind = astropulse._generated.WorkloadKind() # WorkloadKind | Workload owner kind
    name = 'name_example' # str | Workload name

    try:
        # Get live per-CVE detail for one scanned workload
        api_response = api_instance.get_cluster_addon_finding_detail(cluster_name, addon_type, namespace, kind, name)
        print("The response of ClusterAddOnsApi->get_cluster_addon_finding_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterAddOnsApi->get_cluster_addon_finding_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **addon_type** | [**ClusterAddonType**](.md)| Add-on type. Takes only &#x60;vulnerability-scanning&#x60;. | 
 **namespace** | **str**| Workload namespace | 
 **kind** | [**WorkloadKind**](.md)| Workload owner kind | 
 **name** | **str**| Workload name | 

### Return type

[**VulnerabilityFindingDetailResponse**](VulnerabilityFindingDetailResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_addon_findings**
> ClusterScanFindingsSummaryResponse get_cluster_addon_findings(cluster_name, addon_type)

Get the latest vulnerability scan findings for a cluster

Returns the latest per-workload and per-image vulnerability severity counts. Freshness timestamps are included so callers can evaluate the result against the cluster's configured scan frequency. With no results, a 404 says why: its reason is ScannerNotInstalled, NothingToScan, ImagesNotScannable, ScanPending or ScanOverdue, with the title and nextStep that say what to do; its details list any unscannedImages.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_addon_type import ClusterAddonType
from astropulse._generated.models.cluster_scan_findings_summary_response import ClusterScanFindingsSummaryResponse
from astropulse._generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astropulse.io
# See configuration.py for a list of all supported configuration parameters.
configuration = astropulse._generated.Configuration(
    host = "https://api.astropulse.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = astropulse._generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with astropulse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astropulse._generated.ClusterAddOnsApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    addon_type = astropulse._generated.ClusterAddonType() # ClusterAddonType | Add-on type. Takes only `vulnerability-scanning`.

    try:
        # Get the latest vulnerability scan findings for a cluster
        api_response = api_instance.get_cluster_addon_findings(cluster_name, addon_type)
        print("The response of ClusterAddOnsApi->get_cluster_addon_findings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterAddOnsApi->get_cluster_addon_findings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **addon_type** | [**ClusterAddonType**](.md)| Add-on type. Takes only &#x60;vulnerability-scanning&#x60;. | 

### Return type

[**ClusterScanFindingsSummaryResponse**](ClusterScanFindingsSummaryResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_addon_metrics_series**
> ClusterAddonMetricsSeriesResponse get_cluster_addon_metrics_series(cluster_name, addon_type, window=window)

Get managed cluster add-on resource usage

Returns CPU, memory, and network usage for the add-on. A window with no reported sample is absent rather than zero; an astro-agent not yet recorded as the cluster's add-on reports none.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_addon_metrics_series_response import ClusterAddonMetricsSeriesResponse
from astropulse._generated.models.cluster_addon_type import ClusterAddonType
from astropulse._generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astropulse.io
# See configuration.py for a list of all supported configuration parameters.
configuration = astropulse._generated.Configuration(
    host = "https://api.astropulse.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = astropulse._generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with astropulse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astropulse._generated.ClusterAddOnsApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    addon_type = astropulse._generated.ClusterAddonType() # ClusterAddonType | Add-on type
    window = '1h' # str | Window duration (for example 15m, 1h, 24h) (optional) (default to '1h')

    try:
        # Get managed cluster add-on resource usage
        api_response = api_instance.get_cluster_addon_metrics_series(cluster_name, addon_type, window=window)
        print("The response of ClusterAddOnsApi->get_cluster_addon_metrics_series:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterAddOnsApi->get_cluster_addon_metrics_series: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **addon_type** | [**ClusterAddonType**](.md)| Add-on type | 
 **window** | **str**| Window duration (for example 15m, 1h, 24h) | [optional] [default to &#39;1h&#39;]

### Return type

[**ClusterAddonMetricsSeriesResponse**](ClusterAddonMetricsSeriesResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_addon_spec**
> K8sClusterAddonManifestResponse get_cluster_addon_spec(cluster_name, addon_type)

Get a managed cluster add-on's manifest

Returns the manifest of an installed add-on, its version and configuration, in the shape an add-on apply takes. Credential values are never included.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_addon_type import ClusterAddonType
from astropulse._generated.models.k8s_cluster_addon_manifest_response import K8sClusterAddonManifestResponse
from astropulse._generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astropulse.io
# See configuration.py for a list of all supported configuration parameters.
configuration = astropulse._generated.Configuration(
    host = "https://api.astropulse.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = astropulse._generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with astropulse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astropulse._generated.ClusterAddOnsApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    addon_type = astropulse._generated.ClusterAddonType() # ClusterAddonType | Add-on type

    try:
        # Get a managed cluster add-on's manifest
        api_response = api_instance.get_cluster_addon_spec(cluster_name, addon_type)
        print("The response of ClusterAddOnsApi->get_cluster_addon_spec:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterAddOnsApi->get_cluster_addon_spec: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **addon_type** | [**ClusterAddonType**](.md)| Add-on type | 

### Return type

[**K8sClusterAddonManifestResponse**](K8sClusterAddonManifestResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Unsupported add-on type or invalid cluster name |  -  |
**401** | Missing or invalid credentials |  -  |
**403** | Not a member of the cluster&#39;s organization |  -  |
**404** | Cluster not found, or the add-on is not installed |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Add-on state is temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_exposure**
> ClusterExposureResponse get_cluster_exposure(cluster_name)

Get a cluster's exposure

Returns how the cluster exposes applications over TLS: the ClusterIssuer in use and whether the agent observed it Ready, who runs cert-manager and external-dns, and whether exposure takes the gateway path.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_exposure_response import ClusterExposureResponse
from astropulse._generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astropulse.io
# See configuration.py for a list of all supported configuration parameters.
configuration = astropulse._generated.Configuration(
    host = "https://api.astropulse.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = astropulse._generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with astropulse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astropulse._generated.ClusterAddOnsApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name

    try:
        # Get a cluster's exposure
        api_response = api_instance.get_cluster_exposure(cluster_name)
        print("The response of ClusterAddOnsApi->get_cluster_exposure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterAddOnsApi->get_cluster_exposure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 

### Return type

[**ClusterExposureResponse**](ClusterExposureResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cluster_addon_history**
> ClusterAddonHistoryResponseEnvelope list_cluster_addon_history(cluster_name, addon_type)

Get managed cluster add-on deployment history

Returns the add-on's deployment and update history. An add-on that is not installed on the cluster is not found; an astro-agent not yet recorded as the cluster's add-on has an empty history.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_addon_history_response_envelope import ClusterAddonHistoryResponseEnvelope
from astropulse._generated.models.cluster_addon_type import ClusterAddonType
from astropulse._generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astropulse.io
# See configuration.py for a list of all supported configuration parameters.
configuration = astropulse._generated.Configuration(
    host = "https://api.astropulse.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = astropulse._generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with astropulse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astropulse._generated.ClusterAddOnsApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    addon_type = astropulse._generated.ClusterAddonType() # ClusterAddonType | Add-on type

    try:
        # Get managed cluster add-on deployment history
        api_response = api_instance.list_cluster_addon_history(cluster_name, addon_type)
        print("The response of ClusterAddOnsApi->list_cluster_addon_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterAddOnsApi->list_cluster_addon_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **addon_type** | [**ClusterAddonType**](.md)| Add-on type | 

### Return type

[**ClusterAddonHistoryResponseEnvelope**](ClusterAddonHistoryResponseEnvelope.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cluster_addon_versions**
> ClusterAddonVersionListResponse list_cluster_addon_versions(cluster_name, addon_type)

List supported versions for a managed cluster add-on

Returns the versions of the add-on that can be applied to this cluster. When none is offered, data is empty and message says why.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_addon_type import ClusterAddonType
from astropulse._generated.models.cluster_addon_version_list_response import ClusterAddonVersionListResponse
from astropulse._generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astropulse.io
# See configuration.py for a list of all supported configuration parameters.
configuration = astropulse._generated.Configuration(
    host = "https://api.astropulse.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = astropulse._generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with astropulse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astropulse._generated.ClusterAddOnsApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    addon_type = astropulse._generated.ClusterAddonType() # ClusterAddonType | Add-on type

    try:
        # List supported versions for a managed cluster add-on
        api_response = api_instance.list_cluster_addon_versions(cluster_name, addon_type)
        print("The response of ClusterAddOnsApi->list_cluster_addon_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterAddOnsApi->list_cluster_addon_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **addon_type** | [**ClusterAddonType**](.md)| Add-on type | 

### Return type

[**ClusterAddonVersionListResponse**](ClusterAddonVersionListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cluster_addons**
> ClusterAddonListResponse list_cluster_addons(cluster_name)

List managed add-ons for a cluster

Returns the managed add-ons installed on the cluster and their current lifecycle state.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_addon_list_response import ClusterAddonListResponse
from astropulse._generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astropulse.io
# See configuration.py for a list of all supported configuration parameters.
configuration = astropulse._generated.Configuration(
    host = "https://api.astropulse.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = astropulse._generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with astropulse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astropulse._generated.ClusterAddOnsApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name

    try:
        # List managed add-ons for a cluster
        api_response = api_instance.list_cluster_addons(cluster_name)
        print("The response of ClusterAddOnsApi->list_cluster_addons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterAddOnsApi->list_cluster_addons: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 

### Return type

[**ClusterAddonListResponse**](ClusterAddonListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resync_cluster_addon**
> ClusterAddonResyncResponseEnvelope resync_cluster_addon(cluster_name, addon_type, application_resync_request=application_resync_request)

Resync a managed cluster add-on

Builds the add-on again from its saved configuration at its installed version and deploys it, even when nothing changed. An astro-agent not yet recorded as the cluster's add-on is refused with the reason.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.application_resync_request import ApplicationResyncRequest
from astropulse._generated.models.cluster_addon_resync_response_envelope import ClusterAddonResyncResponseEnvelope
from astropulse._generated.models.cluster_addon_type import ClusterAddonType
from astropulse._generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astropulse.io
# See configuration.py for a list of all supported configuration parameters.
configuration = astropulse._generated.Configuration(
    host = "https://api.astropulse.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = astropulse._generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with astropulse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astropulse._generated.ClusterAddOnsApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    addon_type = astropulse._generated.ClusterAddonType() # ClusterAddonType | Add-on type
    application_resync_request = astropulse._generated.ApplicationResyncRequest() # ApplicationResyncRequest | Resync options (optional)

    try:
        # Resync a managed cluster add-on
        api_response = api_instance.resync_cluster_addon(cluster_name, addon_type, application_resync_request=application_resync_request)
        print("The response of ClusterAddOnsApi->resync_cluster_addon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterAddOnsApi->resync_cluster_addon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **addon_type** | [**ClusterAddonType**](.md)| Add-on type | 
 **application_resync_request** | [**ApplicationResyncRequest**](ApplicationResyncRequest.md)| Resync options | [optional] 

### Return type

[**ClusterAddonResyncResponseEnvelope**](ClusterAddonResyncResponseEnvelope.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rollback_cluster_addon**
> ClusterAddonOperationResponse rollback_cluster_addon(cluster_name, addon_type, rollback_cluster_addon_request)

Roll back a managed cluster add-on

Rolls an add-on back to a prior successful version. Manual-only add-ons require explicit approval. Set dryRun to check the rollback without running it.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_addon_operation_response import ClusterAddonOperationResponse
from astropulse._generated.models.cluster_addon_type import ClusterAddonType
from astropulse._generated.models.rollback_cluster_addon_request import RollbackClusterAddonRequest
from astropulse._generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astropulse.io
# See configuration.py for a list of all supported configuration parameters.
configuration = astropulse._generated.Configuration(
    host = "https://api.astropulse.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = astropulse._generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with astropulse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astropulse._generated.ClusterAddOnsApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    addon_type = astropulse._generated.ClusterAddonType() # ClusterAddonType | Add-on type
    rollback_cluster_addon_request = astropulse._generated.RollbackClusterAddonRequest() # RollbackClusterAddonRequest | Rollback request

    try:
        # Roll back a managed cluster add-on
        api_response = api_instance.rollback_cluster_addon(cluster_name, addon_type, rollback_cluster_addon_request)
        print("The response of ClusterAddOnsApi->rollback_cluster_addon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterAddOnsApi->rollback_cluster_addon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **addon_type** | [**ClusterAddonType**](.md)| Add-on type | 
 **rollback_cluster_addon_request** | [**RollbackClusterAddonRequest**](RollbackClusterAddonRequest.md)| Rollback request | 

### Return type

[**ClusterAddonOperationResponse**](ClusterAddonOperationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_addon**
> ClusterAddonOperationResponse update_cluster_addon(cluster_name, addon_type, update_cluster_addon_request)

Update a managed cluster add-on

Updates the managed add-on's version or configuration. Applying the configuration the add-on already runs changes nothing. A configuration whose last deployment failed is refused with 409; fix the cause, then resync the add-on to retry it.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_addon_operation_response import ClusterAddonOperationResponse
from astropulse._generated.models.cluster_addon_type import ClusterAddonType
from astropulse._generated.models.update_cluster_addon_request import UpdateClusterAddonRequest
from astropulse._generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astropulse.io
# See configuration.py for a list of all supported configuration parameters.
configuration = astropulse._generated.Configuration(
    host = "https://api.astropulse.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = astropulse._generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with astropulse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astropulse._generated.ClusterAddOnsApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    addon_type = astropulse._generated.ClusterAddonType() # ClusterAddonType | Add-on type
    update_cluster_addon_request = astropulse._generated.UpdateClusterAddonRequest() # UpdateClusterAddonRequest | Update request

    try:
        # Update a managed cluster add-on
        api_response = api_instance.update_cluster_addon(cluster_name, addon_type, update_cluster_addon_request)
        print("The response of ClusterAddOnsApi->update_cluster_addon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterAddOnsApi->update_cluster_addon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **addon_type** | [**ClusterAddonType**](.md)| Add-on type | 
 **update_cluster_addon_request** | [**UpdateClusterAddonRequest**](UpdateClusterAddonRequest.md)| Update request | 

### Return type

[**ClusterAddonOperationResponse**](ClusterAddonOperationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dry-run validation succeeded, or nothing was started and a notice says why |  -  |
**202** | Update initiated |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_exposure**
> ClusterExposureResponse update_cluster_exposure(cluster_name, cluster_exposure_settings)

Set a cluster's exposure settings

Names the ClusterIssuer exposed applications' certificates come from when cert-manager runs outside AstroPulse. An empty name clears it; the resolved exposure is returned.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_exposure_response import ClusterExposureResponse
from astropulse._generated.models.cluster_exposure_settings import ClusterExposureSettings
from astropulse._generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astropulse.io
# See configuration.py for a list of all supported configuration parameters.
configuration = astropulse._generated.Configuration(
    host = "https://api.astropulse.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = astropulse._generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with astropulse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astropulse._generated.ClusterAddOnsApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    cluster_exposure_settings = astropulse._generated.ClusterExposureSettings() # ClusterExposureSettings | Exposure settings

    try:
        # Set a cluster's exposure settings
        api_response = api_instance.update_cluster_exposure(cluster_name, cluster_exposure_settings)
        print("The response of ClusterAddOnsApi->update_cluster_exposure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterAddOnsApi->update_cluster_exposure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **cluster_exposure_settings** | [**ClusterExposureSettings**](ClusterExposureSettings.md)| Exposure settings | 

### Return type

[**ClusterExposureResponse**](ClusterExposureResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

