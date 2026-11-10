# astropulse._generated.CloudAccountsApi

All URIs are relative to *https://api.astropulse.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connect_aws_account**](CloudAccountsApi.md#connect_aws_account) | **POST** /api/v1/cloud/aws/connect | Connect AWS account for cluster provisioning
[**connect_azure_subscription**](CloudAccountsApi.md#connect_azure_subscription) | **POST** /api/v1/cloud/azure/connect | Connect Azure subscription for cluster provisioning
[**connect_gcp_project**](CloudAccountsApi.md#connect_gcp_project) | **POST** /api/v1/cloud/gcp/connect | Connect GCP project for cluster provisioning
[**connect_self_hosted**](CloudAccountsApi.md#connect_self_hosted) | **POST** /api/v1/cloud/selfhosted/connect | Store self-hosted cluster credentials
[**delete_self_hosted_credentials**](CloudAccountsApi.md#delete_self_hosted_credentials) | **DELETE** /api/v1/cloud/selfhosted/credentials | Delete self-hosted cluster credentials
[**dismiss_cloud_connection**](CloudAccountsApi.md#dismiss_cloud_connection) | **DELETE** /api/v1/cloud/connections/{connectionId} | Dismiss a failed or unfinished cloud connection
[**forget_self_hosted_setup**](CloudAccountsApi.md#forget_self_hosted_setup) | **DELETE** /api/v1/cloud/{provider}/selfhosted/setup | Forget a self-hosted cluster&#39;s setup
[**get_aws_connection_status**](CloudAccountsApi.md#get_aws_connection_status) | **GET** /api/v1/cloud/aws/{id}/status | Get AWS cloud account connection status
[**get_aws_credentials**](CloudAccountsApi.md#get_aws_credentials) | **POST** /api/v1/cloud/aws/credentials | Get AWS temporary credentials
[**get_azure_connection_status**](CloudAccountsApi.md#get_azure_connection_status) | **GET** /api/v1/cloud/azure/{id}/status | Get Azure cloud account connection status
[**get_azure_credentials**](CloudAccountsApi.md#get_azure_credentials) | **GET** /api/v1/cloud/azure/credentials | Get Azure temporary credentials
[**get_cloud_connection**](CloudAccountsApi.md#get_cloud_connection) | **GET** /api/v1/cloud/{provider}/connection | Check a cloud account connection
[**get_gcp_connection_status**](CloudAccountsApi.md#get_gcp_connection_status) | **GET** /api/v1/cloud/gcp/{id}/status | Get GCP cloud account connection status
[**get_gcp_credentials**](CloudAccountsApi.md#get_gcp_credentials) | **POST** /api/v1/cloud/gcp/credentials | Get GCP temporary credentials
[**get_self_hosted_aws_template**](CloudAccountsApi.md#get_self_hosted_aws_template) | **GET** /api/v1/cloud/aws/selfhosted/template | Get the self-hosted AWS setup template
[**get_self_hosted_cloud_connection**](CloudAccountsApi.md#get_self_hosted_cloud_connection) | **GET** /api/v1/cloud/selfhosted/connection | Check a self-hosted cluster&#39;s cloud credentials
[**get_self_hosted_credentials_status**](CloudAccountsApi.md#get_self_hosted_credentials_status) | **GET** /api/v1/cloud/selfhosted/credentials/status | Get self-hosted credential vault status
[**get_self_hosted_setup**](CloudAccountsApi.md#get_self_hosted_setup) | **GET** /api/v1/cloud/{provider}/selfhosted/setup | Get a self-hosted cluster&#39;s setup
[**list_aws_capacity_reservations**](CloudAccountsApi.md#list_aws_capacity_reservations) | **GET** /api/v1/cloud/aws/capacity-reservations | List the account&#39;s capacity reservations and Capacity Blocks
[**list_cloud_accounts**](CloudAccountsApi.md#list_cloud_accounts) | **GET** /api/v1/cloud/accounts | List the organization&#39;s cloud accounts
[**list_cloud_connections**](CloudAccountsApi.md#list_cloud_connections) | **GET** /api/v1/cloud/connections | List the organization&#39;s cloud connections
[**list_kubernetes_versions**](CloudAccountsApi.md#list_kubernetes_versions) | **GET** /api/v1/cloud/k8s-versions | Get supported Kubernetes versions
[**start_self_hosted_setup**](CloudAccountsApi.md#start_self_hosted_setup) | **POST** /api/v1/cloud/{provider}/selfhosted/setup | Start a self-hosted cluster&#39;s setup


# **connect_aws_account**
> AWSConnectStatusResponse connect_aws_account(aws_connect_request)

Connect AWS account for cluster provisioning

Connect your AWS account so AstroPulse can provision EKS clusters. Creates an IAM role via CloudFormation.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.aws_connect_request import AWSConnectRequest
from astropulse._generated.models.aws_connect_status_response import AWSConnectStatusResponse
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
    api_instance = astropulse._generated.CloudAccountsApi(api_client)
    aws_connect_request = astropulse._generated.AWSConnectRequest() # AWSConnectRequest | AWS cloud account request

    try:
        # Connect AWS account for cluster provisioning
        api_response = api_instance.connect_aws_account(aws_connect_request)
        print("The response of CloudAccountsApi->connect_aws_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudAccountsApi->connect_aws_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aws_connect_request** | [**AWSConnectRequest**](AWSConnectRequest.md)| AWS cloud account request | 

### Return type

[**AWSConnectStatusResponse**](AWSConnectStatusResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Cloud account provisioning accepted |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | Caller is not an organization admin |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Temporarily unavailable; try again |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connect_azure_subscription**
> AzureConnectStatusResponse connect_azure_subscription(azure_connect_request)

Connect Azure subscription for cluster provisioning

Connect your Azure subscription so AstroPulse can provision AKS clusters via Workload Identity Federation.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.azure_connect_request import AzureConnectRequest
from astropulse._generated.models.azure_connect_status_response import AzureConnectStatusResponse
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
    api_instance = astropulse._generated.CloudAccountsApi(api_client)
    azure_connect_request = astropulse._generated.AzureConnectRequest() # AzureConnectRequest | Azure cloud account request

    try:
        # Connect Azure subscription for cluster provisioning
        api_response = api_instance.connect_azure_subscription(azure_connect_request)
        print("The response of CloudAccountsApi->connect_azure_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudAccountsApi->connect_azure_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_connect_request** | [**AzureConnectRequest**](AzureConnectRequest.md)| Azure cloud account request | 

### Return type

[**AzureConnectStatusResponse**](AzureConnectStatusResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Cloud account provisioning accepted |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | Caller is not an organization admin |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Temporarily unavailable; try again |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connect_gcp_project**
> GCPConnectStatusResponse connect_gcp_project(gcp_connect_request)

Connect GCP project for cluster provisioning

Connect your GCP project so AstroPulse can provision GKE clusters. Sets up Workload Identity Federation.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.gcp_connect_request import GCPConnectRequest
from astropulse._generated.models.gcp_connect_status_response import GCPConnectStatusResponse
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
    api_instance = astropulse._generated.CloudAccountsApi(api_client)
    gcp_connect_request = astropulse._generated.GCPConnectRequest() # GCPConnectRequest | GCP cloud account request

    try:
        # Connect GCP project for cluster provisioning
        api_response = api_instance.connect_gcp_project(gcp_connect_request)
        print("The response of CloudAccountsApi->connect_gcp_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudAccountsApi->connect_gcp_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gcp_connect_request** | [**GCPConnectRequest**](GCPConnectRequest.md)| GCP cloud account request | 

### Return type

[**GCPConnectStatusResponse**](GCPConnectStatusResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Cloud account provisioning accepted |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | Caller is not an organization admin |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Temporarily unavailable; try again |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connect_self_hosted**
> SelfHostedConnectionResponse connect_self_hosted(self_hosted_connect_request)

Store self-hosted cluster credentials

Checks AWS or GCP credentials for a self-hosted cluster against the account (identity, state bucket, required roles and APIs),
stores them encrypted in AstroPulse only when every check passes, and records both steps on the cluster's setup.
A failed check is refused with 400 naming the check, what to fix and the cloud provider's error.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.self_hosted_connect_request import SelfHostedConnectRequest
from astropulse._generated.models.self_hosted_connection_response import SelfHostedConnectionResponse
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
    api_instance = astropulse._generated.CloudAccountsApi(api_client)
    self_hosted_connect_request = astropulse._generated.SelfHostedConnectRequest() # SelfHostedConnectRequest | Self-hosted connect request

    try:
        # Store self-hosted cluster credentials
        api_response = api_instance.connect_self_hosted(self_hosted_connect_request)
        print("The response of CloudAccountsApi->connect_self_hosted:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudAccountsApi->connect_self_hosted: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **self_hosted_connect_request** | [**SelfHostedConnectRequest**](SelfHostedConnectRequest.md)| Self-hosted connect request | 

### Return type

[**SelfHostedConnectionResponse**](SelfHostedConnectionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | Caller is not an organization admin |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable; retry after the Retry-After interval |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_self_hosted_credentials**
> SelfHostedCredentialRevocationResponse delete_self_hosted_credentials(cluster_name)

Delete self-hosted cluster credentials

Deletes AstroPulse's stored copy of a self-hosted cluster's credentials. The key stays valid in the cloud account;
the message names it and how to delete it there.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.self_hosted_credential_revocation_response import SelfHostedCredentialRevocationResponse
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
    api_instance = astropulse._generated.CloudAccountsApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name

    try:
        # Delete self-hosted cluster credentials
        api_response = api_instance.delete_self_hosted_credentials(cluster_name)
        print("The response of CloudAccountsApi->delete_self_hosted_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudAccountsApi->delete_self_hosted_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 

### Return type

[**SelfHostedCredentialRevocationResponse**](SelfHostedCredentialRevocationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | What was deleted and what is still valid |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | Caller is not an organization admin |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dismiss_cloud_connection**
> CloudConnectionResponse dismiss_cloud_connection(connection_id)

Dismiss a failed or unfinished cloud connection

Removes AstroPulse's record of a connection whose setup failed or never finished; nothing in the cloud account changes.
A connected connection, or one whose setup is still running, is refused with 409.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cloud_connection_response import CloudConnectionResponse
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
    api_instance = astropulse._generated.CloudAccountsApi(api_client)
    connection_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Connection ID the connect endpoint returned

    try:
        # Dismiss a failed or unfinished cloud connection
        api_response = api_instance.dismiss_cloud_connection(connection_id)
        print("The response of CloudAccountsApi->dismiss_cloud_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudAccountsApi->dismiss_cloud_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **UUID**| Connection ID the connect endpoint returned | 

### Return type

[**CloudConnectionResponse**](CloudConnectionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connection dismissed |  -  |
**400** | Invalid connection ID |  -  |
**401** | Missing or invalid API key |  -  |
**403** | Caller is not an organization admin |  -  |
**404** | No such connection in the organization |  -  |
**409** | The connection is connected, or its setup is still running |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Temporarily unavailable; try again |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forget_self_hosted_setup**
> SelfHostedSetupResponse forget_self_hosted_setup(provider, cluster_name)

Forget a self-hosted cluster's setup

Removes the record of a cluster's self-hosted setup and ends the setup if it is still waiting for credentials.
Nothing in your AWS account or GCP project is changed; the message names the cleanup command for what the setup created.
Refused while credentials are stored for the cluster: disconnect them first.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.provider import Provider
from astropulse._generated.models.self_hosted_setup_response import SelfHostedSetupResponse
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
    api_instance = astropulse._generated.CloudAccountsApi(api_client)
    provider = astropulse._generated.Provider() # Provider | Cloud provider. Takes only `aws` or `gcp`.
    cluster_name = 'cluster_name_example' # str | Cluster name

    try:
        # Forget a self-hosted cluster's setup
        api_response = api_instance.forget_self_hosted_setup(provider, cluster_name)
        print("The response of CloudAccountsApi->forget_self_hosted_setup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudAccountsApi->forget_self_hosted_setup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | [**Provider**](.md)| Cloud provider. Takes only &#x60;aws&#x60; or &#x60;gcp&#x60;. | 
 **cluster_name** | **str**| Cluster name | 

### Return type

[**SelfHostedSetupResponse**](SelfHostedSetupResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The setup that was forgotten |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | Caller is not an organization admin |  -  |
**404** | No setup is recorded for the cluster |  -  |
**409** | Credentials are stored for the cluster |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable; retry after the Retry-After interval |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aws_connection_status**
> AWSConnectStatusResponse get_aws_connection_status(id)

Get AWS cloud account connection status

Polls an AWS account connection started by POST /api/v1/cloud/aws/connect.
Returns nextStep once setup is ready: the CloudFormation console link that creates the role in your account, pre-filled, with what to do.
Once ready, if the account's stack is at an older template, nextStep is its update link and command.
Then reports a terminal status when setup completes or fails.
While a check of the account fails, lastError says why and how long AstroPulse has been retrying.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.aws_connect_status_response import AWSConnectStatusResponse
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
    api_instance = astropulse._generated.CloudAccountsApi(api_client)
    id = 'id_example' # str | Cloud connection ID returned by the connect endpoint

    try:
        # Get AWS cloud account connection status
        api_response = api_instance.get_aws_connection_status(id)
        print("The response of CloudAccountsApi->get_aws_connection_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudAccountsApi->get_aws_connection_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cloud connection ID returned by the connect endpoint | 

### Return type

[**AWSConnectStatusResponse**](AWSConnectStatusResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cloud account status retrieved |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | Caller is not an organization admin |  -  |
**404** | Operation not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Temporarily unavailable; try again |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aws_credentials**
> AWSTemporaryCredentialResponse get_aws_credentials(aws_credentials_request)

Get AWS temporary credentials

Get temporary AWS credentials for cluster operations

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.aws_credentials_request import AWSCredentialsRequest
from astropulse._generated.models.aws_temporary_credential_response import AWSTemporaryCredentialResponse
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
    api_instance = astropulse._generated.CloudAccountsApi(api_client)
    aws_credentials_request = astropulse._generated.AWSCredentialsRequest() # AWSCredentialsRequest | AWS credential request

    try:
        # Get AWS temporary credentials
        api_response = api_instance.get_aws_credentials(aws_credentials_request)
        print("The response of CloudAccountsApi->get_aws_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudAccountsApi->get_aws_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aws_credentials_request** | [**AWSCredentialsRequest**](AWSCredentialsRequest.md)| AWS credential request | 

### Return type

[**AWSTemporaryCredentialResponse**](AWSTemporaryCredentialResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Temporary credentials retrieved |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | Caller is not an organization admin |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Temporarily unavailable; try again |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_azure_connection_status**
> AzureConnectStatusResponse get_azure_connection_status(id)

Get Azure cloud account connection status

Polls an Azure subscription connection started by POST /api/v1/cloud/azure/connect.
Returns nextStep once setup is ready: the Azure Cloud Shell link, the command to paste there and the setup script it runs.
While a check of the subscription fails, lastError says why and how long AstroPulse has been retrying.
Then reports a terminal status when setup completes or fails.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.azure_connect_status_response import AzureConnectStatusResponse
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
    api_instance = astropulse._generated.CloudAccountsApi(api_client)
    id = 'id_example' # str | Cloud connection ID returned by the connect endpoint

    try:
        # Get Azure cloud account connection status
        api_response = api_instance.get_azure_connection_status(id)
        print("The response of CloudAccountsApi->get_azure_connection_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudAccountsApi->get_azure_connection_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cloud connection ID returned by the connect endpoint | 

### Return type

[**AzureConnectStatusResponse**](AzureConnectStatusResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cloud account status retrieved |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | Caller is not an organization admin |  -  |
**404** | Operation not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Temporarily unavailable; try again |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_azure_credentials**
> AzureTemporaryCredentialResponse get_azure_credentials(cluster_name, subscription_id=subscription_id, resource_group=resource_group, target_region=target_region, duration=duration)

Get Azure temporary credentials

Get temporary Azure credentials for cluster operations

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.azure_temporary_credential_response import AzureTemporaryCredentialResponse
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
    api_instance = astropulse._generated.CloudAccountsApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    subscription_id = 'subscription_id_example' # str | Azure subscription ID (optional)
    resource_group = 'resource_group_example' # str | Azure resource group (optional)
    target_region = 'target_region_example' # str | Azure region (optional)
    duration = 'duration_example' # str | Credential duration (optional)

    try:
        # Get Azure temporary credentials
        api_response = api_instance.get_azure_credentials(cluster_name, subscription_id=subscription_id, resource_group=resource_group, target_region=target_region, duration=duration)
        print("The response of CloudAccountsApi->get_azure_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudAccountsApi->get_azure_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **subscription_id** | **str**| Azure subscription ID | [optional] 
 **resource_group** | **str**| Azure resource group | [optional] 
 **target_region** | **str**| Azure region | [optional] 
 **duration** | **str**| Credential duration | [optional] 

### Return type

[**AzureTemporaryCredentialResponse**](AzureTemporaryCredentialResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Temporary credentials retrieved |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | Caller is not an organization admin |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Temporarily unavailable; try again |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_connection**
> CloudConnectionResponse get_cloud_connection(provider, cluster_name, account_id=account_id, region=region, resource_group=resource_group)

Check a cloud account connection

Reports whether AstroPulse can reach the account connected for a cluster right now, the same way for every provider:
NotConnected, Pending, Connected, OutdatedTemplate (AWS), Failed, or Unknown when it could not be checked just now.
It never returns credentials.
An OutdatedTemplate answer carries nextStep: the stack's update link and command.
For a member who is not an organization admin the answer omits accountId, region, resourceGroup, connectionId, nextStep and the template versions.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cloud_connection_response import CloudConnectionResponse
from astropulse._generated.models.provider import Provider
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
    api_instance = astropulse._generated.CloudAccountsApi(api_client)
    provider = astropulse._generated.Provider() # Provider | The cloud the connection is to
    cluster_name = 'cluster_name_example' # str | Cluster name the connection was made for
    account_id = 'account_id_example' # str | AWS account ID, GCP project ID or Azure subscription ID; looked up from the cluster when omitted (optional)
    region = 'region_example' # str | Region; looked up from the cluster when omitted (optional)
    resource_group = 'resource_group_example' # str | Azure resource group; looked up from the cluster when omitted (optional)

    try:
        # Check a cloud account connection
        api_response = api_instance.get_cloud_connection(provider, cluster_name, account_id=account_id, region=region, resource_group=resource_group)
        print("The response of CloudAccountsApi->get_cloud_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudAccountsApi->get_cloud_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | [**Provider**](.md)| The cloud the connection is to | 
 **cluster_name** | **str**| Cluster name the connection was made for | 
 **account_id** | **str**| AWS account ID, GCP project ID or Azure subscription ID; looked up from the cluster when omitted | [optional] 
 **region** | **str**| Region; looked up from the cluster when omitted | [optional] 
 **resource_group** | **str**| Azure resource group; looked up from the cluster when omitted | [optional] 

### Return type

[**CloudConnectionResponse**](CloudConnectionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connection checked |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | Caller is not a member of the organization |  -  |
**404** | No such cluster, when a value to look up is omitted |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Temporarily unavailable; try again |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gcp_connection_status**
> GCPConnectStatusResponse get_gcp_connection_status(id)

Get GCP cloud account connection status

Polls a GCP project connection started by POST /api/v1/cloud/gcp/connect.
Returns nextStep once setup is ready: the Cloud Shell link for your project, the command to paste there and the setup script it runs.
While a check of the project fails, lastError says why and how long AstroPulse has been retrying.
Then reports a terminal status when setup completes or fails.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.gcp_connect_status_response import GCPConnectStatusResponse
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
    api_instance = astropulse._generated.CloudAccountsApi(api_client)
    id = 'id_example' # str | Cloud connection ID returned by the connect endpoint

    try:
        # Get GCP cloud account connection status
        api_response = api_instance.get_gcp_connection_status(id)
        print("The response of CloudAccountsApi->get_gcp_connection_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudAccountsApi->get_gcp_connection_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cloud connection ID returned by the connect endpoint | 

### Return type

[**GCPConnectStatusResponse**](GCPConnectStatusResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cloud account status retrieved |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | Caller is not an organization admin |  -  |
**404** | Operation not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Temporarily unavailable; try again |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gcp_credentials**
> GCPTemporaryCredentialResponse get_gcp_credentials(gcp_credentials_request)

Get GCP temporary credentials

Get temporary GCP credentials for cluster operations

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.gcp_credentials_request import GCPCredentialsRequest
from astropulse._generated.models.gcp_temporary_credential_response import GCPTemporaryCredentialResponse
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
    api_instance = astropulse._generated.CloudAccountsApi(api_client)
    gcp_credentials_request = astropulse._generated.GCPCredentialsRequest() # GCPCredentialsRequest | GCP credential request

    try:
        # Get GCP temporary credentials
        api_response = api_instance.get_gcp_credentials(gcp_credentials_request)
        print("The response of CloudAccountsApi->get_gcp_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudAccountsApi->get_gcp_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gcp_credentials_request** | [**GCPCredentialsRequest**](GCPCredentialsRequest.md)| GCP credential request | 

### Return type

[**GCPTemporaryCredentialResponse**](GCPTemporaryCredentialResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Temporary credentials retrieved |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | Caller is not an organization admin |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Temporarily unavailable; try again |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_self_hosted_aws_template**
> SelfHostedTemplateResponse get_self_hosted_aws_template()

Get the self-hosted AWS setup template

Returns the CloudFormation template a self-hosted cluster's setup deploys, for review or an IaC pipeline.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.self_hosted_template_response import SelfHostedTemplateResponse
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
    api_instance = astropulse._generated.CloudAccountsApi(api_client)

    try:
        # Get the self-hosted AWS setup template
        api_response = api_instance.get_self_hosted_aws_template()
        print("The response of CloudAccountsApi->get_self_hosted_aws_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudAccountsApi->get_self_hosted_aws_template: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SelfHostedTemplateResponse**](SelfHostedTemplateResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CloudFormation template |  -  |
**401** | Missing or invalid API key |  -  |
**403** | Caller is not an organization admin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_self_hosted_cloud_connection**
> CloudConnectionResponse get_self_hosted_cloud_connection(cluster_name, account_id=account_id, region=region, cloud=cloud)

Check a self-hosted cluster's cloud credentials

Reports whether AstroPulse can reach the cloud account a self-hosted cluster's stored credentials are for, with the same answers as getCloudConnection.
It never returns credentials.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cloud_connection_response import CloudConnectionResponse
from astropulse._generated.models.provider import Provider
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
    api_instance = astropulse._generated.CloudAccountsApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name the credentials were stored for
    account_id = 'account_id_example' # str | AWS account ID or GCP project ID; looked up from the cluster when omitted (optional)
    region = 'region_example' # str | Region; looked up from the cluster when omitted (optional)
    cloud = astropulse._generated.Provider() # Provider | The cloud the self-hosted cluster runs in; looked up from the cluster when omitted. Takes only `aws` or `gcp`. (optional)

    try:
        # Check a self-hosted cluster's cloud credentials
        api_response = api_instance.get_self_hosted_cloud_connection(cluster_name, account_id=account_id, region=region, cloud=cloud)
        print("The response of CloudAccountsApi->get_self_hosted_cloud_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudAccountsApi->get_self_hosted_cloud_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name the credentials were stored for | 
 **account_id** | **str**| AWS account ID or GCP project ID; looked up from the cluster when omitted | [optional] 
 **region** | **str**| Region; looked up from the cluster when omitted | [optional] 
 **cloud** | [**Provider**](.md)| The cloud the self-hosted cluster runs in; looked up from the cluster when omitted. Takes only &#x60;aws&#x60; or &#x60;gcp&#x60;. | [optional] 

### Return type

[**CloudConnectionResponse**](CloudConnectionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connection checked |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | Caller is not a member of the organization |  -  |
**404** | No such cluster, when a value to look up is omitted |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Temporarily unavailable; try again |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_self_hosted_credentials_status**
> SelfHostedCredentialStatusResponse get_self_hosted_credentials_status(cluster_name, provider=provider)

Get self-hosted credential vault status

Returns the status of stored credentials for a self-hosted cluster

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.provider import Provider
from astropulse._generated.models.self_hosted_credential_status_response import SelfHostedCredentialStatusResponse
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
    api_instance = astropulse._generated.CloudAccountsApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    provider = astropulse._generated.Provider() # Provider | The cluster's cloud, so the answer names only its command when no key is stored. Takes only `aws` or `gcp`. (optional)

    try:
        # Get self-hosted credential vault status
        api_response = api_instance.get_self_hosted_credentials_status(cluster_name, provider=provider)
        print("The response of CloudAccountsApi->get_self_hosted_credentials_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudAccountsApi->get_self_hosted_credentials_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **provider** | [**Provider**](.md)| The cluster&#39;s cloud, so the answer names only its command when no key is stored. Takes only &#x60;aws&#x60; or &#x60;gcp&#x60;. | [optional] 

### Return type

[**SelfHostedCredentialStatusResponse**](SelfHostedCredentialStatusResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | Caller is not an organization admin |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_self_hosted_setup**
> SelfHostedSetupResponse get_self_hosted_setup(provider, cluster_name)

Get a self-hosted cluster's setup

Returns each recorded setup step with its state (pending, running, done, failed, skipped), when it changed,
a plain-language reason and, on failure, the cloud provider's own error, plus nextStep: what to do now.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.provider import Provider
from astropulse._generated.models.self_hosted_setup_response import SelfHostedSetupResponse
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
    api_instance = astropulse._generated.CloudAccountsApi(api_client)
    provider = astropulse._generated.Provider() # Provider | Cloud provider. Takes only `aws` or `gcp`.
    cluster_name = 'cluster_name_example' # str | Cluster name

    try:
        # Get a self-hosted cluster's setup
        api_response = api_instance.get_self_hosted_setup(provider, cluster_name)
        print("The response of CloudAccountsApi->get_self_hosted_setup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudAccountsApi->get_self_hosted_setup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | [**Provider**](.md)| Cloud provider. Takes only &#x60;aws&#x60; or &#x60;gcp&#x60;. | 
 **cluster_name** | **str**| Cluster name | 

### Return type

[**SelfHostedSetupResponse**](SelfHostedSetupResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Setup retrieved |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | Caller is not an organization admin |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable; retry after the Retry-After interval |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_aws_capacity_reservations**
> CapacityReservationListResponse list_aws_capacity_reservations(cluster_name, account_id=account_id, region=region, zones=zones)

List the account's capacity reservations and Capacity Blocks

Lists, through the cluster's AWS connection, the capacity reservations and Capacity Blocks in a region: machine type, zone,
free and total instances, start and end, state, and whether a node group (instanceType Reserved or CapacityBlock) or the
Karpenter GPU pool could use each in the cluster's zones. No credentials are returned.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.capacity_reservation_list_response import CapacityReservationListResponse
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
    api_instance = astropulse._generated.CloudAccountsApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name the connection was made for
    account_id = 'account_id_example' # str | AWS account ID; looked up from the cluster when omitted (optional)
    region = 'region_example' # str | AWS region; looked up from the cluster when omitted (optional)
    zones = 'zones_example' # str | Comma-separated zones the cluster runs in; defaults to the zones AstroPulse picks in the region (optional)

    try:
        # List the account's capacity reservations and Capacity Blocks
        api_response = api_instance.list_aws_capacity_reservations(cluster_name, account_id=account_id, region=region, zones=zones)
        print("The response of CloudAccountsApi->list_aws_capacity_reservations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudAccountsApi->list_aws_capacity_reservations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name the connection was made for | 
 **account_id** | **str**| AWS account ID; looked up from the cluster when omitted | [optional] 
 **region** | **str**| AWS region; looked up from the cluster when omitted | [optional] 
 **zones** | **str**| Comma-separated zones the cluster runs in; defaults to the zones AstroPulse picks in the region | [optional] 

### Return type

[**CapacityReservationListResponse**](CapacityReservationListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reservations in the region |  -  |
**400** | Invalid request, or the account is not connected |  -  |
**401** | Missing or invalid API key |  -  |
**403** | Caller is not an organization admin |  -  |
**404** | No such cluster, when accountId or region is omitted |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable; retry after the Retry-After interval |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cloud_accounts**
> CloudAccountListResponse list_cloud_accounts(include_failed=include_failed)

List the organization's cloud accounts

One entry per cloud account (and Azure resource group) the organization connected or runs clusters in, with its state, the
clusters in it and the connections made for clusters that do not exist yet. Connections not checked in the last five minutes are checked again when the list is read; verifiedAt is when a check last got an answer from the account.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cloud_account_list_response import CloudAccountListResponse
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
    api_instance = astropulse._generated.CloudAccountsApi(api_client)
    include_failed = True # bool | Also count failed or unfinished setups older than three days (optional)

    try:
        # List the organization's cloud accounts
        api_response = api_instance.list_cloud_accounts(include_failed=include_failed)
        print("The response of CloudAccountsApi->list_cloud_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudAccountsApi->list_cloud_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_failed** | **bool**| Also count failed or unfinished setups older than three days | [optional] 

### Return type

[**CloudAccountListResponse**](CloudAccountListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Accounts listed |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | Caller is not a member of the organization |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Temporarily unavailable; try again |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cloud_connections**
> CloudConnectionListResponse list_cloud_connections(include_failed=include_failed)

List the organization's cloud connections

Every cloud account connection the organization has set up, newest first, as AstroPulse last recorded it. Failed or unfinished
setups older than three days are left out unless includeFailed is true. Connections not checked in the last five minutes are checked again when the list is read; no credentials are returned.
For a member who is not an organization admin each connection omits accountId, region, resourceGroup, connectionId, the template versions and createdAt.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cloud_connection_list_response import CloudConnectionListResponse
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
    api_instance = astropulse._generated.CloudAccountsApi(api_client)
    include_failed = True # bool | Also list failed or unfinished setups older than three days (optional)

    try:
        # List the organization's cloud connections
        api_response = api_instance.list_cloud_connections(include_failed=include_failed)
        print("The response of CloudAccountsApi->list_cloud_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudAccountsApi->list_cloud_connections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_failed** | **bool**| Also list failed or unfinished setups older than three days | [optional] 

### Return type

[**CloudConnectionListResponse**](CloudConnectionListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connections listed |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | Caller is not a member of the organization |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Temporarily unavailable; try again |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_kubernetes_versions**
> SupportedK8sVersionsResponseEnvelope list_kubernetes_versions(cloud_provider, provisioner_type, region=region, release_channel=release_channel, autopilot=autopilot, account_id=account_id)

Get supported Kubernetes versions

Get the list of supported Kubernetes versions for a specific provisioner and cloud provider. For GKE, you can filter by release channel to see versions available in that channel.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.gke_release_channel import GKEReleaseChannel
from astropulse._generated.models.provider import Provider
from astropulse._generated.models.provisioner_type import ProvisionerType
from astropulse._generated.models.supported_k8s_versions_response_envelope import SupportedK8sVersionsResponseEnvelope
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
    api_instance = astropulse._generated.CloudAccountsApi(api_client)
    cloud_provider = astropulse._generated.Provider() # Provider | Cloud provider
    provisioner_type = astropulse._generated.ProvisionerType() # ProvisionerType | Provisioner type. Takes only `eks`, `gke`, `aks` or `selfHosted`.
    region = 'region_example' # str | Cloud region (optional, uses default region per provider) (optional)
    release_channel = astropulse._generated.GKEReleaseChannel() # GKEReleaseChannel | GKE release channel filter (GKE only) (optional)
    autopilot = True # bool | Filter for GKE Autopilot compatible versions (GKE only) (optional)
    account_id = 'account_id_example' # str | A cloud account connected to your organization (a 12-digit AWS account ID for EKS); the response then also lists the AMI families each version offers there (optional)

    try:
        # Get supported Kubernetes versions
        api_response = api_instance.list_kubernetes_versions(cloud_provider, provisioner_type, region=region, release_channel=release_channel, autopilot=autopilot, account_id=account_id)
        print("The response of CloudAccountsApi->list_kubernetes_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudAccountsApi->list_kubernetes_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_provider** | [**Provider**](.md)| Cloud provider | 
 **provisioner_type** | [**ProvisionerType**](.md)| Provisioner type. Takes only &#x60;eks&#x60;, &#x60;gke&#x60;, &#x60;aks&#x60; or &#x60;selfHosted&#x60;. | 
 **region** | **str**| Cloud region (optional, uses default region per provider) | [optional] 
 **release_channel** | [**GKEReleaseChannel**](.md)| GKE release channel filter (GKE only) | [optional] 
 **autopilot** | **bool**| Filter for GKE Autopilot compatible versions (GKE only) | [optional] 
 **account_id** | **str**| A cloud account connected to your organization (a 12-digit AWS account ID for EKS); the response then also lists the AMI families each version offers there | [optional] 

### Return type

[**SupportedK8sVersionsResponseEnvelope**](SupportedK8sVersionsResponseEnvelope.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Supported K8s versions retrieved successfully |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | Caller is not a member of the organization, or accountId is not connected to it |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Temporarily unavailable; try again |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_self_hosted_setup**
> SelfHostedSetupResponse start_self_hosted_setup(provider, self_hosted_setup_request)

Start a self-hosted cluster's setup

Plans the resources a self-hosted cluster needs in your AWS account or GCP project and starts recording the setup.
Poll GET on the same path for each step's state and nextStep: the console link and command that create the resources.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.provider import Provider
from astropulse._generated.models.self_hosted_setup_request import SelfHostedSetupRequest
from astropulse._generated.models.self_hosted_setup_response import SelfHostedSetupResponse
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
    api_instance = astropulse._generated.CloudAccountsApi(api_client)
    provider = astropulse._generated.Provider() # Provider | Cloud provider. Takes only `aws` or `gcp`.
    self_hosted_setup_request = astropulse._generated.SelfHostedSetupRequest() # SelfHostedSetupRequest | Setup request

    try:
        # Start a self-hosted cluster's setup
        api_response = api_instance.start_self_hosted_setup(provider, self_hosted_setup_request)
        print("The response of CloudAccountsApi->start_self_hosted_setup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudAccountsApi->start_self_hosted_setup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | [**Provider**](.md)| Cloud provider. Takes only &#x60;aws&#x60; or &#x60;gcp&#x60;. | 
 **self_hosted_setup_request** | [**SelfHostedSetupRequest**](SelfHostedSetupRequest.md)| Setup request | 

### Return type

[**SelfHostedSetupResponse**](SelfHostedSetupResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Setup started |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | Caller is not an organization admin |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable; retry after the Retry-After interval |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

