# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .scan_frequency_option import ScanFrequencyOption

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ScanSchedule(pydantic.BaseModel):
    time: str = pydantic.Field()
    """
    Time of the day when the scan are repeated. For scans that are executed once, this is the time when the scan was started. This is formatted as `HH:MM:SS`.
    """

    frequency: ScanFrequencyOption = pydantic.Field()
    """
    Periodicity of the scan; for example, weekly, means that the scan will be repeated every `repeat_interval` weeks.
    """

    repeat_interval: int = pydantic.Field()
    """
    Number of days, weeks, months, or years between scans. For example, `1` means that the scan will be repeated once every `frequency` period.
    """

    days: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Days of the week when the scan will be repeated. For example, `["monday", "friday"]`
    means that the scan will be repeated on Monday and Friday on the schedule defined by
    `frequency` and `repeat_interval`.
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
