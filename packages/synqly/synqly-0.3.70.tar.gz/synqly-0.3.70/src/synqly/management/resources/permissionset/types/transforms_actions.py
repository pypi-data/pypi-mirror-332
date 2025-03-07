# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TransformsActions(str, enum.Enum):
    LIST = "list"
    CREATE = "create"
    GET = "get"
    UPDATE = "update"
    PATCH = "patch"
    DELETE = "delete"
    ALL = "*"

    def visit(
        self,
        list_: typing.Callable[[], T_Result],
        create: typing.Callable[[], T_Result],
        get: typing.Callable[[], T_Result],
        update: typing.Callable[[], T_Result],
        patch: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransformsActions.LIST:
            return list_()
        if self is TransformsActions.CREATE:
            return create()
        if self is TransformsActions.GET:
            return get()
        if self is TransformsActions.UPDATE:
            return update()
        if self is TransformsActions.PATCH:
            return patch()
        if self is TransformsActions.DELETE:
            return delete()
        if self is TransformsActions.ALL:
            return all_()
