# astropulse._generated.IntegrationsApi

All URIs are relative to *https://api.astropulse.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**browse_github_repository**](IntegrationsApi.md#browse_github_repository) | **GET** /api/v1/integrations/github/repository/browse | Browse repository content
[**claim_github_installation**](IntegrationsApi.md#claim_github_installation) | **POST** /api/v1/integrations/github/installations/claim | Claim a GitHub installation
[**complete_github_installation**](IntegrationsApi.md#complete_github_installation) | **GET** /api/v1/integrations/github/callback | Process GitHub App installation callback
[**connect_huggingface**](IntegrationsApi.md#connect_huggingface) | **PUT** /api/v1/integrations/huggingface | Connect Hugging Face
[**create_github_installation_token**](IntegrationsApi.md#create_github_installation_token) | **POST** /api/v1/integrations/github/installations/{installation_id}/token | Generate installation token
[**create_github_repository_token**](IntegrationsApi.md#create_github_repository_token) | **POST** /api/v1/integrations/github/repository-token | Generate repository token
[**delete_github_installation**](IntegrationsApi.md#delete_github_installation) | **DELETE** /api/v1/integrations/github/installations/{installation_id} | Delete GitHub installation
[**detect_github_installations**](IntegrationsApi.md#detect_github_installations) | **POST** /api/v1/integrations/github/installations/detect | Detect and sync GitHub installations
[**disconnect_huggingface**](IntegrationsApi.md#disconnect_huggingface) | **DELETE** /api/v1/integrations/huggingface | Disconnect Hugging Face
[**get_github_installation**](IntegrationsApi.md#get_github_installation) | **GET** /api/v1/integrations/github/installations/{installation_id} | Get a specific GitHub installation
[**get_github_repository_file**](IntegrationsApi.md#get_github_repository_file) | **GET** /api/v1/integrations/github/repository/file | Get file content
[**get_huggingface_integration**](IntegrationsApi.md#get_huggingface_integration) | **GET** /api/v1/integrations/huggingface | Get Hugging Face integration status
[**get_vault_lease**](IntegrationsApi.md#get_vault_lease) | **GET** /api/v1/vault/leases/{leaseId} | Get one credential
[**list_github_installation_repositories**](IntegrationsApi.md#list_github_installation_repositories) | **GET** /api/v1/integrations/github/installations/{installation_id}/repositories | List repositories for a GitHub installation
[**list_github_installations**](IntegrationsApi.md#list_github_installations) | **GET** /api/v1/integrations/github/installations | List GitHub installations
[**list_github_repository_branches**](IntegrationsApi.md#list_github_repository_branches) | **GET** /api/v1/integrations/github/repository/branches | List repository branches
[**list_vault_leases**](IntegrationsApi.md#list_vault_leases) | **GET** /api/v1/vault/leases | List the organization&#39;s credentials
[**map_github_installation**](IntegrationsApi.md#map_github_installation) | **POST** /api/v1/integrations/github/installations/{installation_id}/map | Map GitHub installation to organization
[**replace_vault_lease**](IntegrationsApi.md#replace_vault_lease) | **POST** /api/v1/vault/leases/{leaseId}/replace | Replace a self-hosted cluster&#39;s stored key
[**revoke_vault_lease**](IntegrationsApi.md#revoke_vault_lease) | **DELETE** /api/v1/vault/leases/{leaseId} | Revoke a credential
[**start_github_installation**](IntegrationsApi.md#start_github_installation) | **POST** /api/v1/integrations/github/installations/state | Start a GitHub App installation
[**validate_github_path**](IntegrationsApi.md#validate_github_path) | **POST** /api/v1/integrations/github/validate-path | Validate file path in a GitHub repository


# **browse_github_repository**
> GitHubContentListResponse browse_github_repository(repo_url, branch=branch, path=path)

Browse repository content

Returns file and directory entries for the given path in the repository. Defaults to the repository root if no path is specified.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.git_hub_content_list_response import GitHubContentListResponse
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
    api_instance = astropulse._generated.IntegrationsApi(api_client)
    repo_url = 'repo_url_example' # str | Repository URL
    branch = 'branch_example' # str | Branch name (defaults to default branch) (optional)
    path = 'path_example' # str | Path within repository (defaults to root) (optional)

    try:
        # Browse repository content
        api_response = api_instance.browse_github_repository(repo_url, branch=branch, path=path)
        print("The response of IntegrationsApi->browse_github_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->browse_github_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_url** | **str**| Repository URL | 
 **branch** | **str**| Branch name (defaults to default branch) | [optional] 
 **path** | **str**| Path within repository (defaults to root) | [optional] 

### Return type

[**GitHubContentListResponse**](GitHubContentListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Repository content |  -  |
**400** | Invalid parameters |  -  |
**401** | Missing or invalid API key |  -  |
**404** | Repository or path not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **claim_github_installation**
> GitHubInstallationResponse claim_github_installation(git_hub_installation_claim_request)

Claim a GitHub installation

Links a GitHub App installation to the organization when the given GitHub user token proves its user administers the account the app is installed on: an admin of that GitHub organization, or the personal account's own user. Organization owner only; the token is not stored.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.git_hub_installation_claim_request import GitHubInstallationClaimRequest
from astropulse._generated.models.git_hub_installation_response import GitHubInstallationResponse
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
    api_instance = astropulse._generated.IntegrationsApi(api_client)
    git_hub_installation_claim_request = astropulse._generated.GitHubInstallationClaimRequest() # GitHubInstallationClaimRequest | The installation and the person's GitHub user token

    try:
        # Claim a GitHub installation
        api_response = api_instance.claim_github_installation(git_hub_installation_claim_request)
        print("The response of IntegrationsApi->claim_github_installation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->claim_github_installation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **git_hub_installation_claim_request** | [**GitHubInstallationClaimRequest**](GitHubInstallationClaimRequest.md)| The installation and the person&#39;s GitHub user token | 

### Return type

[**GitHubInstallationResponse**](GitHubInstallationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Installation linked to the organization |  -  |
**400** | Invalid request |  -  |
**401** | Missing or invalid credentials |  -  |
**403** | Not the organization owner; the GitHub user does not administer the account the installation belongs to; GitHubAuthorizationExpired, when GitHub no longer accepts the GitHub authorization; or GitHubPermissionRequired, when the GitHub App needs the Organization Members (read) permission approved by an owner of the GitHub organization |  -  |
**500** | Internal server error |  -  |
**503** | GitHub could not be reached, the GitHub integration is not configured, or the link could not be saved; try again |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_github_installation**
> GitHubInstallationResultResponse complete_github_installation(installation_id, setup_action, state)

Process GitHub App installation callback

Acknowledges GitHub's redirect after an app install; it links nothing. Link the installation with claimGithubInstallation. Organization owner only, with the state startGithubInstallation issued to the same user.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.git_hub_installation_result_response import GitHubInstallationResultResponse
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
    api_instance = astropulse._generated.IntegrationsApi(api_client)
    installation_id = 'installation_id_example' # str | GitHub Installation ID
    setup_action = 'setup_action_example' # str | Setup Action
    state = 'state_example' # str | The state from startGithubInstallation, as GitHub returned it

    try:
        # Process GitHub App installation callback
        api_response = api_instance.complete_github_installation(installation_id, setup_action, state)
        print("The response of IntegrationsApi->complete_github_installation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->complete_github_installation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installation_id** | **str**| GitHub Installation ID | 
 **setup_action** | **str**| Setup Action | 
 **state** | **str**| The state from startGithubInstallation, as GitHub returned it | 

### Return type

[**GitHubInstallationResultResponse**](GitHubInstallationResultResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Callback acknowledged; no installation was linked |  -  |
**400** | Invalid installation parameters |  -  |
**403** | Not the organization owner, or the state was not issued to this user and organization |  -  |
**503** | The GitHub integration is not configured |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connect_huggingface**
> HuggingFaceIntegrationResponse connect_huggingface(hugging_face_integration_request, x_astro_organization_id=x_astro_organization_id)

Connect Hugging Face

Stores a read-only Hugging Face token for the organization so gated hf:// models deploy without a per-application Secret. The token is always checked with Hugging Face first and stored only if Hugging Face accepts it: a rejected token is refused (400), and when Hugging Face cannot be reached nothing is stored (503). Replaces any previously connected token; the token is never returned.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.hugging_face_integration_request import HuggingFaceIntegrationRequest
from astropulse._generated.models.hugging_face_integration_response import HuggingFaceIntegrationResponse
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
    api_instance = astropulse._generated.IntegrationsApi(api_client)
    hugging_face_integration_request = astropulse._generated.HuggingFaceIntegrationRequest() # HuggingFaceIntegrationRequest | Hugging Face token
    x_astro_organization_id = 'x_astro_organization_id_example' # str | Organization to act in with a bearer token; defaults to the user's current organization. Ignored with an API key, which carries its own. (optional)

    try:
        # Connect Hugging Face
        api_response = api_instance.connect_huggingface(hugging_face_integration_request, x_astro_organization_id=x_astro_organization_id)
        print("The response of IntegrationsApi->connect_huggingface:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->connect_huggingface: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hugging_face_integration_request** | [**HuggingFaceIntegrationRequest**](HuggingFaceIntegrationRequest.md)| Hugging Face token | 
 **x_astro_organization_id** | **str**| Organization to act in with a bearer token; defaults to the user&#39;s current organization. Ignored with an API key, which carries its own. | [optional] 

### Return type

[**HuggingFaceIntegrationResponse**](HuggingFaceIntegrationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Integration status |  -  |
**400** | Invalid token, or Hugging Face rejected it |  -  |
**401** | Missing or invalid authentication |  -  |
**403** | Caller is not an organization admin |  -  |
**409** | A stored token can&#39;t be read (reason CredentialUnreadable): revoke it, then connect again |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Credential storage is not configured |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_github_installation_token**
> GitHubTokenResponse create_github_installation_token(installation_id)

Generate installation token

Returns a short-lived GitHub App installation access token scoped to the given installation. Use this token to make authenticated GitHub API calls on behalf of the installation.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.git_hub_token_response import GitHubTokenResponse
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
    api_instance = astropulse._generated.IntegrationsApi(api_client)
    installation_id = 'installation_id_example' # str | Installation ID

    try:
        # Generate installation token
        api_response = api_instance.create_github_installation_token(installation_id)
        print("The response of IntegrationsApi->create_github_installation_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->create_github_installation_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installation_id** | **str**| Installation ID | 

### Return type

[**GitHubTokenResponse**](GitHubTokenResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Token generated successfully |  -  |
**400** | Invalid installation |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The installation is not linked to your organization |  -  |
**404** | Installation not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_github_repository_token**
> GitHubTokenResponse create_github_repository_token(git_hub_repository_token_request)

Generate repository token

Returns a short-lived access token scoped to a single repository. Intended for CI/CD systems that need read access to deploy configuration files.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.git_hub_repository_token_request import GitHubRepositoryTokenRequest
from astropulse._generated.models.git_hub_token_response import GitHubTokenResponse
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
    api_instance = astropulse._generated.IntegrationsApi(api_client)
    git_hub_repository_token_request = astropulse._generated.GitHubRepositoryTokenRequest() # GitHubRepositoryTokenRequest | Repository information

    try:
        # Generate repository token
        api_response = api_instance.create_github_repository_token(git_hub_repository_token_request)
        print("The response of IntegrationsApi->create_github_repository_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->create_github_repository_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **git_hub_repository_token_request** | [**GitHubRepositoryTokenRequest**](GitHubRepositoryTokenRequest.md)| Repository information | 

### Return type

[**GitHubTokenResponse**](GitHubTokenResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Token generated successfully |  -  |
**400** | Invalid repository |  -  |
**401** | Missing or invalid API key |  -  |
**404** | Installation not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_github_installation**
> GitHubInstallationDeletedResponse delete_github_installation(installation_id)

Delete GitHub installation

Unlinks the GitHub App installation from the organization and revokes the organization's deployment credentials for it. Other organizations linked to it keep their links and credentials, and it remains installed on GitHub.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.git_hub_installation_deleted_response import GitHubInstallationDeletedResponse
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
    api_instance = astropulse._generated.IntegrationsApi(api_client)
    installation_id = 'installation_id_example' # str | Installation ID

    try:
        # Delete GitHub installation
        api_response = api_instance.delete_github_installation(installation_id)
        print("The response of IntegrationsApi->delete_github_installation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->delete_github_installation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installation_id** | **str**| Installation ID | 

### Return type

[**GitHubInstallationDeletedResponse**](GitHubInstallationDeletedResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Installation deleted successfully |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The installation is not linked to your organization |  -  |
**404** | Installation not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detect_github_installations**
> GitHubDetectedInstallationsResponse detect_github_installations(git_hub_detect_request=git_hub_detect_request)

Detect and sync GitHub installations

Returns the organization's GitHub App installations with their status on GitHub, as linked; available is always empty. With refresh=true, also re-creates their deployment credentials.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.git_hub_detect_request import GitHubDetectRequest
from astropulse._generated.models.git_hub_detected_installations_response import GitHubDetectedInstallationsResponse
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
    api_instance = astropulse._generated.IntegrationsApi(api_client)
    git_hub_detect_request = astropulse._generated.GitHubDetectRequest() # GitHubDetectRequest | Detection options (optional)

    try:
        # Detect and sync GitHub installations
        api_response = api_instance.detect_github_installations(git_hub_detect_request=git_hub_detect_request)
        print("The response of IntegrationsApi->detect_github_installations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->detect_github_installations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **git_hub_detect_request** | [**GitHubDetectRequest**](GitHubDetectRequest.md)| Detection options | [optional] 

### Return type

[**GitHubDetectedInstallationsResponse**](GitHubDetectedInstallationsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Detection results |  -  |
**401** | Missing or invalid API key |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disconnect_huggingface**
> HuggingFaceIntegrationResponse disconnect_huggingface(x_astro_organization_id=x_astro_organization_id)

Disconnect Hugging Face

Deletes the organization's stored Hugging Face token. Within about ten minutes the token is withdrawn from your clusters: running model pods keep what they downloaded, and new or restarted model pods read gated models only through a Secret the cluster's model-serving add-on names, if one is set. The token stays valid at Hugging Face until it is revoked there. Repeating the call has no further effect.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.hugging_face_integration_response import HuggingFaceIntegrationResponse
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
    api_instance = astropulse._generated.IntegrationsApi(api_client)
    x_astro_organization_id = 'x_astro_organization_id_example' # str | Organization to act in with a bearer token; defaults to the user's current organization. Ignored with an API key, which carries its own. (optional)

    try:
        # Disconnect Hugging Face
        api_response = api_instance.disconnect_huggingface(x_astro_organization_id=x_astro_organization_id)
        print("The response of IntegrationsApi->disconnect_huggingface:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->disconnect_huggingface: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_astro_organization_id** | **str**| Organization to act in with a bearer token; defaults to the user&#39;s current organization. Ignored with an API key, which carries its own. | [optional] 

### Return type

[**HuggingFaceIntegrationResponse**](HuggingFaceIntegrationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Integration status |  -  |
**401** | Missing or invalid authentication |  -  |
**403** | Caller is not an organization admin |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Credential storage is not configured |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_github_installation**
> GitHubInstallationResponse get_github_installation(installation_id)

Get a specific GitHub installation

Returns account details, permissions, and sync status for the specified GitHub App installation.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.git_hub_installation_response import GitHubInstallationResponse
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
    api_instance = astropulse._generated.IntegrationsApi(api_client)
    installation_id = 'installation_id_example' # str | Installation ID

    try:
        # Get a specific GitHub installation
        api_response = api_instance.get_github_installation(installation_id)
        print("The response of IntegrationsApi->get_github_installation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_github_installation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installation_id** | **str**| Installation ID | 

### Return type

[**GitHubInstallationResponse**](GitHubInstallationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Installation details |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The installation is not linked to your organization |  -  |
**404** | Installation not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_github_repository_file**
> GitHubFileContentResponse get_github_repository_file(repo_url, file_path, branch=branch)

Get file content

Returns the decoded content of a file at the specified path and ref. Supports YAML, JSON, and plain text files up to GitHub's API size limit.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.git_hub_file_content_response import GitHubFileContentResponse
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
    api_instance = astropulse._generated.IntegrationsApi(api_client)
    repo_url = 'repo_url_example' # str | Repository URL
    file_path = 'file_path_example' # str | File path within repository
    branch = 'branch_example' # str | Branch name (defaults to main) (optional)

    try:
        # Get file content
        api_response = api_instance.get_github_repository_file(repo_url, file_path, branch=branch)
        print("The response of IntegrationsApi->get_github_repository_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_github_repository_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_url** | **str**| Repository URL | 
 **file_path** | **str**| File path within repository | 
 **branch** | **str**| Branch name (defaults to main) | [optional] 

### Return type

[**GitHubFileContentResponse**](GitHubFileContentResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File content |  -  |
**400** | Invalid parameters |  -  |
**401** | Missing or invalid API key |  -  |
**404** | Repository or file not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_huggingface_integration**
> HuggingFaceIntegrationResponse get_huggingface_integration(x_astro_organization_id=x_astro_organization_id)

Get Hugging Face integration status

Reports whether the organization has connected Hugging Face, when the token was last updated, and the token's last four characters. The token itself is never returned. For a member who is not an organization admin, tokenFingerprint is omitted.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.hugging_face_integration_response import HuggingFaceIntegrationResponse
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
    api_instance = astropulse._generated.IntegrationsApi(api_client)
    x_astro_organization_id = 'x_astro_organization_id_example' # str | Organization to act in with a bearer token; defaults to the user's current organization. Ignored with an API key, which carries its own. (optional)

    try:
        # Get Hugging Face integration status
        api_response = api_instance.get_huggingface_integration(x_astro_organization_id=x_astro_organization_id)
        print("The response of IntegrationsApi->get_huggingface_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_huggingface_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_astro_organization_id** | **str**| Organization to act in with a bearer token; defaults to the user&#39;s current organization. Ignored with an API key, which carries its own. | [optional] 

### Return type

[**HuggingFaceIntegrationResponse**](HuggingFaceIntegrationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Integration status |  -  |
**401** | Missing or invalid authentication |  -  |
**403** | Caller is not a member of the organization |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Credential storage is not configured |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vault_lease**
> VaultLeaseResponse get_vault_lease(lease_id, x_astro_organization_id=x_astro_organization_id)

Get one credential

Returns one of your organization's credentials as a lease: what it is, what it powers, its version, who stored it,
and when it was stored, rotated and last checked, with what that check found. The value is never returned.
Organization admins only.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.vault_lease_response import VaultLeaseResponse
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
    api_instance = astropulse._generated.IntegrationsApi(api_client)
    lease_id = 'lease_id_example' # str | Lease ID: a UUID, or the unreadable--<kind>--<scope> ID a listed unreadable entry carries
    x_astro_organization_id = 'x_astro_organization_id_example' # str | Organization to act in with a bearer token; defaults to the user's current organization. Ignored with an API key, which carries its own. (optional)

    try:
        # Get one credential
        api_response = api_instance.get_vault_lease(lease_id, x_astro_organization_id=x_astro_organization_id)
        print("The response of IntegrationsApi->get_vault_lease:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_vault_lease: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **str**| Lease ID: a UUID, or the unreadable--&lt;kind&gt;--&lt;scope&gt; ID a listed unreadable entry carries | 
 **x_astro_organization_id** | **str**| Organization to act in with a bearer token; defaults to the user&#39;s current organization. Ignored with an API key, which carries its own. | [optional] 

### Return type

[**VaultLeaseResponse**](VaultLeaseResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The credential |  -  |
**400** | The lease ID is not valid |  -  |
**401** | Missing or invalid authentication |  -  |
**403** | Caller is not an organization admin |  -  |
**404** | The organization holds no such credential; reason LeaseNotFound |  -  |
**429** | Rate limit exceeded; reason VaultRateLimited |  -  |
**500** | Internal server error |  -  |
**503** | The vault is not configured or cannot be reached; reason VaultUnavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_github_installation_repositories**
> GitHubRepositoryListResponse list_github_installation_repositories(installation_id)

List repositories for a GitHub installation

Returns all repositories the GitHub App installation has been granted access to, filtered by the specified installation ID.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.git_hub_repository_list_response import GitHubRepositoryListResponse
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
    api_instance = astropulse._generated.IntegrationsApi(api_client)
    installation_id = 'installation_id_example' # str | Installation ID

    try:
        # List repositories for a GitHub installation
        api_response = api_instance.list_github_installation_repositories(installation_id)
        print("The response of IntegrationsApi->list_github_installation_repositories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->list_github_installation_repositories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installation_id** | **str**| Installation ID | 

### Return type

[**GitHubRepositoryListResponse**](GitHubRepositoryListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of repositories |  -  |
**401** | Missing or invalid API key |  -  |
**403** | The installation is not linked to your organization |  -  |
**404** | Installation not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_github_installations**
> GitHubInstallationListResponse list_github_installations()

List GitHub installations

Returns all GitHub App installations linked to the organization, including account login, type, and sync status.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.git_hub_installation_list_response import GitHubInstallationListResponse
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
    api_instance = astropulse._generated.IntegrationsApi(api_client)

    try:
        # List GitHub installations
        api_response = api_instance.list_github_installations()
        print("The response of IntegrationsApi->list_github_installations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->list_github_installations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GitHubInstallationListResponse**](GitHubInstallationListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of installations |  -  |
**401** | Missing or invalid API key |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_github_repository_branches**
> GitHubBranchListResponse list_github_repository_branches(repo_url)

List repository branches

Returns all branch names in the specified GitHub repository, useful for populating branch selectors when deploying.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.git_hub_branch_list_response import GitHubBranchListResponse
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
    api_instance = astropulse._generated.IntegrationsApi(api_client)
    repo_url = 'repo_url_example' # str | Repository URL

    try:
        # List repository branches
        api_response = api_instance.list_github_repository_branches(repo_url)
        print("The response of IntegrationsApi->list_github_repository_branches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->list_github_repository_branches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_url** | **str**| Repository URL | 

### Return type

[**GitHubBranchListResponse**](GitHubBranchListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of branches |  -  |
**400** | Invalid parameters |  -  |
**401** | Missing or invalid API key |  -  |
**404** | Repository not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vault_leases**
> VaultLeaseListResponse list_vault_leases(x_astro_organization_id=x_astro_organization_id, kind=kind, cluster=cluster, scope=scope, page_size=page_size, page_token=page_token)

List the organization's credentials

Lists the credentials your organization has given AstroPulse (a Hugging Face token, a registry login, a self-hosted
cluster's cloud keys, ...), one page at a time, oldest first. Each entry says what the credential is, what it powers, who
stored it, and when it was stored, rotated and last checked. A credential's value is never returned. Filter by kind,
cluster or scope; pass nextPageToken back as pageToken for the next page. Every member may list; for a member
who is not an organization admin each entry omits leaseId, path, producer, version, updatedAt, expiresAt,
createdBy, lastWrittenBy, fingerprint and last4. A credential AstroPulse cannot read is listed with state
Unreadable: revoke it and connect it again.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.vault_lease_kind import VaultLeaseKind
from astropulse._generated.models.vault_lease_list_response import VaultLeaseListResponse
from astropulse._generated.models.vault_lease_scope import VaultLeaseScope
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
    api_instance = astropulse._generated.IntegrationsApi(api_client)
    x_astro_organization_id = 'x_astro_organization_id_example' # str | Organization to act in with a bearer token; defaults to the user's current organization. Ignored with an API key, which carries its own. (optional)
    kind = [astropulse._generated.VaultLeaseKind()] # List[VaultLeaseKind] | Only these kinds; repeat for several (optional)
    cluster = 'cluster_example' # str | Only the credentials of this cluster (optional)
    scope = astropulse._generated.VaultLeaseScope() # VaultLeaseScope | Only organization-wide, named or cluster credentials (optional)
    page_size = 100 # int | Leases per page (optional) (default to 100)
    page_token = 'page_token_example' # str | nextPageToken from the previous page (optional)

    try:
        # List the organization's credentials
        api_response = api_instance.list_vault_leases(x_astro_organization_id=x_astro_organization_id, kind=kind, cluster=cluster, scope=scope, page_size=page_size, page_token=page_token)
        print("The response of IntegrationsApi->list_vault_leases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->list_vault_leases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_astro_organization_id** | **str**| Organization to act in with a bearer token; defaults to the user&#39;s current organization. Ignored with an API key, which carries its own. | [optional] 
 **kind** | [**List[VaultLeaseKind]**](VaultLeaseKind.md)| Only these kinds; repeat for several | [optional] 
 **cluster** | **str**| Only the credentials of this cluster | [optional] 
 **scope** | [**VaultLeaseScope**](.md)| Only organization-wide, named or cluster credentials | [optional] 
 **page_size** | **int**| Leases per page | [optional] [default to 100]
 **page_token** | **str**| nextPageToken from the previous page | [optional] 

### Return type

[**VaultLeaseListResponse**](VaultLeaseListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | One page of credentials |  -  |
**400** | A filter or page token is not valid |  -  |
**401** | Missing or invalid authentication |  -  |
**403** | Caller is not a member of the organization |  -  |
**429** | Rate limit exceeded; reason VaultRateLimited |  -  |
**500** | Internal server error |  -  |
**503** | The vault is not configured or cannot be reached; reason VaultUnavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_github_installation**
> GitHubInstallationResponse map_github_installation(installation_id)

Map GitHub installation to organization

Re-links a GitHub App installation that is already connected to this organization. A new installation is connected by installing the app from the organization (startGithubInstallation).

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.git_hub_installation_response import GitHubInstallationResponse
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
    api_instance = astropulse._generated.IntegrationsApi(api_client)
    installation_id = 'installation_id_example' # str | Installation ID

    try:
        # Map GitHub installation to organization
        api_response = api_instance.map_github_installation(installation_id)
        print("The response of IntegrationsApi->map_github_installation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->map_github_installation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installation_id** | **str**| Installation ID | 

### Return type

[**GitHubInstallationResponse**](GitHubInstallationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Installation mapped successfully |  -  |
**401** | Missing or invalid API key |  -  |
**403** | Not the organization owner, or the installation is not connected to this organization |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_vault_lease**
> SelfHostedConnectionResponse replace_vault_lease(lease_id, vault_lease_replace_request, x_astro_organization_id=x_astro_organization_id)

Replace a self-hosted cluster's stored key

Checks a new key for the self-hosted cluster a credential belongs to against its cloud account and, only when every
check passes, stores it in place of the old one. The old key stays valid in your cloud account; the message names it
and how to delete it there. Organization admins only.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.self_hosted_connection_response import SelfHostedConnectionResponse
from astropulse._generated.models.vault_lease_replace_request import VaultLeaseReplaceRequest
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
    api_instance = astropulse._generated.IntegrationsApi(api_client)
    lease_id = 'lease_id_example' # str | Lease ID of the self-hosted cluster's stored key
    vault_lease_replace_request = astropulse._generated.VaultLeaseReplaceRequest() # VaultLeaseReplaceRequest | The new key
    x_astro_organization_id = 'x_astro_organization_id_example' # str | Organization to act in with a bearer token; defaults to the user's current organization. Ignored with an API key, which carries its own. (optional)

    try:
        # Replace a self-hosted cluster's stored key
        api_response = api_instance.replace_vault_lease(lease_id, vault_lease_replace_request, x_astro_organization_id=x_astro_organization_id)
        print("The response of IntegrationsApi->replace_vault_lease:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->replace_vault_lease: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **str**| Lease ID of the self-hosted cluster&#39;s stored key | 
 **vault_lease_replace_request** | [**VaultLeaseReplaceRequest**](VaultLeaseReplaceRequest.md)| The new key | 
 **x_astro_organization_id** | **str**| Organization to act in with a bearer token; defaults to the user&#39;s current organization. Ignored with an API key, which carries its own. | [optional] 

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
**200** | New key checked and stored |  -  |
**400** | The key is refused, does not match the credential&#39;s cloud, or the credential is not a self-hosted cluster&#39;s key |  -  |
**401** | Missing or invalid authentication |  -  |
**403** | Caller is not an organization admin |  -  |
**404** | The organization holds no such credential; reason LeaseNotFound |  -  |
**409** | AstroPulse has no account and region on record for the cluster |  -  |
**429** | Rate limit exceeded; reason VaultRateLimited |  -  |
**500** | Internal server error |  -  |
**503** | The vault or the cluster&#39;s setup cannot be reached; try again |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_vault_lease**
> VaultRevocationResponse revoke_vault_lease(lease_id, x_astro_organization_id=x_astro_organization_id)

Revoke a credential

Deletes every stored version of the credential and, for kinds that support it, revokes it at its provider too. The
answer says what stops working and how the provider answered: a failed callback means AstroPulse's copy is gone
but the credential may still work at the provider, so revoke it there. A credential that was replaced or removed
since you read it answers 404 and nothing is deleted. A self-hosted cluster's key is not revoked while the cluster
has an operation in progress. Organization admins only.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.vault_revocation_response import VaultRevocationResponse
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
    api_instance = astropulse._generated.IntegrationsApi(api_client)
    lease_id = 'lease_id_example' # str | Lease ID: a UUID, or the unreadable--<kind>--<scope> ID a listed unreadable entry carries
    x_astro_organization_id = 'x_astro_organization_id_example' # str | Organization to act in with a bearer token; defaults to the user's current organization. Ignored with an API key, which carries its own. (optional)

    try:
        # Revoke a credential
        api_response = api_instance.revoke_vault_lease(lease_id, x_astro_organization_id=x_astro_organization_id)
        print("The response of IntegrationsApi->revoke_vault_lease:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->revoke_vault_lease: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | **str**| Lease ID: a UUID, or the unreadable--&lt;kind&gt;--&lt;scope&gt; ID a listed unreadable entry carries | 
 **x_astro_organization_id** | **str**| Organization to act in with a bearer token; defaults to the user&#39;s current organization. Ignored with an API key, which carries its own. | [optional] 

### Return type

[**VaultRevocationResponse**](VaultRevocationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Credential revoked |  -  |
**400** | The lease ID is not valid, or the key&#39;s cluster has an operation in progress; reason ClusterOperationInProgress |  -  |
**401** | Missing or invalid authentication |  -  |
**403** | Caller is not an organization admin |  -  |
**404** | The organization holds no such credential; reason LeaseNotFound |  -  |
**409** | The credential changed while it was being revoked; reason LeaseChanged |  -  |
**429** | Rate limit exceeded; reason VaultRateLimited |  -  |
**500** | Internal server error |  -  |
**503** | The vault is not configured or cannot be reached (reason VaultUnavailable), or the key&#39;s cluster could not be checked; try again |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_github_installation**
> GitHubInstallStateResponse start_github_installation()

Start a GitHub App installation

Returns a short-lived state to pass to GitHub when installing the app. The installation callback accepts the install only with this state, from the same user and organization. Organization owner only.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.git_hub_install_state_response import GitHubInstallStateResponse
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
    api_instance = astropulse._generated.IntegrationsApi(api_client)

    try:
        # Start a GitHub App installation
        api_response = api_instance.start_github_installation()
        print("The response of IntegrationsApi->start_github_installation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->start_github_installation: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GitHubInstallStateResponse**](GitHubInstallStateResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The state to pass to GitHub |  -  |
**401** | Missing or invalid credentials |  -  |
**403** | Not the organization owner |  -  |
**429** | Rate limit exceeded |  -  |
**503** | The GitHub integration is not configured |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_github_path**
> GitHubPathValidationResponse validate_github_path(git_hub_path_validation_request)

Validate file path in a GitHub repository

Looks a path up on a branch of a repository and returns what is there. A path the repository does not have answers 404 with reason GitHubPathNotFound.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.git_hub_path_validation_request import GitHubPathValidationRequest
from astropulse._generated.models.git_hub_path_validation_response import GitHubPathValidationResponse
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
    api_instance = astropulse._generated.IntegrationsApi(api_client)
    git_hub_path_validation_request = astropulse._generated.GitHubPathValidationRequest() # GitHubPathValidationRequest | Repository and path information

    try:
        # Validate file path in a GitHub repository
        api_response = api_instance.validate_github_path(git_hub_path_validation_request)
        print("The response of IntegrationsApi->validate_github_path:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->validate_github_path: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **git_hub_path_validation_request** | [**GitHubPathValidationRequest**](GitHubPathValidationRequest.md)| Repository and path information | 

### Return type

[**GitHubPathValidationResponse**](GitHubPathValidationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | What the repository has at the path |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**404** | The repository has nothing at the path (reason GitHubPathNotFound), or the repository or installation was not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

