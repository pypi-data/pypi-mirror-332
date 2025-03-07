# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from .container import Container

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Request(pydantic.BaseModel):
    """
    The Request Elements object describes characteristics of an API request.
    """

    containers: typing.Optional[typing.List[Container]] = pydantic.Field(default=None)
    """
    When working with containerized applications, the set of containers which write to the standard the output of a particular logging driver. For example, this may be the set of containers involved in handling api requests and responses for a containerized application.
    """

    data: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    The additional data that is associated with the api request.
    """

    flags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The list of communication flags, normalized to the captions of the flag_ids values. In the case of 'Other', they are defined by the event source.
    """

    uid: str = pydantic.Field()
    """
    The unique request identifier.
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
