# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
from ..core.request_options import RequestOptions
from ..errors.not_found_error import NotFoundError
from ..errors.not_implemented_error import NotImplementedError
from ..types.feedback_score_batch_item import FeedbackScoreBatchItem
from ..types.feedback_score_source import FeedbackScoreSource
from ..types.json_node import JsonNode
from ..types.json_node_write import JsonNodeWrite
from ..types.span_page_public import SpanPagePublic
from ..types.span_public import SpanPublic
from ..types.span_write import SpanWrite
from ..types.span_write_type import SpanWriteType
from .types.get_spans_by_project_request_type import GetSpansByProjectRequestType

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class SpansClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def add_span_feedback_score(
        self,
        id: str,
        *,
        name: str,
        value: float,
        source: FeedbackScoreSource,
        category_name: typing.Optional[str] = OMIT,
        reason: typing.Optional[str] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        last_updated_at: typing.Optional[dt.datetime] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        last_updated_by: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Add span feedback score

        Parameters
        ----------
        id : str

        name : str

        value : float

        source : FeedbackScoreSource

        category_name : typing.Optional[str]

        reason : typing.Optional[str]

        created_at : typing.Optional[dt.datetime]

        last_updated_at : typing.Optional[dt.datetime]

        created_by : typing.Optional[str]

        last_updated_by : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from Opik.client import OpikApi

        client = OpikApi()
        client.spans.add_span_feedback_score(
            id="id",
            name="name",
            value=1.1,
            source="ui",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/private/spans/{jsonable_encoder(id)}/feedback-scores",
            method="PUT",
            json={
                "name": name,
                "category_name": category_name,
                "value": value,
                "reason": reason,
                "source": source,
                "created_at": created_at,
                "last_updated_at": last_updated_at,
                "created_by": created_by,
                "last_updated_by": last_updated_by,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_spans_by_project(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        project_name: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        trace_id: typing.Optional[str] = None,
        type: typing.Optional[GetSpansByProjectRequestType] = None,
        filters: typing.Optional[str] = None,
        truncate: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SpanPagePublic:
        """
        Get spans by project_name or project_id and optionally by trace_id and/or type

        Parameters
        ----------
        page : typing.Optional[int]

        size : typing.Optional[int]

        project_name : typing.Optional[str]

        project_id : typing.Optional[str]

        trace_id : typing.Optional[str]

        type : typing.Optional[GetSpansByProjectRequestType]

        filters : typing.Optional[str]

        truncate : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpanPagePublic
            Spans resource

        Examples
        --------
        from Opik.client import OpikApi

        client = OpikApi()
        client.spans.get_spans_by_project()
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/private/spans",
            method="GET",
            params={
                "page": page,
                "size": size,
                "project_name": project_name,
                "project_id": project_id,
                "trace_id": trace_id,
                "type": type,
                "filters": filters,
                "truncate": truncate,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(SpanPagePublic, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_span(
        self,
        *,
        trace_id: str,
        name: str,
        type: SpanWriteType,
        start_time: dt.datetime,
        id: typing.Optional[str] = OMIT,
        project_name: typing.Optional[str] = OMIT,
        parent_span_id: typing.Optional[str] = OMIT,
        end_time: typing.Optional[dt.datetime] = OMIT,
        input: typing.Optional[JsonNodeWrite] = OMIT,
        output: typing.Optional[JsonNodeWrite] = OMIT,
        metadata: typing.Optional[JsonNodeWrite] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        usage: typing.Optional[typing.Dict[str, int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Create span

        Parameters
        ----------
        trace_id : str

        name : str

        type : SpanWriteType

        start_time : dt.datetime

        id : typing.Optional[str]

        project_name : typing.Optional[str]
            If null, the default project is used

        parent_span_id : typing.Optional[str]

        end_time : typing.Optional[dt.datetime]

        input : typing.Optional[JsonNodeWrite]

        output : typing.Optional[JsonNodeWrite]

        metadata : typing.Optional[JsonNodeWrite]

        tags : typing.Optional[typing.Sequence[str]]

        usage : typing.Optional[typing.Dict[str, int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import datetime

        from Opik.client import OpikApi

        client = OpikApi()
        client.spans.create_span(
            trace_id="trace_id",
            name="name",
            type="general",
            start_time=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/private/spans",
            method="POST",
            json={
                "id": id,
                "project_name": project_name,
                "trace_id": trace_id,
                "parent_span_id": parent_span_id,
                "name": name,
                "type": type,
                "start_time": start_time,
                "end_time": end_time,
                "input": input,
                "output": output,
                "metadata": metadata,
                "tags": tags,
                "usage": usage,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_spans(
        self,
        *,
        spans: typing.Sequence[SpanWrite],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Create spans

        Parameters
        ----------
        spans : typing.Sequence[SpanWrite]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import datetime

        from Opik import SpanWrite
        from Opik.client import OpikApi

        client = OpikApi()
        client.spans.create_spans(
            spans=[
                SpanWrite(
                    trace_id="trace_id",
                    name="name",
                    type="general",
                    start_time=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                )
            ],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/private/spans/batch",
            method="POST",
            json={"spans": spans},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_span_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SpanPublic:
        """
        Get span by id

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpanPublic
            Span resource

        Examples
        --------
        from Opik.client import OpikApi

        client = OpikApi()
        client.spans.get_span_by_id(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/private/spans/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(SpanPublic, _response.json())  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_span_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete span by id

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from Opik.client import OpikApi

        client = OpikApi()
        client.spans.delete_span_by_id(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/private/spans/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 501:
                raise NotImplementedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update_span(
        self,
        id: str,
        *,
        trace_id: str,
        project_name: typing.Optional[str] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        parent_span_id: typing.Optional[str] = OMIT,
        end_time: typing.Optional[dt.datetime] = OMIT,
        input: typing.Optional[JsonNode] = OMIT,
        output: typing.Optional[JsonNode] = OMIT,
        metadata: typing.Optional[JsonNode] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        usage: typing.Optional[typing.Dict[str, int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update span by id

        Parameters
        ----------
        id : str

        trace_id : str

        project_name : typing.Optional[str]
            If null and project_id not specified, Default Project is assumed

        project_id : typing.Optional[str]
            If null and project_name not specified, Default Project is assumed

        parent_span_id : typing.Optional[str]

        end_time : typing.Optional[dt.datetime]

        input : typing.Optional[JsonNode]

        output : typing.Optional[JsonNode]

        metadata : typing.Optional[JsonNode]

        tags : typing.Optional[typing.Sequence[str]]

        usage : typing.Optional[typing.Dict[str, int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from Opik.client import OpikApi

        client = OpikApi()
        client.spans.update_span(
            id="id",
            trace_id="trace_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/private/spans/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "project_name": project_name,
                "project_id": project_id,
                "trace_id": trace_id,
                "parent_span_id": parent_span_id,
                "end_time": end_time,
                "input": input,
                "output": output,
                "metadata": metadata,
                "tags": tags,
                "usage": usage,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 404:
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_span_feedback_score(
        self,
        id: str,
        *,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete span feedback score

        Parameters
        ----------
        id : str

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from Opik.client import OpikApi

        client = OpikApi()
        client.spans.delete_span_feedback_score(
            id="id",
            name="name",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/private/spans/{jsonable_encoder(id)}/feedback-scores/delete",
            method="POST",
            json={"name": name},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def score_batch_of_spans(
        self,
        *,
        scores: typing.Sequence[FeedbackScoreBatchItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Batch feedback scoring for spans

        Parameters
        ----------
        scores : typing.Sequence[FeedbackScoreBatchItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from Opik import FeedbackScoreBatchItem
        from Opik.client import OpikApi

        client = OpikApi()
        client.spans.score_batch_of_spans(
            scores=[
                FeedbackScoreBatchItem(
                    id="id",
                    name="name",
                    value=1.1,
                    source="ui",
                )
            ],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/private/spans/feedback-scores",
            method="PUT",
            json={"scores": scores},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncSpansClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def add_span_feedback_score(
        self,
        id: str,
        *,
        name: str,
        value: float,
        source: FeedbackScoreSource,
        category_name: typing.Optional[str] = OMIT,
        reason: typing.Optional[str] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        last_updated_at: typing.Optional[dt.datetime] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        last_updated_by: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Add span feedback score

        Parameters
        ----------
        id : str

        name : str

        value : float

        source : FeedbackScoreSource

        category_name : typing.Optional[str]

        reason : typing.Optional[str]

        created_at : typing.Optional[dt.datetime]

        last_updated_at : typing.Optional[dt.datetime]

        created_by : typing.Optional[str]

        last_updated_by : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from Opik.client import AsyncOpikApi

        client = AsyncOpikApi()


        async def main() -> None:
            await client.spans.add_span_feedback_score(
                id="id",
                name="name",
                value=1.1,
                source="ui",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/private/spans/{jsonable_encoder(id)}/feedback-scores",
            method="PUT",
            json={
                "name": name,
                "category_name": category_name,
                "value": value,
                "reason": reason,
                "source": source,
                "created_at": created_at,
                "last_updated_at": last_updated_at,
                "created_by": created_by,
                "last_updated_by": last_updated_by,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_spans_by_project(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        project_name: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        trace_id: typing.Optional[str] = None,
        type: typing.Optional[GetSpansByProjectRequestType] = None,
        filters: typing.Optional[str] = None,
        truncate: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SpanPagePublic:
        """
        Get spans by project_name or project_id and optionally by trace_id and/or type

        Parameters
        ----------
        page : typing.Optional[int]

        size : typing.Optional[int]

        project_name : typing.Optional[str]

        project_id : typing.Optional[str]

        trace_id : typing.Optional[str]

        type : typing.Optional[GetSpansByProjectRequestType]

        filters : typing.Optional[str]

        truncate : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpanPagePublic
            Spans resource

        Examples
        --------
        import asyncio

        from Opik.client import AsyncOpikApi

        client = AsyncOpikApi()


        async def main() -> None:
            await client.spans.get_spans_by_project()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/private/spans",
            method="GET",
            params={
                "page": page,
                "size": size,
                "project_name": project_name,
                "project_id": project_id,
                "trace_id": trace_id,
                "type": type,
                "filters": filters,
                "truncate": truncate,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(SpanPagePublic, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_span(
        self,
        *,
        trace_id: str,
        name: str,
        type: SpanWriteType,
        start_time: dt.datetime,
        id: typing.Optional[str] = OMIT,
        project_name: typing.Optional[str] = OMIT,
        parent_span_id: typing.Optional[str] = OMIT,
        end_time: typing.Optional[dt.datetime] = OMIT,
        input: typing.Optional[JsonNodeWrite] = OMIT,
        output: typing.Optional[JsonNodeWrite] = OMIT,
        metadata: typing.Optional[JsonNodeWrite] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        usage: typing.Optional[typing.Dict[str, int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Create span

        Parameters
        ----------
        trace_id : str

        name : str

        type : SpanWriteType

        start_time : dt.datetime

        id : typing.Optional[str]

        project_name : typing.Optional[str]
            If null, the default project is used

        parent_span_id : typing.Optional[str]

        end_time : typing.Optional[dt.datetime]

        input : typing.Optional[JsonNodeWrite]

        output : typing.Optional[JsonNodeWrite]

        metadata : typing.Optional[JsonNodeWrite]

        tags : typing.Optional[typing.Sequence[str]]

        usage : typing.Optional[typing.Dict[str, int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio
        import datetime

        from Opik.client import AsyncOpikApi

        client = AsyncOpikApi()


        async def main() -> None:
            await client.spans.create_span(
                trace_id="trace_id",
                name="name",
                type="general",
                start_time=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/private/spans",
            method="POST",
            json={
                "id": id,
                "project_name": project_name,
                "trace_id": trace_id,
                "parent_span_id": parent_span_id,
                "name": name,
                "type": type,
                "start_time": start_time,
                "end_time": end_time,
                "input": input,
                "output": output,
                "metadata": metadata,
                "tags": tags,
                "usage": usage,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_spans(
        self,
        *,
        spans: typing.Sequence[SpanWrite],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Create spans

        Parameters
        ----------
        spans : typing.Sequence[SpanWrite]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio
        import datetime

        from Opik import SpanWrite
        from Opik.client import AsyncOpikApi

        client = AsyncOpikApi()


        async def main() -> None:
            await client.spans.create_spans(
                spans=[
                    SpanWrite(
                        trace_id="trace_id",
                        name="name",
                        type="general",
                        start_time=datetime.datetime.fromisoformat(
                            "2024-01-15 09:30:00+00:00",
                        ),
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/private/spans/batch",
            method="POST",
            json={"spans": spans},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_span_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SpanPublic:
        """
        Get span by id

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpanPublic
            Span resource

        Examples
        --------
        import asyncio

        from Opik.client import AsyncOpikApi

        client = AsyncOpikApi()


        async def main() -> None:
            await client.spans.get_span_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/private/spans/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(SpanPublic, _response.json())  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_span_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete span by id

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from Opik.client import AsyncOpikApi

        client = AsyncOpikApi()


        async def main() -> None:
            await client.spans.delete_span_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/private/spans/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 501:
                raise NotImplementedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update_span(
        self,
        id: str,
        *,
        trace_id: str,
        project_name: typing.Optional[str] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        parent_span_id: typing.Optional[str] = OMIT,
        end_time: typing.Optional[dt.datetime] = OMIT,
        input: typing.Optional[JsonNode] = OMIT,
        output: typing.Optional[JsonNode] = OMIT,
        metadata: typing.Optional[JsonNode] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        usage: typing.Optional[typing.Dict[str, int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update span by id

        Parameters
        ----------
        id : str

        trace_id : str

        project_name : typing.Optional[str]
            If null and project_id not specified, Default Project is assumed

        project_id : typing.Optional[str]
            If null and project_name not specified, Default Project is assumed

        parent_span_id : typing.Optional[str]

        end_time : typing.Optional[dt.datetime]

        input : typing.Optional[JsonNode]

        output : typing.Optional[JsonNode]

        metadata : typing.Optional[JsonNode]

        tags : typing.Optional[typing.Sequence[str]]

        usage : typing.Optional[typing.Dict[str, int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from Opik.client import AsyncOpikApi

        client = AsyncOpikApi()


        async def main() -> None:
            await client.spans.update_span(
                id="id",
                trace_id="trace_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/private/spans/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "project_name": project_name,
                "project_id": project_id,
                "trace_id": trace_id,
                "parent_span_id": parent_span_id,
                "end_time": end_time,
                "input": input,
                "output": output,
                "metadata": metadata,
                "tags": tags,
                "usage": usage,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 404:
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_span_feedback_score(
        self,
        id: str,
        *,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete span feedback score

        Parameters
        ----------
        id : str

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from Opik.client import AsyncOpikApi

        client = AsyncOpikApi()


        async def main() -> None:
            await client.spans.delete_span_feedback_score(
                id="id",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/private/spans/{jsonable_encoder(id)}/feedback-scores/delete",
            method="POST",
            json={"name": name},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def score_batch_of_spans(
        self,
        *,
        scores: typing.Sequence[FeedbackScoreBatchItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Batch feedback scoring for spans

        Parameters
        ----------
        scores : typing.Sequence[FeedbackScoreBatchItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from Opik import FeedbackScoreBatchItem
        from Opik.client import AsyncOpikApi

        client = AsyncOpikApi()


        async def main() -> None:
            await client.spans.score_batch_of_spans(
                scores=[
                    FeedbackScoreBatchItem(
                        id="id",
                        name="name",
                        value=1.1,
                        source="ui",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/private/spans/feedback-scores",
            method="PUT",
            json={"scores": scores},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
