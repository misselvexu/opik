# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .dataset_item_source import DatasetItemSource
from .experiment_item import ExperimentItem
from .json_node import JsonNode


class DatasetItem(pydantic_v1.BaseModel):
    id: typing.Optional[str] = None
    input: typing.Optional[JsonNode] = None
    expected_output: typing.Optional[JsonNode] = None
    metadata: typing.Optional[JsonNode] = None
    trace_id: typing.Optional[str] = None
    span_id: typing.Optional[str] = None
    source: DatasetItemSource
    data: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]] = None
    experiment_items: typing.Optional[typing.List[ExperimentItem]] = None
    created_at: typing.Optional[dt.datetime] = None
    last_updated_at: typing.Optional[dt.datetime] = None
    created_by: typing.Optional[str] = None
    last_updated_by: typing.Optional[str] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
