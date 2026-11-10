# astropulse._generated.ApplicationsApi

All URIs are relative to *https://api.astropulse.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close_application_endpoint**](ApplicationsApi.md#close_application_endpoint) | **POST** /api/v1/applications/{appName}/endpoint/close | Close an application&#39;s managed endpoint
[**delete_application**](ApplicationsApi.md#delete_application) | **DELETE** /api/v1/applications/{appName} | Delete an application
[**deploy_application**](ApplicationsApi.md#deploy_application) | **POST** /api/v1/applications/deploy | Deploy an application
[**get_application**](ApplicationsApi.md#get_application) | **GET** /api/v1/applications/{appName} | Get an application
[**get_application_cost_series**](ApplicationsApi.md#get_application_cost_series) | **GET** /api/v1/applications/{appName}/cost/series | Get one application&#39;s cost time series
[**get_application_cost_summary**](ApplicationsApi.md#get_application_cost_summary) | **GET** /api/v1/applications/{appName}/cost/summary | Get one application&#39;s cost summary
[**get_application_endpoint**](ApplicationsApi.md#get_application_endpoint) | **GET** /api/v1/applications/{appName}/endpoint | Get an application&#39;s managed endpoint
[**get_application_metrics_series**](ApplicationsApi.md#get_application_metrics_series) | **GET** /api/v1/applications/{appName}/metrics/series | Get one application&#39;s live resource-usage series
[**get_application_spec**](ApplicationsApi.md#get_application_spec) | **GET** /api/v1/applications/{appName}/spec | Get application request specification
[**list_application_history**](ApplicationsApi.md#list_application_history) | **GET** /api/v1/applications/{appName}/history | Get application deploy history
[**list_applications**](ApplicationsApi.md#list_applications) | **GET** /api/v1/applications | List all applications
[**reopen_application_endpoint**](ApplicationsApi.md#reopen_application_endpoint) | **POST** /api/v1/applications/{appName}/endpoint/reopen | Reopen an application&#39;s managed endpoint
[**resume_application**](ApplicationsApi.md#resume_application) | **POST** /api/v1/applications/{appName}/resume | Resume a git-pinned application
[**resync_application**](ApplicationsApi.md#resync_application) | **POST** /api/v1/applications/{appName}/resync | Resync an application
[**rollback_application**](ApplicationsApi.md#rollback_application) | **POST** /api/v1/applications/{appName}/rollback | Roll an application back to a previous version
[**stream_application_events**](ApplicationsApi.md#stream_application_events) | **GET** /api/v1/applications/{appName}/events/ws | Stream application events via WebSocket
[**stream_application_logs**](ApplicationsApi.md#stream_application_logs) | **GET** /api/v1/applications/{appName}/logs/ws | Stream application logs via WebSocket
[**stream_application_status**](ApplicationsApi.md#stream_application_status) | **GET** /api/v1/applications/{appName}/status/ws | Stream application status


# **close_application_endpoint**
> EndpointStatusResponse close_application_endpoint(app_name, endpoint_change_request, x_astro_organization_id=x_astro_organization_id)

Close an application's managed endpoint

Withdraws the public route; the application keeps running on its internal address. Durable across redeploys, and asynchronous. Send the current generation.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.endpoint_change_request import EndpointChangeRequest
from astropulse._generated.models.endpoint_status_response import EndpointStatusResponse
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
    api_instance = astropulse._generated.ApplicationsApi(api_client)
    app_name = 'app_name_example' # str | Application name
    endpoint_change_request = astropulse._generated.EndpointChangeRequest() # EndpointChangeRequest | Current endpoint generation
    x_astro_organization_id = 'x_astro_organization_id_example' # str | Organization to act in with a bearer token; defaults to the user's current organization. Ignored with an API key, which carries its own. (optional)

    try:
        # Close an application's managed endpoint
        api_response = api_instance.close_application_endpoint(app_name, endpoint_change_request, x_astro_organization_id=x_astro_organization_id)
        print("The response of ApplicationsApi->close_application_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->close_application_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| Application name | 
 **endpoint_change_request** | [**EndpointChangeRequest**](EndpointChangeRequest.md)| Current endpoint generation | 
 **x_astro_organization_id** | **str**| Organization to act in with a bearer token; defaults to the user&#39;s current organization. Ignored with an API key, which carries its own. | [optional] 

### Return type

[**EndpointStatusResponse**](EndpointStatusResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | The endpoint changed while this request was in flight: reason EndpointChanged; run the request again |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application**
> delete_application(app_name)

Delete an application

Permanently removes the application and its associated resources. Organization admins and owners can delete applications.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
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
    api_instance = astropulse._generated.ApplicationsApi(api_client)
    app_name = 'app_name_example' # str | Application name

    try:
        # Delete an application
        api_instance.delete_application(app_name)
    except Exception as e:
        print("Exception when calling ApplicationsApi->delete_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| Application name | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Application successfully deleted |  -  |
**403** | forbidden to delete application. Only the owner of the organization can delete the application |  -  |
**404** | application not found |  -  |
**500** | unable to delete application |  -  |
**503** | Service temporarily unavailable; retry after the Retry-After interval |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy_application**
> DeployValidationResultResponse deploy_application(application_manifest, dry_run=dry_run)

Deploy an application

Deploy an application from an Application specification. Use ?dryRun=true to validate without deploying. A Helm or repository source's values.type is optional; it is inferred from whether object or files is set.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.application_manifest import ApplicationManifest
from astropulse._generated.models.deploy_validation_result_response import DeployValidationResultResponse
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
    api_instance = astropulse._generated.ApplicationsApi(api_client)
    application_manifest = astropulse._generated.ApplicationManifest() # ApplicationManifest | Application deployment data
    dry_run = True # bool | When true, validates the configuration without deploying (optional)

    try:
        # Deploy an application
        api_response = api_instance.deploy_application(application_manifest, dry_run=dry_run)
        print("The response of ApplicationsApi->deploy_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->deploy_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_manifest** | [**ApplicationManifest**](ApplicationManifest.md)| Application deployment data | 
 **dry_run** | **bool**| When true, validates the configuration without deploying | [optional] 

### Return type

[**DeployValidationResultResponse**](DeployValidationResultResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dry run: the application would deploy as submitted |  -  |
**201** | Application deployed successfully |  -  |
**400** | Validation error in request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**402** | Feature not available in current plan or application limit reached |  -  |
**403** | Not authorized to deploy applications or insufficient permissions |  -  |
**404** | Application profile not found or organization not found |  -  |
**409** | Resource already exists |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application**
> ApplicationResponse get_application(app_name)

Get an application

Retrieve details of a specific application within an organization

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.application_response import ApplicationResponse
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
    api_instance = astropulse._generated.ApplicationsApi(api_client)
    app_name = 'app_name_example' # str | Application name

    try:
        # Get an application
        api_response = api_instance.get_application(app_name)
        print("The response of ApplicationsApi->get_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| Application name | 

### Return type

[**ApplicationResponse**](ApplicationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Detailed information about the application |  -  |
**404** | application not found |  -  |
**500** | Unable to fetch application |  -  |
**503** | Service temporarily unavailable; retry after the Retry-After interval |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_cost_series**
> ClusterCostSeriesResponse get_application_cost_series(app_name, window=window, interval=interval)

Get one application's cost time series

Returns closed-hour cost and usage buckets for one application; its cluster is resolved from the application record. Missing and gap buckets stay explicit and are never reported as zero spend.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_cost_series_response import ClusterCostSeriesResponse
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
    api_instance = astropulse._generated.ApplicationsApi(api_client)
    app_name = 'app_name_example' # str | Application name
    window = '24h' # str | Window duration (for example 24h, 7d, 30d) (optional) (default to '24h')
    interval = 'auto' # str | Bucket interval (auto, 1h, 6h, 12h, 1d) (optional) (default to 'auto')

    try:
        # Get one application's cost time series
        api_response = api_instance.get_application_cost_series(app_name, window=window, interval=interval)
        print("The response of ApplicationsApi->get_application_cost_series:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get_application_cost_series: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| Application name | 
 **window** | **str**| Window duration (for example 24h, 7d, 30d) | [optional] [default to &#39;24h&#39;]
 **interval** | **str**| Bucket interval (auto, 1h, 6h, 12h, 1d) | [optional] [default to &#39;auto&#39;]

### Return type

[**ClusterCostSeriesResponse**](ClusterCostSeriesResponse.md)

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

# **get_application_cost_summary**
> ApplicationCostSummaryResponse get_application_cost_summary(app_name, window=window)

Get one application's cost summary

Aggregates closed hourly cost rollups for one application over the window. Coverage says how completely the cluster reported; an application that contributed nothing reports reporting=false, not zero spend.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.application_cost_summary_response import ApplicationCostSummaryResponse
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
    api_instance = astropulse._generated.ApplicationsApi(api_client)
    app_name = 'app_name_example' # str | Application name
    window = '24h' # str | Window duration (for example 24h, 7d, 30d) (optional) (default to '24h')

    try:
        # Get one application's cost summary
        api_response = api_instance.get_application_cost_summary(app_name, window=window)
        print("The response of ApplicationsApi->get_application_cost_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get_application_cost_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| Application name | 
 **window** | **str**| Window duration (for example 24h, 7d, 30d) | [optional] [default to &#39;24h&#39;]

### Return type

[**ApplicationCostSummaryResponse**](ApplicationCostSummaryResponse.md)

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

# **get_application_endpoint**
> EndpointStatusResponse get_application_endpoint(app_name, x_astro_organization_id=x_astro_organization_id)

Get an application's managed endpoint

Where the application is served, and whether it is open. A model's URL lives here; an endpoint still settling reports Pending with no URL, and its message says what it waits for.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.endpoint_status_response import EndpointStatusResponse
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
    api_instance = astropulse._generated.ApplicationsApi(api_client)
    app_name = 'app_name_example' # str | Application name
    x_astro_organization_id = 'x_astro_organization_id_example' # str | Organization to act in with a bearer token; defaults to the user's current organization. Ignored with an API key, which carries its own. (optional)

    try:
        # Get an application's managed endpoint
        api_response = api_instance.get_application_endpoint(app_name, x_astro_organization_id=x_astro_organization_id)
        print("The response of ApplicationsApi->get_application_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get_application_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| Application name | 
 **x_astro_organization_id** | **str**| Organization to act in with a bearer token; defaults to the user&#39;s current organization. Ignored with an API key, which carries its own. | [optional] 

### Return type

[**EndpointStatusResponse**](EndpointStatusResponse.md)

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
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_metrics_series**
> ApplicationMetricsSeriesResponse get_application_metrics_series(app_name, window=window)

Get one application's live resource-usage series

Returns stored resource-usage samples for one application at the resolution the agent recorded them. A window with no sample is absent from points rather than a zero, and each point carries its own coverage.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.application_metrics_series_response import ApplicationMetricsSeriesResponse
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
    api_instance = astropulse._generated.ApplicationsApi(api_client)
    app_name = 'app_name_example' # str | Application name
    window = '1h' # str | Window duration (for example 15m, 1h, 24h); minutes-scale, not truncated to whole hours (optional) (default to '1h')

    try:
        # Get one application's live resource-usage series
        api_response = api_instance.get_application_metrics_series(app_name, window=window)
        print("The response of ApplicationsApi->get_application_metrics_series:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get_application_metrics_series: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| Application name | 
 **window** | **str**| Window duration (for example 15m, 1h, 24h); minutes-scale, not truncated to whole hours | [optional] [default to &#39;1h&#39;]

### Return type

[**ApplicationMetricsSeriesResponse**](ApplicationMetricsSeriesResponse.md)

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

# **get_application_spec**
> ApplicationRequestResponse get_application_spec(app_name)

Get application request specification

Returns the original deployment specification for the application, useful for auditing or re-deploying with modified parameters.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.application_request_response import ApplicationRequestResponse
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
    api_instance = astropulse._generated.ApplicationsApi(api_client)
    app_name = 'app_name_example' # str | Application name

    try:
        # Get application request specification
        api_response = api_instance.get_application_spec(app_name)
        print("The response of ApplicationsApi->get_application_spec:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get_application_spec: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| Application name | 

### Return type

[**ApplicationRequestResponse**](ApplicationRequestResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Application request specification retrieved successfully |  -  |
**400** | Invalid application ID |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to view this application |  -  |
**404** | Application not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_application_history**
> ApplicationHistoryResponse list_application_history(app_name)

Get application deploy history

Returns the version history (deploys/rollbacks) for an application with rollback eligibility.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.application_history_response import ApplicationHistoryResponse
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
    api_instance = astropulse._generated.ApplicationsApi(api_client)
    app_name = 'app_name_example' # str | Application name

    try:
        # Get application deploy history
        api_response = api_instance.list_application_history(app_name)
        print("The response of ApplicationsApi->list_application_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->list_application_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| Application name | 

### Return type

[**ApplicationHistoryResponse**](ApplicationHistoryResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deploy history |  -  |
**401** | Missing or invalid API key |  -  |
**403** | Not authorized to read this application |  -  |
**404** | Application or organization not found |  -  |
**500** | Internal server error |  -  |
**503** | Version history temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_applications**
> ApplicationListResponse list_applications(cluster=cluster)

List all applications

Returns all applications deployed within the authenticated user's organization.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.application_list_response import ApplicationListResponse
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
    api_instance = astropulse._generated.ApplicationsApi(api_client)
    cluster = 'cluster_example' # str | Return only the applications recorded on this cluster (optional)

    try:
        # List all applications
        api_response = api_instance.list_applications(cluster=cluster)
        print("The response of ApplicationsApi->list_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->list_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| Return only the applications recorded on this cluster | [optional] 

### Return type

[**ApplicationListResponse**](ApplicationListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of applications |  -  |
**401** | Missing or invalid authorization token |  -  |
**403** | Insufficient permissions |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable; retry after the Retry-After interval |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reopen_application_endpoint**
> EndpointStatusResponse reopen_application_endpoint(app_name, endpoint_change_request, x_astro_organization_id=x_astro_organization_id)

Reopen an application's managed endpoint

Publishes a closed endpoint again, once the cluster re-checks its policy and certificate. A deleted application's endpoint cannot be reopened. Send the current generation.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.endpoint_change_request import EndpointChangeRequest
from astropulse._generated.models.endpoint_status_response import EndpointStatusResponse
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
    api_instance = astropulse._generated.ApplicationsApi(api_client)
    app_name = 'app_name_example' # str | Application name
    endpoint_change_request = astropulse._generated.EndpointChangeRequest() # EndpointChangeRequest | Current endpoint generation
    x_astro_organization_id = 'x_astro_organization_id_example' # str | Organization to act in with a bearer token; defaults to the user's current organization. Ignored with an API key, which carries its own. (optional)

    try:
        # Reopen an application's managed endpoint
        api_response = api_instance.reopen_application_endpoint(app_name, endpoint_change_request, x_astro_organization_id=x_astro_organization_id)
        print("The response of ApplicationsApi->reopen_application_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->reopen_application_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| Application name | 
 **endpoint_change_request** | [**EndpointChangeRequest**](EndpointChangeRequest.md)| Current endpoint generation | 
 **x_astro_organization_id** | **str**| Organization to act in with a bearer token; defaults to the user&#39;s current organization. Ignored with an API key, which carries its own. | [optional] 

### Return type

[**EndpointStatusResponse**](EndpointStatusResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | The endpoint changed while this request was in flight: reason EndpointChanged; run the request again |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_application**
> ApplicationResumePlanResponse resume_application(app_name, dry_run=dry_run)

Resume a git-pinned application

Clears a rollback's pin so the configured branch deploys again. dryRun=true returns the plan and changes nothing.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.application_resume_plan_response import ApplicationResumePlanResponse
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
    api_instance = astropulse._generated.ApplicationsApi(api_client)
    app_name = 'app_name_example' # str | Application name
    dry_run = True # bool | Return the resume plan without applying (optional)

    try:
        # Resume a git-pinned application
        api_response = api_instance.resume_application(app_name, dry_run=dry_run)
        print("The response of ApplicationsApi->resume_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->resume_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| Application name | 
 **dry_run** | **bool**| Return the resume plan without applying | [optional] 

### Return type

[**ApplicationResumePlanResponse**](ApplicationResumePlanResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resume plan (dry-run) |  -  |
**202** | Resume started |  -  |
**401** | Missing or invalid API key |  -  |
**402** | Feature not available in current plan |  -  |
**403** | Not authorized to resume this application |  -  |
**404** | Application or organization not found |  -  |
**409** | Application is not pinned by rollback, or an operation is in progress |  -  |
**500** | Internal server error |  -  |
**503** | Version store temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resync_application**
> ApplicationResyncResponse resync_application(app_name, application_resync_request=application_resync_request)

Resync an application

Triggers an immediate GitOps resync for the application, reconciling the deployed state with the desired configuration in the repository.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.application_resync_request import ApplicationResyncRequest
from astropulse._generated.models.application_resync_response import ApplicationResyncResponse
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
    api_instance = astropulse._generated.ApplicationsApi(api_client)
    app_name = 'app_name_example' # str | Application name
    application_resync_request = astropulse._generated.ApplicationResyncRequest() # ApplicationResyncRequest | Resync options (optional)

    try:
        # Resync an application
        api_response = api_instance.resync_application(app_name, application_resync_request=application_resync_request)
        print("The response of ApplicationsApi->resync_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->resync_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| Application name | 
 **application_resync_request** | [**ApplicationResyncRequest**](ApplicationResyncRequest.md)| Resync options | [optional] 

### Return type

[**ApplicationResyncResponse**](ApplicationResyncResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Application resync initiated successfully |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | Not authorized to resync applications |  -  |
**404** | Application not found |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable; retry after the Retry-After interval |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rollback_application**
> ApplicationRollbackPlanResponse rollback_application(app_name, dry_run=dry_run, application_rollback_request=application_rollback_request)

Roll an application back to a previous version

Redeploys an earlier version and pins it there; a git source stops following its branch until resumed. dryRun=true returns the plan and changes nothing.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.application_rollback_plan_response import ApplicationRollbackPlanResponse
from astropulse._generated.models.application_rollback_request import ApplicationRollbackRequest
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
    api_instance = astropulse._generated.ApplicationsApi(api_client)
    app_name = 'app_name_example' # str | Application name
    dry_run = True # bool | Return the rollback plan without applying (optional)
    application_rollback_request = astropulse._generated.ApplicationRollbackRequest() # ApplicationRollbackRequest | Rollback options (optional)

    try:
        # Roll an application back to a previous version
        api_response = api_instance.rollback_application(app_name, dry_run=dry_run, application_rollback_request=application_rollback_request)
        print("The response of ApplicationsApi->rollback_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->rollback_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| Application name | 
 **dry_run** | **bool**| Return the rollback plan without applying | [optional] 
 **application_rollback_request** | [**ApplicationRollbackRequest**](ApplicationRollbackRequest.md)| Rollback options | [optional] 

### Return type

[**ApplicationRollbackPlanResponse**](ApplicationRollbackPlanResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rollback plan (dry-run or ineligible) |  -  |
**202** | Rollback started |  -  |
**400** | No rollback target, or the spec contains a value that may be a secret |  -  |
**401** | Missing or invalid API key |  -  |
**402** | Feature not available in current plan |  -  |
**403** | Not authorized to roll back this application |  -  |
**404** | Application or organization not found |  -  |
**409** | Operation in progress, application pinned, or target can no longer be rolled back to |  -  |
**500** | Internal server error |  -  |
**503** | Deployment engine temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_application_events**
> StreamTicket stream_application_events(app_name, k8s=k8s, watch=watch, accept=accept, x_astro_stream_origin=x_astro_stream_origin)

Stream application events via WebSocket

Establishes a WebSocket connection for real-time application event streaming. Upgrades HTTP to WebSocket and streams Pulse (CD) service and optionally Kubernetes events.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.stream_ticket import StreamTicket
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
    api_instance = astropulse._generated.ApplicationsApi(api_client)
    app_name = 'app_name_example' # str | Application name
    k8s = False # bool | Include Kubernetes events in addition to application events (optional) (default to False)
    watch = True # bool | Keep sending new events as they happen; false sends only the events that exist now (optional) (default to True)
    accept = 'accept_example' # str | Send application/vnd.astropulse.stream-ticket+json with a bearer token to get a single-use ticket for this stream instead of opening it (optional)
    x_astro_stream_origin = 'x_astro_stream_origin_example' # str | With a ticket request: the browser origin the stream will be opened from (optional)

    try:
        # Stream application events via WebSocket
        api_response = api_instance.stream_application_events(app_name, k8s=k8s, watch=watch, accept=accept, x_astro_stream_origin=x_astro_stream_origin)
        print("The response of ApplicationsApi->stream_application_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->stream_application_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| Application name | 
 **k8s** | **bool**| Include Kubernetes events in addition to application events | [optional] [default to False]
 **watch** | **bool**| Keep sending new events as they happen; false sends only the events that exist now | [optional] [default to True]
 **accept** | **str**| Send application/vnd.astropulse.stream-ticket+json with a bearer token to get a single-use ticket for this stream instead of opening it | [optional] 
 **x_astro_stream_origin** | **str**| With a ticket request: the browser origin the stream will be opened from | [optional] 

### Return type

[**StreamTicket**](StreamTicket.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**101** | Switching Protocols - WebSocket connection established |  -  |
**200** | Ticket request: a single-use ticket for this stream, valid for at most 30 seconds |  -  |
**400** | Invalid application ID, query parameters, or WebSocket upgrade failed |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to stream application events |  -  |
**404** | Application not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Streams cannot be opened from the console right now; try again |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_application_logs**
> StreamTicket stream_application_logs(app_name, follow=follow, tail=tail, previous=previous, pod=pod, container=container, since=since, since_time=since_time, level=level, context=context, include_previous=include_previous, accept=accept, x_astro_stream_origin=x_astro_stream_origin)

Stream application logs via WebSocket

Establishes a WebSocket connection for real-time application log streaming. Upgrades HTTP to WebSocket and streams logs with optional pod and container targeting.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.log_level import LogLevel
from astropulse._generated.models.stream_ticket import StreamTicket
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
    api_instance = astropulse._generated.ApplicationsApi(api_client)
    app_name = 'app_name_example' # str | Application name
    follow = True # bool | Follow logs in real-time (optional) (default to True)
    tail = 56 # int | Number of lines to show from the end of the logs (optional)
    previous = True # bool | Show previous logs from terminated containers (optional)
    pod = 'pod_example' # str | Specific pod name to get logs from (optional)
    container = 'container_example' # str | Specific container name within the pod (optional)
    since = 'since_example' # str | Read lines newer than this duration, e.g. 30m or 2h (a bounded read) (optional)
    since_time = 'since_time_example' # str | Read lines from this RFC 3339 time on; exclusive with since (a bounded read) (optional)
    level = astropulse._generated.LogLevel() # LogLevel | Keep lines at this severity and above, with context, and end with a log_summary message (optional)
    context = 2 # int | Lines kept around each matching line when level is set (0-20) (optional) (default to 2)
    include_previous = True # bool | When the container has restarted, read the crashed previous container first, then the current one (optional)
    accept = 'accept_example' # str | Send application/vnd.astropulse.stream-ticket+json with a bearer token to get a single-use ticket for this stream instead of opening it (optional)
    x_astro_stream_origin = 'x_astro_stream_origin_example' # str | With a ticket request: the browser origin the stream will be opened from (optional)

    try:
        # Stream application logs via WebSocket
        api_response = api_instance.stream_application_logs(app_name, follow=follow, tail=tail, previous=previous, pod=pod, container=container, since=since, since_time=since_time, level=level, context=context, include_previous=include_previous, accept=accept, x_astro_stream_origin=x_astro_stream_origin)
        print("The response of ApplicationsApi->stream_application_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->stream_application_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| Application name | 
 **follow** | **bool**| Follow logs in real-time | [optional] [default to True]
 **tail** | **int**| Number of lines to show from the end of the logs | [optional] 
 **previous** | **bool**| Show previous logs from terminated containers | [optional] 
 **pod** | **str**| Specific pod name to get logs from | [optional] 
 **container** | **str**| Specific container name within the pod | [optional] 
 **since** | **str**| Read lines newer than this duration, e.g. 30m or 2h (a bounded read) | [optional] 
 **since_time** | **str**| Read lines from this RFC 3339 time on; exclusive with since (a bounded read) | [optional] 
 **level** | [**LogLevel**](.md)| Keep lines at this severity and above, with context, and end with a log_summary message | [optional] 
 **context** | **int**| Lines kept around each matching line when level is set (0-20) | [optional] [default to 2]
 **include_previous** | **bool**| When the container has restarted, read the crashed previous container first, then the current one | [optional] 
 **accept** | **str**| Send application/vnd.astropulse.stream-ticket+json with a bearer token to get a single-use ticket for this stream instead of opening it | [optional] 
 **x_astro_stream_origin** | **str**| With a ticket request: the browser origin the stream will be opened from | [optional] 

### Return type

[**StreamTicket**](StreamTicket.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**101** | Switching Protocols - WebSocket connection established |  -  |
**200** | Ticket request: a single-use ticket for this stream, valid for at most 30 seconds |  -  |
**400** | Invalid application ID, query parameters, or WebSocket upgrade failed |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to stream application logs |  -  |
**404** | Application not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Streams cannot be opened from the console right now; try again |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_application_status**
> StreamTicket stream_application_status(app_name, accept=accept, x_astro_stream_origin=x_astro_stream_origin)

Stream application status

Opens a WebSocket connection that streams real-time status events for the specified application, including deployment progress, health conditions, and deploy service sync state.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.stream_ticket import StreamTicket
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
    api_instance = astropulse._generated.ApplicationsApi(api_client)
    app_name = 'app_name_example' # str | Application name
    accept = 'accept_example' # str | Send application/vnd.astropulse.stream-ticket+json with a bearer token to get a single-use ticket for this stream instead of opening it (optional)
    x_astro_stream_origin = 'x_astro_stream_origin_example' # str | With a ticket request: the browser origin the stream will be opened from (optional)

    try:
        # Stream application status
        api_response = api_instance.stream_application_status(app_name, accept=accept, x_astro_stream_origin=x_astro_stream_origin)
        print("The response of ApplicationsApi->stream_application_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->stream_application_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| Application name | 
 **accept** | **str**| Send application/vnd.astropulse.stream-ticket+json with a bearer token to get a single-use ticket for this stream instead of opening it | [optional] 
 **x_astro_stream_origin** | **str**| With a ticket request: the browser origin the stream will be opened from | [optional] 

### Return type

[**StreamTicket**](StreamTicket.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**101** | Switching protocols — WebSocket connection established |  -  |
**200** | Ticket request: a single-use ticket for this stream, valid for at most 30 seconds |  -  |
**401** | Missing or invalid authorization token |  -  |
**403** | The caller may not open this stream, or the browser origin is not allowed |  -  |
**404** | Application not found |  -  |
**429** | Too many streams are open, or rate limit exceeded |  -  |
**503** | Streams cannot be opened from the console right now; try again |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

