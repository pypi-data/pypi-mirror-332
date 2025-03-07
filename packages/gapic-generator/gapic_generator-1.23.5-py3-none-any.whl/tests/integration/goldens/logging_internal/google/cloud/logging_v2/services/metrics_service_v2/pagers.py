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
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.api_core import retry_async as retries_async
from typing import Any, AsyncIterator, Awaitable, Callable, Sequence, Tuple, Optional, Iterator, Union
try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault, None]
    OptionalAsyncRetry = Union[retries_async.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object, None]  # type: ignore
    OptionalAsyncRetry = Union[retries_async.AsyncRetry, object, None]  # type: ignore

from google.cloud.logging_v2.types import logging_metrics


class _ListLogMetricsPager:
    """A pager for iterating through ``_list_log_metrics`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.logging_v2.types.ListLogMetricsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``metrics`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``_ListLogMetrics`` requests and continue to iterate
    through the ``metrics`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.logging_v2.types.ListLogMetricsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., logging_metrics.ListLogMetricsResponse],
            request: logging_metrics.ListLogMetricsRequest,
            response: logging_metrics.ListLogMetricsResponse,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.logging_v2.types.ListLogMetricsRequest):
                The initial request object.
            response (google.cloud.logging_v2.types.ListLogMetricsResponse):
                The initial response object.
            retry (google.api_core.retry.Retry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = logging_metrics.ListLogMetricsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[logging_metrics.ListLogMetricsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, retry=self._retry, timeout=self._timeout, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[logging_metrics.LogMetric]:
        for page in self.pages:
            yield from page.metrics

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class _ListLogMetricsAsyncPager:
    """A pager for iterating through ``_list_log_metrics`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.logging_v2.types.ListLogMetricsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``metrics`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``_ListLogMetrics`` requests and continue to iterate
    through the ``metrics`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.logging_v2.types.ListLogMetricsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[logging_metrics.ListLogMetricsResponse]],
            request: logging_metrics.ListLogMetricsRequest,
            response: logging_metrics.ListLogMetricsResponse,
            *,
            retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.logging_v2.types.ListLogMetricsRequest):
                The initial request object.
            response (google.cloud.logging_v2.types.ListLogMetricsResponse):
                The initial response object.
            retry (google.api_core.retry.AsyncRetry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = logging_metrics.ListLogMetricsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[logging_metrics.ListLogMetricsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, retry=self._retry, timeout=self._timeout, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[logging_metrics.LogMetric]:
        async def async_generator():
            async for page in self.pages:
                for response in page.metrics:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)
