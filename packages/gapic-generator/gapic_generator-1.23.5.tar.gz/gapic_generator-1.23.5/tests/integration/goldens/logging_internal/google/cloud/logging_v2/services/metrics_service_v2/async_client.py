# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import logging as std_logging
from collections import OrderedDict
import re
from typing import Dict, Callable, Mapping, MutableMapping, MutableSequence, Optional, Sequence, Tuple, Type, Union

from google.cloud.logging_v2 import gapic_version as package_version

from google.api_core.client_options import ClientOptions
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry_async as retries
from google.auth import credentials as ga_credentials   # type: ignore
from google.oauth2 import service_account              # type: ignore


try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

from google.api import distribution_pb2  # type: ignore
from google.api import metric_pb2  # type: ignore
from google.cloud.logging_v2.services.metrics_service_v2 import pagers
from google.cloud.logging_v2.types import logging_metrics
from google.longrunning import operations_pb2 # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from .transports.base import MetricsServiceV2Transport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import MetricsServiceV2GrpcAsyncIOTransport
from .client import BaseMetricsServiceV2Client

try:
    from google.api_core import client_logging  # type: ignore
    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)

class BaseMetricsServiceV2AsyncClient:
    """Service for configuring logs-based metrics."""

    _client: BaseMetricsServiceV2Client

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = BaseMetricsServiceV2Client.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = BaseMetricsServiceV2Client.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = BaseMetricsServiceV2Client._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = BaseMetricsServiceV2Client._DEFAULT_UNIVERSE

    log_metric_path = staticmethod(BaseMetricsServiceV2Client.log_metric_path)
    parse_log_metric_path = staticmethod(BaseMetricsServiceV2Client.parse_log_metric_path)
    common_billing_account_path = staticmethod(BaseMetricsServiceV2Client.common_billing_account_path)
    parse_common_billing_account_path = staticmethod(BaseMetricsServiceV2Client.parse_common_billing_account_path)
    common_folder_path = staticmethod(BaseMetricsServiceV2Client.common_folder_path)
    parse_common_folder_path = staticmethod(BaseMetricsServiceV2Client.parse_common_folder_path)
    common_organization_path = staticmethod(BaseMetricsServiceV2Client.common_organization_path)
    parse_common_organization_path = staticmethod(BaseMetricsServiceV2Client.parse_common_organization_path)
    common_project_path = staticmethod(BaseMetricsServiceV2Client.common_project_path)
    parse_common_project_path = staticmethod(BaseMetricsServiceV2Client.parse_common_project_path)
    common_location_path = staticmethod(BaseMetricsServiceV2Client.common_location_path)
    parse_common_location_path = staticmethod(BaseMetricsServiceV2Client.parse_common_location_path)

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            BaseMetricsServiceV2AsyncClient: The constructed client.
        """
        return BaseMetricsServiceV2Client.from_service_account_info.__func__(BaseMetricsServiceV2AsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            BaseMetricsServiceV2AsyncClient: The constructed client.
        """
        return BaseMetricsServiceV2Client.from_service_account_file.__func__(BaseMetricsServiceV2AsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(cls, client_options: Optional[ClientOptions] = None):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variable is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return BaseMetricsServiceV2Client.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> MetricsServiceV2Transport:
        """Returns the transport used by the client instance.

        Returns:
            MetricsServiceV2Transport: The transport used by the client instance.
        """
        return self._client.transport

    @property
    def api_endpoint(self):
        """Return the API endpoint used by the client instance.

        Returns:
            str: The API endpoint used by the client instance.
        """
        return self._client._api_endpoint

    @property
    def universe_domain(self) -> str:
        """Return the universe domain used by the client instance.

        Returns:
            str: The universe domain used
                by the client instance.
        """
        return self._client._universe_domain

    get_transport_class = BaseMetricsServiceV2Client.get_transport_class

    def __init__(self, *,
            credentials: Optional[ga_credentials.Credentials] = None,
            transport: Optional[Union[str, MetricsServiceV2Transport, Callable[..., MetricsServiceV2Transport]]] = "grpc_asyncio",
            client_options: Optional[ClientOptions] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            ) -> None:
        """Instantiates the base metrics service v2 async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,MetricsServiceV2Transport,Callable[..., MetricsServiceV2Transport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the MetricsServiceV2Transport constructor.
                If set to None, a transport is chosen automatically.
            client_options (Optional[Union[google.api_core.client_options.ClientOptions, dict]]):
                Custom options for the client.

                1. The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client when ``transport`` is
                not explicitly provided. Only if this property is not set and
                ``transport`` was not explicitly provided, the endpoint is
                determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment
                variable, which have one of the following values:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto-switch to the
                default mTLS endpoint if client certificate is present; this is
                the default value).

                2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide a client certificate for mTLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

                3. The ``universe_domain`` property can be used to override the
                default "googleapis.com" universe. Note that ``api_endpoint``
                property still takes precedence; and ``universe_domain`` is
                currently not supported for mTLS.

            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = BaseMetricsServiceV2Client(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,

        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(std_logging.DEBUG):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.logging_v2.BaseMetricsServiceV2AsyncClient`.",
                extra = {
                    "serviceName": "google.logging.v2.MetricsServiceV2",
                    "universeDomain": getattr(self._client._transport._credentials, "universe_domain", ""),
                    "credentialsType": f"{type(self._client._transport._credentials).__module__}.{type(self._client._transport._credentials).__qualname__}",
                    "credentialsInfo": getattr(self.transport._credentials, "get_cred_info", lambda: None)(),
                } if hasattr(self._client._transport, "_credentials") else {
                    "serviceName": "google.logging.v2.MetricsServiceV2",
                    "credentialsType": None,
                }
            )

    async def _list_log_metrics(self,
            request: Optional[Union[logging_metrics.ListLogMetricsRequest, dict]] = None,
            *,
            parent: Optional[str] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
            ) -> pagers._ListLogMetricsAsyncPager:
        r"""Lists logs-based metrics.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import logging_v2

            async def sample__list_log_metrics():
                # Create a client
                client = logging_v2.BaseMetricsServiceV2AsyncClient()

                # Initialize request argument(s)
                request = logging_v2.ListLogMetricsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client._list_log_metrics(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.logging_v2.types.ListLogMetricsRequest, dict]]):
                The request object. The parameters to ListLogMetrics.
            parent (:class:`str`):
                Required. The name of the project containing the
                metrics:

                ::

                    "projects/[PROJECT_ID]"

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.logging_v2.services.metrics_service_v2.pagers._ListLogMetricsAsyncPager:
                Result returned from ListLogMetrics.

                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = len([param for param in flattened_params if param is not None]) > 0
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, logging_metrics.ListLogMetricsRequest):
            request = logging_metrics.ListLogMetricsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport._list_log_metrics]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("parent", request.parent),
            )),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers._ListLogMetricsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def _get_log_metric(self,
            request: Optional[Union[logging_metrics.GetLogMetricRequest, dict]] = None,
            *,
            metric_name: Optional[str] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
            ) -> logging_metrics.LogMetric:
        r"""Gets a logs-based metric.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import logging_v2

            async def sample__get_log_metric():
                # Create a client
                client = logging_v2.BaseMetricsServiceV2AsyncClient()

                # Initialize request argument(s)
                request = logging_v2.GetLogMetricRequest(
                    metric_name="metric_name_value",
                )

                # Make the request
                response = await client._get_log_metric(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.logging_v2.types.GetLogMetricRequest, dict]]):
                The request object. The parameters to GetLogMetric.
            metric_name (:class:`str`):
                Required. The resource name of the desired metric:

                ::

                    "projects/[PROJECT_ID]/metrics/[METRIC_ID]"

                This corresponds to the ``metric_name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.logging_v2.types.LogMetric:
                Describes a logs-based metric. The
                value of the metric is the number of log
                entries that match a logs filter in a
                given time interval.

                Logs-based metrics can also be used to
                extract values from logs and create a
                distribution of the values. The
                distribution records the statistics of
                the extracted values along with an
                optional histogram of the values as
                specified by the bucket options.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [metric_name]
        has_flattened_params = len([param for param in flattened_params if param is not None]) > 0
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, logging_metrics.GetLogMetricRequest):
            request = logging_metrics.GetLogMetricRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if metric_name is not None:
            request.metric_name = metric_name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport._get_log_metric]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("metric_name", request.metric_name),
            )),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def _create_log_metric(self,
            request: Optional[Union[logging_metrics.CreateLogMetricRequest, dict]] = None,
            *,
            parent: Optional[str] = None,
            metric: Optional[logging_metrics.LogMetric] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
            ) -> logging_metrics.LogMetric:
        r"""Creates a logs-based metric.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import logging_v2

            async def sample__create_log_metric():
                # Create a client
                client = logging_v2.BaseMetricsServiceV2AsyncClient()

                # Initialize request argument(s)
                metric = logging_v2.LogMetric()
                metric.name = "name_value"
                metric.filter = "filter_value"

                request = logging_v2.CreateLogMetricRequest(
                    parent="parent_value",
                    metric=metric,
                )

                # Make the request
                response = await client._create_log_metric(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.logging_v2.types.CreateLogMetricRequest, dict]]):
                The request object. The parameters to CreateLogMetric.
            parent (:class:`str`):
                Required. The resource name of the project in which to
                create the metric:

                ::

                    "projects/[PROJECT_ID]"

                The new metric must be provided in the request.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            metric (:class:`google.cloud.logging_v2.types.LogMetric`):
                Required. The new logs-based metric,
                which must not have an identifier that
                already exists.

                This corresponds to the ``metric`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.logging_v2.types.LogMetric:
                Describes a logs-based metric. The
                value of the metric is the number of log
                entries that match a logs filter in a
                given time interval.

                Logs-based metrics can also be used to
                extract values from logs and create a
                distribution of the values. The
                distribution records the statistics of
                the extracted values along with an
                optional histogram of the values as
                specified by the bucket options.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, metric]
        has_flattened_params = len([param for param in flattened_params if param is not None]) > 0
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, logging_metrics.CreateLogMetricRequest):
            request = logging_metrics.CreateLogMetricRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if metric is not None:
            request.metric = metric

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport._create_log_metric]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("parent", request.parent),
            )),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def _update_log_metric(self,
            request: Optional[Union[logging_metrics.UpdateLogMetricRequest, dict]] = None,
            *,
            metric_name: Optional[str] = None,
            metric: Optional[logging_metrics.LogMetric] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
            ) -> logging_metrics.LogMetric:
        r"""Creates or updates a logs-based metric.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import logging_v2

            async def sample__update_log_metric():
                # Create a client
                client = logging_v2.BaseMetricsServiceV2AsyncClient()

                # Initialize request argument(s)
                metric = logging_v2.LogMetric()
                metric.name = "name_value"
                metric.filter = "filter_value"

                request = logging_v2.UpdateLogMetricRequest(
                    metric_name="metric_name_value",
                    metric=metric,
                )

                # Make the request
                response = await client._update_log_metric(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.logging_v2.types.UpdateLogMetricRequest, dict]]):
                The request object. The parameters to UpdateLogMetric.
            metric_name (:class:`str`):
                Required. The resource name of the metric to update:

                ::

                    "projects/[PROJECT_ID]/metrics/[METRIC_ID]"

                The updated metric must be provided in the request and
                it's ``name`` field must be the same as ``[METRIC_ID]``
                If the metric does not exist in ``[PROJECT_ID]``, then a
                new metric is created.

                This corresponds to the ``metric_name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            metric (:class:`google.cloud.logging_v2.types.LogMetric`):
                Required. The updated metric.
                This corresponds to the ``metric`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.logging_v2.types.LogMetric:
                Describes a logs-based metric. The
                value of the metric is the number of log
                entries that match a logs filter in a
                given time interval.

                Logs-based metrics can also be used to
                extract values from logs and create a
                distribution of the values. The
                distribution records the statistics of
                the extracted values along with an
                optional histogram of the values as
                specified by the bucket options.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [metric_name, metric]
        has_flattened_params = len([param for param in flattened_params if param is not None]) > 0
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, logging_metrics.UpdateLogMetricRequest):
            request = logging_metrics.UpdateLogMetricRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if metric_name is not None:
            request.metric_name = metric_name
        if metric is not None:
            request.metric = metric

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport._update_log_metric]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("metric_name", request.metric_name),
            )),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def _delete_log_metric(self,
            request: Optional[Union[logging_metrics.DeleteLogMetricRequest, dict]] = None,
            *,
            metric_name: Optional[str] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
            ) -> None:
        r"""Deletes a logs-based metric.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import logging_v2

            async def sample__delete_log_metric():
                # Create a client
                client = logging_v2.BaseMetricsServiceV2AsyncClient()

                # Initialize request argument(s)
                request = logging_v2.DeleteLogMetricRequest(
                    metric_name="metric_name_value",
                )

                # Make the request
                await client._delete_log_metric(request=request)

        Args:
            request (Optional[Union[google.cloud.logging_v2.types.DeleteLogMetricRequest, dict]]):
                The request object. The parameters to DeleteLogMetric.
            metric_name (:class:`str`):
                Required. The resource name of the metric to delete:

                ::

                    "projects/[PROJECT_ID]/metrics/[METRIC_ID]"

                This corresponds to the ``metric_name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [metric_name]
        has_flattened_params = len([param for param in flattened_params if param is not None]) > 0
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, logging_metrics.DeleteLogMetricRequest):
            request = logging_metrics.DeleteLogMetricRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if metric_name is not None:
            request.metric_name = metric_name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport._delete_log_metric]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("metric_name", request.metric_name),
            )),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def list_operations(
        self,
        request: Optional[operations_pb2.ListOperationsRequest] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operations_pb2.ListOperationsResponse:
        r"""Lists operations that match the specified filter in the request.

        Args:
            request (:class:`~.operations_pb2.ListOperationsRequest`):
                The request object. Request message for
                `ListOperations` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.operations_pb2.ListOperationsResponse:
                Response message for ``ListOperations`` method.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = operations_pb2.ListOperationsRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.list_operations]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def get_operation(
        self,
        request: Optional[operations_pb2.GetOperationRequest] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operations_pb2.Operation:
        r"""Gets the latest state of a long-running operation.

        Args:
            request (:class:`~.operations_pb2.GetOperationRequest`):
                The request object. Request message for
                `GetOperation` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.operations_pb2.Operation:
                An ``Operation`` object.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = operations_pb2.GetOperationRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.get_operation]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def cancel_operation(
        self,
        request: Optional[operations_pb2.CancelOperationRequest] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Starts asynchronous cancellation on a long-running operation.

        The server makes a best effort to cancel the operation, but success
        is not guaranteed.  If the server doesn't support this method, it returns
        `google.rpc.Code.UNIMPLEMENTED`.

        Args:
            request (:class:`~.operations_pb2.CancelOperationRequest`):
                The request object. Request message for
                `CancelOperation` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            None
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = operations_pb2.CancelOperationRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.cancel_operation]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

    async def __aenter__(self) -> "BaseMetricsServiceV2AsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(gapic_version=package_version.__version__)


__all__ = (
    "BaseMetricsServiceV2AsyncClient",
)
