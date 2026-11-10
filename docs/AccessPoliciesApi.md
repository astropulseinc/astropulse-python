# astropulse._generated.AccessPoliciesApi

All URIs are relative to *https://api.astropulse.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_access_policy_key**](AccessPoliciesApi.md#create_access_policy_key) | **POST** /api/v1/access-policies/{name}/keys | Create an API key for an access policy
[**delete_access_policy**](AccessPoliciesApi.md#delete_access_policy) | **DELETE** /api/v1/access-policies/{name} | Delete an unreferenced access policy
[**get_access_policy**](AccessPoliciesApi.md#get_access_policy) | **GET** /api/v1/access-policies/{name} | Get an access policy revision
[**list_access_policies**](AccessPoliciesApi.md#list_access_policies) | **GET** /api/v1/access-policies | List access policies
[**list_access_policy_keys**](AccessPoliciesApi.md#list_access_policy_keys) | **GET** /api/v1/access-policies/{name}/keys | List an access policy&#39;s API keys
[**revoke_access_policy_key**](AccessPoliciesApi.md#revoke_access_policy_key) | **DELETE** /api/v1/access-policies/{name}/keys/{keyId} | Revoke an access policy&#39;s API key
[**test_access_policy_token**](AccessPoliciesApi.md#test_access_policy_token) | **POST** /api/v1/access-policies/{name}/test | Test a token against an access policy
[**upsert_access_policy**](AccessPoliciesApi.md#upsert_access_policy) | **PUT** /api/v1/access-policies/{name} | Create or revise an access policy


# **create_access_policy_key**
> AccessPolicyKeyCreatedResponse create_access_policy_key(name, access_policy_key_request, x_astro_organization_id=x_astro_organization_id)

Create an API key for an access policy

Creates a caller API key for a policy whose keys AstroPulse keeps. The key is returned only in this response; endpoints on the policy accept it within a minute, with no redeploy.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.access_policy_key_created_response import AccessPolicyKeyCreatedResponse
from astropulse._generated.models.access_policy_key_request import AccessPolicyKeyRequest
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
    api_instance = astropulse._generated.AccessPoliciesApi(api_client)
    name = 'name_example' # str | Policy name
    access_policy_key_request = astropulse._generated.AccessPolicyKeyRequest() # AccessPolicyKeyRequest | Who the key is for, and when it expires
    x_astro_organization_id = 'x_astro_organization_id_example' # str | Organization to act in with a bearer token; defaults to the user's current organization. Ignored with an API key, which carries its own. (optional)

    try:
        # Create an API key for an access policy
        api_response = api_instance.create_access_policy_key(name, access_policy_key_request, x_astro_organization_id=x_astro_organization_id)
        print("The response of AccessPoliciesApi->create_access_policy_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessPoliciesApi->create_access_policy_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Policy name | 
 **access_policy_key_request** | [**AccessPolicyKeyRequest**](AccessPolicyKeyRequest.md)| Who the key is for, and when it expires | 
 **x_astro_organization_id** | **str**| Organization to act in with a bearer token; defaults to the user&#39;s current organization. Ignored with an API key, which carries its own. | [optional] 

### Return type

[**AccessPolicyKeyCreatedResponse**](AccessPolicyKeyCreatedResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Invalid label or expiry |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | No such access policy |  -  |
**409** | The policy does not keep its keys in AstroPulse, or already holds the most keys it can |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Credential storage is unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_access_policy**
> delete_access_policy(name, revision, x_astro_organization_id=x_astro_organization_id)

Delete an unreferenced access policy

Deletes a policy no endpoint references, with any API keys AstroPulse keeps for it. One still attached to an application is refused.

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
    api_instance = astropulse._generated.AccessPoliciesApi(api_client)
    name = 'name_example' # str | Policy name
    revision = 56 # int | Policy revision; GET defaults to latest
    x_astro_organization_id = 'x_astro_organization_id_example' # str | Organization to act in with a bearer token; defaults to the user's current organization. Ignored with an API key, which carries its own. (optional)

    try:
        # Delete an unreferenced access policy
        api_instance.delete_access_policy(name, revision, x_astro_organization_id=x_astro_organization_id)
    except Exception as e:
        print("Exception when calling AccessPoliciesApi->delete_access_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Policy name | 
 **revision** | **int**| Policy revision; GET defaults to latest | 
 **x_astro_organization_id** | **str**| Organization to act in with a bearer token; defaults to the user&#39;s current organization. Ignored with an API key, which carries its own. | [optional] 

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
**204** | The policy is gone |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_policy**
> AccessPolicyResponse get_access_policy(name, x_astro_organization_id=x_astro_organization_id, revision=revision)

Get an access policy revision

One access policy, including the revision an endpoint quotes to prove which version it enforces.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.access_policy_response import AccessPolicyResponse
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
    api_instance = astropulse._generated.AccessPoliciesApi(api_client)
    name = 'name_example' # str | Policy name
    x_astro_organization_id = 'x_astro_organization_id_example' # str | Organization to act in with a bearer token; defaults to the user's current organization. Ignored with an API key, which carries its own. (optional)
    revision = 56 # int | Policy revision; GET defaults to latest (optional)

    try:
        # Get an access policy revision
        api_response = api_instance.get_access_policy(name, x_astro_organization_id=x_astro_organization_id, revision=revision)
        print("The response of AccessPoliciesApi->get_access_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessPoliciesApi->get_access_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Policy name | 
 **x_astro_organization_id** | **str**| Organization to act in with a bearer token; defaults to the user&#39;s current organization. Ignored with an API key, which carries its own. | [optional] 
 **revision** | **int**| Policy revision; GET defaults to latest | [optional] 

### Return type

[**AccessPolicyResponse**](AccessPolicyResponse.md)

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

# **list_access_policies**
> AccessPolicyListResponse list_access_policies(x_astro_organization_id=x_astro_organization_id)

List access policies

The organization's access policies: what each accepts, its revision, and the applications attached.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.access_policy_list_response import AccessPolicyListResponse
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
    api_instance = astropulse._generated.AccessPoliciesApi(api_client)
    x_astro_organization_id = 'x_astro_organization_id_example' # str | Organization to act in with a bearer token; defaults to the user's current organization. Ignored with an API key, which carries its own. (optional)

    try:
        # List access policies
        api_response = api_instance.list_access_policies(x_astro_organization_id=x_astro_organization_id)
        print("The response of AccessPoliciesApi->list_access_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessPoliciesApi->list_access_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_astro_organization_id** | **str**| Organization to act in with a bearer token; defaults to the user&#39;s current organization. Ignored with an API key, which carries its own. | [optional] 

### Return type

[**AccessPolicyListResponse**](AccessPolicyListResponse.md)

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

# **list_access_policy_keys**
> AccessPolicyKeyListResponse list_access_policy_keys(name, x_astro_organization_id=x_astro_organization_id)

List an access policy's API keys

The API keys of a policy whose keys AstroPulse keeps: ID, label, creation and expiry. Key values are never returned.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.access_policy_key_list_response import AccessPolicyKeyListResponse
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
    api_instance = astropulse._generated.AccessPoliciesApi(api_client)
    name = 'name_example' # str | Policy name
    x_astro_organization_id = 'x_astro_organization_id_example' # str | Organization to act in with a bearer token; defaults to the user's current organization. Ignored with an API key, which carries its own. (optional)

    try:
        # List an access policy's API keys
        api_response = api_instance.list_access_policy_keys(name, x_astro_organization_id=x_astro_organization_id)
        print("The response of AccessPoliciesApi->list_access_policy_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessPoliciesApi->list_access_policy_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Policy name | 
 **x_astro_organization_id** | **str**| Organization to act in with a bearer token; defaults to the user&#39;s current organization. Ignored with an API key, which carries its own. | [optional] 

### Return type

[**AccessPolicyKeyListResponse**](AccessPolicyKeyListResponse.md)

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
**404** | No such access policy |  -  |
**409** | The policy does not keep its keys in AstroPulse |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Credential storage is unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_access_policy_key**
> revoke_access_policy_key(name, key_id, x_astro_organization_id=x_astro_organization_id)

Revoke an access policy's API key

Deletes the key from AstroPulse first; every endpoint on the policy refuses it within a minute, with no redeploy. A revoked key cannot be restored.

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
    api_instance = astropulse._generated.AccessPoliciesApi(api_client)
    name = 'name_example' # str | Policy name
    key_id = 'key_id_example' # str | API key ID
    x_astro_organization_id = 'x_astro_organization_id_example' # str | Organization to act in with a bearer token; defaults to the user's current organization. Ignored with an API key, which carries its own. (optional)

    try:
        # Revoke an access policy's API key
        api_instance.revoke_access_policy_key(name, key_id, x_astro_organization_id=x_astro_organization_id)
    except Exception as e:
        print("Exception when calling AccessPoliciesApi->revoke_access_policy_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Policy name | 
 **key_id** | **str**| API key ID | 
 **x_astro_organization_id** | **str**| Organization to act in with a bearer token; defaults to the user&#39;s current organization. Ignored with an API key, which carries its own. | [optional] 

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
**204** | The key is revoked |  -  |
**400** | Malformed key ID |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | No such access policy or key |  -  |
**409** | The policy does not keep its keys in AstroPulse |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Credential storage is unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_access_policy_token**
> AccessPolicyTokenResultResponse test_access_policy_token(name, access_policy_token_test, x_astro_organization_id=x_astro_organization_id)

Test a token against an access policy

Whether an endpoint under the policy's latest revision would accept this JWT, and if not exactly why. The token is never stored, logged or audited.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.access_policy_token_result_response import AccessPolicyTokenResultResponse
from astropulse._generated.models.access_policy_token_test import AccessPolicyTokenTest
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
    api_instance = astropulse._generated.AccessPoliciesApi(api_client)
    name = 'name_example' # str | Policy name
    access_policy_token_test = astropulse._generated.AccessPolicyTokenTest() # AccessPolicyTokenTest | The token to test
    x_astro_organization_id = 'x_astro_organization_id_example' # str | Organization to act in with a bearer token; defaults to the user's current organization. Ignored with an API key, which carries its own. (optional)

    try:
        # Test a token against an access policy
        api_response = api_instance.test_access_policy_token(name, access_policy_token_test, x_astro_organization_id=x_astro_organization_id)
        print("The response of AccessPoliciesApi->test_access_policy_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessPoliciesApi->test_access_policy_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Policy name | 
 **access_policy_token_test** | [**AccessPolicyTokenTest**](AccessPolicyTokenTest.md)| The token to test | 
 **x_astro_organization_id** | **str**| Organization to act in with a bearer token; defaults to the user&#39;s current organization. Ignored with an API key, which carries its own. | [optional] 

### Return type

[**AccessPolicyTokenResultResponse**](AccessPolicyTokenResultResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | No token, or the policy does not accept JWTs |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_access_policy**
> AccessPolicyResponse upsert_access_policy(name, access_policy, x_astro_organization_id=x_astro_organization_id, allow_unverified=allow_unverified, dry_run=dry_run)

Create or revise an access policy

Revision must be zero to create, or the current revision to change it; the same policy applied again returns its current revision. A JWT policy's provider is checked first; an issuer alone fills jwksUri from discovery.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.access_policy import AccessPolicy
from astropulse._generated.models.access_policy_response import AccessPolicyResponse
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
    api_instance = astropulse._generated.AccessPoliciesApi(api_client)
    name = 'name_example' # str | Policy name
    access_policy = astropulse._generated.AccessPolicy() # AccessPolicy | Access policy manifest
    x_astro_organization_id = 'x_astro_organization_id_example' # str | Organization to act in with a bearer token; defaults to the user's current organization. Ignored with an API key, which carries its own. (optional)
    allow_unverified = True # bool | Save a JWT policy even when its identity provider cannot be reached; a provider that answers wrongly is still refused (optional)
    dry_run = True # bool | When true, runs every check an apply runs, saves nothing, and returns the policy as it would be saved (optional)

    try:
        # Create or revise an access policy
        api_response = api_instance.upsert_access_policy(name, access_policy, x_astro_organization_id=x_astro_organization_id, allow_unverified=allow_unverified, dry_run=dry_run)
        print("The response of AccessPoliciesApi->upsert_access_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessPoliciesApi->upsert_access_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Policy name | 
 **access_policy** | [**AccessPolicy**](AccessPolicy.md)| Access policy manifest | 
 **x_astro_organization_id** | **str**| Organization to act in with a bearer token; defaults to the user&#39;s current organization. Ignored with an API key, which carries its own. | [optional] 
 **allow_unverified** | **bool**| Save a JWT policy even when its identity provider cannot be reached; a provider that answers wrongly is still refused | [optional] 
 **dry_run** | **bool**| When true, runs every check an apply runs, saves nothing, and returns the policy as it would be saved | [optional] 

### Return type

[**AccessPolicyResponse**](AccessPolicyResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The policy as saved, or with dryRun&#x3D;true as it would be saved |  -  |
**400** | Invalid policy, or the identity provider&#39;s discovery document or key set is wrong |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | The identity provider could not be reached; retry, or save with allowUnverified |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

