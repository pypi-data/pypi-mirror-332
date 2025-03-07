# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .qualys_cloud_credential import QualysCloudCredential

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class VulnerabilitiesQualysCloud(pydantic.BaseModel):
    """
    Configuration for Qualys Cloud Platform as a Vulnerabilities Provider
    """

    credential: QualysCloudCredential
    url: str = pydantic.Field()
    """
    URL for the Qualys Cloud API. This should be the base URL for the API, without any path components and must be HTTPS. For example, "https://qualysguard.qg4.apps.qualys.com".
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
