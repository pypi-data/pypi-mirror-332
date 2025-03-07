# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from .analytic_type_id import AnalyticTypeId
from .object import Object

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Analytic(pydantic.BaseModel):
    """
    The Analytic object contains details about the analytic technique used to analyze and derive insights from the data or information that led to the creation of a finding or conclusion.
    """

    category: typing.Optional[str] = pydantic.Field(default=None)
    """
    The analytic category.
    """

    desc: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the analytic that generated the finding.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the analytic that generated the finding.
    """

    related_analytics: typing.Optional[typing.List[Object]] = pydantic.Field(default=None)
    """
    Other analytics related to this analytic.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The analytic type.
    """

    type_id: AnalyticTypeId = pydantic.Field()
    """
    The analytic type ID.
    """

    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the analytic that generated the finding.
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The analytic version. For example: <code>1.1</code>.
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
