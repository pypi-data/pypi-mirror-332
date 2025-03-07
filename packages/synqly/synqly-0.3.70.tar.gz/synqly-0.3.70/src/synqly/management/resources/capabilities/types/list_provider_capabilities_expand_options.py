# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ListProviderCapabilitiesExpandOptions(str, enum.Enum):
    CONNECTOR = "connector"
    OPERATIONS = "operations"
    PROVIDER_CONFIG = "provider_config"

    def visit(
        self,
        connector: typing.Callable[[], T_Result],
        operations: typing.Callable[[], T_Result],
        provider_config: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListProviderCapabilitiesExpandOptions.CONNECTOR:
            return connector()
        if self is ListProviderCapabilitiesExpandOptions.OPERATIONS:
            return operations()
        if self is ListProviderCapabilitiesExpandOptions.PROVIDER_CONFIG:
            return provider_config()
