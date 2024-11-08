# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
from ..core.request_options import RequestOptions
from ..types.feedback_score_batch_item import FeedbackScoreBatchItem
from ..types.feedback_score_source import FeedbackScoreSource
from ..types.json_node import JsonNode
from ..types.json_node_write import JsonNodeWrite
from ..types.trace_page_public import TracePagePublic
from ..types.trace_public import TracePublic
from ..types.trace_write import TraceWrite

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class TracesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def add_trace_feedback_score(
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
        Add trace feedback score

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
        client.traces.add_trace_feedback_score(
            id="id",
            name="name",
            value=1.1,
            source="ui",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/private/traces/{jsonable_encoder(id)}/feedback-scores",
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

    def get_traces_by_project(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        project_name: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        filters: typing.Optional[str] = None,
        truncate: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TracePagePublic:
        """
        Get traces by project_name or project_id

        Parameters
        ----------
        page : typing.Optional[int]

        size : typing.Optional[int]

        project_name : typing.Optional[str]

        project_id : typing.Optional[str]

        filters : typing.Optional[str]

        truncate : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TracePagePublic
            Trace resource

        Examples
        --------
        from Opik.client import OpikApi

        client = OpikApi()
        client.traces.get_traces_by_project()
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/private/traces",
            method="GET",
            params={
                "page": page,
                "size": size,
                "project_name": project_name,
                "project_id": project_id,
                "filters": filters,
                "truncate": truncate,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(TracePagePublic, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_trace(
        self,
        *,
        name: str,
        start_time: dt.datetime,
        id: typing.Optional[str] = OMIT,
        project_name: typing.Optional[str] = OMIT,
        end_time: typing.Optional[dt.datetime] = OMIT,
        input: typing.Optional[JsonNodeWrite] = OMIT,
        output: typing.Optional[JsonNodeWrite] = OMIT,
        metadata: typing.Optional[JsonNodeWrite] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Get trace

        Parameters
        ----------
        name : str

        start_time : dt.datetime

        id : typing.Optional[str]

        project_name : typing.Optional[str]
            If null, the default project is used

        end_time : typing.Optional[dt.datetime]

        input : typing.Optional[JsonNodeWrite]

        output : typing.Optional[JsonNodeWrite]

        metadata : typing.Optional[JsonNodeWrite]

        tags : typing.Optional[typing.Sequence[str]]

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
        client.traces.create_trace(
            name="name",
            start_time=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/private/traces",
            method="POST",
            json={
                "id": id,
                "project_name": project_name,
                "name": name,
                "start_time": start_time,
                "end_time": end_time,
                "input": input,
                "output": output,
                "metadata": metadata,
                "tags": tags,
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

    def create_traces(
        self,
        *,
        traces: typing.Sequence[TraceWrite],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Create traces

        Parameters
        ----------
        traces : typing.Sequence[TraceWrite]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import datetime

        from Opik import TraceWrite
        from Opik.client import OpikApi

        client = OpikApi()
        client.traces.create_traces(
            traces=[
                TraceWrite(
                    name="name",
                    start_time=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                )
            ],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/private/traces/batch",
            method="POST",
            json={"traces": traces},
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

    def get_trace_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TracePublic:
        """
        Get trace by id

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TracePublic
            Trace resource

        Examples
        --------
        from Opik.client import OpikApi

        client = OpikApi()
        client.traces.get_trace_by_id(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/private/traces/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(TracePublic, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_trace_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete trace by id

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
        client.traces.delete_trace_by_id(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/private/traces/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update_trace(
        self,
        id: str,
        *,
        project_name: typing.Optional[str] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        end_time: typing.Optional[dt.datetime] = OMIT,
        input: typing.Optional[JsonNode] = OMIT,
        output: typing.Optional[JsonNode] = OMIT,
        metadata: typing.Optional[JsonNode] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update trace by id

        Parameters
        ----------
        id : str

        project_name : typing.Optional[str]
            If null and project_id not specified, Default Project is assumed

        project_id : typing.Optional[str]
            If null and project_name not specified, Default Project is assumed

        end_time : typing.Optional[dt.datetime]

        input : typing.Optional[JsonNode]

        output : typing.Optional[JsonNode]

        metadata : typing.Optional[JsonNode]

        tags : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from Opik.client import OpikApi

        client = OpikApi()
        client.traces.update_trace(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/private/traces/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "project_name": project_name,
                "project_id": project_id,
                "end_time": end_time,
                "input": input,
                "output": output,
                "metadata": metadata,
                "tags": tags,
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

    def delete_trace_feedback_score(
        self,
        id: str,
        *,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete trace feedback score

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
        client.traces.delete_trace_feedback_score(
            id="id",
            name="name",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/private/traces/{jsonable_encoder(id)}/feedback-scores/delete",
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

    def delete_traces(
        self,
        *,
        ids: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete traces

        Parameters
        ----------
        ids : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from Opik.client import OpikApi

        client = OpikApi()
        client.traces.delete_traces(
            ids=["ids"],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/private/traces/delete",
            method="POST",
            json={"ids": ids},
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

    def score_batch_of_traces(
        self,
        *,
        scores: typing.Sequence[FeedbackScoreBatchItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Batch feedback scoring for traces

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
        client.traces.score_batch_of_traces(
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
            "v1/private/traces/feedback-scores",
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


class AsyncTracesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def add_trace_feedback_score(
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
        Add trace feedback score

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
            await client.traces.add_trace_feedback_score(
                id="id",
                name="name",
                value=1.1,
                source="ui",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/private/traces/{jsonable_encoder(id)}/feedback-scores",
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

    async def get_traces_by_project(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        project_name: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        filters: typing.Optional[str] = None,
        truncate: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TracePagePublic:
        """
        Get traces by project_name or project_id

        Parameters
        ----------
        page : typing.Optional[int]

        size : typing.Optional[int]

        project_name : typing.Optional[str]

        project_id : typing.Optional[str]

        filters : typing.Optional[str]

        truncate : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TracePagePublic
            Trace resource

        Examples
        --------
        import asyncio

        from Opik.client import AsyncOpikApi

        client = AsyncOpikApi()


        async def main() -> None:
            await client.traces.get_traces_by_project()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/private/traces",
            method="GET",
            params={
                "page": page,
                "size": size,
                "project_name": project_name,
                "project_id": project_id,
                "filters": filters,
                "truncate": truncate,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(TracePagePublic, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_trace(
        self,
        *,
        name: str,
        start_time: dt.datetime,
        id: typing.Optional[str] = OMIT,
        project_name: typing.Optional[str] = OMIT,
        end_time: typing.Optional[dt.datetime] = OMIT,
        input: typing.Optional[JsonNodeWrite] = OMIT,
        output: typing.Optional[JsonNodeWrite] = OMIT,
        metadata: typing.Optional[JsonNodeWrite] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Get trace

        Parameters
        ----------
        name : str

        start_time : dt.datetime

        id : typing.Optional[str]

        project_name : typing.Optional[str]
            If null, the default project is used

        end_time : typing.Optional[dt.datetime]

        input : typing.Optional[JsonNodeWrite]

        output : typing.Optional[JsonNodeWrite]

        metadata : typing.Optional[JsonNodeWrite]

        tags : typing.Optional[typing.Sequence[str]]

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
            await client.traces.create_trace(
                name="name",
                start_time=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/private/traces",
            method="POST",
            json={
                "id": id,
                "project_name": project_name,
                "name": name,
                "start_time": start_time,
                "end_time": end_time,
                "input": input,
                "output": output,
                "metadata": metadata,
                "tags": tags,
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

    async def create_traces(
        self,
        *,
        traces: typing.Sequence[TraceWrite],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Create traces

        Parameters
        ----------
        traces : typing.Sequence[TraceWrite]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio
        import datetime

        from Opik import TraceWrite
        from Opik.client import AsyncOpikApi

        client = AsyncOpikApi()


        async def main() -> None:
            await client.traces.create_traces(
                traces=[
                    TraceWrite(
                        name="name",
                        start_time=datetime.datetime.fromisoformat(
                            "2024-01-15 09:30:00+00:00",
                        ),
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/private/traces/batch",
            method="POST",
            json={"traces": traces},
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

    async def get_trace_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TracePublic:
        """
        Get trace by id

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TracePublic
            Trace resource

        Examples
        --------
        import asyncio

        from Opik.client import AsyncOpikApi

        client = AsyncOpikApi()


        async def main() -> None:
            await client.traces.get_trace_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/private/traces/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(TracePublic, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_trace_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete trace by id

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
            await client.traces.delete_trace_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/private/traces/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update_trace(
        self,
        id: str,
        *,
        project_name: typing.Optional[str] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        end_time: typing.Optional[dt.datetime] = OMIT,
        input: typing.Optional[JsonNode] = OMIT,
        output: typing.Optional[JsonNode] = OMIT,
        metadata: typing.Optional[JsonNode] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update trace by id

        Parameters
        ----------
        id : str

        project_name : typing.Optional[str]
            If null and project_id not specified, Default Project is assumed

        project_id : typing.Optional[str]
            If null and project_name not specified, Default Project is assumed

        end_time : typing.Optional[dt.datetime]

        input : typing.Optional[JsonNode]

        output : typing.Optional[JsonNode]

        metadata : typing.Optional[JsonNode]

        tags : typing.Optional[typing.Sequence[str]]

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
            await client.traces.update_trace(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/private/traces/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "project_name": project_name,
                "project_id": project_id,
                "end_time": end_time,
                "input": input,
                "output": output,
                "metadata": metadata,
                "tags": tags,
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

    async def delete_trace_feedback_score(
        self,
        id: str,
        *,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete trace feedback score

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
            await client.traces.delete_trace_feedback_score(
                id="id",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/private/traces/{jsonable_encoder(id)}/feedback-scores/delete",
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

    async def delete_traces(
        self,
        *,
        ids: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete traces

        Parameters
        ----------
        ids : typing.Sequence[str]

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
            await client.traces.delete_traces(
                ids=["ids"],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/private/traces/delete",
            method="POST",
            json={"ids": ids},
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

    async def score_batch_of_traces(
        self,
        *,
        scores: typing.Sequence[FeedbackScoreBatchItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Batch feedback scoring for traces

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
            await client.traces.score_batch_of_traces(
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
            "v1/private/traces/feedback-scores",
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
