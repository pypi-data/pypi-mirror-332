# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..........core.datetime_utils import serialize_datetime
from ...base.types.email_address import EmailAddress
from .domain_contact_type_id import DomainContactTypeId
from .location import Location

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class DomainContact(pydantic.BaseModel):
    """
    The contact information related to a domain registration, e.g., registrant, administrator, abuse, billing, or technical contact.
    """

    email_addr: typing.Optional[EmailAddress] = pydantic.Field(default=None)
    """
    The user's primary email address.
    """

    location: typing.Optional[Location] = pydantic.Field(default=None)
    """
    Location details for the contract such as the city, state/province, country, etc.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The individual or organization name for the contact.
    """

    phone_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The number associated with the phone.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Domain Contact type, normalized to the caption of the <code>type_id</code> value. In the case of 'Other', it is defined by the source
    """

    type_id: DomainContactTypeId = pydantic.Field()
    """
    The normalized domain contact type ID.
    """

    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the contact information, typically provided in WHOIS information.
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
