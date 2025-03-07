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
import inspect
import json
import pickle
import logging as std_logging
import warnings
from typing import Awaitable, Callable, Dict, Optional, Sequence, Tuple, Union

from google.api_core import gapic_v1
from google.api_core import grpc_helpers_async
from google.api_core import exceptions as core_exceptions
from google.api_core import retry_async as retries
from google.api_core import operations_v1
from google.auth import credentials as ga_credentials   # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.protobuf.json_format import MessageToJson
import google.protobuf.message

import grpc                        # type: ignore
import proto                       # type: ignore
from grpc.experimental import aio  # type: ignore

from google.cloud.logging_v2.types import logging_config
from google.longrunning import operations_pb2 # type: ignore
from google.protobuf import empty_pb2  # type: ignore
from .base import ConfigServiceV2Transport, DEFAULT_CLIENT_INFO
from .grpc import ConfigServiceV2GrpcTransport

try:
    from google.api_core import client_logging  # type: ignore
    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class _LoggingClientAIOInterceptor(grpc.aio.UnaryUnaryClientInterceptor):  # pragma: NO COVER
    async def intercept_unary_unary(self, continuation, client_call_details, request):
        logging_enabled = CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(std_logging.DEBUG)
        if logging_enabled:  # pragma: NO COVER
            request_metadata = client_call_details.metadata
            if isinstance(request, proto.Message):
                request_payload = type(request).to_json(request)
            elif isinstance(request, google.protobuf.message.Message):
                request_payload = MessageToJson(request)
            else:
                request_payload = f"{type(request).__name__}: {pickle.dumps(request)}"

            request_metadata = {
                key: value.decode("utf-8") if isinstance(value, bytes) else value
                for key, value in request_metadata
            }
            grpc_request = {
                "payload": request_payload,
                "requestMethod": "grpc",
                "metadata": dict(request_metadata),
            }
            _LOGGER.debug(
                f"Sending request for {client_call_details.method}",
                extra = {
                    "serviceName": "google.logging.v2.ConfigServiceV2",
                    "rpcName": str(client_call_details.method),
                    "request": grpc_request,
                    "metadata": grpc_request["metadata"],
                },
            )
        response = await continuation(client_call_details, request)
        if logging_enabled:  # pragma: NO COVER
            response_metadata = await response.trailing_metadata()
            # Convert gRPC metadata `<class 'grpc.aio._metadata.Metadata'>` to list of tuples
            metadata = dict([(k, str(v)) for k, v in response_metadata]) if response_metadata else None
            result = await response
            if isinstance(result, proto.Message):
                response_payload = type(result).to_json(result)
            elif isinstance(result, google.protobuf.message.Message):
                response_payload = MessageToJson(result)
            else:
                response_payload = f"{type(result).__name__}: {pickle.dumps(result)}"
            grpc_response = {
                "payload": response_payload,
                "metadata": metadata,
                "status": "OK",
            }
            _LOGGER.debug(
                f"Received response to rpc {client_call_details.method}.",
                extra = {
                    "serviceName": "google.logging.v2.ConfigServiceV2",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class ConfigServiceV2GrpcAsyncIOTransport(ConfigServiceV2Transport):
    """gRPC AsyncIO backend transport for ConfigServiceV2.

    Service for configuring sinks used to route log entries.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _grpc_channel: aio.Channel
    _stubs: Dict[str, Callable] = {}

    @classmethod
    def create_channel(cls,
                       host: str = 'logging.googleapis.com',
                       credentials: Optional[ga_credentials.Credentials] = None,
                       credentials_file: Optional[str] = None,
                       scopes: Optional[Sequence[str]] = None,
                       quota_project_id: Optional[str] = None,
                       **kwargs) -> aio.Channel:
        """Create and return a gRPC AsyncIO channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            aio.Channel: A gRPC AsyncIO channel object.
        """

        return grpc_helpers_async.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs
        )

    def __init__(self, *,
            host: str = 'logging.googleapis.com',
            credentials: Optional[ga_credentials.Credentials] = None,
            credentials_file: Optional[str] = None,
            scopes: Optional[Sequence[str]] = None,
            channel: Optional[Union[aio.Channel, Callable[..., aio.Channel]]] = None,
            api_mtls_endpoint: Optional[str] = None,
            client_cert_source: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
            ssl_channel_credentials: Optional[grpc.ChannelCredentials] = None,
            client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
            quota_project_id: Optional[str] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool] = False,
            api_audience: Optional[str] = None,
            ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'logging.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if a ``channel`` instance is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if a ``channel`` instance is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            channel (Optional[Union[aio.Channel, Callable[..., aio.Channel]]]):
                A ``Channel`` instance through which to make calls, or a Callable
                that constructs and returns one. If set to None, ``self.create_channel``
                is used to create the channel. If a Callable is given, it will be called
                with the same arguments as used in ``self.create_channel``.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or application default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for the grpc channel. It is ignored if a ``channel`` instance is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure a mutual TLS channel. It is
                ignored if a ``channel`` instance or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}
        self._operations_client: Optional[operations_v1.OperationsAsyncClient] = None

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if isinstance(channel, aio.Channel):
            # Ignore credentials if a channel was passed.
            credentials = None
            self._ignore_credentials = True
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None
        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience,
        )

        if not self._grpc_channel:
            # initialize with the provided callable or the default channel
            channel_init = channel or type(self).create_channel
            self._grpc_channel = channel_init(
                self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                # Set ``credentials_file`` to ``None`` here as
                # the credentials that we saved earlier should be used.
                credentials_file=None,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        self._interceptor = _LoggingClientAIOInterceptor()
        self._grpc_channel._unary_unary_interceptors.append(self._interceptor)
        self._logged_channel = self._grpc_channel
        self._wrap_with_kind = "kind" in inspect.signature(gapic_v1.method_async.wrap_method).parameters
        # Wrap messages. This must be done after self._logged_channel exists
        self._prep_wrapped_messages(client_info)

    @property
    def grpc_channel(self) -> aio.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Return the channel from cache.
        return self._grpc_channel

    @property
    def operations_client(self) -> operations_v1.OperationsAsyncClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Quick check: Only create a new client if we do not already have one.
        if self._operations_client is None:
            self._operations_client = operations_v1.OperationsAsyncClient(
                self._logged_channel
            )

        # Return the client from cache.
        return self._operations_client

    @property
    def list_buckets(self) -> Callable[
            [logging_config.ListBucketsRequest],
            Awaitable[logging_config.ListBucketsResponse]]:
        r"""Return a callable for the list buckets method over gRPC.

        Lists log buckets.

        Returns:
            Callable[[~.ListBucketsRequest],
                    Awaitable[~.ListBucketsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_buckets' not in self._stubs:
            self._stubs['list_buckets'] = self._logged_channel.unary_unary(
                '/google.logging.v2.ConfigServiceV2/ListBuckets',
                request_serializer=logging_config.ListBucketsRequest.serialize,
                response_deserializer=logging_config.ListBucketsResponse.deserialize,
            )
        return self._stubs['list_buckets']

    @property
    def get_bucket(self) -> Callable[
            [logging_config.GetBucketRequest],
            Awaitable[logging_config.LogBucket]]:
        r"""Return a callable for the get bucket method over gRPC.

        Gets a log bucket.

        Returns:
            Callable[[~.GetBucketRequest],
                    Awaitable[~.LogBucket]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_bucket' not in self._stubs:
            self._stubs['get_bucket'] = self._logged_channel.unary_unary(
                '/google.logging.v2.ConfigServiceV2/GetBucket',
                request_serializer=logging_config.GetBucketRequest.serialize,
                response_deserializer=logging_config.LogBucket.deserialize,
            )
        return self._stubs['get_bucket']

    @property
    def create_bucket_async(self) -> Callable[
            [logging_config.CreateBucketRequest],
            Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the create bucket async method over gRPC.

        Creates a log bucket asynchronously that can be used
        to store log entries.
        After a bucket has been created, the bucket's location
        cannot be changed.

        Returns:
            Callable[[~.CreateBucketRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'create_bucket_async' not in self._stubs:
            self._stubs['create_bucket_async'] = self._logged_channel.unary_unary(
                '/google.logging.v2.ConfigServiceV2/CreateBucketAsync',
                request_serializer=logging_config.CreateBucketRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs['create_bucket_async']

    @property
    def update_bucket_async(self) -> Callable[
            [logging_config.UpdateBucketRequest],
            Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the update bucket async method over gRPC.

        Updates a log bucket asynchronously.

        If the bucket has a ``lifecycle_state`` of ``DELETE_REQUESTED``,
        then ``FAILED_PRECONDITION`` will be returned.

        After a bucket has been created, the bucket's location cannot be
        changed.

        Returns:
            Callable[[~.UpdateBucketRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'update_bucket_async' not in self._stubs:
            self._stubs['update_bucket_async'] = self._logged_channel.unary_unary(
                '/google.logging.v2.ConfigServiceV2/UpdateBucketAsync',
                request_serializer=logging_config.UpdateBucketRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs['update_bucket_async']

    @property
    def create_bucket(self) -> Callable[
            [logging_config.CreateBucketRequest],
            Awaitable[logging_config.LogBucket]]:
        r"""Return a callable for the create bucket method over gRPC.

        Creates a log bucket that can be used to store log
        entries. After a bucket has been created, the bucket's
        location cannot be changed.

        Returns:
            Callable[[~.CreateBucketRequest],
                    Awaitable[~.LogBucket]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'create_bucket' not in self._stubs:
            self._stubs['create_bucket'] = self._logged_channel.unary_unary(
                '/google.logging.v2.ConfigServiceV2/CreateBucket',
                request_serializer=logging_config.CreateBucketRequest.serialize,
                response_deserializer=logging_config.LogBucket.deserialize,
            )
        return self._stubs['create_bucket']

    @property
    def update_bucket(self) -> Callable[
            [logging_config.UpdateBucketRequest],
            Awaitable[logging_config.LogBucket]]:
        r"""Return a callable for the update bucket method over gRPC.

        Updates a log bucket.

        If the bucket has a ``lifecycle_state`` of ``DELETE_REQUESTED``,
        then ``FAILED_PRECONDITION`` will be returned.

        After a bucket has been created, the bucket's location cannot be
        changed.

        Returns:
            Callable[[~.UpdateBucketRequest],
                    Awaitable[~.LogBucket]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'update_bucket' not in self._stubs:
            self._stubs['update_bucket'] = self._logged_channel.unary_unary(
                '/google.logging.v2.ConfigServiceV2/UpdateBucket',
                request_serializer=logging_config.UpdateBucketRequest.serialize,
                response_deserializer=logging_config.LogBucket.deserialize,
            )
        return self._stubs['update_bucket']

    @property
    def delete_bucket(self) -> Callable[
            [logging_config.DeleteBucketRequest],
            Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the delete bucket method over gRPC.

        Deletes a log bucket.

        Changes the bucket's ``lifecycle_state`` to the
        ``DELETE_REQUESTED`` state. After 7 days, the bucket will be
        purged and all log entries in the bucket will be permanently
        deleted.

        Returns:
            Callable[[~.DeleteBucketRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'delete_bucket' not in self._stubs:
            self._stubs['delete_bucket'] = self._logged_channel.unary_unary(
                '/google.logging.v2.ConfigServiceV2/DeleteBucket',
                request_serializer=logging_config.DeleteBucketRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs['delete_bucket']

    @property
    def undelete_bucket(self) -> Callable[
            [logging_config.UndeleteBucketRequest],
            Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the undelete bucket method over gRPC.

        Undeletes a log bucket. A bucket that has been
        deleted can be undeleted within the grace period of 7
        days.

        Returns:
            Callable[[~.UndeleteBucketRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'undelete_bucket' not in self._stubs:
            self._stubs['undelete_bucket'] = self._logged_channel.unary_unary(
                '/google.logging.v2.ConfigServiceV2/UndeleteBucket',
                request_serializer=logging_config.UndeleteBucketRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs['undelete_bucket']

    @property
    def list_views(self) -> Callable[
            [logging_config.ListViewsRequest],
            Awaitable[logging_config.ListViewsResponse]]:
        r"""Return a callable for the list views method over gRPC.

        Lists views on a log bucket.

        Returns:
            Callable[[~.ListViewsRequest],
                    Awaitable[~.ListViewsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_views' not in self._stubs:
            self._stubs['list_views'] = self._logged_channel.unary_unary(
                '/google.logging.v2.ConfigServiceV2/ListViews',
                request_serializer=logging_config.ListViewsRequest.serialize,
                response_deserializer=logging_config.ListViewsResponse.deserialize,
            )
        return self._stubs['list_views']

    @property
    def get_view(self) -> Callable[
            [logging_config.GetViewRequest],
            Awaitable[logging_config.LogView]]:
        r"""Return a callable for the get view method over gRPC.

        Gets a view on a log bucket..

        Returns:
            Callable[[~.GetViewRequest],
                    Awaitable[~.LogView]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_view' not in self._stubs:
            self._stubs['get_view'] = self._logged_channel.unary_unary(
                '/google.logging.v2.ConfigServiceV2/GetView',
                request_serializer=logging_config.GetViewRequest.serialize,
                response_deserializer=logging_config.LogView.deserialize,
            )
        return self._stubs['get_view']

    @property
    def create_view(self) -> Callable[
            [logging_config.CreateViewRequest],
            Awaitable[logging_config.LogView]]:
        r"""Return a callable for the create view method over gRPC.

        Creates a view over log entries in a log bucket. A
        bucket may contain a maximum of 30 views.

        Returns:
            Callable[[~.CreateViewRequest],
                    Awaitable[~.LogView]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'create_view' not in self._stubs:
            self._stubs['create_view'] = self._logged_channel.unary_unary(
                '/google.logging.v2.ConfigServiceV2/CreateView',
                request_serializer=logging_config.CreateViewRequest.serialize,
                response_deserializer=logging_config.LogView.deserialize,
            )
        return self._stubs['create_view']

    @property
    def update_view(self) -> Callable[
            [logging_config.UpdateViewRequest],
            Awaitable[logging_config.LogView]]:
        r"""Return a callable for the update view method over gRPC.

        Updates a view on a log bucket. This method replaces the
        following fields in the existing view with values from the new
        view: ``filter``. If an ``UNAVAILABLE`` error is returned, this
        indicates that system is not in a state where it can update the
        view. If this occurs, please try again in a few minutes.

        Returns:
            Callable[[~.UpdateViewRequest],
                    Awaitable[~.LogView]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'update_view' not in self._stubs:
            self._stubs['update_view'] = self._logged_channel.unary_unary(
                '/google.logging.v2.ConfigServiceV2/UpdateView',
                request_serializer=logging_config.UpdateViewRequest.serialize,
                response_deserializer=logging_config.LogView.deserialize,
            )
        return self._stubs['update_view']

    @property
    def delete_view(self) -> Callable[
            [logging_config.DeleteViewRequest],
            Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the delete view method over gRPC.

        Deletes a view on a log bucket. If an ``UNAVAILABLE`` error is
        returned, this indicates that system is not in a state where it
        can delete the view. If this occurs, please try again in a few
        minutes.

        Returns:
            Callable[[~.DeleteViewRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'delete_view' not in self._stubs:
            self._stubs['delete_view'] = self._logged_channel.unary_unary(
                '/google.logging.v2.ConfigServiceV2/DeleteView',
                request_serializer=logging_config.DeleteViewRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs['delete_view']

    @property
    def list_sinks(self) -> Callable[
            [logging_config.ListSinksRequest],
            Awaitable[logging_config.ListSinksResponse]]:
        r"""Return a callable for the list sinks method over gRPC.

        Lists sinks.

        Returns:
            Callable[[~.ListSinksRequest],
                    Awaitable[~.ListSinksResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_sinks' not in self._stubs:
            self._stubs['list_sinks'] = self._logged_channel.unary_unary(
                '/google.logging.v2.ConfigServiceV2/ListSinks',
                request_serializer=logging_config.ListSinksRequest.serialize,
                response_deserializer=logging_config.ListSinksResponse.deserialize,
            )
        return self._stubs['list_sinks']

    @property
    def get_sink(self) -> Callable[
            [logging_config.GetSinkRequest],
            Awaitable[logging_config.LogSink]]:
        r"""Return a callable for the get sink method over gRPC.

        Gets a sink.

        Returns:
            Callable[[~.GetSinkRequest],
                    Awaitable[~.LogSink]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_sink' not in self._stubs:
            self._stubs['get_sink'] = self._logged_channel.unary_unary(
                '/google.logging.v2.ConfigServiceV2/GetSink',
                request_serializer=logging_config.GetSinkRequest.serialize,
                response_deserializer=logging_config.LogSink.deserialize,
            )
        return self._stubs['get_sink']

    @property
    def create_sink(self) -> Callable[
            [logging_config.CreateSinkRequest],
            Awaitable[logging_config.LogSink]]:
        r"""Return a callable for the create sink method over gRPC.

        Creates a sink that exports specified log entries to a
        destination. The export of newly-ingested log entries begins
        immediately, unless the sink's ``writer_identity`` is not
        permitted to write to the destination. A sink can export log
        entries only from the resource owning the sink.

        Returns:
            Callable[[~.CreateSinkRequest],
                    Awaitable[~.LogSink]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'create_sink' not in self._stubs:
            self._stubs['create_sink'] = self._logged_channel.unary_unary(
                '/google.logging.v2.ConfigServiceV2/CreateSink',
                request_serializer=logging_config.CreateSinkRequest.serialize,
                response_deserializer=logging_config.LogSink.deserialize,
            )
        return self._stubs['create_sink']

    @property
    def update_sink(self) -> Callable[
            [logging_config.UpdateSinkRequest],
            Awaitable[logging_config.LogSink]]:
        r"""Return a callable for the update sink method over gRPC.

        Updates a sink. This method replaces the following fields in the
        existing sink with values from the new sink: ``destination``,
        and ``filter``.

        The updated sink might also have a new ``writer_identity``; see
        the ``unique_writer_identity`` field.

        Returns:
            Callable[[~.UpdateSinkRequest],
                    Awaitable[~.LogSink]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'update_sink' not in self._stubs:
            self._stubs['update_sink'] = self._logged_channel.unary_unary(
                '/google.logging.v2.ConfigServiceV2/UpdateSink',
                request_serializer=logging_config.UpdateSinkRequest.serialize,
                response_deserializer=logging_config.LogSink.deserialize,
            )
        return self._stubs['update_sink']

    @property
    def delete_sink(self) -> Callable[
            [logging_config.DeleteSinkRequest],
            Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the delete sink method over gRPC.

        Deletes a sink. If the sink has a unique ``writer_identity``,
        then that service account is also deleted.

        Returns:
            Callable[[~.DeleteSinkRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'delete_sink' not in self._stubs:
            self._stubs['delete_sink'] = self._logged_channel.unary_unary(
                '/google.logging.v2.ConfigServiceV2/DeleteSink',
                request_serializer=logging_config.DeleteSinkRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs['delete_sink']

    @property
    def create_link(self) -> Callable[
            [logging_config.CreateLinkRequest],
            Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the create link method over gRPC.

        Asynchronously creates a linked dataset in BigQuery
        which makes it possible to use BigQuery to read the logs
        stored in the log bucket. A log bucket may currently
        only contain one link.

        Returns:
            Callable[[~.CreateLinkRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'create_link' not in self._stubs:
            self._stubs['create_link'] = self._logged_channel.unary_unary(
                '/google.logging.v2.ConfigServiceV2/CreateLink',
                request_serializer=logging_config.CreateLinkRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs['create_link']

    @property
    def delete_link(self) -> Callable[
            [logging_config.DeleteLinkRequest],
            Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the delete link method over gRPC.

        Deletes a link. This will also delete the
        corresponding BigQuery linked dataset.

        Returns:
            Callable[[~.DeleteLinkRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'delete_link' not in self._stubs:
            self._stubs['delete_link'] = self._logged_channel.unary_unary(
                '/google.logging.v2.ConfigServiceV2/DeleteLink',
                request_serializer=logging_config.DeleteLinkRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs['delete_link']

    @property
    def list_links(self) -> Callable[
            [logging_config.ListLinksRequest],
            Awaitable[logging_config.ListLinksResponse]]:
        r"""Return a callable for the list links method over gRPC.

        Lists links.

        Returns:
            Callable[[~.ListLinksRequest],
                    Awaitable[~.ListLinksResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_links' not in self._stubs:
            self._stubs['list_links'] = self._logged_channel.unary_unary(
                '/google.logging.v2.ConfigServiceV2/ListLinks',
                request_serializer=logging_config.ListLinksRequest.serialize,
                response_deserializer=logging_config.ListLinksResponse.deserialize,
            )
        return self._stubs['list_links']

    @property
    def get_link(self) -> Callable[
            [logging_config.GetLinkRequest],
            Awaitable[logging_config.Link]]:
        r"""Return a callable for the get link method over gRPC.

        Gets a link.

        Returns:
            Callable[[~.GetLinkRequest],
                    Awaitable[~.Link]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_link' not in self._stubs:
            self._stubs['get_link'] = self._logged_channel.unary_unary(
                '/google.logging.v2.ConfigServiceV2/GetLink',
                request_serializer=logging_config.GetLinkRequest.serialize,
                response_deserializer=logging_config.Link.deserialize,
            )
        return self._stubs['get_link']

    @property
    def list_exclusions(self) -> Callable[
            [logging_config.ListExclusionsRequest],
            Awaitable[logging_config.ListExclusionsResponse]]:
        r"""Return a callable for the list exclusions method over gRPC.

        Lists all the exclusions on the \_Default sink in a parent
        resource.

        Returns:
            Callable[[~.ListExclusionsRequest],
                    Awaitable[~.ListExclusionsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_exclusions' not in self._stubs:
            self._stubs['list_exclusions'] = self._logged_channel.unary_unary(
                '/google.logging.v2.ConfigServiceV2/ListExclusions',
                request_serializer=logging_config.ListExclusionsRequest.serialize,
                response_deserializer=logging_config.ListExclusionsResponse.deserialize,
            )
        return self._stubs['list_exclusions']

    @property
    def get_exclusion(self) -> Callable[
            [logging_config.GetExclusionRequest],
            Awaitable[logging_config.LogExclusion]]:
        r"""Return a callable for the get exclusion method over gRPC.

        Gets the description of an exclusion in the \_Default sink.

        Returns:
            Callable[[~.GetExclusionRequest],
                    Awaitable[~.LogExclusion]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_exclusion' not in self._stubs:
            self._stubs['get_exclusion'] = self._logged_channel.unary_unary(
                '/google.logging.v2.ConfigServiceV2/GetExclusion',
                request_serializer=logging_config.GetExclusionRequest.serialize,
                response_deserializer=logging_config.LogExclusion.deserialize,
            )
        return self._stubs['get_exclusion']

    @property
    def create_exclusion(self) -> Callable[
            [logging_config.CreateExclusionRequest],
            Awaitable[logging_config.LogExclusion]]:
        r"""Return a callable for the create exclusion method over gRPC.

        Creates a new exclusion in the \_Default sink in a specified
        parent resource. Only log entries belonging to that resource can
        be excluded. You can have up to 10 exclusions in a resource.

        Returns:
            Callable[[~.CreateExclusionRequest],
                    Awaitable[~.LogExclusion]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'create_exclusion' not in self._stubs:
            self._stubs['create_exclusion'] = self._logged_channel.unary_unary(
                '/google.logging.v2.ConfigServiceV2/CreateExclusion',
                request_serializer=logging_config.CreateExclusionRequest.serialize,
                response_deserializer=logging_config.LogExclusion.deserialize,
            )
        return self._stubs['create_exclusion']

    @property
    def update_exclusion(self) -> Callable[
            [logging_config.UpdateExclusionRequest],
            Awaitable[logging_config.LogExclusion]]:
        r"""Return a callable for the update exclusion method over gRPC.

        Changes one or more properties of an existing exclusion in the
        \_Default sink.

        Returns:
            Callable[[~.UpdateExclusionRequest],
                    Awaitable[~.LogExclusion]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'update_exclusion' not in self._stubs:
            self._stubs['update_exclusion'] = self._logged_channel.unary_unary(
                '/google.logging.v2.ConfigServiceV2/UpdateExclusion',
                request_serializer=logging_config.UpdateExclusionRequest.serialize,
                response_deserializer=logging_config.LogExclusion.deserialize,
            )
        return self._stubs['update_exclusion']

    @property
    def delete_exclusion(self) -> Callable[
            [logging_config.DeleteExclusionRequest],
            Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the delete exclusion method over gRPC.

        Deletes an exclusion in the \_Default sink.

        Returns:
            Callable[[~.DeleteExclusionRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'delete_exclusion' not in self._stubs:
            self._stubs['delete_exclusion'] = self._logged_channel.unary_unary(
                '/google.logging.v2.ConfigServiceV2/DeleteExclusion',
                request_serializer=logging_config.DeleteExclusionRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs['delete_exclusion']

    @property
    def get_cmek_settings(self) -> Callable[
            [logging_config.GetCmekSettingsRequest],
            Awaitable[logging_config.CmekSettings]]:
        r"""Return a callable for the get cmek settings method over gRPC.

        Gets the Logging CMEK settings for the given resource.

        Note: CMEK for the Log Router can be configured for Google Cloud
        projects, folders, organizations and billing accounts. Once
        configured for an organization, it applies to all projects and
        folders in the Google Cloud organization.

        See `Enabling CMEK for Log
        Router <https://cloud.google.com/logging/docs/routing/managed-encryption>`__
        for more information.

        Returns:
            Callable[[~.GetCmekSettingsRequest],
                    Awaitable[~.CmekSettings]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_cmek_settings' not in self._stubs:
            self._stubs['get_cmek_settings'] = self._logged_channel.unary_unary(
                '/google.logging.v2.ConfigServiceV2/GetCmekSettings',
                request_serializer=logging_config.GetCmekSettingsRequest.serialize,
                response_deserializer=logging_config.CmekSettings.deserialize,
            )
        return self._stubs['get_cmek_settings']

    @property
    def update_cmek_settings(self) -> Callable[
            [logging_config.UpdateCmekSettingsRequest],
            Awaitable[logging_config.CmekSettings]]:
        r"""Return a callable for the update cmek settings method over gRPC.

        Updates the Log Router CMEK settings for the given resource.

        Note: CMEK for the Log Router can currently only be configured
        for Google Cloud organizations. Once configured, it applies to
        all projects and folders in the Google Cloud organization.

        [UpdateCmekSettings][google.logging.v2.ConfigServiceV2.UpdateCmekSettings]
        will fail if 1) ``kms_key_name`` is invalid, or 2) the
        associated service account does not have the required
        ``roles/cloudkms.cryptoKeyEncrypterDecrypter`` role assigned for
        the key, or 3) access to the key is disabled.

        See `Enabling CMEK for Log
        Router <https://cloud.google.com/logging/docs/routing/managed-encryption>`__
        for more information.

        Returns:
            Callable[[~.UpdateCmekSettingsRequest],
                    Awaitable[~.CmekSettings]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'update_cmek_settings' not in self._stubs:
            self._stubs['update_cmek_settings'] = self._logged_channel.unary_unary(
                '/google.logging.v2.ConfigServiceV2/UpdateCmekSettings',
                request_serializer=logging_config.UpdateCmekSettingsRequest.serialize,
                response_deserializer=logging_config.CmekSettings.deserialize,
            )
        return self._stubs['update_cmek_settings']

    @property
    def get_settings(self) -> Callable[
            [logging_config.GetSettingsRequest],
            Awaitable[logging_config.Settings]]:
        r"""Return a callable for the get settings method over gRPC.

        Gets the Log Router settings for the given resource.

        Note: Settings for the Log Router can be get for Google Cloud
        projects, folders, organizations and billing accounts. Currently
        it can only be configured for organizations. Once configured for
        an organization, it applies to all projects and folders in the
        Google Cloud organization.

        See `Enabling CMEK for Log
        Router <https://cloud.google.com/logging/docs/routing/managed-encryption>`__
        for more information.

        Returns:
            Callable[[~.GetSettingsRequest],
                    Awaitable[~.Settings]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_settings' not in self._stubs:
            self._stubs['get_settings'] = self._logged_channel.unary_unary(
                '/google.logging.v2.ConfigServiceV2/GetSettings',
                request_serializer=logging_config.GetSettingsRequest.serialize,
                response_deserializer=logging_config.Settings.deserialize,
            )
        return self._stubs['get_settings']

    @property
    def update_settings(self) -> Callable[
            [logging_config.UpdateSettingsRequest],
            Awaitable[logging_config.Settings]]:
        r"""Return a callable for the update settings method over gRPC.

        Updates the Log Router settings for the given resource.

        Note: Settings for the Log Router can currently only be
        configured for Google Cloud organizations. Once configured, it
        applies to all projects and folders in the Google Cloud
        organization.

        [UpdateSettings][google.logging.v2.ConfigServiceV2.UpdateSettings]
        will fail if 1) ``kms_key_name`` is invalid, or 2) the
        associated service account does not have the required
        ``roles/cloudkms.cryptoKeyEncrypterDecrypter`` role assigned for
        the key, or 3) access to the key is disabled. 4) ``location_id``
        is not supported by Logging. 5) ``location_id`` violate
        OrgPolicy.

        See `Enabling CMEK for Log
        Router <https://cloud.google.com/logging/docs/routing/managed-encryption>`__
        for more information.

        Returns:
            Callable[[~.UpdateSettingsRequest],
                    Awaitable[~.Settings]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'update_settings' not in self._stubs:
            self._stubs['update_settings'] = self._logged_channel.unary_unary(
                '/google.logging.v2.ConfigServiceV2/UpdateSettings',
                request_serializer=logging_config.UpdateSettingsRequest.serialize,
                response_deserializer=logging_config.Settings.deserialize,
            )
        return self._stubs['update_settings']

    @property
    def copy_log_entries(self) -> Callable[
            [logging_config.CopyLogEntriesRequest],
            Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the copy log entries method over gRPC.

        Copies a set of log entries from a log bucket to a
        Cloud Storage bucket.

        Returns:
            Callable[[~.CopyLogEntriesRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'copy_log_entries' not in self._stubs:
            self._stubs['copy_log_entries'] = self._logged_channel.unary_unary(
                '/google.logging.v2.ConfigServiceV2/CopyLogEntries',
                request_serializer=logging_config.CopyLogEntriesRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs['copy_log_entries']

    def _prep_wrapped_messages(self, client_info):
        """ Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.list_buckets: self._wrap_method(
                self.list_buckets,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_bucket: self._wrap_method(
                self.get_bucket,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_bucket_async: self._wrap_method(
                self.create_bucket_async,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_bucket_async: self._wrap_method(
                self.update_bucket_async,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_bucket: self._wrap_method(
                self.create_bucket,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_bucket: self._wrap_method(
                self.update_bucket,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_bucket: self._wrap_method(
                self.delete_bucket,
                default_timeout=None,
                client_info=client_info,
            ),
            self.undelete_bucket: self._wrap_method(
                self.undelete_bucket,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_views: self._wrap_method(
                self.list_views,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_view: self._wrap_method(
                self.get_view,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_view: self._wrap_method(
                self.create_view,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_view: self._wrap_method(
                self.update_view,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_view: self._wrap_method(
                self.delete_view,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_sinks: self._wrap_method(
                self.list_sinks,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.InternalServerError,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_sink: self._wrap_method(
                self.get_sink,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.InternalServerError,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_sink: self._wrap_method(
                self.create_sink,
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.update_sink: self._wrap_method(
                self.update_sink,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.InternalServerError,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_sink: self._wrap_method(
                self.delete_sink,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.InternalServerError,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_link: self._wrap_method(
                self.create_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_link: self._wrap_method(
                self.delete_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_links: self._wrap_method(
                self.list_links,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_link: self._wrap_method(
                self.get_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_exclusions: self._wrap_method(
                self.list_exclusions,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.InternalServerError,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_exclusion: self._wrap_method(
                self.get_exclusion,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.InternalServerError,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_exclusion: self._wrap_method(
                self.create_exclusion,
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.update_exclusion: self._wrap_method(
                self.update_exclusion,
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.delete_exclusion: self._wrap_method(
                self.delete_exclusion,
                default_retry=retries.AsyncRetry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.InternalServerError,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_cmek_settings: self._wrap_method(
                self.get_cmek_settings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_cmek_settings: self._wrap_method(
                self.update_cmek_settings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_settings: self._wrap_method(
                self.get_settings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_settings: self._wrap_method(
                self.update_settings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.copy_log_entries: self._wrap_method(
                self.copy_log_entries,
                default_timeout=None,
                client_info=client_info,
            ),
            self.cancel_operation: self._wrap_method(
                self.cancel_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_operation: self._wrap_method(
                self.get_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_operations: self._wrap_method(
                self.list_operations,
                default_timeout=None,
                client_info=client_info,
            ),
        }

    def _wrap_method(self, func, *args, **kwargs):
        if self._wrap_with_kind:  # pragma: NO COVER
            kwargs["kind"] = self.kind
        return gapic_v1.method_async.wrap_method(func, *args, **kwargs)

    def close(self):
        return self._logged_channel.close()

    @property
    def kind(self) -> str:
        return "grpc_asyncio"

    @property
    def cancel_operation(
        self,
    ) -> Callable[[operations_pb2.CancelOperationRequest], None]:
        r"""Return a callable for the cancel_operation method over gRPC.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "cancel_operation" not in self._stubs:
            self._stubs["cancel_operation"] = self._logged_channel.unary_unary(
                "/google.longrunning.Operations/CancelOperation",
                request_serializer=operations_pb2.CancelOperationRequest.SerializeToString,
                response_deserializer=None,
            )
        return self._stubs["cancel_operation"]

    @property
    def get_operation(
        self,
    ) -> Callable[[operations_pb2.GetOperationRequest], operations_pb2.Operation]:
        r"""Return a callable for the get_operation method over gRPC.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_operation" not in self._stubs:
            self._stubs["get_operation"] = self._logged_channel.unary_unary(
                "/google.longrunning.Operations/GetOperation",
                request_serializer=operations_pb2.GetOperationRequest.SerializeToString,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["get_operation"]

    @property
    def list_operations(
        self,
    ) -> Callable[[operations_pb2.ListOperationsRequest], operations_pb2.ListOperationsResponse]:
        r"""Return a callable for the list_operations method over gRPC.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_operations" not in self._stubs:
            self._stubs["list_operations"] = self._logged_channel.unary_unary(
                "/google.longrunning.Operations/ListOperations",
                request_serializer=operations_pb2.ListOperationsRequest.SerializeToString,
                response_deserializer=operations_pb2.ListOperationsResponse.FromString,
            )
        return self._stubs["list_operations"]


__all__ = (
    'ConfigServiceV2GrpcAsyncIOTransport',
)
