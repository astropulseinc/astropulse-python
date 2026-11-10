# astropulse._generated.AuditApi

All URIs are relative to *https://api.astropulse.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_audit_events**](AuditApi.md#export_audit_events) | **GET** /api/v1/audit/events/export | Download audit events as a file
[**get_audit_event**](AuditApi.md#get_audit_event) | **GET** /api/v1/audit/events/{eventId} | Get audit event details
[**get_audit_stats**](AuditApi.md#get_audit_stats) | **GET** /api/v1/audit/stats | Get audit statistics for an organization
[**list_audit_events**](AuditApi.md#list_audit_events) | **GET** /api/v1/audit/events | List audit events for an organization


# **export_audit_events**
> str export_audit_events(format=format, event_type=event_type, action=action, user_id=user_id, resource_id=resource_id, dry_run=dry_run, include_dry_runs=include_dry_runs, include_reads=include_reads, q=q, start_date=start_date, end_date=end_date)

Download audit events as a file

Downloads every matching event as a file, CSV or JSON: the body is the file itself, not the usual envelope. To read them as data, list them instead. Enterprise plan. Organization admins and owners export every event; other members only their own. Each event names the actor who performed it. At most 50000 events are exported; when more match, the newest 50000 are returned and X-Audit-Export-Truncated is true.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.audit_action import AuditAction
from astropulse._generated.models.audit_event_type import AuditEventType
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
    api_instance = astropulse._generated.AuditApi(api_client)
    format = astropulse._generated.AuditExportFormat() # AuditExportFormat | The file format; CSV when omitted (optional)
    event_type = astropulse._generated.AuditEventType() # AuditEventType | Only events of this type (optional)
    action = astropulse._generated.AuditAction() # AuditAction | Only events with this action (optional)
    user_id = 'user_id_example' # str | Filter by user ID (optional)
    resource_id = 'resource_id_example' # str | Only events on this resource ID (exact match) (optional)
    dry_run = True # bool | true lists only dry runs, requests that checked a change and made none (optional)
    include_dry_runs = True # bool | true lists dry runs alongside real changes; without it or dryRun, only real changes are listed (optional)
    include_reads = True # bool | true lists recorded reads of sensitive data, such as of this log; without it, reads are listed only when action is Read (optional)
    q = 'q_example' # str | Case-insensitive text search over action, resource, resource ID, actor name and email, source and IP address (optional)
    start_date = 'start_date_example' # str | Start of the range: an instant (2024-01-15T10:30:00Z) or a date (2024-01-15, from its start, UTC). Alone, the range runs to now. (optional)
    end_date = 'end_date_example' # str | End of the range: an instant (2024-01-16T23:59:59Z) or a date (2024-01-16, through its end, UTC). Alone, the range reaches back 30 days. (optional)

    try:
        # Download audit events as a file
        api_response = api_instance.export_audit_events(format=format, event_type=event_type, action=action, user_id=user_id, resource_id=resource_id, dry_run=dry_run, include_dry_runs=include_dry_runs, include_reads=include_reads, q=q, start_date=start_date, end_date=end_date)
        print("The response of AuditApi->export_audit_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditApi->export_audit_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**AuditExportFormat**](.md)| The file format; CSV when omitted | [optional] 
 **event_type** | [**AuditEventType**](.md)| Only events of this type | [optional] 
 **action** | [**AuditAction**](.md)| Only events with this action | [optional] 
 **user_id** | **str**| Filter by user ID | [optional] 
 **resource_id** | **str**| Only events on this resource ID (exact match) | [optional] 
 **dry_run** | **bool**| true lists only dry runs, requests that checked a change and made none | [optional] 
 **include_dry_runs** | **bool**| true lists dry runs alongside real changes; without it or dryRun, only real changes are listed | [optional] 
 **include_reads** | **bool**| true lists recorded reads of sensitive data, such as of this log; without it, reads are listed only when action is Read | [optional] 
 **q** | **str**| Case-insensitive text search over action, resource, resource ID, actor name and email, source and IP address | [optional] 
 **start_date** | **str**| Start of the range: an instant (2024-01-15T10:30:00Z) or a date (2024-01-15, from its start, UTC). Alone, the range runs to now. | [optional] 
 **end_date** | **str**| End of the range: an instant (2024-01-16T23:59:59Z) or a date (2024-01-16, through its end, UTC). Alone, the range reaches back 30 days. | [optional] 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The export, as a file download |  * X-Audit-Export-Limit - The most events one export returns <br>  * X-Audit-Export-Truncated - true when more events matched than the export limit <br>  |
**400** | Invalid query parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | Not enterprise organization or insufficient permissions |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Audit storage temporarily unavailable; retry after the Retry-After interval |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_event**
> AuditEventResponse get_audit_event(event_id)

Get audit event details

Get one audit event by ID, at any age. Enterprise plan. Below admin, only the caller's own events; anyone else's answers not found.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.audit_event_response import AuditEventResponse
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
    api_instance = astropulse._generated.AuditApi(api_client)
    event_id = 'event_id_example' # str | Event ID

    try:
        # Get audit event details
        api_response = api_instance.get_audit_event(event_id)
        print("The response of AuditApi->get_audit_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditApi->get_audit_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**| Event ID | 

### Return type

[**AuditEventResponse**](AuditEventResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Audit event retrieved successfully |  -  |
**400** | Invalid event ID |  -  |
**401** | Missing or invalid API key |  -  |
**403** | Not enterprise organization or insufficient permissions |  -  |
**404** | Audit event not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Audit storage temporarily unavailable; retry after the Retry-After interval |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_stats**
> AuditStatsResponse get_audit_stats(period=period, include_dry_runs=include_dry_runs, include_reads=include_reads)

Get audit statistics for an organization

Get audit statistics and analytics for an organization. Requires enterprise plan and admin role.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.audit_stats_response import AuditStatsResponse
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
    api_instance = astropulse._generated.AuditApi(api_client)
    period = '30d' # str | The period the statistics cover: 7d, 30d or 90d (optional) (default to '30d')
    include_dry_runs = True # bool | true also counts dry runs; by default only real changes are counted (optional)
    include_reads = True # bool | true also counts recorded reads of sensitive data (optional)

    try:
        # Get audit statistics for an organization
        api_response = api_instance.get_audit_stats(period=period, include_dry_runs=include_dry_runs, include_reads=include_reads)
        print("The response of AuditApi->get_audit_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditApi->get_audit_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period** | **str**| The period the statistics cover: 7d, 30d or 90d | [optional] [default to &#39;30d&#39;]
 **include_dry_runs** | **bool**| true also counts dry runs; by default only real changes are counted | [optional] 
 **include_reads** | **bool**| true also counts recorded reads of sensitive data | [optional] 

### Return type

[**AuditStatsResponse**](AuditStatsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Audit statistics retrieved successfully |  -  |
**400** | Invalid query parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | Not enterprise organization or insufficient permissions |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Audit storage temporarily unavailable; retry after the Retry-After interval |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_audit_events**
> AuditEventListResponse list_audit_events(limit=limit, page_token=page_token, page=page, page_size=page_size, event_type=event_type, action=action, user_id=user_id, resource_id=resource_id, dry_run=dry_run, include_dry_runs=include_dry_runs, include_reads=include_reads, q=q, start_date=start_date, end_date=end_date)

List audit events for an organization

List audit events with filtering and pagination, newest first; dry runs and reads only when asked for. Enterprise plan. Organization admins and owners see every event; other members see only their own. With no dates the last 30 days are listed.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.audit_action import AuditAction
from astropulse._generated.models.audit_event_list_response import AuditEventListResponse
from astropulse._generated.models.audit_event_type import AuditEventType
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
    api_instance = astropulse._generated.AuditApi(api_client)
    limit = 50 # int | Page size from 1 through 100; overrides pageSize (optional) (default to 50)
    page_token = 'page_token_example' # str | Opaque continuation token from nextPageToken; it pins the original filters, so filter parameters sent with it are ignored (optional)
    page = 56 # int | Page number (default: 1). Prefer pageToken. (optional)
    page_size = 56 # int | Items per page (default: 50, max: 100). Prefer limit. (optional)
    event_type = astropulse._generated.AuditEventType() # AuditEventType | Only events of this type (optional)
    action = astropulse._generated.AuditAction() # AuditAction | Only events with this action (optional)
    user_id = 'user_id_example' # str | Filter by user ID (optional)
    resource_id = 'resource_id_example' # str | Only events on this resource ID (exact match) (optional)
    dry_run = True # bool | true lists only dry runs, requests that checked a change and made none (optional)
    include_dry_runs = True # bool | true lists dry runs alongside real changes; without it or dryRun, only real changes are listed (optional)
    include_reads = True # bool | true lists recorded reads of sensitive data, such as of this log; without it, reads are listed only when action is Read (optional)
    q = 'q_example' # str | Case-insensitive text search over action, resource, resource ID, actor name and email, source and IP address (optional)
    start_date = 'start_date_example' # str | Start of the range: an instant (2024-01-15T10:30:00Z) or a date (2024-01-15, from its start, UTC). Alone, the range runs to now. (optional)
    end_date = 'end_date_example' # str | End of the range: an instant (2024-01-16T23:59:59Z) or a date (2024-01-16, through its end, UTC). Alone, the range reaches back 30 days. (optional)

    try:
        # List audit events for an organization
        api_response = api_instance.list_audit_events(limit=limit, page_token=page_token, page=page, page_size=page_size, event_type=event_type, action=action, user_id=user_id, resource_id=resource_id, dry_run=dry_run, include_dry_runs=include_dry_runs, include_reads=include_reads, q=q, start_date=start_date, end_date=end_date)
        print("The response of AuditApi->list_audit_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditApi->list_audit_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Page size from 1 through 100; overrides pageSize | [optional] [default to 50]
 **page_token** | **str**| Opaque continuation token from nextPageToken; it pins the original filters, so filter parameters sent with it are ignored | [optional] 
 **page** | **int**| Page number (default: 1). Prefer pageToken. | [optional] 
 **page_size** | **int**| Items per page (default: 50, max: 100). Prefer limit. | [optional] 
 **event_type** | [**AuditEventType**](.md)| Only events of this type | [optional] 
 **action** | [**AuditAction**](.md)| Only events with this action | [optional] 
 **user_id** | **str**| Filter by user ID | [optional] 
 **resource_id** | **str**| Only events on this resource ID (exact match) | [optional] 
 **dry_run** | **bool**| true lists only dry runs, requests that checked a change and made none | [optional] 
 **include_dry_runs** | **bool**| true lists dry runs alongside real changes; without it or dryRun, only real changes are listed | [optional] 
 **include_reads** | **bool**| true lists recorded reads of sensitive data, such as of this log; without it, reads are listed only when action is Read | [optional] 
 **q** | **str**| Case-insensitive text search over action, resource, resource ID, actor name and email, source and IP address | [optional] 
 **start_date** | **str**| Start of the range: an instant (2024-01-15T10:30:00Z) or a date (2024-01-15, from its start, UTC). Alone, the range runs to now. | [optional] 
 **end_date** | **str**| End of the range: an instant (2024-01-16T23:59:59Z) or a date (2024-01-16, through its end, UTC). Alone, the range reaches back 30 days. | [optional] 

### Return type

[**AuditEventListResponse**](AuditEventListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Audit events retrieved successfully |  -  |
**400** | Invalid query parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | Not enterprise organization or insufficient permissions |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Audit storage temporarily unavailable; retry after the Retry-After interval |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

