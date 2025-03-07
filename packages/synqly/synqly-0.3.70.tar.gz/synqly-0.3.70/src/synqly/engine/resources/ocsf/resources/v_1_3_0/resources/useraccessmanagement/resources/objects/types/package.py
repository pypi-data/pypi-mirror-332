# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from .fingerprint import Fingerprint
from .package_type_id import PackageTypeId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Package(pydantic.BaseModel):
    """
    The Software Package object describes details about a software package. Defined by D3FEND <a target='_blank' href='https://d3fend.mitre.org/dao/artifact/d3f:SoftwarePackage/'>d3f:SoftwarePackage</a>.
    """

    architecture: typing.Optional[str] = pydantic.Field(default=None)
    """
    Architecture is a shorthand name describing the type of computer hardware the packaged software is meant to run on.
    """

    cpe_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Common Platform Enumeration (CPE) name for the software package.
    """

    epoch: typing.Optional[int] = pydantic.Field(default=None)
    """
    The software package epoch. Epoch is a way to define weighted dependencies based on version numbers.
    """

    hash: typing.Optional[Fingerprint] = pydantic.Field(default=None)
    """
    Cryptographic hash to identify the binary instance of a software component. This can include any component such file, package, or library.
    """

    license: typing.Optional[str] = pydantic.Field(default=None)
    """
    The software license applied to this package.
    """

    name: str = pydantic.Field()
    """
    The software package name.
    """

    purl: typing.Optional[str] = pydantic.Field(default=None)
    """
    A purl is a URL string used to identify and locate a software package in a mostly universal and uniform way across programming languages, package managers, packaging conventions, tools, APIs and databases.
    """

    release: typing.Optional[str] = pydantic.Field(default=None)
    """
    Release is the number of times a version of the software has been packaged.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of software package, normalized to the caption of the type_id value. In the case of 'Other', it is defined by the source.
    """

    type_id: typing.Optional[PackageTypeId] = pydantic.Field(default=None)
    """
    The type of software package.
    """

    vendor_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the vendor who published the software package.
    """

    version: str = pydantic.Field()
    """
    The software package version.
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
