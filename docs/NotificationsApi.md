# astropulse._generated.NotificationsApi

All URIs are relative to *https://api.astropulse.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_notification_integration**](NotificationsApi.md#delete_notification_integration) | **DELETE** /api/v1/notifications/integrations/{channel} | Delete notification integration
[**delete_notification_subscription**](NotificationsApi.md#delete_notification_subscription) | **DELETE** /api/v1/notifications/subscriptions/{topic} | Delete notification subscription
[**get_notification_integration**](NotificationsApi.md#get_notification_integration) | **GET** /api/v1/notifications/integrations/{channel} | Get specific notification integration
[**get_notification_subscription**](NotificationsApi.md#get_notification_subscription) | **GET** /api/v1/notifications/subscriptions/{topic} | Get specific notification subscription
[**list_notification_channel_availability**](NotificationsApi.md#list_notification_channel_availability) | **GET** /api/v1/notifications/channels/availability | Get which notification channels this organization&#39;s plan includes
[**list_notification_channels**](NotificationsApi.md#list_notification_channels) | **GET** /api/v1/notifications/channels | Get available channels
[**list_notification_integrations**](NotificationsApi.md#list_notification_integrations) | **GET** /api/v1/notifications/integrations | List notification integrations
[**list_notification_subscriptions**](NotificationsApi.md#list_notification_subscriptions) | **GET** /api/v1/notifications/subscriptions | List notification subscriptions
[**list_notification_topics**](NotificationsApi.md#list_notification_topics) | **GET** /api/v1/notifications/topics | Get available notification topics
[**test_notification_integration**](NotificationsApi.md#test_notification_integration) | **POST** /api/v1/notifications/integrations/{channel}/test | Send a test notification
[**unsubscribe_notifications**](NotificationsApi.md#unsubscribe_notifications) | **POST** /api/v1/notifications/unsubscribe | Unsubscribe from notifications
[**upsert_notification_integration**](NotificationsApi.md#upsert_notification_integration) | **POST** /api/v1/notifications/integrations | Configure notification integration
[**upsert_notification_subscription**](NotificationsApi.md#upsert_notification_subscription) | **POST** /api/v1/notifications/subscriptions | Create or update notification subscription


# **delete_notification_integration**
> BooleanResponse delete_notification_integration(channel, x_astro_organization_id=x_astro_organization_id)

Delete notification integration

Removes the notification delivery integration for the specified channel. Existing subscriptions using this channel will no longer deliver notifications.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.boolean_response import BooleanResponse
from astropulse._generated.models.notification_channel_type import NotificationChannelType
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
    api_instance = astropulse._generated.NotificationsApi(api_client)
    channel = astropulse._generated.NotificationChannelType() # NotificationChannelType | The delivery channel
    x_astro_organization_id = 'x_astro_organization_id_example' # str | Organization to act in with a bearer token; defaults to the user's current organization. Ignored with an API key, which carries its own. (optional)

    try:
        # Delete notification integration
        api_response = api_instance.delete_notification_integration(channel, x_astro_organization_id=x_astro_organization_id)
        print("The response of NotificationsApi->delete_notification_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->delete_notification_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel** | [**NotificationChannelType**](.md)| The delivery channel | 
 **x_astro_organization_id** | **str**| Organization to act in with a bearer token; defaults to the user&#39;s current organization. Ignored with an API key, which carries its own. | [optional] 

### Return type

[**BooleanResponse**](BooleanResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Integration deleted successfully |  -  |
**400** | Invalid parameters |  -  |
**401** | Missing or invalid authentication |  -  |
**403** | User does not have permission to configure notifications |  -  |
**404** | Integration not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification_subscription**
> BooleanResponse delete_notification_subscription(topic, x_astro_organization_id=x_astro_organization_id)

Delete notification subscription

Removes the notification subscription for the given topic. The organization will no longer receive alerts for this event type.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.boolean_response import BooleanResponse
from astropulse._generated.models.notification_topic import NotificationTopic
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
    api_instance = astropulse._generated.NotificationsApi(api_client)
    topic = astropulse._generated.NotificationTopic() # NotificationTopic | Notification topic
    x_astro_organization_id = 'x_astro_organization_id_example' # str | Organization to act in with a bearer token; defaults to the user's current organization. Ignored with an API key, which carries its own. (optional)

    try:
        # Delete notification subscription
        api_response = api_instance.delete_notification_subscription(topic, x_astro_organization_id=x_astro_organization_id)
        print("The response of NotificationsApi->delete_notification_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->delete_notification_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | [**NotificationTopic**](.md)| Notification topic | 
 **x_astro_organization_id** | **str**| Organization to act in with a bearer token; defaults to the user&#39;s current organization. Ignored with an API key, which carries its own. | [optional] 

### Return type

[**BooleanResponse**](BooleanResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription deleted successfully |  -  |
**400** | Invalid parameters |  -  |
**401** | Missing or invalid authentication |  -  |
**403** | User does not have permission to configure notifications |  -  |
**404** | Subscription not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_integration**
> NotificationIntegrationResponse get_notification_integration(channel, x_astro_organization_id=x_astro_organization_id)

Get specific notification integration

Returns the configuration for the specified notification delivery channel (email or slack).

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.notification_channel_type import NotificationChannelType
from astropulse._generated.models.notification_integration_response import NotificationIntegrationResponse
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
    api_instance = astropulse._generated.NotificationsApi(api_client)
    channel = astropulse._generated.NotificationChannelType() # NotificationChannelType | The delivery channel
    x_astro_organization_id = 'x_astro_organization_id_example' # str | Organization to act in with a bearer token; defaults to the user's current organization. Ignored with an API key, which carries its own. (optional)

    try:
        # Get specific notification integration
        api_response = api_instance.get_notification_integration(channel, x_astro_organization_id=x_astro_organization_id)
        print("The response of NotificationsApi->get_notification_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->get_notification_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel** | [**NotificationChannelType**](.md)| The delivery channel | 
 **x_astro_organization_id** | **str**| Organization to act in with a bearer token; defaults to the user&#39;s current organization. Ignored with an API key, which carries its own. | [optional] 

### Return type

[**NotificationIntegrationResponse**](NotificationIntegrationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Notification integration details |  -  |
**400** | Invalid parameters |  -  |
**401** | Missing or invalid authentication |  -  |
**403** | User does not have permission to view notifications |  -  |
**404** | Integration not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_subscription**
> NotificationSubscriptionResponse get_notification_subscription(topic, x_astro_organization_id=x_astro_organization_id)

Get specific notification subscription

Returns the notification subscription configuration for the specified event topic, including its enabled channels.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.notification_subscription_response import NotificationSubscriptionResponse
from astropulse._generated.models.notification_topic import NotificationTopic
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
    api_instance = astropulse._generated.NotificationsApi(api_client)
    topic = astropulse._generated.NotificationTopic() # NotificationTopic | Notification topic
    x_astro_organization_id = 'x_astro_organization_id_example' # str | Organization to act in with a bearer token; defaults to the user's current organization. Ignored with an API key, which carries its own. (optional)

    try:
        # Get specific notification subscription
        api_response = api_instance.get_notification_subscription(topic, x_astro_organization_id=x_astro_organization_id)
        print("The response of NotificationsApi->get_notification_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->get_notification_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | [**NotificationTopic**](.md)| Notification topic | 
 **x_astro_organization_id** | **str**| Organization to act in with a bearer token; defaults to the user&#39;s current organization. Ignored with an API key, which carries its own. | [optional] 

### Return type

[**NotificationSubscriptionResponse**](NotificationSubscriptionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Notification subscription details |  -  |
**400** | Invalid parameters |  -  |
**401** | Missing or invalid authentication |  -  |
**403** | User does not have permission to view notifications |  -  |
**404** | Subscription not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notification_channel_availability**
> NotificationChannelAvailabilityListResponse list_notification_channel_availability()

Get which notification channels this organization's plan includes

For each notification channel, whether the organization's plan includes it and, when it does not, the plan that does.
Configuring an integration or subscription on a channel the plan does not include is refused.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.notification_channel_availability_list_response import NotificationChannelAvailabilityListResponse
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
    api_instance = astropulse._generated.NotificationsApi(api_client)

    try:
        # Get which notification channels this organization's plan includes
        api_response = api_instance.list_notification_channel_availability()
        print("The response of NotificationsApi->list_notification_channel_availability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->list_notification_channel_availability: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**NotificationChannelAvailabilityListResponse**](NotificationChannelAvailabilityListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Channels and whether the plan includes each |  -  |
**401** | Missing or invalid authentication |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notification_channels**
> NotificationChannelTypeListResponse list_notification_channels()

Get available channels

Returns the supported notification delivery channels (e.g., email, slack) that can be configured for the organization.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.notification_channel_type_list_response import NotificationChannelTypeListResponse
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
    api_instance = astropulse._generated.NotificationsApi(api_client)

    try:
        # Get available channels
        api_response = api_instance.list_notification_channels()
        print("The response of NotificationsApi->list_notification_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->list_notification_channels: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**NotificationChannelTypeListResponse**](NotificationChannelTypeListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of available notification channels |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notification_integrations**
> NotificationIntegrationListResponse list_notification_integrations(x_astro_organization_id=x_astro_organization_id)

List notification integrations

Returns all configured notification delivery integrations (e.g., email, Slack) for the organization.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.notification_integration_list_response import NotificationIntegrationListResponse
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
    api_instance = astropulse._generated.NotificationsApi(api_client)
    x_astro_organization_id = 'x_astro_organization_id_example' # str | Organization to act in with a bearer token; defaults to the user's current organization. Ignored with an API key, which carries its own. (optional)

    try:
        # List notification integrations
        api_response = api_instance.list_notification_integrations(x_astro_organization_id=x_astro_organization_id)
        print("The response of NotificationsApi->list_notification_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->list_notification_integrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_astro_organization_id** | **str**| Organization to act in with a bearer token; defaults to the user&#39;s current organization. Ignored with an API key, which carries its own. | [optional] 

### Return type

[**NotificationIntegrationListResponse**](NotificationIntegrationListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of notification integrations |  -  |
**400** | Invalid organization ID |  -  |
**401** | Missing or invalid authentication |  -  |
**403** | User does not have permission to view notifications |  -  |
**404** | Organization not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notification_subscriptions**
> NotificationSubscriptionListResponse list_notification_subscriptions(x_astro_organization_id=x_astro_organization_id)

List notification subscriptions

Returns all configured notification subscriptions for the organization, including topics and delivery channels.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.notification_subscription_list_response import NotificationSubscriptionListResponse
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
    api_instance = astropulse._generated.NotificationsApi(api_client)
    x_astro_organization_id = 'x_astro_organization_id_example' # str | Organization to act in with a bearer token; defaults to the user's current organization. Ignored with an API key, which carries its own. (optional)

    try:
        # List notification subscriptions
        api_response = api_instance.list_notification_subscriptions(x_astro_organization_id=x_astro_organization_id)
        print("The response of NotificationsApi->list_notification_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->list_notification_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_astro_organization_id** | **str**| Organization to act in with a bearer token; defaults to the user&#39;s current organization. Ignored with an API key, which carries its own. | [optional] 

### Return type

[**NotificationSubscriptionListResponse**](NotificationSubscriptionListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of notification subscriptions |  -  |
**400** | Invalid organization ID |  -  |
**401** | Missing or invalid authentication |  -  |
**403** | User does not have permission to view notifications |  -  |
**404** | Organization not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notification_topics**
> NotificationTopicListResponse list_notification_topics()

Get available notification topics

Returns the notification topics an organization can subscribe to.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.notification_topic_list_response import NotificationTopicListResponse
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
    api_instance = astropulse._generated.NotificationsApi(api_client)

    try:
        # Get available notification topics
        api_response = api_instance.list_notification_topics()
        print("The response of NotificationsApi->list_notification_topics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->list_notification_topics: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**NotificationTopicListResponse**](NotificationTopicListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of available notification topics |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_notification_integration**
> BooleanResponse test_notification_integration(channel, x_astro_organization_id=x_astro_organization_id)

Send a test notification

Sends a test message through the saved configuration of the given delivery channel, so the channel can be checked without re-entering its settings. Only the slack channel can be tested.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.boolean_response import BooleanResponse
from astropulse._generated.models.notification_channel_type import NotificationChannelType
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
    api_instance = astropulse._generated.NotificationsApi(api_client)
    channel = astropulse._generated.NotificationChannelType() # NotificationChannelType | The delivery channel; only slack can be tested
    x_astro_organization_id = 'x_astro_organization_id_example' # str | Organization to act in with a bearer token; defaults to the user's current organization. Ignored with an API key, which carries its own. (optional)

    try:
        # Send a test notification
        api_response = api_instance.test_notification_integration(channel, x_astro_organization_id=x_astro_organization_id)
        print("The response of NotificationsApi->test_notification_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->test_notification_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel** | [**NotificationChannelType**](.md)| The delivery channel; only slack can be tested | 
 **x_astro_organization_id** | **str**| Organization to act in with a bearer token; defaults to the user&#39;s current organization. Ignored with an API key, which carries its own. | [optional] 

### Return type

[**BooleanResponse**](BooleanResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Test message sent |  -  |
**400** | Invalid parameters, or the message could not be delivered |  -  |
**401** | Missing or invalid authentication |  -  |
**403** | User does not have permission to configure notifications |  -  |
**404** | Integration not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribe_notifications**
> BooleanResponse unsubscribe_notifications(unsubscribe_from_notifications_request, x_astro_organization_id=x_astro_organization_id)

Unsubscribe from notifications

Processes an unsubscribe link click, disabling the specified notification subscription for the organization associated with the unsubscribe token.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.boolean_response import BooleanResponse
from astropulse._generated.models.unsubscribe_from_notifications_request import UnsubscribeFromNotificationsRequest
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
    api_instance = astropulse._generated.NotificationsApi(api_client)
    unsubscribe_from_notifications_request = astropulse._generated.UnsubscribeFromNotificationsRequest() # UnsubscribeFromNotificationsRequest | Unsubscribe request
    x_astro_organization_id = 'x_astro_organization_id_example' # str | Organization to act in with a bearer token; defaults to the user's current organization. Ignored with an API key, which carries its own. (optional)

    try:
        # Unsubscribe from notifications
        api_response = api_instance.unsubscribe_notifications(unsubscribe_from_notifications_request, x_astro_organization_id=x_astro_organization_id)
        print("The response of NotificationsApi->unsubscribe_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->unsubscribe_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unsubscribe_from_notifications_request** | [**UnsubscribeFromNotificationsRequest**](UnsubscribeFromNotificationsRequest.md)| Unsubscribe request | 
 **x_astro_organization_id** | **str**| Organization to act in with a bearer token; defaults to the user&#39;s current organization. Ignored with an API key, which carries its own. | [optional] 

### Return type

[**BooleanResponse**](BooleanResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unsubscribed successfully |  -  |
**400** | Invalid parameters |  -  |
**401** | Missing or invalid authentication |  -  |
**403** | User does not have permission to configure notifications |  -  |
**404** | Subscription not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_notification_integration**
> NotificationIntegrationResponse upsert_notification_integration(notification_integration_request, x_astro_organization_id=x_astro_organization_id)

Configure notification integration

Saves the delivery channel configuration (e.g., Slack webhook URL or email recipients) for the organization, replacing any existing settings for that channel type. Leaving the Slack webhook URL out, or sending back the masked one, keeps the saved URL. Slack notifications are delivered through an incoming webhook only; a Slack app installation is refused.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.notification_integration_request import NotificationIntegrationRequest
from astropulse._generated.models.notification_integration_response import NotificationIntegrationResponse
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
    api_instance = astropulse._generated.NotificationsApi(api_client)
    notification_integration_request = astropulse._generated.NotificationIntegrationRequest() # NotificationIntegrationRequest | Integration configuration
    x_astro_organization_id = 'x_astro_organization_id_example' # str | Organization to act in with a bearer token; defaults to the user's current organization. Ignored with an API key, which carries its own. (optional)

    try:
        # Configure notification integration
        api_response = api_instance.upsert_notification_integration(notification_integration_request, x_astro_organization_id=x_astro_organization_id)
        print("The response of NotificationsApi->upsert_notification_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->upsert_notification_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_integration_request** | [**NotificationIntegrationRequest**](NotificationIntegrationRequest.md)| Integration configuration | 
 **x_astro_organization_id** | **str**| Organization to act in with a bearer token; defaults to the user&#39;s current organization. Ignored with an API key, which carries its own. | [optional] 

### Return type

[**NotificationIntegrationResponse**](NotificationIntegrationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Integration configured successfully |  -  |
**400** | Invalid integration data |  -  |
**401** | Missing or invalid authentication |  -  |
**403** | User does not have permission to configure notifications |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_notification_subscription**
> NotificationSubscriptionResponse upsert_notification_subscription(notification_subscription_request, x_astro_organization_id=x_astro_organization_id)

Create or update notification subscription

Saves the notification subscription for the given topic, replacing any existing configuration. At least one delivery channel is required.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.notification_subscription_request import NotificationSubscriptionRequest
from astropulse._generated.models.notification_subscription_response import NotificationSubscriptionResponse
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
    api_instance = astropulse._generated.NotificationsApi(api_client)
    notification_subscription_request = astropulse._generated.NotificationSubscriptionRequest() # NotificationSubscriptionRequest | Subscription configuration
    x_astro_organization_id = 'x_astro_organization_id_example' # str | Organization to act in with a bearer token; defaults to the user's current organization. Ignored with an API key, which carries its own. (optional)

    try:
        # Create or update notification subscription
        api_response = api_instance.upsert_notification_subscription(notification_subscription_request, x_astro_organization_id=x_astro_organization_id)
        print("The response of NotificationsApi->upsert_notification_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->upsert_notification_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_subscription_request** | [**NotificationSubscriptionRequest**](NotificationSubscriptionRequest.md)| Subscription configuration | 
 **x_astro_organization_id** | **str**| Organization to act in with a bearer token; defaults to the user&#39;s current organization. Ignored with an API key, which carries its own. | [optional] 

### Return type

[**NotificationSubscriptionResponse**](NotificationSubscriptionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription created or updated successfully |  -  |
**400** | Invalid subscription data |  -  |
**401** | Missing or invalid authentication |  -  |
**403** | User does not have permission to configure notifications |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

