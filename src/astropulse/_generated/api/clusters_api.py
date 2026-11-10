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
from typing import Any, Optional
from typing_extensions import Annotated
from astropulse._generated.models.agent_certificate_bundle_response import AgentCertificateBundleResponse
from astropulse._generated.models.agent_certificate_signing_request import AgentCertificateSigningRequest
from astropulse._generated.models.cancel_cluster_operation_request import CancelClusterOperationRequest
from astropulse._generated.models.cluster_accelerators_response import ClusterAcceleratorsResponse
from astropulse._generated.models.cluster_access_token_response import ClusterAccessTokenResponse
from astropulse._generated.models.cluster_approval_action import ClusterApprovalAction
from astropulse._generated.models.cluster_approval_response import ClusterApprovalResponse
from astropulse._generated.models.cluster_cost_allocation_response import ClusterCostAllocationResponse
from astropulse._generated.models.cluster_cost_series_response import ClusterCostSeriesResponse
from astropulse._generated.models.cluster_cost_summary_response import ClusterCostSummaryResponse
from astropulse._generated.models.cluster_deletion_response import ClusterDeletionResponse
from astropulse._generated.models.cluster_dry_run_response import ClusterDryRunResponse
from astropulse._generated.models.cluster_metrics_allocation_response import ClusterMetricsAllocationResponse
from astropulse._generated.models.cluster_metrics_summary_response import ClusterMetricsSummaryResponse
from astropulse._generated.models.cluster_operation_result_response import ClusterOperationResultResponse
from astropulse._generated.models.cluster_progress_page_response import ClusterProgressPageResponse
from astropulse._generated.models.cluster_progress_response import ClusterProgressResponse
from astropulse._generated.models.cluster_registration_response import ClusterRegistrationResponse
from astropulse._generated.models.cluster_registration_status_response import ClusterRegistrationStatusResponse
from astropulse._generated.models.cluster_storage_response import ClusterStorageResponse
from astropulse._generated.models.cluster_update_dry_run import ClusterUpdateDryRun
from astropulse._generated.models.cost_allocation_group_by import CostAllocationGroupBy
from astropulse._generated.models.credentials import Credentials
from astropulse._generated.models.k8s_cluster_list_response import K8sClusterListResponse
from astropulse._generated.models.k8s_cluster_manifest import K8sClusterManifest
from astropulse._generated.models.k8s_cluster_manifest_response import K8sClusterManifestResponse
from astropulse._generated.models.k8s_cluster_registration import K8sClusterRegistration
from astropulse._generated.models.k8s_cluster_response import K8sClusterResponse
from astropulse._generated.models.k8s_cluster_update import K8sClusterUpdate
from astropulse._generated.models.kubeconfig_request import KubeconfigRequest
from astropulse._generated.models.kubeconfig_response import KubeconfigResponse
from astropulse._generated.models.operation_status import OperationStatus
from astropulse._generated.models.operation_type import OperationType
from astropulse._generated.models.set_cluster_storage_request import SetClusterStorageRequest
from astropulse._generated.models.sort_order import SortOrder
from astropulse._generated.models.stream_ticket import StreamTicket
from astropulse._generated.models.string_response import StringResponse

from astropulse._generated.api_client import ApiClient, RequestSerialized
from astropulse._generated.api_response import ApiResponse
from astropulse._generated.rest import RESTResponseType


class ClustersApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def cancel_cluster_operation(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        dry_run: Annotated[Optional[StrictBool], Field(description="Answer what the cancel would do, naming the node groups it would remove, without sending it")] = None,
        cancel_cluster_operation_request: Annotated[Optional[CancelClusterOperationRequest], Field(description="Why the operation is being cancelled")] = None,
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
    ) -> ClusterOperationResultResponse:
        """Cancel the running cluster operation

        Asks the running update, scale, upgrade or rollback of a cluster to stop, and answers once the request is accepted, naming the node groups it removes. The operation stops its current step and removes any node group it was adding; changes already made to other node groups stay. Follow it with the cluster read: lastCancellation is CANCELLING while that runs, then CANCELLED with what was removed. A create, a delete or a registration can't be cancelled.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param dry_run: Answer what the cancel would do, naming the node groups it would remove, without sending it
        :type dry_run: bool
        :param cancel_cluster_operation_request: Why the operation is being cancelled
        :type cancel_cluster_operation_request: CancelClusterOperationRequest
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

        _param = self._cancel_cluster_operation_serialize(
            cluster_name=cluster_name,
            dry_run=dry_run,
            cancel_cluster_operation_request=cancel_cluster_operation_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterOperationResultResponse",
            '202': "ClusterOperationResultResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '409': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def cancel_cluster_operation_with_http_info(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        dry_run: Annotated[Optional[StrictBool], Field(description="Answer what the cancel would do, naming the node groups it would remove, without sending it")] = None,
        cancel_cluster_operation_request: Annotated[Optional[CancelClusterOperationRequest], Field(description="Why the operation is being cancelled")] = None,
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
    ) -> ApiResponse[ClusterOperationResultResponse]:
        """Cancel the running cluster operation

        Asks the running update, scale, upgrade or rollback of a cluster to stop, and answers once the request is accepted, naming the node groups it removes. The operation stops its current step and removes any node group it was adding; changes already made to other node groups stay. Follow it with the cluster read: lastCancellation is CANCELLING while that runs, then CANCELLED with what was removed. A create, a delete or a registration can't be cancelled.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param dry_run: Answer what the cancel would do, naming the node groups it would remove, without sending it
        :type dry_run: bool
        :param cancel_cluster_operation_request: Why the operation is being cancelled
        :type cancel_cluster_operation_request: CancelClusterOperationRequest
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

        _param = self._cancel_cluster_operation_serialize(
            cluster_name=cluster_name,
            dry_run=dry_run,
            cancel_cluster_operation_request=cancel_cluster_operation_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterOperationResultResponse",
            '202': "ClusterOperationResultResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '409': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def cancel_cluster_operation_without_preload_content(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        dry_run: Annotated[Optional[StrictBool], Field(description="Answer what the cancel would do, naming the node groups it would remove, without sending it")] = None,
        cancel_cluster_operation_request: Annotated[Optional[CancelClusterOperationRequest], Field(description="Why the operation is being cancelled")] = None,
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
        """Cancel the running cluster operation

        Asks the running update, scale, upgrade or rollback of a cluster to stop, and answers once the request is accepted, naming the node groups it removes. The operation stops its current step and removes any node group it was adding; changes already made to other node groups stay. Follow it with the cluster read: lastCancellation is CANCELLING while that runs, then CANCELLED with what was removed. A create, a delete or a registration can't be cancelled.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param dry_run: Answer what the cancel would do, naming the node groups it would remove, without sending it
        :type dry_run: bool
        :param cancel_cluster_operation_request: Why the operation is being cancelled
        :type cancel_cluster_operation_request: CancelClusterOperationRequest
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

        _param = self._cancel_cluster_operation_serialize(
            cluster_name=cluster_name,
            dry_run=dry_run,
            cancel_cluster_operation_request=cancel_cluster_operation_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterOperationResultResponse",
            '202': "ClusterOperationResultResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '409': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _cancel_cluster_operation_serialize(
        self,
        cluster_name,
        dry_run,
        cancel_cluster_operation_request,
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
        if cluster_name is not None:
            _path_params['clusterName'] = cluster_name
        # process the query parameters
        if dry_run is not None:
            
            _query_params.append(('dryRun', dry_run))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if cancel_cluster_operation_request is not None:
            _body_params = cancel_cluster_operation_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'ApiKeyAuth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v1/clusters/{clusterName}/cancel',
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
    def create_cluster(
        self,
        k8s_cluster_manifest: Annotated[K8sClusterManifest, Field(description="Cluster deployment configuration")],
        dry_run: Annotated[Optional[StrictBool], Field(description="When true, returns the checklist without creating the cluster")] = None,
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
    ) -> ClusterDryRunResponse:
        """Deploy a new Kubernetes cluster

        Deploys a new Kubernetes cluster from a K8sCluster specification, in the manifest envelope or the flat request shape. A dry run (?dryRun=true) and a create run the same checks: the spec, the region's zones, node group bounds, the cloud account connection (connected, setup template current) and the provider preflight. The account connection is the first check. A dry run answers 200 with the checklist whether or not the checks pass: read data.valid and data.checks; data.complete is false when some checks did not finish, named in data.unfinishedChecks. A create whose checks fail answers 400 with reason PreflightFailed and the same checks in details.checks; nothing is created. The body is decoded strictly: a field the request type does not have is refused with 400, naming it in details.field.

        :param k8s_cluster_manifest: Cluster deployment configuration (required)
        :type k8s_cluster_manifest: K8sClusterManifest
        :param dry_run: When true, returns the checklist without creating the cluster
        :type dry_run: bool
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

        _param = self._create_cluster_serialize(
            k8s_cluster_manifest=k8s_cluster_manifest,
            dry_run=dry_run,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterDryRunResponse",
            '202': "ClusterCreationResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '409': "ErrorResponse",
            '422': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
            '504': "ErrorResponse",
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
    def create_cluster_with_http_info(
        self,
        k8s_cluster_manifest: Annotated[K8sClusterManifest, Field(description="Cluster deployment configuration")],
        dry_run: Annotated[Optional[StrictBool], Field(description="When true, returns the checklist without creating the cluster")] = None,
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
    ) -> ApiResponse[ClusterDryRunResponse]:
        """Deploy a new Kubernetes cluster

        Deploys a new Kubernetes cluster from a K8sCluster specification, in the manifest envelope or the flat request shape. A dry run (?dryRun=true) and a create run the same checks: the spec, the region's zones, node group bounds, the cloud account connection (connected, setup template current) and the provider preflight. The account connection is the first check. A dry run answers 200 with the checklist whether or not the checks pass: read data.valid and data.checks; data.complete is false when some checks did not finish, named in data.unfinishedChecks. A create whose checks fail answers 400 with reason PreflightFailed and the same checks in details.checks; nothing is created. The body is decoded strictly: a field the request type does not have is refused with 400, naming it in details.field.

        :param k8s_cluster_manifest: Cluster deployment configuration (required)
        :type k8s_cluster_manifest: K8sClusterManifest
        :param dry_run: When true, returns the checklist without creating the cluster
        :type dry_run: bool
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

        _param = self._create_cluster_serialize(
            k8s_cluster_manifest=k8s_cluster_manifest,
            dry_run=dry_run,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterDryRunResponse",
            '202': "ClusterCreationResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '409': "ErrorResponse",
            '422': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
            '504': "ErrorResponse",
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
    def create_cluster_without_preload_content(
        self,
        k8s_cluster_manifest: Annotated[K8sClusterManifest, Field(description="Cluster deployment configuration")],
        dry_run: Annotated[Optional[StrictBool], Field(description="When true, returns the checklist without creating the cluster")] = None,
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
        """Deploy a new Kubernetes cluster

        Deploys a new Kubernetes cluster from a K8sCluster specification, in the manifest envelope or the flat request shape. A dry run (?dryRun=true) and a create run the same checks: the spec, the region's zones, node group bounds, the cloud account connection (connected, setup template current) and the provider preflight. The account connection is the first check. A dry run answers 200 with the checklist whether or not the checks pass: read data.valid and data.checks; data.complete is false when some checks did not finish, named in data.unfinishedChecks. A create whose checks fail answers 400 with reason PreflightFailed and the same checks in details.checks; nothing is created. The body is decoded strictly: a field the request type does not have is refused with 400, naming it in details.field.

        :param k8s_cluster_manifest: Cluster deployment configuration (required)
        :type k8s_cluster_manifest: K8sClusterManifest
        :param dry_run: When true, returns the checklist without creating the cluster
        :type dry_run: bool
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

        _param = self._create_cluster_serialize(
            k8s_cluster_manifest=k8s_cluster_manifest,
            dry_run=dry_run,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterDryRunResponse",
            '202': "ClusterCreationResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '409': "ErrorResponse",
            '422': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
            '504': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _create_cluster_serialize(
        self,
        k8s_cluster_manifest,
        dry_run,
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
        if dry_run is not None:
            
            _query_params.append(('dryRun', dry_run))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if k8s_cluster_manifest is not None:
            _body_params = k8s_cluster_manifest


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'ApiKeyAuth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v1/clusters',
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
    def create_cluster_access_token(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
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
    ) -> ClusterAccessTokenResponse:
        """Get a cluster access token

        Returns a short-lived access token for the cluster's API, for as long as the kubeconfig you generated is valid. The kubeconfig from `astroctl infra k8s generate-kubeconfig` or `set-context` requests one automatically and renews it before it expires.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
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

        _param = self._create_cluster_access_token_serialize(
            cluster_name=cluster_name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterAccessTokenResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '409': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def create_cluster_access_token_with_http_info(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
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
    ) -> ApiResponse[ClusterAccessTokenResponse]:
        """Get a cluster access token

        Returns a short-lived access token for the cluster's API, for as long as the kubeconfig you generated is valid. The kubeconfig from `astroctl infra k8s generate-kubeconfig` or `set-context` requests one automatically and renews it before it expires.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
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

        _param = self._create_cluster_access_token_serialize(
            cluster_name=cluster_name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterAccessTokenResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '409': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def create_cluster_access_token_without_preload_content(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
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
        """Get a cluster access token

        Returns a short-lived access token for the cluster's API, for as long as the kubeconfig you generated is valid. The kubeconfig from `astroctl infra k8s generate-kubeconfig` or `set-context` requests one automatically and renews it before it expires.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
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

        _param = self._create_cluster_access_token_serialize(
            cluster_name=cluster_name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterAccessTokenResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '409': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _create_cluster_access_token_serialize(
        self,
        cluster_name,
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
        if cluster_name is not None:
            _path_params['clusterName'] = cluster_name
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
            method='POST',
            resource_path='/api/v1/clusters/{clusterName}/access-token',
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
    def delete_cluster(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        record_only: Annotated[Optional[StrictBool], Field(description="Remove only AstroPulse's record of a self-hosted cluster whose stored key is gone, leaving your cloud account as it is")] = None,
        dry_run: Annotated[Optional[StrictBool], Field(description="List what the delete would leave in your cloud account, and delete nothing")] = None,
        show_all: Annotated[Optional[StrictStr], Field(description="On a dry run, a comma-separated list of group kinds (Applications, Addons, Volumes, CloudResources, AccessPolicies) to return uncapped instead of the first page")] = None,
        credentials: Annotated[Optional[Credentials], Field(description="Optional credentials for cluster deletion")] = None,
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
    ) -> ClusterDeletionResponse:
        """Delete a Kubernetes cluster

        Permanently removes the cluster and the cloud resources created for it; disks its volumes use are kept in your cloud account and listed. Registered (agent-based) clusters must use the unregister endpoint instead. With recordOnly=true, removes only AstroPulse's record of a self-hosted cluster whose stored key is gone; nothing in your cloud account is deleted. With dryRun=true, lists the volumes the delete would leave in your cloud account and deletes nothing.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param record_only: Remove only AstroPulse's record of a self-hosted cluster whose stored key is gone, leaving your cloud account as it is
        :type record_only: bool
        :param dry_run: List what the delete would leave in your cloud account, and delete nothing
        :type dry_run: bool
        :param show_all: On a dry run, a comma-separated list of group kinds (Applications, Addons, Volumes, CloudResources, AccessPolicies) to return uncapped instead of the first page
        :type show_all: str
        :param credentials: Optional credentials for cluster deletion
        :type credentials: Credentials
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

        _param = self._delete_cluster_serialize(
            cluster_name=cluster_name,
            record_only=record_only,
            dry_run=dry_run,
            show_all=show_all,
            credentials=credentials,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterDeletionResponse",
            '202': "ClusterDeletionResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '409': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def delete_cluster_with_http_info(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        record_only: Annotated[Optional[StrictBool], Field(description="Remove only AstroPulse's record of a self-hosted cluster whose stored key is gone, leaving your cloud account as it is")] = None,
        dry_run: Annotated[Optional[StrictBool], Field(description="List what the delete would leave in your cloud account, and delete nothing")] = None,
        show_all: Annotated[Optional[StrictStr], Field(description="On a dry run, a comma-separated list of group kinds (Applications, Addons, Volumes, CloudResources, AccessPolicies) to return uncapped instead of the first page")] = None,
        credentials: Annotated[Optional[Credentials], Field(description="Optional credentials for cluster deletion")] = None,
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
    ) -> ApiResponse[ClusterDeletionResponse]:
        """Delete a Kubernetes cluster

        Permanently removes the cluster and the cloud resources created for it; disks its volumes use are kept in your cloud account and listed. Registered (agent-based) clusters must use the unregister endpoint instead. With recordOnly=true, removes only AstroPulse's record of a self-hosted cluster whose stored key is gone; nothing in your cloud account is deleted. With dryRun=true, lists the volumes the delete would leave in your cloud account and deletes nothing.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param record_only: Remove only AstroPulse's record of a self-hosted cluster whose stored key is gone, leaving your cloud account as it is
        :type record_only: bool
        :param dry_run: List what the delete would leave in your cloud account, and delete nothing
        :type dry_run: bool
        :param show_all: On a dry run, a comma-separated list of group kinds (Applications, Addons, Volumes, CloudResources, AccessPolicies) to return uncapped instead of the first page
        :type show_all: str
        :param credentials: Optional credentials for cluster deletion
        :type credentials: Credentials
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

        _param = self._delete_cluster_serialize(
            cluster_name=cluster_name,
            record_only=record_only,
            dry_run=dry_run,
            show_all=show_all,
            credentials=credentials,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterDeletionResponse",
            '202': "ClusterDeletionResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '409': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def delete_cluster_without_preload_content(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        record_only: Annotated[Optional[StrictBool], Field(description="Remove only AstroPulse's record of a self-hosted cluster whose stored key is gone, leaving your cloud account as it is")] = None,
        dry_run: Annotated[Optional[StrictBool], Field(description="List what the delete would leave in your cloud account, and delete nothing")] = None,
        show_all: Annotated[Optional[StrictStr], Field(description="On a dry run, a comma-separated list of group kinds (Applications, Addons, Volumes, CloudResources, AccessPolicies) to return uncapped instead of the first page")] = None,
        credentials: Annotated[Optional[Credentials], Field(description="Optional credentials for cluster deletion")] = None,
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
        """Delete a Kubernetes cluster

        Permanently removes the cluster and the cloud resources created for it; disks its volumes use are kept in your cloud account and listed. Registered (agent-based) clusters must use the unregister endpoint instead. With recordOnly=true, removes only AstroPulse's record of a self-hosted cluster whose stored key is gone; nothing in your cloud account is deleted. With dryRun=true, lists the volumes the delete would leave in your cloud account and deletes nothing.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param record_only: Remove only AstroPulse's record of a self-hosted cluster whose stored key is gone, leaving your cloud account as it is
        :type record_only: bool
        :param dry_run: List what the delete would leave in your cloud account, and delete nothing
        :type dry_run: bool
        :param show_all: On a dry run, a comma-separated list of group kinds (Applications, Addons, Volumes, CloudResources, AccessPolicies) to return uncapped instead of the first page
        :type show_all: str
        :param credentials: Optional credentials for cluster deletion
        :type credentials: Credentials
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

        _param = self._delete_cluster_serialize(
            cluster_name=cluster_name,
            record_only=record_only,
            dry_run=dry_run,
            show_all=show_all,
            credentials=credentials,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterDeletionResponse",
            '202': "ClusterDeletionResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '409': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _delete_cluster_serialize(
        self,
        cluster_name,
        record_only,
        dry_run,
        show_all,
        credentials,
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
        if cluster_name is not None:
            _path_params['clusterName'] = cluster_name
        # process the query parameters
        if record_only is not None:
            
            _query_params.append(('recordOnly', record_only))
            
        if dry_run is not None:
            
            _query_params.append(('dryRun', dry_run))
            
        if show_all is not None:
            
            _query_params.append(('showAll', show_all))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if credentials is not None:
            _body_params = credentials


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'ApiKeyAuth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/api/v1/clusters/{clusterName}',
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
    def generate_cluster_kubeconfig(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        kubeconfig_request: Annotated[KubeconfigRequest, Field(description="Kubeconfig generation request")],
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
    ) -> KubeconfigResponse:
        """Generate kubeconfig for a cluster

        Generates your kubeconfig for the cluster, valid for the lifetime you choose. A kubeconfig that signs in through astroctl (every cluster but a self-hosted one) is returned immediately; a self-hosted cluster's carries a client certificate, returns 202 and requires polling via GET. With native, the kubeconfig signs in with your own cloud identity through your cloud provider's tool instead, and the message says what it needs.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param kubeconfig_request: Kubeconfig generation request (required)
        :type kubeconfig_request: KubeconfigRequest
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

        _param = self._generate_cluster_kubeconfig_serialize(
            cluster_name=cluster_name,
            kubeconfig_request=kubeconfig_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "KubeconfigResponse",
            '202': "KubeconfigGenerationResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '409': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def generate_cluster_kubeconfig_with_http_info(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        kubeconfig_request: Annotated[KubeconfigRequest, Field(description="Kubeconfig generation request")],
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
    ) -> ApiResponse[KubeconfigResponse]:
        """Generate kubeconfig for a cluster

        Generates your kubeconfig for the cluster, valid for the lifetime you choose. A kubeconfig that signs in through astroctl (every cluster but a self-hosted one) is returned immediately; a self-hosted cluster's carries a client certificate, returns 202 and requires polling via GET. With native, the kubeconfig signs in with your own cloud identity through your cloud provider's tool instead, and the message says what it needs.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param kubeconfig_request: Kubeconfig generation request (required)
        :type kubeconfig_request: KubeconfigRequest
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

        _param = self._generate_cluster_kubeconfig_serialize(
            cluster_name=cluster_name,
            kubeconfig_request=kubeconfig_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "KubeconfigResponse",
            '202': "KubeconfigGenerationResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '409': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def generate_cluster_kubeconfig_without_preload_content(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        kubeconfig_request: Annotated[KubeconfigRequest, Field(description="Kubeconfig generation request")],
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
        """Generate kubeconfig for a cluster

        Generates your kubeconfig for the cluster, valid for the lifetime you choose. A kubeconfig that signs in through astroctl (every cluster but a self-hosted one) is returned immediately; a self-hosted cluster's carries a client certificate, returns 202 and requires polling via GET. With native, the kubeconfig signs in with your own cloud identity through your cloud provider's tool instead, and the message says what it needs.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param kubeconfig_request: Kubeconfig generation request (required)
        :type kubeconfig_request: KubeconfigRequest
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

        _param = self._generate_cluster_kubeconfig_serialize(
            cluster_name=cluster_name,
            kubeconfig_request=kubeconfig_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "KubeconfigResponse",
            '202': "KubeconfigGenerationResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '409': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _generate_cluster_kubeconfig_serialize(
        self,
        cluster_name,
        kubeconfig_request,
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
        if cluster_name is not None:
            _path_params['clusterName'] = cluster_name
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if kubeconfig_request is not None:
            _body_params = kubeconfig_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'ApiKeyAuth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v1/clusters/{clusterName}/kubeconfig',
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
    def get_cluster(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
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
    ) -> K8sClusterResponse:
        """Get cluster details

        Retrieves detailed information about a specific Kubernetes cluster

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
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

        _param = self._get_cluster_serialize(
            cluster_name=cluster_name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "K8sClusterResponse",
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
    def get_cluster_with_http_info(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
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
    ) -> ApiResponse[K8sClusterResponse]:
        """Get cluster details

        Retrieves detailed information about a specific Kubernetes cluster

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
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

        _param = self._get_cluster_serialize(
            cluster_name=cluster_name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "K8sClusterResponse",
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
    def get_cluster_without_preload_content(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
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
        """Get cluster details

        Retrieves detailed information about a specific Kubernetes cluster

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
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

        _param = self._get_cluster_serialize(
            cluster_name=cluster_name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "K8sClusterResponse",
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


    def _get_cluster_serialize(
        self,
        cluster_name,
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
        if cluster_name is not None:
            _path_params['clusterName'] = cluster_name
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
            resource_path='/api/v1/clusters/{clusterName}',
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
    def get_cluster_accelerators(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
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
    ) -> ClusterAcceleratorsResponse:
        """List the GPUs a cluster can provide

        Returns the GPUs a model replica can ask for on the cluster: those its node groups carry and those its autoscaling pools can launch, with the most one replica can ask for and whether each can be placed now.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
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

        _param = self._get_cluster_accelerators_serialize(
            cluster_name=cluster_name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterAcceleratorsResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def get_cluster_accelerators_with_http_info(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
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
    ) -> ApiResponse[ClusterAcceleratorsResponse]:
        """List the GPUs a cluster can provide

        Returns the GPUs a model replica can ask for on the cluster: those its node groups carry and those its autoscaling pools can launch, with the most one replica can ask for and whether each can be placed now.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
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

        _param = self._get_cluster_accelerators_serialize(
            cluster_name=cluster_name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterAcceleratorsResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def get_cluster_accelerators_without_preload_content(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
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
        """List the GPUs a cluster can provide

        Returns the GPUs a model replica can ask for on the cluster: those its node groups carry and those its autoscaling pools can launch, with the most one replica can ask for and whether each can be placed now.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
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

        _param = self._get_cluster_accelerators_serialize(
            cluster_name=cluster_name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterAcceleratorsResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_cluster_accelerators_serialize(
        self,
        cluster_name,
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
        if cluster_name is not None:
            _path_params['clusterName'] = cluster_name
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
            resource_path='/api/v1/clusters/{clusterName}/accelerators',
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
    def get_cluster_agent(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        operation_id: Annotated[Optional[StrictStr], Field(description="Operation ID for in-flight registration polling")] = None,
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
    ) -> ClusterRegistrationStatusResponse:
        """Get agent status for a cluster

        Returns agent connection status and registration progress. Use operationId during an in-flight registration. Install instructions are returned to organization admins and owners only.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param operation_id: Operation ID for in-flight registration polling
        :type operation_id: str
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

        _param = self._get_cluster_agent_serialize(
            cluster_name=cluster_name,
            operation_id=operation_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterRegistrationStatusResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def get_cluster_agent_with_http_info(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        operation_id: Annotated[Optional[StrictStr], Field(description="Operation ID for in-flight registration polling")] = None,
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
    ) -> ApiResponse[ClusterRegistrationStatusResponse]:
        """Get agent status for a cluster

        Returns agent connection status and registration progress. Use operationId during an in-flight registration. Install instructions are returned to organization admins and owners only.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param operation_id: Operation ID for in-flight registration polling
        :type operation_id: str
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

        _param = self._get_cluster_agent_serialize(
            cluster_name=cluster_name,
            operation_id=operation_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterRegistrationStatusResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def get_cluster_agent_without_preload_content(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        operation_id: Annotated[Optional[StrictStr], Field(description="Operation ID for in-flight registration polling")] = None,
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
        """Get agent status for a cluster

        Returns agent connection status and registration progress. Use operationId during an in-flight registration. Install instructions are returned to organization admins and owners only.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param operation_id: Operation ID for in-flight registration polling
        :type operation_id: str
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

        _param = self._get_cluster_agent_serialize(
            cluster_name=cluster_name,
            operation_id=operation_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterRegistrationStatusResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_cluster_agent_serialize(
        self,
        cluster_name,
        operation_id,
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
        if cluster_name is not None:
            _path_params['clusterName'] = cluster_name
        # process the query parameters
        if operation_id is not None:
            
            _query_params.append(('operationId', operation_id))
            
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
            resource_path='/api/v1/clusters/{clusterName}/agent',
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
    def get_cluster_cost_allocation(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        group_by: Annotated[CostAllocationGroupBy, Field(description="What the allocations are broken down by")],
        window: Annotated[Optional[StrictStr], Field(description="Window duration (for example 24h, 7d, 30d)")] = None,
        application: Annotated[Optional[StrictStr], Field(description="Application name; the display name or the managed resource name both work. Valid only with groupBy=Application")] = None,
        search: Annotated[Optional[StrictStr], Field(description="Case-insensitive allocation name search")] = None,
        sort_by: Annotated[Optional[Any], Field(description="What the allocations are ordered by")] = None,
        sort_order: Annotated[Optional[SortOrder], Field(description="The direction of the order; rows with no value always come last. Ascending by default for Name, Descending otherwise")] = None,
        currency: Annotated[Optional[StrictStr], Field(description="ISO 4217 currency for cost ordering; mixed-currency results fall back to name ordering when omitted")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="Page size from 1 through 200")] = None,
        page_token: Annotated[Optional[StrictStr], Field(description="Opaque continuation token; it pins the original window and filters")] = None,
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
    ) -> ClusterCostAllocationResponse:
        """Get cluster cost allocation

        Aggregates provider-neutral, closed hourly metering rollups by namespace, application, or node group.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param group_by: What the allocations are broken down by (required)
        :type group_by: CostAllocationGroupBy
        :param window: Window duration (for example 24h, 7d, 30d)
        :type window: str
        :param application: Application name; the display name or the managed resource name both work. Valid only with groupBy=Application
        :type application: str
        :param search: Case-insensitive allocation name search
        :type search: str
        :param sort_by: What the allocations are ordered by
        :type sort_by: CostAllocationSortBy
        :param sort_order: The direction of the order; rows with no value always come last. Ascending by default for Name, Descending otherwise
        :type sort_order: SortOrder
        :param currency: ISO 4217 currency for cost ordering; mixed-currency results fall back to name ordering when omitted
        :type currency: str
        :param limit: Page size from 1 through 200
        :type limit: int
        :param page_token: Opaque continuation token; it pins the original window and filters
        :type page_token: str
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

        _param = self._get_cluster_cost_allocation_serialize(
            cluster_name=cluster_name,
            group_by=group_by,
            window=window,
            application=application,
            search=search,
            sort_by=sort_by,
            sort_order=sort_order,
            currency=currency,
            limit=limit,
            page_token=page_token,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterCostAllocationResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def get_cluster_cost_allocation_with_http_info(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        group_by: Annotated[CostAllocationGroupBy, Field(description="What the allocations are broken down by")],
        window: Annotated[Optional[StrictStr], Field(description="Window duration (for example 24h, 7d, 30d)")] = None,
        application: Annotated[Optional[StrictStr], Field(description="Application name; the display name or the managed resource name both work. Valid only with groupBy=Application")] = None,
        search: Annotated[Optional[StrictStr], Field(description="Case-insensitive allocation name search")] = None,
        sort_by: Annotated[Optional[Any], Field(description="What the allocations are ordered by")] = None,
        sort_order: Annotated[Optional[SortOrder], Field(description="The direction of the order; rows with no value always come last. Ascending by default for Name, Descending otherwise")] = None,
        currency: Annotated[Optional[StrictStr], Field(description="ISO 4217 currency for cost ordering; mixed-currency results fall back to name ordering when omitted")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="Page size from 1 through 200")] = None,
        page_token: Annotated[Optional[StrictStr], Field(description="Opaque continuation token; it pins the original window and filters")] = None,
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
    ) -> ApiResponse[ClusterCostAllocationResponse]:
        """Get cluster cost allocation

        Aggregates provider-neutral, closed hourly metering rollups by namespace, application, or node group.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param group_by: What the allocations are broken down by (required)
        :type group_by: CostAllocationGroupBy
        :param window: Window duration (for example 24h, 7d, 30d)
        :type window: str
        :param application: Application name; the display name or the managed resource name both work. Valid only with groupBy=Application
        :type application: str
        :param search: Case-insensitive allocation name search
        :type search: str
        :param sort_by: What the allocations are ordered by
        :type sort_by: CostAllocationSortBy
        :param sort_order: The direction of the order; rows with no value always come last. Ascending by default for Name, Descending otherwise
        :type sort_order: SortOrder
        :param currency: ISO 4217 currency for cost ordering; mixed-currency results fall back to name ordering when omitted
        :type currency: str
        :param limit: Page size from 1 through 200
        :type limit: int
        :param page_token: Opaque continuation token; it pins the original window and filters
        :type page_token: str
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

        _param = self._get_cluster_cost_allocation_serialize(
            cluster_name=cluster_name,
            group_by=group_by,
            window=window,
            application=application,
            search=search,
            sort_by=sort_by,
            sort_order=sort_order,
            currency=currency,
            limit=limit,
            page_token=page_token,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterCostAllocationResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def get_cluster_cost_allocation_without_preload_content(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        group_by: Annotated[CostAllocationGroupBy, Field(description="What the allocations are broken down by")],
        window: Annotated[Optional[StrictStr], Field(description="Window duration (for example 24h, 7d, 30d)")] = None,
        application: Annotated[Optional[StrictStr], Field(description="Application name; the display name or the managed resource name both work. Valid only with groupBy=Application")] = None,
        search: Annotated[Optional[StrictStr], Field(description="Case-insensitive allocation name search")] = None,
        sort_by: Annotated[Optional[Any], Field(description="What the allocations are ordered by")] = None,
        sort_order: Annotated[Optional[SortOrder], Field(description="The direction of the order; rows with no value always come last. Ascending by default for Name, Descending otherwise")] = None,
        currency: Annotated[Optional[StrictStr], Field(description="ISO 4217 currency for cost ordering; mixed-currency results fall back to name ordering when omitted")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="Page size from 1 through 200")] = None,
        page_token: Annotated[Optional[StrictStr], Field(description="Opaque continuation token; it pins the original window and filters")] = None,
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
        """Get cluster cost allocation

        Aggregates provider-neutral, closed hourly metering rollups by namespace, application, or node group.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param group_by: What the allocations are broken down by (required)
        :type group_by: CostAllocationGroupBy
        :param window: Window duration (for example 24h, 7d, 30d)
        :type window: str
        :param application: Application name; the display name or the managed resource name both work. Valid only with groupBy=Application
        :type application: str
        :param search: Case-insensitive allocation name search
        :type search: str
        :param sort_by: What the allocations are ordered by
        :type sort_by: CostAllocationSortBy
        :param sort_order: The direction of the order; rows with no value always come last. Ascending by default for Name, Descending otherwise
        :type sort_order: SortOrder
        :param currency: ISO 4217 currency for cost ordering; mixed-currency results fall back to name ordering when omitted
        :type currency: str
        :param limit: Page size from 1 through 200
        :type limit: int
        :param page_token: Opaque continuation token; it pins the original window and filters
        :type page_token: str
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

        _param = self._get_cluster_cost_allocation_serialize(
            cluster_name=cluster_name,
            group_by=group_by,
            window=window,
            application=application,
            search=search,
            sort_by=sort_by,
            sort_order=sort_order,
            currency=currency,
            limit=limit,
            page_token=page_token,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterCostAllocationResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_cluster_cost_allocation_serialize(
        self,
        cluster_name,
        group_by,
        window,
        application,
        search,
        sort_by,
        sort_order,
        currency,
        limit,
        page_token,
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
        if cluster_name is not None:
            _path_params['clusterName'] = cluster_name
        # process the query parameters
        if window is not None:
            
            _query_params.append(('window', window))
            
        if group_by is not None:
            
            _query_params.append(('groupBy', group_by.value))
            
        if application is not None:
            
            _query_params.append(('application', application))
            
        if search is not None:
            
            _query_params.append(('search', search))
            
        if sort_by is not None:
            
            _query_params.append(('sortBy', sort_by.value))
            
        if sort_order is not None:
            
            _query_params.append(('sortOrder', sort_order.value))
            
        if currency is not None:
            
            _query_params.append(('currency', currency))
            
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if page_token is not None:
            
            _query_params.append(('pageToken', page_token))
            
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
            resource_path='/api/v1/clusters/{clusterName}/cost/allocation',
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
    def get_cluster_cost_series(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        window: Annotated[Optional[StrictStr], Field(description="Window duration (for example 24h, 7d, 30d)")] = None,
        interval: Annotated[Optional[StrictStr], Field(description="Bucket interval (auto, 1h, 6h, 12h, 1d)")] = None,
        group_by: Annotated[Optional[CostAllocationGroupBy], Field(description="The breakdown `name` is a row of")] = None,
        name: Annotated[Optional[StrictStr], Field(description="The row's exact name; requires groupBy")] = None,
        application: Annotated[Optional[StrictStr], Field(description="An application's name, as groupBy=Application with this name; the display name or the managed resource name both work")] = None,
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
    ) -> ClusterCostSeriesResponse:
        """Get cluster cost time series

        Returns bounded, closed-hour cost and usage buckets for charts. Missing and gap buckets remain explicit and are never converted to zero spend.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param window: Window duration (for example 24h, 7d, 30d)
        :type window: str
        :param interval: Bucket interval (auto, 1h, 6h, 12h, 1d)
        :type interval: str
        :param group_by: The breakdown `name` is a row of
        :type group_by: CostAllocationGroupBy
        :param name: The row's exact name; requires groupBy
        :type name: str
        :param application: An application's name, as groupBy=Application with this name; the display name or the managed resource name both work
        :type application: str
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

        _param = self._get_cluster_cost_series_serialize(
            cluster_name=cluster_name,
            window=window,
            interval=interval,
            group_by=group_by,
            name=name,
            application=application,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterCostSeriesResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def get_cluster_cost_series_with_http_info(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        window: Annotated[Optional[StrictStr], Field(description="Window duration (for example 24h, 7d, 30d)")] = None,
        interval: Annotated[Optional[StrictStr], Field(description="Bucket interval (auto, 1h, 6h, 12h, 1d)")] = None,
        group_by: Annotated[Optional[CostAllocationGroupBy], Field(description="The breakdown `name` is a row of")] = None,
        name: Annotated[Optional[StrictStr], Field(description="The row's exact name; requires groupBy")] = None,
        application: Annotated[Optional[StrictStr], Field(description="An application's name, as groupBy=Application with this name; the display name or the managed resource name both work")] = None,
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
    ) -> ApiResponse[ClusterCostSeriesResponse]:
        """Get cluster cost time series

        Returns bounded, closed-hour cost and usage buckets for charts. Missing and gap buckets remain explicit and are never converted to zero spend.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param window: Window duration (for example 24h, 7d, 30d)
        :type window: str
        :param interval: Bucket interval (auto, 1h, 6h, 12h, 1d)
        :type interval: str
        :param group_by: The breakdown `name` is a row of
        :type group_by: CostAllocationGroupBy
        :param name: The row's exact name; requires groupBy
        :type name: str
        :param application: An application's name, as groupBy=Application with this name; the display name or the managed resource name both work
        :type application: str
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

        _param = self._get_cluster_cost_series_serialize(
            cluster_name=cluster_name,
            window=window,
            interval=interval,
            group_by=group_by,
            name=name,
            application=application,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterCostSeriesResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def get_cluster_cost_series_without_preload_content(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        window: Annotated[Optional[StrictStr], Field(description="Window duration (for example 24h, 7d, 30d)")] = None,
        interval: Annotated[Optional[StrictStr], Field(description="Bucket interval (auto, 1h, 6h, 12h, 1d)")] = None,
        group_by: Annotated[Optional[CostAllocationGroupBy], Field(description="The breakdown `name` is a row of")] = None,
        name: Annotated[Optional[StrictStr], Field(description="The row's exact name; requires groupBy")] = None,
        application: Annotated[Optional[StrictStr], Field(description="An application's name, as groupBy=Application with this name; the display name or the managed resource name both work")] = None,
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
        """Get cluster cost time series

        Returns bounded, closed-hour cost and usage buckets for charts. Missing and gap buckets remain explicit and are never converted to zero spend.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param window: Window duration (for example 24h, 7d, 30d)
        :type window: str
        :param interval: Bucket interval (auto, 1h, 6h, 12h, 1d)
        :type interval: str
        :param group_by: The breakdown `name` is a row of
        :type group_by: CostAllocationGroupBy
        :param name: The row's exact name; requires groupBy
        :type name: str
        :param application: An application's name, as groupBy=Application with this name; the display name or the managed resource name both work
        :type application: str
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

        _param = self._get_cluster_cost_series_serialize(
            cluster_name=cluster_name,
            window=window,
            interval=interval,
            group_by=group_by,
            name=name,
            application=application,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterCostSeriesResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_cluster_cost_series_serialize(
        self,
        cluster_name,
        window,
        interval,
        group_by,
        name,
        application,
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
        if cluster_name is not None:
            _path_params['clusterName'] = cluster_name
        # process the query parameters
        if window is not None:
            
            _query_params.append(('window', window))
            
        if interval is not None:
            
            _query_params.append(('interval', interval))
            
        if group_by is not None:
            
            _query_params.append(('groupBy', group_by.value))
            
        if name is not None:
            
            _query_params.append(('name', name))
            
        if application is not None:
            
            _query_params.append(('application', application))
            
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
            resource_path='/api/v1/clusters/{clusterName}/cost/series',
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
    def get_cluster_cost_summary(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        window: Annotated[Optional[StrictStr], Field(description="Window duration (for example 24h, 7d, 30d)")] = None,
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
    ) -> ClusterCostSummaryResponse:
        """Get cluster cost summary

        Aggregates provider-neutral, closed hourly metering rollups for a cluster. Missing and gap windows are explicit and are never rendered as zero spend.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param window: Window duration (for example 24h, 7d, 30d)
        :type window: str
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

        _param = self._get_cluster_cost_summary_serialize(
            cluster_name=cluster_name,
            window=window,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterCostSummaryResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def get_cluster_cost_summary_with_http_info(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        window: Annotated[Optional[StrictStr], Field(description="Window duration (for example 24h, 7d, 30d)")] = None,
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
    ) -> ApiResponse[ClusterCostSummaryResponse]:
        """Get cluster cost summary

        Aggregates provider-neutral, closed hourly metering rollups for a cluster. Missing and gap windows are explicit and are never rendered as zero spend.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param window: Window duration (for example 24h, 7d, 30d)
        :type window: str
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

        _param = self._get_cluster_cost_summary_serialize(
            cluster_name=cluster_name,
            window=window,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterCostSummaryResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def get_cluster_cost_summary_without_preload_content(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        window: Annotated[Optional[StrictStr], Field(description="Window duration (for example 24h, 7d, 30d)")] = None,
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
        """Get cluster cost summary

        Aggregates provider-neutral, closed hourly metering rollups for a cluster. Missing and gap windows are explicit and are never rendered as zero spend.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param window: Window duration (for example 24h, 7d, 30d)
        :type window: str
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

        _param = self._get_cluster_cost_summary_serialize(
            cluster_name=cluster_name,
            window=window,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterCostSummaryResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_cluster_cost_summary_serialize(
        self,
        cluster_name,
        window,
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
        if cluster_name is not None:
            _path_params['clusterName'] = cluster_name
        # process the query parameters
        if window is not None:
            
            _query_params.append(('window', window))
            
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
            resource_path='/api/v1/clusters/{clusterName}/cost/summary',
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
    def get_cluster_kubeconfig(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
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
    ) -> KubeconfigResponse:
        """Get cluster kubeconfig

        Returns the kubeconfig for the cluster. Returns 202 Accepted while generation is in progress (self-managed clusters), or 200 with the config when ready.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
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

        _param = self._get_cluster_kubeconfig_serialize(
            cluster_name=cluster_name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "KubeconfigResponse",
            '202': "KubeconfigGenerationResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '409': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def get_cluster_kubeconfig_with_http_info(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
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
    ) -> ApiResponse[KubeconfigResponse]:
        """Get cluster kubeconfig

        Returns the kubeconfig for the cluster. Returns 202 Accepted while generation is in progress (self-managed clusters), or 200 with the config when ready.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
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

        _param = self._get_cluster_kubeconfig_serialize(
            cluster_name=cluster_name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "KubeconfigResponse",
            '202': "KubeconfigGenerationResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '409': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def get_cluster_kubeconfig_without_preload_content(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
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
        """Get cluster kubeconfig

        Returns the kubeconfig for the cluster. Returns 202 Accepted while generation is in progress (self-managed clusters), or 200 with the config when ready.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
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

        _param = self._get_cluster_kubeconfig_serialize(
            cluster_name=cluster_name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "KubeconfigResponse",
            '202': "KubeconfigGenerationResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '409': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_cluster_kubeconfig_serialize(
        self,
        cluster_name,
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
        if cluster_name is not None:
            _path_params['clusterName'] = cluster_name
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
            resource_path='/api/v1/clusters/{clusterName}/kubeconfig',
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
    def get_cluster_metrics_allocation(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        window: Annotated[Optional[StrictStr], Field(description="Window duration (for example 15m, 1h, 24h); minutes-scale, not truncated to whole hours")] = None,
        sort_by: Annotated[Optional[Any], Field(description="What the page is ordered by")] = None,
        sort_order: Annotated[Optional[SortOrder], Field(description="Sort direction, Ascending by name and Descending otherwise when omitted; missing values always remain last")] = None,
        search: Annotated[Optional[StrictStr], Field(description="Case-insensitive application name search")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="Page size from 1 through 200")] = None,
        offset: Annotated[Optional[StrictInt], Field(description="Page offset")] = None,
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
    ) -> ClusterMetricsAllocationResponse:
        """Get cluster metrics allocation

        Lists every platform-managed application on the cluster with its resource usage averaged over the window, so heavy workloads surface without naming one. An application with no stored sample is absent rather than zero.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param window: Window duration (for example 15m, 1h, 24h); minutes-scale, not truncated to whole hours
        :type window: str
        :param sort_by: What the page is ordered by
        :type sort_by: ClusterMetricsSortField
        :param sort_order: Sort direction, Ascending by name and Descending otherwise when omitted; missing values always remain last
        :type sort_order: SortOrder
        :param search: Case-insensitive application name search
        :type search: str
        :param limit: Page size from 1 through 200
        :type limit: int
        :param offset: Page offset
        :type offset: int
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

        _param = self._get_cluster_metrics_allocation_serialize(
            cluster_name=cluster_name,
            window=window,
            sort_by=sort_by,
            sort_order=sort_order,
            search=search,
            limit=limit,
            offset=offset,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterMetricsAllocationResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def get_cluster_metrics_allocation_with_http_info(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        window: Annotated[Optional[StrictStr], Field(description="Window duration (for example 15m, 1h, 24h); minutes-scale, not truncated to whole hours")] = None,
        sort_by: Annotated[Optional[Any], Field(description="What the page is ordered by")] = None,
        sort_order: Annotated[Optional[SortOrder], Field(description="Sort direction, Ascending by name and Descending otherwise when omitted; missing values always remain last")] = None,
        search: Annotated[Optional[StrictStr], Field(description="Case-insensitive application name search")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="Page size from 1 through 200")] = None,
        offset: Annotated[Optional[StrictInt], Field(description="Page offset")] = None,
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
    ) -> ApiResponse[ClusterMetricsAllocationResponse]:
        """Get cluster metrics allocation

        Lists every platform-managed application on the cluster with its resource usage averaged over the window, so heavy workloads surface without naming one. An application with no stored sample is absent rather than zero.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param window: Window duration (for example 15m, 1h, 24h); minutes-scale, not truncated to whole hours
        :type window: str
        :param sort_by: What the page is ordered by
        :type sort_by: ClusterMetricsSortField
        :param sort_order: Sort direction, Ascending by name and Descending otherwise when omitted; missing values always remain last
        :type sort_order: SortOrder
        :param search: Case-insensitive application name search
        :type search: str
        :param limit: Page size from 1 through 200
        :type limit: int
        :param offset: Page offset
        :type offset: int
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

        _param = self._get_cluster_metrics_allocation_serialize(
            cluster_name=cluster_name,
            window=window,
            sort_by=sort_by,
            sort_order=sort_order,
            search=search,
            limit=limit,
            offset=offset,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterMetricsAllocationResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def get_cluster_metrics_allocation_without_preload_content(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        window: Annotated[Optional[StrictStr], Field(description="Window duration (for example 15m, 1h, 24h); minutes-scale, not truncated to whole hours")] = None,
        sort_by: Annotated[Optional[Any], Field(description="What the page is ordered by")] = None,
        sort_order: Annotated[Optional[SortOrder], Field(description="Sort direction, Ascending by name and Descending otherwise when omitted; missing values always remain last")] = None,
        search: Annotated[Optional[StrictStr], Field(description="Case-insensitive application name search")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="Page size from 1 through 200")] = None,
        offset: Annotated[Optional[StrictInt], Field(description="Page offset")] = None,
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
        """Get cluster metrics allocation

        Lists every platform-managed application on the cluster with its resource usage averaged over the window, so heavy workloads surface without naming one. An application with no stored sample is absent rather than zero.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param window: Window duration (for example 15m, 1h, 24h); minutes-scale, not truncated to whole hours
        :type window: str
        :param sort_by: What the page is ordered by
        :type sort_by: ClusterMetricsSortField
        :param sort_order: Sort direction, Ascending by name and Descending otherwise when omitted; missing values always remain last
        :type sort_order: SortOrder
        :param search: Case-insensitive application name search
        :type search: str
        :param limit: Page size from 1 through 200
        :type limit: int
        :param offset: Page offset
        :type offset: int
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

        _param = self._get_cluster_metrics_allocation_serialize(
            cluster_name=cluster_name,
            window=window,
            sort_by=sort_by,
            sort_order=sort_order,
            search=search,
            limit=limit,
            offset=offset,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterMetricsAllocationResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_cluster_metrics_allocation_serialize(
        self,
        cluster_name,
        window,
        sort_by,
        sort_order,
        search,
        limit,
        offset,
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
        if cluster_name is not None:
            _path_params['clusterName'] = cluster_name
        # process the query parameters
        if window is not None:
            
            _query_params.append(('window', window))
            
        if sort_by is not None:
            
            _query_params.append(('sortBy', sort_by.value))
            
        if sort_order is not None:
            
            _query_params.append(('sortOrder', sort_order.value))
            
        if search is not None:
            
            _query_params.append(('search', search))
            
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if offset is not None:
            
            _query_params.append(('offset', offset))
            
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
            resource_path='/api/v1/clusters/{clusterName}/metrics/allocation',
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
    def get_cluster_metrics_summary(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        window: Annotated[Optional[StrictStr], Field(description="Window duration (for example 15m, 1h, 24h); minutes-scale, not truncated to whole hours")] = None,
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
    ) -> ClusterMetricsSummaryResponse:
        """Get cluster metrics summary

        Cluster-wide totals and coverage: how many applications reported resource usage in the window, how many samples backed that, and whether every sample was complete. An application that reported nothing is not counted.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param window: Window duration (for example 15m, 1h, 24h); minutes-scale, not truncated to whole hours
        :type window: str
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

        _param = self._get_cluster_metrics_summary_serialize(
            cluster_name=cluster_name,
            window=window,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterMetricsSummaryResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def get_cluster_metrics_summary_with_http_info(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        window: Annotated[Optional[StrictStr], Field(description="Window duration (for example 15m, 1h, 24h); minutes-scale, not truncated to whole hours")] = None,
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
    ) -> ApiResponse[ClusterMetricsSummaryResponse]:
        """Get cluster metrics summary

        Cluster-wide totals and coverage: how many applications reported resource usage in the window, how many samples backed that, and whether every sample was complete. An application that reported nothing is not counted.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param window: Window duration (for example 15m, 1h, 24h); minutes-scale, not truncated to whole hours
        :type window: str
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

        _param = self._get_cluster_metrics_summary_serialize(
            cluster_name=cluster_name,
            window=window,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterMetricsSummaryResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def get_cluster_metrics_summary_without_preload_content(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        window: Annotated[Optional[StrictStr], Field(description="Window duration (for example 15m, 1h, 24h); minutes-scale, not truncated to whole hours")] = None,
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
        """Get cluster metrics summary

        Cluster-wide totals and coverage: how many applications reported resource usage in the window, how many samples backed that, and whether every sample was complete. An application that reported nothing is not counted.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param window: Window duration (for example 15m, 1h, 24h); minutes-scale, not truncated to whole hours
        :type window: str
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

        _param = self._get_cluster_metrics_summary_serialize(
            cluster_name=cluster_name,
            window=window,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterMetricsSummaryResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_cluster_metrics_summary_serialize(
        self,
        cluster_name,
        window,
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
        if cluster_name is not None:
            _path_params['clusterName'] = cluster_name
        # process the query parameters
        if window is not None:
            
            _query_params.append(('window', window))
            
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
            resource_path='/api/v1/clusters/{clusterName}/metrics/summary',
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
    def get_cluster_progress(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        operation_id: Annotated[Optional[StrictStr], Field(description="Operation ID to get progress for (optional)")] = None,
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
    ) -> ClusterProgressResponse:
        """Get cluster progress

        Returns progress details for the most recent or specified cluster operation. Pass operationId to target a specific operation.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param operation_id: Operation ID to get progress for (optional)
        :type operation_id: str
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

        _param = self._get_cluster_progress_serialize(
            cluster_name=cluster_name,
            operation_id=operation_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterProgressResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def get_cluster_progress_with_http_info(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        operation_id: Annotated[Optional[StrictStr], Field(description="Operation ID to get progress for (optional)")] = None,
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
    ) -> ApiResponse[ClusterProgressResponse]:
        """Get cluster progress

        Returns progress details for the most recent or specified cluster operation. Pass operationId to target a specific operation.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param operation_id: Operation ID to get progress for (optional)
        :type operation_id: str
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

        _param = self._get_cluster_progress_serialize(
            cluster_name=cluster_name,
            operation_id=operation_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterProgressResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def get_cluster_progress_without_preload_content(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        operation_id: Annotated[Optional[StrictStr], Field(description="Operation ID to get progress for (optional)")] = None,
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
        """Get cluster progress

        Returns progress details for the most recent or specified cluster operation. Pass operationId to target a specific operation.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param operation_id: Operation ID to get progress for (optional)
        :type operation_id: str
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

        _param = self._get_cluster_progress_serialize(
            cluster_name=cluster_name,
            operation_id=operation_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterProgressResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_cluster_progress_serialize(
        self,
        cluster_name,
        operation_id,
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
        if cluster_name is not None:
            _path_params['clusterName'] = cluster_name
        # process the query parameters
        if operation_id is not None:
            
            _query_params.append(('operationId', operation_id))
            
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
            resource_path='/api/v1/clusters/{clusterName}/progress',
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
    def get_cluster_spec(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
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
    ) -> K8sClusterManifestResponse:
        """Get cluster specification

        Returns the manifest the cluster was created from, in the shape the create request takes. Credential values are never included.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
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

        _param = self._get_cluster_spec_serialize(
            cluster_name=cluster_name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "K8sClusterManifestResponse",
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
    def get_cluster_spec_with_http_info(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
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
    ) -> ApiResponse[K8sClusterManifestResponse]:
        """Get cluster specification

        Returns the manifest the cluster was created from, in the shape the create request takes. Credential values are never included.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
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

        _param = self._get_cluster_spec_serialize(
            cluster_name=cluster_name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "K8sClusterManifestResponse",
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
    def get_cluster_spec_without_preload_content(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
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
        """Get cluster specification

        Returns the manifest the cluster was created from, in the shape the create request takes. Credential values are never included.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
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

        _param = self._get_cluster_spec_serialize(
            cluster_name=cluster_name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "K8sClusterManifestResponse",
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


    def _get_cluster_spec_serialize(
        self,
        cluster_name,
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
        if cluster_name is not None:
            _path_params['clusterName'] = cluster_name
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
            resource_path='/api/v1/clusters/{clusterName}/spec',
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
    def get_cluster_storage(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
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
    ) -> ClusterStorageResponse:
        """Get a cluster's storage

        Returns the storage classes the cluster offers, what each one provides, and the names bound to them. Classes are observed, never set here.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
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

        _param = self._get_cluster_storage_serialize(
            cluster_name=cluster_name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterStorageResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def get_cluster_storage_with_http_info(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
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
    ) -> ApiResponse[ClusterStorageResponse]:
        """Get a cluster's storage

        Returns the storage classes the cluster offers, what each one provides, and the names bound to them. Classes are observed, never set here.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
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

        _param = self._get_cluster_storage_serialize(
            cluster_name=cluster_name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterStorageResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def get_cluster_storage_without_preload_content(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
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
        """Get a cluster's storage

        Returns the storage classes the cluster offers, what each one provides, and the names bound to them. Classes are observed, never set here.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
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

        _param = self._get_cluster_storage_serialize(
            cluster_name=cluster_name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterStorageResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_cluster_storage_serialize(
        self,
        cluster_name,
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
        if cluster_name is not None:
            _path_params['clusterName'] = cluster_name
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
            resource_path='/api/v1/clusters/{clusterName}/storage',
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
    def issue_cluster_agent_certificate(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        agent_certificate_signing_request: Annotated[AgentCertificateSigningRequest, Field(description="Signing request for the agent's key")],
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
    ) -> AgentCertificateBundleResponse:
        """Sign a new certificate for a cluster's agent

        Signs a new certificate for a cluster's AstroPulse agent from a certificate signing request for a key you made and keep, to write with that key to the agent's TLS Secret from a machine that can reach the cluster. The certificate carries the cluster's own identity, and once the agent connects with it the agent's previous certificate is no longer accepted. A registered cluster's agent can be issued one while the cluster is being registered or once it is registered; a provisioned cluster's once it is ready.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param agent_certificate_signing_request: Signing request for the agent's key (required)
        :type agent_certificate_signing_request: AgentCertificateSigningRequest
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

        _param = self._issue_cluster_agent_certificate_serialize(
            cluster_name=cluster_name,
            agent_certificate_signing_request=agent_certificate_signing_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AgentCertificateBundleResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '409': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def issue_cluster_agent_certificate_with_http_info(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        agent_certificate_signing_request: Annotated[AgentCertificateSigningRequest, Field(description="Signing request for the agent's key")],
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
    ) -> ApiResponse[AgentCertificateBundleResponse]:
        """Sign a new certificate for a cluster's agent

        Signs a new certificate for a cluster's AstroPulse agent from a certificate signing request for a key you made and keep, to write with that key to the agent's TLS Secret from a machine that can reach the cluster. The certificate carries the cluster's own identity, and once the agent connects with it the agent's previous certificate is no longer accepted. A registered cluster's agent can be issued one while the cluster is being registered or once it is registered; a provisioned cluster's once it is ready.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param agent_certificate_signing_request: Signing request for the agent's key (required)
        :type agent_certificate_signing_request: AgentCertificateSigningRequest
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

        _param = self._issue_cluster_agent_certificate_serialize(
            cluster_name=cluster_name,
            agent_certificate_signing_request=agent_certificate_signing_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AgentCertificateBundleResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '409': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def issue_cluster_agent_certificate_without_preload_content(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        agent_certificate_signing_request: Annotated[AgentCertificateSigningRequest, Field(description="Signing request for the agent's key")],
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
        """Sign a new certificate for a cluster's agent

        Signs a new certificate for a cluster's AstroPulse agent from a certificate signing request for a key you made and keep, to write with that key to the agent's TLS Secret from a machine that can reach the cluster. The certificate carries the cluster's own identity, and once the agent connects with it the agent's previous certificate is no longer accepted. A registered cluster's agent can be issued one while the cluster is being registered or once it is registered; a provisioned cluster's once it is ready.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param agent_certificate_signing_request: Signing request for the agent's key (required)
        :type agent_certificate_signing_request: AgentCertificateSigningRequest
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

        _param = self._issue_cluster_agent_certificate_serialize(
            cluster_name=cluster_name,
            agent_certificate_signing_request=agent_certificate_signing_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AgentCertificateBundleResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '409': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _issue_cluster_agent_certificate_serialize(
        self,
        cluster_name,
        agent_certificate_signing_request,
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
        if cluster_name is not None:
            _path_params['clusterName'] = cluster_name
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if agent_certificate_signing_request is not None:
            _body_params = agent_certificate_signing_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'ApiKeyAuth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v1/clusters/{clusterName}/agent/certificate',
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
    def list_cluster_operations(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        limit: Annotated[Optional[StrictInt], Field(description="Maximum number of operations to return")] = None,
        page_token: Annotated[Optional[StrictStr], Field(description="Page token for pagination")] = None,
        provider: Annotated[Optional[StrictStr], Field(description="Cloud provider: aws, gcp, azure (required if cluster not found)")] = None,
        provisioner_type: Annotated[Optional[StrictStr], Field(description="Provisioner type: selfmanaged, eks, gke, aks (required if cluster not found)")] = None,
        account_id: Annotated[Optional[StrictStr], Field(description="Cloud account ID (required if cluster not found)")] = None,
        region: Annotated[Optional[StrictStr], Field(description="Cloud region (required if cluster not found)")] = None,
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
    ) -> ClusterProgressPageResponse:
        """Get cluster operation history

        Returns historical operations for the cluster. If the cluster record no longer exists, pass provider, provisionerType, accountId, and region as query parameters to look up by storage location.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param limit: Maximum number of operations to return
        :type limit: int
        :param page_token: Page token for pagination
        :type page_token: str
        :param provider: Cloud provider: aws, gcp, azure (required if cluster not found)
        :type provider: str
        :param provisioner_type: Provisioner type: selfmanaged, eks, gke, aks (required if cluster not found)
        :type provisioner_type: str
        :param account_id: Cloud account ID (required if cluster not found)
        :type account_id: str
        :param region: Cloud region (required if cluster not found)
        :type region: str
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

        _param = self._list_cluster_operations_serialize(
            cluster_name=cluster_name,
            limit=limit,
            page_token=page_token,
            provider=provider,
            provisioner_type=provisioner_type,
            account_id=account_id,
            region=region,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterProgressPageResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def list_cluster_operations_with_http_info(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        limit: Annotated[Optional[StrictInt], Field(description="Maximum number of operations to return")] = None,
        page_token: Annotated[Optional[StrictStr], Field(description="Page token for pagination")] = None,
        provider: Annotated[Optional[StrictStr], Field(description="Cloud provider: aws, gcp, azure (required if cluster not found)")] = None,
        provisioner_type: Annotated[Optional[StrictStr], Field(description="Provisioner type: selfmanaged, eks, gke, aks (required if cluster not found)")] = None,
        account_id: Annotated[Optional[StrictStr], Field(description="Cloud account ID (required if cluster not found)")] = None,
        region: Annotated[Optional[StrictStr], Field(description="Cloud region (required if cluster not found)")] = None,
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
    ) -> ApiResponse[ClusterProgressPageResponse]:
        """Get cluster operation history

        Returns historical operations for the cluster. If the cluster record no longer exists, pass provider, provisionerType, accountId, and region as query parameters to look up by storage location.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param limit: Maximum number of operations to return
        :type limit: int
        :param page_token: Page token for pagination
        :type page_token: str
        :param provider: Cloud provider: aws, gcp, azure (required if cluster not found)
        :type provider: str
        :param provisioner_type: Provisioner type: selfmanaged, eks, gke, aks (required if cluster not found)
        :type provisioner_type: str
        :param account_id: Cloud account ID (required if cluster not found)
        :type account_id: str
        :param region: Cloud region (required if cluster not found)
        :type region: str
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

        _param = self._list_cluster_operations_serialize(
            cluster_name=cluster_name,
            limit=limit,
            page_token=page_token,
            provider=provider,
            provisioner_type=provisioner_type,
            account_id=account_id,
            region=region,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterProgressPageResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def list_cluster_operations_without_preload_content(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        limit: Annotated[Optional[StrictInt], Field(description="Maximum number of operations to return")] = None,
        page_token: Annotated[Optional[StrictStr], Field(description="Page token for pagination")] = None,
        provider: Annotated[Optional[StrictStr], Field(description="Cloud provider: aws, gcp, azure (required if cluster not found)")] = None,
        provisioner_type: Annotated[Optional[StrictStr], Field(description="Provisioner type: selfmanaged, eks, gke, aks (required if cluster not found)")] = None,
        account_id: Annotated[Optional[StrictStr], Field(description="Cloud account ID (required if cluster not found)")] = None,
        region: Annotated[Optional[StrictStr], Field(description="Cloud region (required if cluster not found)")] = None,
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
        """Get cluster operation history

        Returns historical operations for the cluster. If the cluster record no longer exists, pass provider, provisionerType, accountId, and region as query parameters to look up by storage location.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param limit: Maximum number of operations to return
        :type limit: int
        :param page_token: Page token for pagination
        :type page_token: str
        :param provider: Cloud provider: aws, gcp, azure (required if cluster not found)
        :type provider: str
        :param provisioner_type: Provisioner type: selfmanaged, eks, gke, aks (required if cluster not found)
        :type provisioner_type: str
        :param account_id: Cloud account ID (required if cluster not found)
        :type account_id: str
        :param region: Cloud region (required if cluster not found)
        :type region: str
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

        _param = self._list_cluster_operations_serialize(
            cluster_name=cluster_name,
            limit=limit,
            page_token=page_token,
            provider=provider,
            provisioner_type=provisioner_type,
            account_id=account_id,
            region=region,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterProgressPageResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _list_cluster_operations_serialize(
        self,
        cluster_name,
        limit,
        page_token,
        provider,
        provisioner_type,
        account_id,
        region,
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
        if cluster_name is not None:
            _path_params['clusterName'] = cluster_name
        # process the query parameters
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if page_token is not None:
            
            _query_params.append(('pageToken', page_token))
            
        if provider is not None:
            
            _query_params.append(('provider', provider))
            
        if provisioner_type is not None:
            
            _query_params.append(('provisionerType', provisioner_type))
            
        if account_id is not None:
            
            _query_params.append(('accountId', account_id))
            
        if region is not None:
            
            _query_params.append(('region', region))
            
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
            resource_path='/api/v1/clusters/{clusterName}/operations',
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
    def list_cluster_progress(
        self,
        operation_type: Annotated[Optional[OperationType], Field(description="Only operations of this type")] = None,
        status: Annotated[Optional[OperationStatus], Field(description="Only operations with this status")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="Limit number of results")] = None,
        page_token: Annotated[Optional[StrictStr], Field(description="Page token for pagination")] = None,
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
    ) -> ClusterProgressPageResponse:
        """List cluster progress for all clusters

        Returns paginated progress records across all clusters in the organization, filterable by operation type and status.

        :param operation_type: Only operations of this type
        :type operation_type: OperationType
        :param status: Only operations with this status
        :type status: OperationStatus
        :param limit: Limit number of results
        :type limit: int
        :param page_token: Page token for pagination
        :type page_token: str
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

        _param = self._list_cluster_progress_serialize(
            operation_type=operation_type,
            status=status,
            limit=limit,
            page_token=page_token,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterProgressPageResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def list_cluster_progress_with_http_info(
        self,
        operation_type: Annotated[Optional[OperationType], Field(description="Only operations of this type")] = None,
        status: Annotated[Optional[OperationStatus], Field(description="Only operations with this status")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="Limit number of results")] = None,
        page_token: Annotated[Optional[StrictStr], Field(description="Page token for pagination")] = None,
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
    ) -> ApiResponse[ClusterProgressPageResponse]:
        """List cluster progress for all clusters

        Returns paginated progress records across all clusters in the organization, filterable by operation type and status.

        :param operation_type: Only operations of this type
        :type operation_type: OperationType
        :param status: Only operations with this status
        :type status: OperationStatus
        :param limit: Limit number of results
        :type limit: int
        :param page_token: Page token for pagination
        :type page_token: str
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

        _param = self._list_cluster_progress_serialize(
            operation_type=operation_type,
            status=status,
            limit=limit,
            page_token=page_token,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterProgressPageResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def list_cluster_progress_without_preload_content(
        self,
        operation_type: Annotated[Optional[OperationType], Field(description="Only operations of this type")] = None,
        status: Annotated[Optional[OperationStatus], Field(description="Only operations with this status")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="Limit number of results")] = None,
        page_token: Annotated[Optional[StrictStr], Field(description="Page token for pagination")] = None,
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
        """List cluster progress for all clusters

        Returns paginated progress records across all clusters in the organization, filterable by operation type and status.

        :param operation_type: Only operations of this type
        :type operation_type: OperationType
        :param status: Only operations with this status
        :type status: OperationStatus
        :param limit: Limit number of results
        :type limit: int
        :param page_token: Page token for pagination
        :type page_token: str
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

        _param = self._list_cluster_progress_serialize(
            operation_type=operation_type,
            status=status,
            limit=limit,
            page_token=page_token,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterProgressPageResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _list_cluster_progress_serialize(
        self,
        operation_type,
        status,
        limit,
        page_token,
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
        if operation_type is not None:
            
            _query_params.append(('operationType', operation_type.value))
            
        if status is not None:
            
            _query_params.append(('status', status.value))
            
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if page_token is not None:
            
            _query_params.append(('pageToken', page_token))
            
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
            resource_path='/api/v1/clusters/progress',
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
    def list_clusters(
        self,
        provider_id: Annotated[Optional[StrictStr], Field(description="Cloud Provider ID (e.g., aws, gcp)")] = None,
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
    ) -> K8sClusterListResponse:
        """List all clusters for your organization

        Retrieves a list of all Kubernetes clusters managed by AstroPulse

        :param provider_id: Cloud Provider ID (e.g., aws, gcp)
        :type provider_id: str
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

        _param = self._list_clusters_serialize(
            provider_id=provider_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "K8sClusterListResponse",
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
    def list_clusters_with_http_info(
        self,
        provider_id: Annotated[Optional[StrictStr], Field(description="Cloud Provider ID (e.g., aws, gcp)")] = None,
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
    ) -> ApiResponse[K8sClusterListResponse]:
        """List all clusters for your organization

        Retrieves a list of all Kubernetes clusters managed by AstroPulse

        :param provider_id: Cloud Provider ID (e.g., aws, gcp)
        :type provider_id: str
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

        _param = self._list_clusters_serialize(
            provider_id=provider_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "K8sClusterListResponse",
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
    def list_clusters_without_preload_content(
        self,
        provider_id: Annotated[Optional[StrictStr], Field(description="Cloud Provider ID (e.g., aws, gcp)")] = None,
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
        """List all clusters for your organization

        Retrieves a list of all Kubernetes clusters managed by AstroPulse

        :param provider_id: Cloud Provider ID (e.g., aws, gcp)
        :type provider_id: str
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

        _param = self._list_clusters_serialize(
            provider_id=provider_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "K8sClusterListResponse",
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


    def _list_clusters_serialize(
        self,
        provider_id,
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
        if provider_id is not None:
            
            _query_params.append(('providerId', provider_id))
            
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
            resource_path='/api/v1/clusters',
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
    def register_cluster_agent(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        k8s_cluster_registration: Annotated[K8sClusterRegistration, Field(description="Cluster registration configuration")],
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
    ) -> ClusterRegistrationResponse:
        """Register an agent on a cluster

        Registers a Kubernetes cluster through the AstroPulse agent. Works with any cluster type (EKS, GKE, AKS, on-premises).

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param k8s_cluster_registration: Cluster registration configuration (required)
        :type k8s_cluster_registration: K8sClusterRegistration
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

        _param = self._register_cluster_agent_serialize(
            cluster_name=cluster_name,
            k8s_cluster_registration=k8s_cluster_registration,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '202': "ClusterRegistrationResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '409': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def register_cluster_agent_with_http_info(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        k8s_cluster_registration: Annotated[K8sClusterRegistration, Field(description="Cluster registration configuration")],
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
    ) -> ApiResponse[ClusterRegistrationResponse]:
        """Register an agent on a cluster

        Registers a Kubernetes cluster through the AstroPulse agent. Works with any cluster type (EKS, GKE, AKS, on-premises).

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param k8s_cluster_registration: Cluster registration configuration (required)
        :type k8s_cluster_registration: K8sClusterRegistration
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

        _param = self._register_cluster_agent_serialize(
            cluster_name=cluster_name,
            k8s_cluster_registration=k8s_cluster_registration,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '202': "ClusterRegistrationResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '409': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def register_cluster_agent_without_preload_content(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        k8s_cluster_registration: Annotated[K8sClusterRegistration, Field(description="Cluster registration configuration")],
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
        """Register an agent on a cluster

        Registers a Kubernetes cluster through the AstroPulse agent. Works with any cluster type (EKS, GKE, AKS, on-premises).

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param k8s_cluster_registration: Cluster registration configuration (required)
        :type k8s_cluster_registration: K8sClusterRegistration
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

        _param = self._register_cluster_agent_serialize(
            cluster_name=cluster_name,
            k8s_cluster_registration=k8s_cluster_registration,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '202': "ClusterRegistrationResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '409': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _register_cluster_agent_serialize(
        self,
        cluster_name,
        k8s_cluster_registration,
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
        if cluster_name is not None:
            _path_params['clusterName'] = cluster_name
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if k8s_cluster_registration is not None:
            _body_params = k8s_cluster_registration


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'ApiKeyAuth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v1/clusters/{clusterName}/agent',
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
    def request_cluster_approval(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Name of the cluster")],
        org_id: Annotated[StrictStr, Field(description="Organization ID")],
        token: Annotated[StrictStr, Field(description="Approval token")],
        action: Annotated[ClusterApprovalAction, Field(description="The decision on the cluster")],
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
    ) -> ClusterApprovalResponse:
        """Request cluster operation approval

        Submits an approve or reject decision for a pending cluster operation. Requires a signed-in organization owner.

        :param cluster_name: Name of the cluster (required)
        :type cluster_name: str
        :param org_id: Organization ID (required)
        :type org_id: str
        :param token: Approval token (required)
        :type token: str
        :param action: The decision on the cluster (required)
        :type action: ClusterApprovalAction
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

        _param = self._request_cluster_approval_serialize(
            cluster_name=cluster_name,
            org_id=org_id,
            token=token,
            action=action,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterApprovalResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '409': "ErrorResponse",
            '422': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def request_cluster_approval_with_http_info(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Name of the cluster")],
        org_id: Annotated[StrictStr, Field(description="Organization ID")],
        token: Annotated[StrictStr, Field(description="Approval token")],
        action: Annotated[ClusterApprovalAction, Field(description="The decision on the cluster")],
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
    ) -> ApiResponse[ClusterApprovalResponse]:
        """Request cluster operation approval

        Submits an approve or reject decision for a pending cluster operation. Requires a signed-in organization owner.

        :param cluster_name: Name of the cluster (required)
        :type cluster_name: str
        :param org_id: Organization ID (required)
        :type org_id: str
        :param token: Approval token (required)
        :type token: str
        :param action: The decision on the cluster (required)
        :type action: ClusterApprovalAction
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

        _param = self._request_cluster_approval_serialize(
            cluster_name=cluster_name,
            org_id=org_id,
            token=token,
            action=action,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterApprovalResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '409': "ErrorResponse",
            '422': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def request_cluster_approval_without_preload_content(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Name of the cluster")],
        org_id: Annotated[StrictStr, Field(description="Organization ID")],
        token: Annotated[StrictStr, Field(description="Approval token")],
        action: Annotated[ClusterApprovalAction, Field(description="The decision on the cluster")],
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
        """Request cluster operation approval

        Submits an approve or reject decision for a pending cluster operation. Requires a signed-in organization owner.

        :param cluster_name: Name of the cluster (required)
        :type cluster_name: str
        :param org_id: Organization ID (required)
        :type org_id: str
        :param token: Approval token (required)
        :type token: str
        :param action: The decision on the cluster (required)
        :type action: ClusterApprovalAction
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

        _param = self._request_cluster_approval_serialize(
            cluster_name=cluster_name,
            org_id=org_id,
            token=token,
            action=action,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterApprovalResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '409': "ErrorResponse",
            '422': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _request_cluster_approval_serialize(
        self,
        cluster_name,
        org_id,
        token,
        action,
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
        if cluster_name is not None:
            
            _query_params.append(('clusterName', cluster_name))
            
        if org_id is not None:
            
            _query_params.append(('orgId', org_id))
            
        if token is not None:
            
            _query_params.append(('token', token))
            
        if action is not None:
            
            _query_params.append(('action', action.value))
            
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
            method='POST',
            resource_path='/api/v1/clusters/approval',
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
    def stream_cluster_progress(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        operation_id: Annotated[Optional[StrictStr], Field(description="Operation ID to stream progress for (optional)")] = None,
        accept: Annotated[Optional[StrictStr], Field(description="Send application/vnd.astropulse.stream-ticket+json with a bearer token to get a single-use ticket for this stream instead of opening it")] = None,
        x_astro_stream_origin: Annotated[Optional[StrictStr], Field(description="With a ticket request: the browser origin the stream will be opened from")] = None,
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
    ) -> StreamTicket:
        """Stream cluster progress via WebSocket

        Opens a WebSocket connection and streams live progress events for an in-progress cluster operation. Use operationId to target a specific run.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param operation_id: Operation ID to stream progress for (optional)
        :type operation_id: str
        :param accept: Send application/vnd.astropulse.stream-ticket+json with a bearer token to get a single-use ticket for this stream instead of opening it
        :type accept: str
        :param x_astro_stream_origin: With a ticket request: the browser origin the stream will be opened from
        :type x_astro_stream_origin: str
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

        _param = self._stream_cluster_progress_serialize(
            cluster_name=cluster_name,
            operation_id=operation_id,
            accept=accept,
            x_astro_stream_origin=x_astro_stream_origin,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '101': "str",
            '200': "StreamTicket",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def stream_cluster_progress_with_http_info(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        operation_id: Annotated[Optional[StrictStr], Field(description="Operation ID to stream progress for (optional)")] = None,
        accept: Annotated[Optional[StrictStr], Field(description="Send application/vnd.astropulse.stream-ticket+json with a bearer token to get a single-use ticket for this stream instead of opening it")] = None,
        x_astro_stream_origin: Annotated[Optional[StrictStr], Field(description="With a ticket request: the browser origin the stream will be opened from")] = None,
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
    ) -> ApiResponse[StreamTicket]:
        """Stream cluster progress via WebSocket

        Opens a WebSocket connection and streams live progress events for an in-progress cluster operation. Use operationId to target a specific run.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param operation_id: Operation ID to stream progress for (optional)
        :type operation_id: str
        :param accept: Send application/vnd.astropulse.stream-ticket+json with a bearer token to get a single-use ticket for this stream instead of opening it
        :type accept: str
        :param x_astro_stream_origin: With a ticket request: the browser origin the stream will be opened from
        :type x_astro_stream_origin: str
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

        _param = self._stream_cluster_progress_serialize(
            cluster_name=cluster_name,
            operation_id=operation_id,
            accept=accept,
            x_astro_stream_origin=x_astro_stream_origin,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '101': "str",
            '200': "StreamTicket",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def stream_cluster_progress_without_preload_content(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        operation_id: Annotated[Optional[StrictStr], Field(description="Operation ID to stream progress for (optional)")] = None,
        accept: Annotated[Optional[StrictStr], Field(description="Send application/vnd.astropulse.stream-ticket+json with a bearer token to get a single-use ticket for this stream instead of opening it")] = None,
        x_astro_stream_origin: Annotated[Optional[StrictStr], Field(description="With a ticket request: the browser origin the stream will be opened from")] = None,
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
        """Stream cluster progress via WebSocket

        Opens a WebSocket connection and streams live progress events for an in-progress cluster operation. Use operationId to target a specific run.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param operation_id: Operation ID to stream progress for (optional)
        :type operation_id: str
        :param accept: Send application/vnd.astropulse.stream-ticket+json with a bearer token to get a single-use ticket for this stream instead of opening it
        :type accept: str
        :param x_astro_stream_origin: With a ticket request: the browser origin the stream will be opened from
        :type x_astro_stream_origin: str
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

        _param = self._stream_cluster_progress_serialize(
            cluster_name=cluster_name,
            operation_id=operation_id,
            accept=accept,
            x_astro_stream_origin=x_astro_stream_origin,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '101': "str",
            '200': "StreamTicket",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _stream_cluster_progress_serialize(
        self,
        cluster_name,
        operation_id,
        accept,
        x_astro_stream_origin,
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
        if cluster_name is not None:
            _path_params['clusterName'] = cluster_name
        # process the query parameters
        if operation_id is not None:
            
            _query_params.append(('operationId', operation_id))
            
        # process the header parameters
        if accept is not None:
            _header_params['Accept'] = accept
        if x_astro_stream_origin is not None:
            _header_params['X-Astro-Stream-Origin'] = x_astro_stream_origin
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
            resource_path='/api/v1/clusters/{clusterName}/progress/stream',
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
    def sync_cluster_auth(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
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
    ) -> StringResponse:
        """Sync cluster authentication configuration

        Re-synchronizes internal authentication configuration for a specific cluster to fix missing certificates or connectivity issues

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
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

        _param = self._sync_cluster_auth_serialize(
            cluster_name=cluster_name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "StringResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def sync_cluster_auth_with_http_info(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
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
    ) -> ApiResponse[StringResponse]:
        """Sync cluster authentication configuration

        Re-synchronizes internal authentication configuration for a specific cluster to fix missing certificates or connectivity issues

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
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

        _param = self._sync_cluster_auth_serialize(
            cluster_name=cluster_name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "StringResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def sync_cluster_auth_without_preload_content(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
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
        """Sync cluster authentication configuration

        Re-synchronizes internal authentication configuration for a specific cluster to fix missing certificates or connectivity issues

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
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

        _param = self._sync_cluster_auth_serialize(
            cluster_name=cluster_name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "StringResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _sync_cluster_auth_serialize(
        self,
        cluster_name,
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
        if cluster_name is not None:
            _path_params['clusterName'] = cluster_name
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
            method='POST',
            resource_path='/api/v1/clusters/{clusterName}/auth/sync',
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
    def unregister_cluster_agent(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        agent_only: Annotated[Optional[StrictBool], Field(description="Disconnect only the agent and keep the cluster's record")] = None,
        delete_apps: Annotated[Optional[StrictBool], Field(description="Delete the applications AstroPulse deployed to the cluster (default: keep them running)")] = None,
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
    ) -> ClusterOperationResultResponse:
        """Unregister an agent from a cluster

        Removes the agent from a registered cluster and the cluster from AstroPulse. With agent-only=true, only the agent is disconnected and the cluster's record is kept.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param agent_only: Disconnect only the agent and keep the cluster's record
        :type agent_only: bool
        :param delete_apps: Delete the applications AstroPulse deployed to the cluster (default: keep them running)
        :type delete_apps: bool
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

        _param = self._unregister_cluster_agent_serialize(
            cluster_name=cluster_name,
            agent_only=agent_only,
            delete_apps=delete_apps,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterOperationResultResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def unregister_cluster_agent_with_http_info(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        agent_only: Annotated[Optional[StrictBool], Field(description="Disconnect only the agent and keep the cluster's record")] = None,
        delete_apps: Annotated[Optional[StrictBool], Field(description="Delete the applications AstroPulse deployed to the cluster (default: keep them running)")] = None,
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
    ) -> ApiResponse[ClusterOperationResultResponse]:
        """Unregister an agent from a cluster

        Removes the agent from a registered cluster and the cluster from AstroPulse. With agent-only=true, only the agent is disconnected and the cluster's record is kept.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param agent_only: Disconnect only the agent and keep the cluster's record
        :type agent_only: bool
        :param delete_apps: Delete the applications AstroPulse deployed to the cluster (default: keep them running)
        :type delete_apps: bool
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

        _param = self._unregister_cluster_agent_serialize(
            cluster_name=cluster_name,
            agent_only=agent_only,
            delete_apps=delete_apps,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterOperationResultResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def unregister_cluster_agent_without_preload_content(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        agent_only: Annotated[Optional[StrictBool], Field(description="Disconnect only the agent and keep the cluster's record")] = None,
        delete_apps: Annotated[Optional[StrictBool], Field(description="Delete the applications AstroPulse deployed to the cluster (default: keep them running)")] = None,
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
        """Unregister an agent from a cluster

        Removes the agent from a registered cluster and the cluster from AstroPulse. With agent-only=true, only the agent is disconnected and the cluster's record is kept.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param agent_only: Disconnect only the agent and keep the cluster's record
        :type agent_only: bool
        :param delete_apps: Delete the applications AstroPulse deployed to the cluster (default: keep them running)
        :type delete_apps: bool
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

        _param = self._unregister_cluster_agent_serialize(
            cluster_name=cluster_name,
            agent_only=agent_only,
            delete_apps=delete_apps,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterOperationResultResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _unregister_cluster_agent_serialize(
        self,
        cluster_name,
        agent_only,
        delete_apps,
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
        if cluster_name is not None:
            _path_params['clusterName'] = cluster_name
        # process the query parameters
        if agent_only is not None:
            
            _query_params.append(('agent-only', agent_only))
            
        if delete_apps is not None:
            
            _query_params.append(('delete-apps', delete_apps))
            
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
            method='DELETE',
            resource_path='/api/v1/clusters/{clusterName}/agent',
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
    def update_cluster(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        k8s_cluster_update: Annotated[K8sClusterUpdate, Field(description="Cluster update configuration")],
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
    ) -> ClusterUpdateDryRun:
        """Update cluster configuration

        Updates a cluster's Kubernetes version, node groups or tags; AstroPulse picks the update strategy from the provider and the change. Dry-run and report requests return 200 — read validationPassed and preflightChecks; checks that did not finish are named in upgradePlan.unfinishedChecks. The body is decoded strictly: a field the request type does not have is refused with 400, naming it in details.field.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param k8s_cluster_update: Cluster update configuration (required)
        :type k8s_cluster_update: K8sClusterUpdate
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

        _param = self._update_cluster_serialize(
            cluster_name=cluster_name,
            k8s_cluster_update=k8s_cluster_update,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterUpdateDryRun",
            '202': "ClusterUpdate",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '409': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def update_cluster_with_http_info(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        k8s_cluster_update: Annotated[K8sClusterUpdate, Field(description="Cluster update configuration")],
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
    ) -> ApiResponse[ClusterUpdateDryRun]:
        """Update cluster configuration

        Updates a cluster's Kubernetes version, node groups or tags; AstroPulse picks the update strategy from the provider and the change. Dry-run and report requests return 200 — read validationPassed and preflightChecks; checks that did not finish are named in upgradePlan.unfinishedChecks. The body is decoded strictly: a field the request type does not have is refused with 400, naming it in details.field.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param k8s_cluster_update: Cluster update configuration (required)
        :type k8s_cluster_update: K8sClusterUpdate
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

        _param = self._update_cluster_serialize(
            cluster_name=cluster_name,
            k8s_cluster_update=k8s_cluster_update,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterUpdateDryRun",
            '202': "ClusterUpdate",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '409': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def update_cluster_without_preload_content(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        k8s_cluster_update: Annotated[K8sClusterUpdate, Field(description="Cluster update configuration")],
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
        """Update cluster configuration

        Updates a cluster's Kubernetes version, node groups or tags; AstroPulse picks the update strategy from the provider and the change. Dry-run and report requests return 200 — read validationPassed and preflightChecks; checks that did not finish are named in upgradePlan.unfinishedChecks. The body is decoded strictly: a field the request type does not have is refused with 400, naming it in details.field.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param k8s_cluster_update: Cluster update configuration (required)
        :type k8s_cluster_update: K8sClusterUpdate
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

        _param = self._update_cluster_serialize(
            cluster_name=cluster_name,
            k8s_cluster_update=k8s_cluster_update,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterUpdateDryRun",
            '202': "ClusterUpdate",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '409': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _update_cluster_serialize(
        self,
        cluster_name,
        k8s_cluster_update,
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
        if cluster_name is not None:
            _path_params['clusterName'] = cluster_name
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if k8s_cluster_update is not None:
            _body_params = k8s_cluster_update


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'ApiKeyAuth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='PATCH',
            resource_path='/api/v1/clusters/{clusterName}',
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
    def update_cluster_storage(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        set_cluster_storage_request: Annotated[SetClusterStorageRequest, Field(description="Storage bindings")],
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
    ) -> ClusterStorageResponse:
        """Set a cluster's storage bindings

        Replaces every storage binding on the cluster; bindings not listed are removed. Each binding names a storage class the cluster has. Storage classes cannot be created here.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param set_cluster_storage_request: Storage bindings (required)
        :type set_cluster_storage_request: SetClusterStorageRequest
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

        _param = self._update_cluster_storage_serialize(
            cluster_name=cluster_name,
            set_cluster_storage_request=set_cluster_storage_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterStorageResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '409': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def update_cluster_storage_with_http_info(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        set_cluster_storage_request: Annotated[SetClusterStorageRequest, Field(description="Storage bindings")],
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
    ) -> ApiResponse[ClusterStorageResponse]:
        """Set a cluster's storage bindings

        Replaces every storage binding on the cluster; bindings not listed are removed. Each binding names a storage class the cluster has. Storage classes cannot be created here.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param set_cluster_storage_request: Storage bindings (required)
        :type set_cluster_storage_request: SetClusterStorageRequest
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

        _param = self._update_cluster_storage_serialize(
            cluster_name=cluster_name,
            set_cluster_storage_request=set_cluster_storage_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterStorageResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '409': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
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
    def update_cluster_storage_without_preload_content(
        self,
        cluster_name: Annotated[StrictStr, Field(description="Cluster name")],
        set_cluster_storage_request: Annotated[SetClusterStorageRequest, Field(description="Storage bindings")],
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
        """Set a cluster's storage bindings

        Replaces every storage binding on the cluster; bindings not listed are removed. Each binding names a storage class the cluster has. Storage classes cannot be created here.

        :param cluster_name: Cluster name (required)
        :type cluster_name: str
        :param set_cluster_storage_request: Storage bindings (required)
        :type set_cluster_storage_request: SetClusterStorageRequest
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

        _param = self._update_cluster_storage_serialize(
            cluster_name=cluster_name,
            set_cluster_storage_request=set_cluster_storage_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ClusterStorageResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '409': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _update_cluster_storage_serialize(
        self,
        cluster_name,
        set_cluster_storage_request,
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
        if cluster_name is not None:
            _path_params['clusterName'] = cluster_name
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if set_cluster_storage_request is not None:
            _body_params = set_cluster_storage_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'ApiKeyAuth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/api/v1/clusters/{clusterName}/storage',
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


