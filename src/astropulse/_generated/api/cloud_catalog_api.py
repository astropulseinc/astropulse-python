"""
    AstroPulse Platform API

    The programmable production foundation for applications, AI workloads, and infrastructure products.  AstroPulse provides a unified control plane for composing cloud infrastructure, deploying workloads, and operating their production lifecycle. Provision and manage Kubernetes clusters, deploy applications and AI models, and manage networking, scaling, access, integrations, observability, cost visibility, and governance.  **Keep your product. Skip rebuilding the production layer.** AstroPulse manages the production machinery underneath your application, runtime, scheduler, inference system, or infrastructure product, while you retain ownership of the capabilities that make it different.  ## Base URL All public API endpoints are served over HTTPS at `https://api.astropulse.io` and versioned under `/api/v1`.  ## Working with AstroPulse The API follows the operational lifecycle of your infrastructure and workloads: - **Connect infrastructure:** Configure cloud accounts, discover regions, machine types, and accelerators, and provision or register Kubernetes clusters. - **Configure environments:** Manage cluster add-ons, application profiles, availability tiers, domains, and endpoint access policies. - **Deploy workloads:** Deploy applications and supported AI models, inspect their state, and discover their serving endpoints. - **Operate and recover:** Monitor deployment progress, manage supported lifecycle operations, inspect version history, plan rollbacks, and recover deployments. - **Observe and govern:** Inspect operational metrics, cost and usage data, activity, integrations, identities, permissions, and audit records.  Resources are organized by their role in the platform. Each operation defines its own parameters, request and response schemas, authentication requirements, and failure conditions.  ## Authentication AstroPulse supports API keys and short-lived bearer tokens. Each endpoint declares which authentication methods it accepts.  **API keys — recommended for automation** Send `X-Astro-API-Key: <key>`. For production automation, use an organization-owned service-account key. Service accounts are managed by organization administrators through the Service Accounts API and do not depend on an individual user's session.  Personal API keys are available under Organization settings > API Keys. API keys are scoped to one organization.  **Bearer tokens — interactive sessions** Send `Authorization: Bearer <jwt>`. These credentials are short-lived access tokens issued by the configured authentication provider.  To print an access token for a direct API request, run `astroctl auth login --print-access-token` (`-p`). A standard `astroctl auth login` stores the authenticated session without printing the token.  For unattended integrations, use API keys instead of interactive session tokens. Store all credentials securely and never expose them in repositories, client-side code, or logs.  ## SDKs and API clients The generated OpenAPI 3 specification is the public contract for AstroPulse REST API consumers and generated clients.  AstroPulse provides operation-specific Python and TypeScript SDK examples in this reference. Each generated SDK exposes resources through typed clients, with method names derived from stable API operation IDs.  **Python SDK:** Install using `pip install \"git+https://github.com/astropulseinc/astropulse-python\"`.  Common operations include `client.clusters.list_clusters()` and `client.applications.deploy_application(...)`. Consult the SDK's documentation for client initialization, authentication, and complete examples.  The same platform capabilities can be accessed through the REST API, supported SDKs, astroctl, and the AstroPulse Console. Refer to the documentation for the supported workflows of each interface.  **Application runtime endpoints:** Applications deployed through AstroPulse expose runtime endpoints separate from the platform control-plane API. Model deployments supporting the OpenAI API protocol can be called with an OpenAI-compatible client configured for the deployed endpoint and its access requirements.  ## Lifecycle and asynchronous operations Infrastructure provisioning, deployment, and certain lifecycle changes can execute asynchronously. An accepted request does not necessarily mean the underlying operation has completed.  Use the operation's response, resource status, and available progress streams to determine completion and inspect failures.  Supported application operations include version history, rollback, resume, and GitOps reconciliation. Rollback operations can provide dry-run plans so callers can inspect an eligible change before applying it.  Consult each operation for its specific state transitions, mutation semantics, retry behavior, and concurrency restrictions.  ## Observability and cost Supported resources expose deployment state, application and cluster metrics, cost and usage series, and operational diagnostics.  Metrics and cost data represent collected observations. Missing samples, incomplete coverage, and unavailable reporting intervals must not be interpreted as zero resource consumption or zero spend.  Use the coverage information, time windows, and aggregation intervals documented by each operation when processing telemetry and cost responses.  ## Real-time streaming Supported application endpoints provide real-time status, event, and log streams over WebSocket connections.  Streaming requests have different connection and authentication semantics from ordinary JSON requests. Supported browser workflows can obtain a short-lived, single-use stream ticket before establishing a WebSocket connection.  Stream tickets are valid for at most 30 seconds. Follow the individual endpoint's documented handshake, authentication, and error-handling requirements.  ## Response format Successful JSON API responses use the documented resource schema, commonly wrapped in an envelope with the result under `data` and optional `id`, `status`, and `message` fields.  Consumers must follow each endpoint's declared response type. Streaming connections and other specialized responses may have different transport semantics.  ## Errors and diagnostics API failures use a consistent JSON error structure containing: - `message`: Human-readable explanation. - `code`: Stable, machine-readable error identifier. - `status`: HTTP response status. - `traceId`: Diagnostic request trace identifier. - `details`: Optional structured error details.  **Branch on HTTP status and `code`, never on the wording of `message`.**  The `X-Trace-ID` response header exposes the request's diagnostic trace identifier. Include it when reporting failures. It is not a distributed tracing propagation header.  Common HTTP errors include: - `400 Bad Request`: Invalid input or request. - `401 Unauthorized`: Missing, invalid, expired, or revoked credentials. - `402 Payment Required`: Requested capability is unavailable under the current plan. - `403 Forbidden`: Insufficient permissions. - `404 Not Found`: Resource or route not found. - `405 Method Not Allowed`: Unsupported HTTP method for a route. - `409 Conflict`: Resource state or concurrent operation conflict. - `429 Too Many Requests`: Rate limit exceeded. - `500 Internal Server Error`: Unexpected server failure. - `503 Service Unavailable`: A required service is temporarily unavailable.  The applicable status codes and response schemas are documented for each operation.  ## Versioning and compatibility Public API versions are identified by the URL path, beginning with `/api/v1`. The generated specification's `info.version` identifies the AstroPulse build from which the document was generated.  Within an API version, backward-compatible evolution can introduce new endpoints, optional request fields, response properties, and values in extensible enumerations.  Clients should tolerate unknown response properties and supported enum extensions. Consumers must not depend on undocumented list ordering or human-readable error messages.  Breaking changes, including removing or renaming fields, changing documented field types, or making previously optional request fields mandatory, require compatibility review and an appropriate API version transition.  The generated OpenAPI specification is the authoritative contract for client generation and compatibility validation.  ## Rate limiting and retries AstroPulse applies layered request rate limits: - Global service-wide limits. - Per-IP limits. - Additional per-API-key limits. - Per-authenticated-principal limits where enabled.  Exceeding an applicable limit returns `429 Too Many Requests`. Respect the `Retry-After` response header and implement bounded exponential backoff with jitter.  Temporary service failures may return `503 Service Unavailable` with retry guidance. Retry state-changing operations only when their documented semantics make repetition safe.  Global and per-IP limits remain applicable regardless of the credential used. Rotating credentials does not bypass those limits.  ## Identity, governance, and audit AstroPulse organizes platform resources within organizations. Authentication, authorization, and applicable plan restrictions govern access to resource operations.  Mutating API requests and designated sensitive reads are recorded for auditability. Audit records capture available actor, organization, resource, action, outcome, and request context without storing request bodies or secrets.  Organization-owned service accounts provide dedicated automation identities, while API keys and user sessions retain their associated authentication and authorization boundaries.  ## Developer documentation This API reference defines the public platform contract. The [AstroPulse Documentation](https://astropulse.io/docs) provides guided workflows, platform concepts, SDK integration, CLI usage, and end-to-end examples.  API schemas and operation definitions are the source of truth for clients, developer tools, and authorized automation.

    The version of the OpenAPI document: v0.0.178
    Contact: contact@astropulse.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from astropulse._generated.models.accelerator_kind import AcceleratorKind
from astropulse._generated.models.accelerator_offering_list_response import AcceleratorOfferingListResponse
from astropulse._generated.models.accelerator_vendor import AcceleratorVendor
from astropulse._generated.models.architecture_type import ArchitectureType
from astropulse._generated.models.cluster_infrastructure_estimate_response import ClusterInfrastructureEstimateResponse
from astropulse._generated.models.compute_type import ComputeType
from astropulse._generated.models.eks_compute_mode import EKSComputeMode
from astropulse._generated.models.machine_type_list_response import MachineTypeListResponse
from astropulse._generated.models.machine_type_response import MachineTypeResponse
from astropulse._generated.models.provider_list_response import ProviderListResponse
from astropulse._generated.models.provider_provisioners_list_response import ProviderProvisionersListResponse
from astropulse._generated.models.provisioner_type import ProvisionerType
from astropulse._generated.models.string_list_response import StringListResponse

from astropulse._generated.api_client import ApiClient, RequestSerialized
from astropulse._generated.api_response import ApiResponse
from astropulse._generated.rest import RESTResponseType


class CloudCatalogApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def get_cluster_infrastructure_estimate(
        self,
        provider_id: Annotated[StrictStr, Field(description="Provider ID (e.g., aws, gcp, azure)")],
        region_id: Annotated[StrictStr, Field(description="Region ID")],
        provisioner: Annotated[ProvisionerType, Field(description="The provisioner the cluster is created with. Takes only `eks`, `gke`, `aks` or `selfHosted`.")],
        compute_mode: Annotated[Optional[EKSComputeMode], Field(description="An EKS cluster's compute mode, as eks.computeMode in the create request")] = None,
        private_cluster: Annotated[Optional[StrictBool], Field(description="A GKE cluster whose nodes have internal addresses only, as gke.privateCluster; other provisioners ignore it")] = None,
        existing_network: Annotated[Optional[StrictBool], Field(description="The cluster is created in a network you name, whose gateways are your own")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ClusterInfrastructureEstimateResponse:
        """Get what a new cluster gets around it, at list price

        The charges outside a new cluster's nodes, such as its control plane and NAT gateways, with how many it gets and each one's published hourly price, where it was read and when. Nodes are priced on their machine types.

        :param provider_id: Provider ID (e.g., aws, gcp, azure) (required)
        :type provider_id: str
        :param region_id: Region ID (required)
        :type region_id: str
        :param provisioner: The provisioner the cluster is created with. Takes only `eks`, `gke`, `aks` or `selfHosted`. (required)
        :type provisioner: ProvisionerType
        :param compute_mode: An EKS cluster's compute mode, as eks.computeMode in the create request
        :type compute_mode: EKSComputeMode
        :param private_cluster: A GKE cluster whose nodes have internal addresses only, as gke.privateCluster; other provisioners ignore it
        :type private_cluster: bool
        :param existing_network: The cluster is created in a network you name, whose gateways are your own
        :type existing_network: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_cluster_infrastructure_estimate_serialize(
            provider_id=provider_id,
            region_id=region_id,
            provisioner=provisioner,
            compute_mode=compute_mode,
            private_cluster=private_cluster,
            existing_network=existing_network,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterInfrastructureEstimateResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_cluster_infrastructure_estimate_with_http_info(
        self,
        provider_id: Annotated[StrictStr, Field(description="Provider ID (e.g., aws, gcp, azure)")],
        region_id: Annotated[StrictStr, Field(description="Region ID")],
        provisioner: Annotated[ProvisionerType, Field(description="The provisioner the cluster is created with. Takes only `eks`, `gke`, `aks` or `selfHosted`.")],
        compute_mode: Annotated[Optional[EKSComputeMode], Field(description="An EKS cluster's compute mode, as eks.computeMode in the create request")] = None,
        private_cluster: Annotated[Optional[StrictBool], Field(description="A GKE cluster whose nodes have internal addresses only, as gke.privateCluster; other provisioners ignore it")] = None,
        existing_network: Annotated[Optional[StrictBool], Field(description="The cluster is created in a network you name, whose gateways are your own")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ClusterInfrastructureEstimateResponse]:
        """Get what a new cluster gets around it, at list price

        The charges outside a new cluster's nodes, such as its control plane and NAT gateways, with how many it gets and each one's published hourly price, where it was read and when. Nodes are priced on their machine types.

        :param provider_id: Provider ID (e.g., aws, gcp, azure) (required)
        :type provider_id: str
        :param region_id: Region ID (required)
        :type region_id: str
        :param provisioner: The provisioner the cluster is created with. Takes only `eks`, `gke`, `aks` or `selfHosted`. (required)
        :type provisioner: ProvisionerType
        :param compute_mode: An EKS cluster's compute mode, as eks.computeMode in the create request
        :type compute_mode: EKSComputeMode
        :param private_cluster: A GKE cluster whose nodes have internal addresses only, as gke.privateCluster; other provisioners ignore it
        :type private_cluster: bool
        :param existing_network: The cluster is created in a network you name, whose gateways are your own
        :type existing_network: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_cluster_infrastructure_estimate_serialize(
            provider_id=provider_id,
            region_id=region_id,
            provisioner=provisioner,
            compute_mode=compute_mode,
            private_cluster=private_cluster,
            existing_network=existing_network,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterInfrastructureEstimateResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_cluster_infrastructure_estimate_without_preload_content(
        self,
        provider_id: Annotated[StrictStr, Field(description="Provider ID (e.g., aws, gcp, azure)")],
        region_id: Annotated[StrictStr, Field(description="Region ID")],
        provisioner: Annotated[ProvisionerType, Field(description="The provisioner the cluster is created with. Takes only `eks`, `gke`, `aks` or `selfHosted`.")],
        compute_mode: Annotated[Optional[EKSComputeMode], Field(description="An EKS cluster's compute mode, as eks.computeMode in the create request")] = None,
        private_cluster: Annotated[Optional[StrictBool], Field(description="A GKE cluster whose nodes have internal addresses only, as gke.privateCluster; other provisioners ignore it")] = None,
        existing_network: Annotated[Optional[StrictBool], Field(description="The cluster is created in a network you name, whose gateways are your own")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get what a new cluster gets around it, at list price

        The charges outside a new cluster's nodes, such as its control plane and NAT gateways, with how many it gets and each one's published hourly price, where it was read and when. Nodes are priced on their machine types.

        :param provider_id: Provider ID (e.g., aws, gcp, azure) (required)
        :type provider_id: str
        :param region_id: Region ID (required)
        :type region_id: str
        :param provisioner: The provisioner the cluster is created with. Takes only `eks`, `gke`, `aks` or `selfHosted`. (required)
        :type provisioner: ProvisionerType
        :param compute_mode: An EKS cluster's compute mode, as eks.computeMode in the create request
        :type compute_mode: EKSComputeMode
        :param private_cluster: A GKE cluster whose nodes have internal addresses only, as gke.privateCluster; other provisioners ignore it
        :type private_cluster: bool
        :param existing_network: The cluster is created in a network you name, whose gateways are your own
        :type existing_network: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_cluster_infrastructure_estimate_serialize(
            provider_id=provider_id,
            region_id=region_id,
            provisioner=provisioner,
            compute_mode=compute_mode,
            private_cluster=private_cluster,
            existing_network=existing_network,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterInfrastructureEstimateResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_cluster_infrastructure_estimate_serialize(
        self,
        provider_id,
        region_id,
        provisioner,
        compute_mode,
        private_cluster,
        existing_network,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if provider_id is not None:
            _path_params['providerId'] = provider_id
        if region_id is not None:
            _path_params['regionId'] = region_id
        # process the query parameters
        if provisioner is not None:
            
            _query_params.append(('provisioner', provisioner.value))
            
        if compute_mode is not None:
            
            _query_params.append(('computeMode', compute_mode.value))
            
        if private_cluster is not None:
            
            _query_params.append(('privateCluster', private_cluster))
            
        if existing_network is not None:
            
            _query_params.append(('existingNetwork', existing_network))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'ApiKeyAuth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/providers/{providerId}/regions/{regionId}/infrastructure',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_machine_type(
        self,
        provider_id: Annotated[StrictStr, Field(description="Provider ID (e.g., aws, gcp, azure)")],
        region_id: Annotated[StrictStr, Field(description="Region name")],
        machinetype_id: Annotated[StrictStr, Field(description="Machine type name")],
        zone_id: Annotated[Optional[StrictStr], Field(description="Zone ID. Pass 'all' for the region-wide view with each machine listed once. If not specified, the first available zone is used")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> MachineTypeResponse:
        """Get machine type details

        What the provider publishes about one machine type, as AstroPulse sees it, at list price. Whether your own account can launch it is answered by the dry run when you apply.

        :param provider_id: Provider ID (e.g., aws, gcp, azure) (required)
        :type provider_id: str
        :param region_id: Region name (required)
        :type region_id: str
        :param machinetype_id: Machine type name (required)
        :type machinetype_id: str
        :param zone_id: Zone ID. Pass 'all' for the region-wide view with each machine listed once. If not specified, the first available zone is used
        :type zone_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_machine_type_serialize(
            provider_id=provider_id,
            region_id=region_id,
            machinetype_id=machinetype_id,
            zone_id=zone_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MachineTypeResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_machine_type_with_http_info(
        self,
        provider_id: Annotated[StrictStr, Field(description="Provider ID (e.g., aws, gcp, azure)")],
        region_id: Annotated[StrictStr, Field(description="Region name")],
        machinetype_id: Annotated[StrictStr, Field(description="Machine type name")],
        zone_id: Annotated[Optional[StrictStr], Field(description="Zone ID. Pass 'all' for the region-wide view with each machine listed once. If not specified, the first available zone is used")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[MachineTypeResponse]:
        """Get machine type details

        What the provider publishes about one machine type, as AstroPulse sees it, at list price. Whether your own account can launch it is answered by the dry run when you apply.

        :param provider_id: Provider ID (e.g., aws, gcp, azure) (required)
        :type provider_id: str
        :param region_id: Region name (required)
        :type region_id: str
        :param machinetype_id: Machine type name (required)
        :type machinetype_id: str
        :param zone_id: Zone ID. Pass 'all' for the region-wide view with each machine listed once. If not specified, the first available zone is used
        :type zone_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_machine_type_serialize(
            provider_id=provider_id,
            region_id=region_id,
            machinetype_id=machinetype_id,
            zone_id=zone_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MachineTypeResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_machine_type_without_preload_content(
        self,
        provider_id: Annotated[StrictStr, Field(description="Provider ID (e.g., aws, gcp, azure)")],
        region_id: Annotated[StrictStr, Field(description="Region name")],
        machinetype_id: Annotated[StrictStr, Field(description="Machine type name")],
        zone_id: Annotated[Optional[StrictStr], Field(description="Zone ID. Pass 'all' for the region-wide view with each machine listed once. If not specified, the first available zone is used")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get machine type details

        What the provider publishes about one machine type, as AstroPulse sees it, at list price. Whether your own account can launch it is answered by the dry run when you apply.

        :param provider_id: Provider ID (e.g., aws, gcp, azure) (required)
        :type provider_id: str
        :param region_id: Region name (required)
        :type region_id: str
        :param machinetype_id: Machine type name (required)
        :type machinetype_id: str
        :param zone_id: Zone ID. Pass 'all' for the region-wide view with each machine listed once. If not specified, the first available zone is used
        :type zone_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_machine_type_serialize(
            provider_id=provider_id,
            region_id=region_id,
            machinetype_id=machinetype_id,
            zone_id=zone_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MachineTypeResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_machine_type_serialize(
        self,
        provider_id,
        region_id,
        machinetype_id,
        zone_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if provider_id is not None:
            _path_params['providerId'] = provider_id
        if region_id is not None:
            _path_params['regionId'] = region_id
        if machinetype_id is not None:
            _path_params['machinetypeId'] = machinetype_id
        # process the query parameters
        if zone_id is not None:
            
            _query_params.append(('zoneId', zone_id))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'ApiKeyAuth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/providers/{providerId}/regions/{regionId}/machinetypes/{machinetypeId}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def list_machine_types(
        self,
        provider_id: Annotated[StrictStr, Field(description="Provider ID (e.g., aws, gcp, azure)")],
        region_id: Annotated[StrictStr, Field(description="Region ID")],
        cpu_min: Annotated[Optional[StrictStr], Field(description="Minimum CPU requirement (e.g., '1', '500m')")] = None,
        cpu_max: Annotated[Optional[StrictStr], Field(description="Maximum CPU requirement (e.g., '4', '2000m')")] = None,
        mem_min: Annotated[Optional[StrictStr], Field(description="Minimum memory requirement (e.g., '1Gi', '512Mi')")] = None,
        mem_max: Annotated[Optional[StrictStr], Field(description="Maximum memory requirement (e.g., '8Gi', '4Gi')")] = None,
        category: Annotated[Optional[ComputeType], Field(description="Machine type category")] = None,
        architecture: Annotated[Optional[ArchitectureType], Field(description="CPU architecture")] = None,
        accelerator_kind: Annotated[Optional[AcceleratorKind], Field(description="Only machine types with an accelerator of this kind")] = None,
        accelerator_vendor: Annotated[Optional[AcceleratorVendor], Field(description="Only machine types whose accelerator comes from this vendor")] = None,
        accelerator_model: Annotated[Optional[StrictStr], Field(description="Only machine types carrying this normalized accelerator model (a100, l4, h100). Provider-native type names are not filterable")] = None,
        accelerator_count_min: Annotated[Optional[StrictInt], Field(description="Minimum accelerators per machine. Machine types whose provider reports no count never satisfy this")] = None,
        accelerator_count_max: Annotated[Optional[StrictInt], Field(description="Maximum accelerators per machine. Machine types whose provider reports no count never satisfy this")] = None,
        accelerator_memory_mi_b_min: Annotated[Optional[StrictInt], Field(description="Minimum memory per accelerator in MiB. Machine types with unavailable accelerator memory never satisfy this")] = None,
        accelerator_memory_mi_b_max: Annotated[Optional[StrictInt], Field(description="Maximum memory per accelerator in MiB. Machine types with unavailable accelerator memory never satisfy this")] = None,
        zone_id: Annotated[Optional[StrictStr], Field(description="Zone ID. Pass 'all' for the region-wide view with each machine listed once. If not specified, the first available zone is used")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> MachineTypeListResponse:
        """List available machine types

        Machine types the provider offers in the region, as AstroPulse sees them, at list price. Whether your own account can launch one — quota, availability, reservations — is answered by the dry run.

        :param provider_id: Provider ID (e.g., aws, gcp, azure) (required)
        :type provider_id: str
        :param region_id: Region ID (required)
        :type region_id: str
        :param cpu_min: Minimum CPU requirement (e.g., '1', '500m')
        :type cpu_min: str
        :param cpu_max: Maximum CPU requirement (e.g., '4', '2000m')
        :type cpu_max: str
        :param mem_min: Minimum memory requirement (e.g., '1Gi', '512Mi')
        :type mem_min: str
        :param mem_max: Maximum memory requirement (e.g., '8Gi', '4Gi')
        :type mem_max: str
        :param category: Machine type category
        :type category: ComputeType
        :param architecture: CPU architecture
        :type architecture: ArchitectureType
        :param accelerator_kind: Only machine types with an accelerator of this kind
        :type accelerator_kind: AcceleratorKind
        :param accelerator_vendor: Only machine types whose accelerator comes from this vendor
        :type accelerator_vendor: AcceleratorVendor
        :param accelerator_model: Only machine types carrying this normalized accelerator model (a100, l4, h100). Provider-native type names are not filterable
        :type accelerator_model: str
        :param accelerator_count_min: Minimum accelerators per machine. Machine types whose provider reports no count never satisfy this
        :type accelerator_count_min: int
        :param accelerator_count_max: Maximum accelerators per machine. Machine types whose provider reports no count never satisfy this
        :type accelerator_count_max: int
        :param accelerator_memory_mi_b_min: Minimum memory per accelerator in MiB. Machine types with unavailable accelerator memory never satisfy this
        :type accelerator_memory_mi_b_min: int
        :param accelerator_memory_mi_b_max: Maximum memory per accelerator in MiB. Machine types with unavailable accelerator memory never satisfy this
        :type accelerator_memory_mi_b_max: int
        :param zone_id: Zone ID. Pass 'all' for the region-wide view with each machine listed once. If not specified, the first available zone is used
        :type zone_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_machine_types_serialize(
            provider_id=provider_id,
            region_id=region_id,
            cpu_min=cpu_min,
            cpu_max=cpu_max,
            mem_min=mem_min,
            mem_max=mem_max,
            category=category,
            architecture=architecture,
            accelerator_kind=accelerator_kind,
            accelerator_vendor=accelerator_vendor,
            accelerator_model=accelerator_model,
            accelerator_count_min=accelerator_count_min,
            accelerator_count_max=accelerator_count_max,
            accelerator_memory_mi_b_min=accelerator_memory_mi_b_min,
            accelerator_memory_mi_b_max=accelerator_memory_mi_b_max,
            zone_id=zone_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MachineTypeListResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def list_machine_types_with_http_info(
        self,
        provider_id: Annotated[StrictStr, Field(description="Provider ID (e.g., aws, gcp, azure)")],
        region_id: Annotated[StrictStr, Field(description="Region ID")],
        cpu_min: Annotated[Optional[StrictStr], Field(description="Minimum CPU requirement (e.g., '1', '500m')")] = None,
        cpu_max: Annotated[Optional[StrictStr], Field(description="Maximum CPU requirement (e.g., '4', '2000m')")] = None,
        mem_min: Annotated[Optional[StrictStr], Field(description="Minimum memory requirement (e.g., '1Gi', '512Mi')")] = None,
        mem_max: Annotated[Optional[StrictStr], Field(description="Maximum memory requirement (e.g., '8Gi', '4Gi')")] = None,
        category: Annotated[Optional[ComputeType], Field(description="Machine type category")] = None,
        architecture: Annotated[Optional[ArchitectureType], Field(description="CPU architecture")] = None,
        accelerator_kind: Annotated[Optional[AcceleratorKind], Field(description="Only machine types with an accelerator of this kind")] = None,
        accelerator_vendor: Annotated[Optional[AcceleratorVendor], Field(description="Only machine types whose accelerator comes from this vendor")] = None,
        accelerator_model: Annotated[Optional[StrictStr], Field(description="Only machine types carrying this normalized accelerator model (a100, l4, h100). Provider-native type names are not filterable")] = None,
        accelerator_count_min: Annotated[Optional[StrictInt], Field(description="Minimum accelerators per machine. Machine types whose provider reports no count never satisfy this")] = None,
        accelerator_count_max: Annotated[Optional[StrictInt], Field(description="Maximum accelerators per machine. Machine types whose provider reports no count never satisfy this")] = None,
        accelerator_memory_mi_b_min: Annotated[Optional[StrictInt], Field(description="Minimum memory per accelerator in MiB. Machine types with unavailable accelerator memory never satisfy this")] = None,
        accelerator_memory_mi_b_max: Annotated[Optional[StrictInt], Field(description="Maximum memory per accelerator in MiB. Machine types with unavailable accelerator memory never satisfy this")] = None,
        zone_id: Annotated[Optional[StrictStr], Field(description="Zone ID. Pass 'all' for the region-wide view with each machine listed once. If not specified, the first available zone is used")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[MachineTypeListResponse]:
        """List available machine types

        Machine types the provider offers in the region, as AstroPulse sees them, at list price. Whether your own account can launch one — quota, availability, reservations — is answered by the dry run.

        :param provider_id: Provider ID (e.g., aws, gcp, azure) (required)
        :type provider_id: str
        :param region_id: Region ID (required)
        :type region_id: str
        :param cpu_min: Minimum CPU requirement (e.g., '1', '500m')
        :type cpu_min: str
        :param cpu_max: Maximum CPU requirement (e.g., '4', '2000m')
        :type cpu_max: str
        :param mem_min: Minimum memory requirement (e.g., '1Gi', '512Mi')
        :type mem_min: str
        :param mem_max: Maximum memory requirement (e.g., '8Gi', '4Gi')
        :type mem_max: str
        :param category: Machine type category
        :type category: ComputeType
        :param architecture: CPU architecture
        :type architecture: ArchitectureType
        :param accelerator_kind: Only machine types with an accelerator of this kind
        :type accelerator_kind: AcceleratorKind
        :param accelerator_vendor: Only machine types whose accelerator comes from this vendor
        :type accelerator_vendor: AcceleratorVendor
        :param accelerator_model: Only machine types carrying this normalized accelerator model (a100, l4, h100). Provider-native type names are not filterable
        :type accelerator_model: str
        :param accelerator_count_min: Minimum accelerators per machine. Machine types whose provider reports no count never satisfy this
        :type accelerator_count_min: int
        :param accelerator_count_max: Maximum accelerators per machine. Machine types whose provider reports no count never satisfy this
        :type accelerator_count_max: int
        :param accelerator_memory_mi_b_min: Minimum memory per accelerator in MiB. Machine types with unavailable accelerator memory never satisfy this
        :type accelerator_memory_mi_b_min: int
        :param accelerator_memory_mi_b_max: Maximum memory per accelerator in MiB. Machine types with unavailable accelerator memory never satisfy this
        :type accelerator_memory_mi_b_max: int
        :param zone_id: Zone ID. Pass 'all' for the region-wide view with each machine listed once. If not specified, the first available zone is used
        :type zone_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_machine_types_serialize(
            provider_id=provider_id,
            region_id=region_id,
            cpu_min=cpu_min,
            cpu_max=cpu_max,
            mem_min=mem_min,
            mem_max=mem_max,
            category=category,
            architecture=architecture,
            accelerator_kind=accelerator_kind,
            accelerator_vendor=accelerator_vendor,
            accelerator_model=accelerator_model,
            accelerator_count_min=accelerator_count_min,
            accelerator_count_max=accelerator_count_max,
            accelerator_memory_mi_b_min=accelerator_memory_mi_b_min,
            accelerator_memory_mi_b_max=accelerator_memory_mi_b_max,
            zone_id=zone_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MachineTypeListResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def list_machine_types_without_preload_content(
        self,
        provider_id: Annotated[StrictStr, Field(description="Provider ID (e.g., aws, gcp, azure)")],
        region_id: Annotated[StrictStr, Field(description="Region ID")],
        cpu_min: Annotated[Optional[StrictStr], Field(description="Minimum CPU requirement (e.g., '1', '500m')")] = None,
        cpu_max: Annotated[Optional[StrictStr], Field(description="Maximum CPU requirement (e.g., '4', '2000m')")] = None,
        mem_min: Annotated[Optional[StrictStr], Field(description="Minimum memory requirement (e.g., '1Gi', '512Mi')")] = None,
        mem_max: Annotated[Optional[StrictStr], Field(description="Maximum memory requirement (e.g., '8Gi', '4Gi')")] = None,
        category: Annotated[Optional[ComputeType], Field(description="Machine type category")] = None,
        architecture: Annotated[Optional[ArchitectureType], Field(description="CPU architecture")] = None,
        accelerator_kind: Annotated[Optional[AcceleratorKind], Field(description="Only machine types with an accelerator of this kind")] = None,
        accelerator_vendor: Annotated[Optional[AcceleratorVendor], Field(description="Only machine types whose accelerator comes from this vendor")] = None,
        accelerator_model: Annotated[Optional[StrictStr], Field(description="Only machine types carrying this normalized accelerator model (a100, l4, h100). Provider-native type names are not filterable")] = None,
        accelerator_count_min: Annotated[Optional[StrictInt], Field(description="Minimum accelerators per machine. Machine types whose provider reports no count never satisfy this")] = None,
        accelerator_count_max: Annotated[Optional[StrictInt], Field(description="Maximum accelerators per machine. Machine types whose provider reports no count never satisfy this")] = None,
        accelerator_memory_mi_b_min: Annotated[Optional[StrictInt], Field(description="Minimum memory per accelerator in MiB. Machine types with unavailable accelerator memory never satisfy this")] = None,
        accelerator_memory_mi_b_max: Annotated[Optional[StrictInt], Field(description="Maximum memory per accelerator in MiB. Machine types with unavailable accelerator memory never satisfy this")] = None,
        zone_id: Annotated[Optional[StrictStr], Field(description="Zone ID. Pass 'all' for the region-wide view with each machine listed once. If not specified, the first available zone is used")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List available machine types

        Machine types the provider offers in the region, as AstroPulse sees them, at list price. Whether your own account can launch one — quota, availability, reservations — is answered by the dry run.

        :param provider_id: Provider ID (e.g., aws, gcp, azure) (required)
        :type provider_id: str
        :param region_id: Region ID (required)
        :type region_id: str
        :param cpu_min: Minimum CPU requirement (e.g., '1', '500m')
        :type cpu_min: str
        :param cpu_max: Maximum CPU requirement (e.g., '4', '2000m')
        :type cpu_max: str
        :param mem_min: Minimum memory requirement (e.g., '1Gi', '512Mi')
        :type mem_min: str
        :param mem_max: Maximum memory requirement (e.g., '8Gi', '4Gi')
        :type mem_max: str
        :param category: Machine type category
        :type category: ComputeType
        :param architecture: CPU architecture
        :type architecture: ArchitectureType
        :param accelerator_kind: Only machine types with an accelerator of this kind
        :type accelerator_kind: AcceleratorKind
        :param accelerator_vendor: Only machine types whose accelerator comes from this vendor
        :type accelerator_vendor: AcceleratorVendor
        :param accelerator_model: Only machine types carrying this normalized accelerator model (a100, l4, h100). Provider-native type names are not filterable
        :type accelerator_model: str
        :param accelerator_count_min: Minimum accelerators per machine. Machine types whose provider reports no count never satisfy this
        :type accelerator_count_min: int
        :param accelerator_count_max: Maximum accelerators per machine. Machine types whose provider reports no count never satisfy this
        :type accelerator_count_max: int
        :param accelerator_memory_mi_b_min: Minimum memory per accelerator in MiB. Machine types with unavailable accelerator memory never satisfy this
        :type accelerator_memory_mi_b_min: int
        :param accelerator_memory_mi_b_max: Maximum memory per accelerator in MiB. Machine types with unavailable accelerator memory never satisfy this
        :type accelerator_memory_mi_b_max: int
        :param zone_id: Zone ID. Pass 'all' for the region-wide view with each machine listed once. If not specified, the first available zone is used
        :type zone_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_machine_types_serialize(
            provider_id=provider_id,
            region_id=region_id,
            cpu_min=cpu_min,
            cpu_max=cpu_max,
            mem_min=mem_min,
            mem_max=mem_max,
            category=category,
            architecture=architecture,
            accelerator_kind=accelerator_kind,
            accelerator_vendor=accelerator_vendor,
            accelerator_model=accelerator_model,
            accelerator_count_min=accelerator_count_min,
            accelerator_count_max=accelerator_count_max,
            accelerator_memory_mi_b_min=accelerator_memory_mi_b_min,
            accelerator_memory_mi_b_max=accelerator_memory_mi_b_max,
            zone_id=zone_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "MachineTypeListResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _list_machine_types_serialize(
        self,
        provider_id,
        region_id,
        cpu_min,
        cpu_max,
        mem_min,
        mem_max,
        category,
        architecture,
        accelerator_kind,
        accelerator_vendor,
        accelerator_model,
        accelerator_count_min,
        accelerator_count_max,
        accelerator_memory_mi_b_min,
        accelerator_memory_mi_b_max,
        zone_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if provider_id is not None:
            _path_params['providerId'] = provider_id
        if region_id is not None:
            _path_params['regionId'] = region_id
        # process the query parameters
        if cpu_min is not None:
            
            _query_params.append(('cpuMin', cpu_min))
            
        if cpu_max is not None:
            
            _query_params.append(('cpuMax', cpu_max))
            
        if mem_min is not None:
            
            _query_params.append(('memMin', mem_min))
            
        if mem_max is not None:
            
            _query_params.append(('memMax', mem_max))
            
        if category is not None:
            
            _query_params.append(('category', category.value))
            
        if architecture is not None:
            
            _query_params.append(('architecture', architecture.value))
            
        if accelerator_kind is not None:
            
            _query_params.append(('acceleratorKind', accelerator_kind.value))
            
        if accelerator_vendor is not None:
            
            _query_params.append(('acceleratorVendor', accelerator_vendor.value))
            
        if accelerator_model is not None:
            
            _query_params.append(('acceleratorModel', accelerator_model))
            
        if accelerator_count_min is not None:
            
            _query_params.append(('acceleratorCountMin', accelerator_count_min))
            
        if accelerator_count_max is not None:
            
            _query_params.append(('acceleratorCountMax', accelerator_count_max))
            
        if accelerator_memory_mi_b_min is not None:
            
            _query_params.append(('acceleratorMemoryMiBMin', accelerator_memory_mi_b_min))
            
        if accelerator_memory_mi_b_max is not None:
            
            _query_params.append(('acceleratorMemoryMiBMax', accelerator_memory_mi_b_max))
            
        if zone_id is not None:
            
            _query_params.append(('zoneId', zone_id))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'ApiKeyAuth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/providers/{providerId}/regions/{regionId}/machinetypes',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def list_provider_provisioners(
        self,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ProviderProvisionersListResponse:
        """List the provisioners each provider offers

        For each cloud AstroPulse supports, the ways it can create a cluster there: display name, a one-line summary of who runs the control plane and what you manage, the documentation page, and whether the account needs a one-time setup first. acceleratorNodeGroups says whether a node group may carry a GPU on that provisioner, and acceleratorMinKubernetesVersion the lowest Kubernetes version such a cluster may run; a create or update outside them is refused.

        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_provider_provisioners_serialize(
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ProviderProvisionersListResponse",
            '401': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def list_provider_provisioners_with_http_info(
        self,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ProviderProvisionersListResponse]:
        """List the provisioners each provider offers

        For each cloud AstroPulse supports, the ways it can create a cluster there: display name, a one-line summary of who runs the control plane and what you manage, the documentation page, and whether the account needs a one-time setup first. acceleratorNodeGroups says whether a node group may carry a GPU on that provisioner, and acceleratorMinKubernetesVersion the lowest Kubernetes version such a cluster may run; a create or update outside them is refused.

        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_provider_provisioners_serialize(
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ProviderProvisionersListResponse",
            '401': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def list_provider_provisioners_without_preload_content(
        self,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List the provisioners each provider offers

        For each cloud AstroPulse supports, the ways it can create a cluster there: display name, a one-line summary of who runs the control plane and what you manage, the documentation page, and whether the account needs a one-time setup first. acceleratorNodeGroups says whether a node group may carry a GPU on that provisioner, and acceleratorMinKubernetesVersion the lowest Kubernetes version such a cluster may run; a create or update outside them is refused.

        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_provider_provisioners_serialize(
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ProviderProvisionersListResponse",
            '401': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _list_provider_provisioners_serialize(
        self,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'ApiKeyAuth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/providers/provisioners',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def list_provider_regions(
        self,
        provider_id: Annotated[StrictStr, Field(description="Provider ID (e.g., aws, gcp, azure)")],
        provisioner: Annotated[Optional[ProvisionerType], Field(description="Only regions this provisioner can create a cluster in. Takes only `eks`, `gke`, `aks` or `selfHosted`.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> StringListResponse:
        """List available regions for a provider

        Regions the provider offers, as AstroPulse sees them. Whether your own account can deploy into one — it may not be opted in — is answered by the dry run when you apply. With provisioner, only the regions that provisioner can create a cluster in: EKS and GKE need a region with at least three zones.

        :param provider_id: Provider ID (e.g., aws, gcp, azure) (required)
        :type provider_id: str
        :param provisioner: Only regions this provisioner can create a cluster in. Takes only `eks`, `gke`, `aks` or `selfHosted`.
        :type provisioner: ProvisionerType
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_provider_regions_serialize(
            provider_id=provider_id,
            provisioner=provisioner,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "StringListResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def list_provider_regions_with_http_info(
        self,
        provider_id: Annotated[StrictStr, Field(description="Provider ID (e.g., aws, gcp, azure)")],
        provisioner: Annotated[Optional[ProvisionerType], Field(description="Only regions this provisioner can create a cluster in. Takes only `eks`, `gke`, `aks` or `selfHosted`.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[StringListResponse]:
        """List available regions for a provider

        Regions the provider offers, as AstroPulse sees them. Whether your own account can deploy into one — it may not be opted in — is answered by the dry run when you apply. With provisioner, only the regions that provisioner can create a cluster in: EKS and GKE need a region with at least three zones.

        :param provider_id: Provider ID (e.g., aws, gcp, azure) (required)
        :type provider_id: str
        :param provisioner: Only regions this provisioner can create a cluster in. Takes only `eks`, `gke`, `aks` or `selfHosted`.
        :type provisioner: ProvisionerType
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_provider_regions_serialize(
            provider_id=provider_id,
            provisioner=provisioner,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "StringListResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def list_provider_regions_without_preload_content(
        self,
        provider_id: Annotated[StrictStr, Field(description="Provider ID (e.g., aws, gcp, azure)")],
        provisioner: Annotated[Optional[ProvisionerType], Field(description="Only regions this provisioner can create a cluster in. Takes only `eks`, `gke`, `aks` or `selfHosted`.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List available regions for a provider

        Regions the provider offers, as AstroPulse sees them. Whether your own account can deploy into one — it may not be opted in — is answered by the dry run when you apply. With provisioner, only the regions that provisioner can create a cluster in: EKS and GKE need a region with at least three zones.

        :param provider_id: Provider ID (e.g., aws, gcp, azure) (required)
        :type provider_id: str
        :param provisioner: Only regions this provisioner can create a cluster in. Takes only `eks`, `gke`, `aks` or `selfHosted`.
        :type provisioner: ProvisionerType
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_provider_regions_serialize(
            provider_id=provider_id,
            provisioner=provisioner,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "StringListResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _list_provider_regions_serialize(
        self,
        provider_id,
        provisioner,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if provider_id is not None:
            _path_params['providerId'] = provider_id
        # process the query parameters
        if provisioner is not None:
            
            _query_params.append(('provisioner', provisioner.value))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'ApiKeyAuth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/providers/{providerId}/regions',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def list_providers(
        self,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ProviderListResponse:
        """List supported providers

        Returns the list of cloud providers available for cluster provisioning on AstroPulse.

        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_providers_serialize(
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ProviderListResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def list_providers_with_http_info(
        self,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ProviderListResponse]:
        """List supported providers

        Returns the list of cloud providers available for cluster provisioning on AstroPulse.

        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_providers_serialize(
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ProviderListResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def list_providers_without_preload_content(
        self,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List supported providers

        Returns the list of cloud providers available for cluster provisioning on AstroPulse.

        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_providers_serialize(
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ProviderListResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _list_providers_serialize(
        self,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'ApiKeyAuth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/providers',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def list_region_accelerators(
        self,
        provider_id: Annotated[StrictStr, Field(description="Provider ID (e.g., aws, gcp, azure)")],
        region_id: Annotated[StrictStr, Field(description="Region ID")],
        zone_id: Annotated[Optional[StrictStr], Field(description="Only accelerators on machine types offered in this zone. Omit it, or pass 'all', for the whole region")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> AcceleratorOfferingListResponse:
        """List distinct accelerators available in a region

        Distinct accelerators in the region's catalog as AstroPulse sees it, at list price; read it to learn which filter values exist. Whether your own account can launch one is answered by the dry run. Each row says how old its prices are (scrapedAt, ageSeconds), whether they are stale, and when the provider's latest refresh failed (refreshFailedAt).

        :param provider_id: Provider ID (e.g., aws, gcp, azure) (required)
        :type provider_id: str
        :param region_id: Region ID (required)
        :type region_id: str
        :param zone_id: Only accelerators on machine types offered in this zone. Omit it, or pass 'all', for the whole region
        :type zone_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_region_accelerators_serialize(
            provider_id=provider_id,
            region_id=region_id,
            zone_id=zone_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AcceleratorOfferingListResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def list_region_accelerators_with_http_info(
        self,
        provider_id: Annotated[StrictStr, Field(description="Provider ID (e.g., aws, gcp, azure)")],
        region_id: Annotated[StrictStr, Field(description="Region ID")],
        zone_id: Annotated[Optional[StrictStr], Field(description="Only accelerators on machine types offered in this zone. Omit it, or pass 'all', for the whole region")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[AcceleratorOfferingListResponse]:
        """List distinct accelerators available in a region

        Distinct accelerators in the region's catalog as AstroPulse sees it, at list price; read it to learn which filter values exist. Whether your own account can launch one is answered by the dry run. Each row says how old its prices are (scrapedAt, ageSeconds), whether they are stale, and when the provider's latest refresh failed (refreshFailedAt).

        :param provider_id: Provider ID (e.g., aws, gcp, azure) (required)
        :type provider_id: str
        :param region_id: Region ID (required)
        :type region_id: str
        :param zone_id: Only accelerators on machine types offered in this zone. Omit it, or pass 'all', for the whole region
        :type zone_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_region_accelerators_serialize(
            provider_id=provider_id,
            region_id=region_id,
            zone_id=zone_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AcceleratorOfferingListResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def list_region_accelerators_without_preload_content(
        self,
        provider_id: Annotated[StrictStr, Field(description="Provider ID (e.g., aws, gcp, azure)")],
        region_id: Annotated[StrictStr, Field(description="Region ID")],
        zone_id: Annotated[Optional[StrictStr], Field(description="Only accelerators on machine types offered in this zone. Omit it, or pass 'all', for the whole region")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List distinct accelerators available in a region

        Distinct accelerators in the region's catalog as AstroPulse sees it, at list price; read it to learn which filter values exist. Whether your own account can launch one is answered by the dry run. Each row says how old its prices are (scrapedAt, ageSeconds), whether they are stale, and when the provider's latest refresh failed (refreshFailedAt).

        :param provider_id: Provider ID (e.g., aws, gcp, azure) (required)
        :type provider_id: str
        :param region_id: Region ID (required)
        :type region_id: str
        :param zone_id: Only accelerators on machine types offered in this zone. Omit it, or pass 'all', for the whole region
        :type zone_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_region_accelerators_serialize(
            provider_id=provider_id,
            region_id=region_id,
            zone_id=zone_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AcceleratorOfferingListResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _list_region_accelerators_serialize(
        self,
        provider_id,
        region_id,
        zone_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if provider_id is not None:
            _path_params['providerId'] = provider_id
        if region_id is not None:
            _path_params['regionId'] = region_id
        # process the query parameters
        if zone_id is not None:
            
            _query_params.append(('zoneId', zone_id))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'ApiKeyAuth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/providers/{providerId}/regions/{regionId}/accelerators',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def list_region_zones(
        self,
        provider_id: Annotated[StrictStr, Field(description="Provider ID (e.g., aws, gcp, azure)")],
        region_id: Annotated[StrictStr, Field(description="Region ID")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> StringListResponse:
        """List available zones for a region

        Zones the provider offers in the region, as AstroPulse sees them. Whether your own account has capacity and quota in one is answered by the dry run when you apply.

        :param provider_id: Provider ID (e.g., aws, gcp, azure) (required)
        :type provider_id: str
        :param region_id: Region ID (required)
        :type region_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_region_zones_serialize(
            provider_id=provider_id,
            region_id=region_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "StringListResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def list_region_zones_with_http_info(
        self,
        provider_id: Annotated[StrictStr, Field(description="Provider ID (e.g., aws, gcp, azure)")],
        region_id: Annotated[StrictStr, Field(description="Region ID")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[StringListResponse]:
        """List available zones for a region

        Zones the provider offers in the region, as AstroPulse sees them. Whether your own account has capacity and quota in one is answered by the dry run when you apply.

        :param provider_id: Provider ID (e.g., aws, gcp, azure) (required)
        :type provider_id: str
        :param region_id: Region ID (required)
        :type region_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_region_zones_serialize(
            provider_id=provider_id,
            region_id=region_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "StringListResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def list_region_zones_without_preload_content(
        self,
        provider_id: Annotated[StrictStr, Field(description="Provider ID (e.g., aws, gcp, azure)")],
        region_id: Annotated[StrictStr, Field(description="Region ID")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List available zones for a region

        Zones the provider offers in the region, as AstroPulse sees them. Whether your own account has capacity and quota in one is answered by the dry run when you apply.

        :param provider_id: Provider ID (e.g., aws, gcp, azure) (required)
        :type provider_id: str
        :param region_id: Region ID (required)
        :type region_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_region_zones_serialize(
            provider_id=provider_id,
            region_id=region_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "StringListResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _list_region_zones_serialize(
        self,
        provider_id,
        region_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if provider_id is not None:
            _path_params['providerId'] = provider_id
        if region_id is not None:
            _path_params['regionId'] = region_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'ApiKeyAuth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/providers/{providerId}/regions/{regionId}/zones',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


