# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Contact: support@gooddata.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from gooddata_api_client import schemas  # noqa: F401


class TabularExportRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Export request object describing the export properties and overrides for tabular exports.
    """


    class MetaOapg:
        required = {
            "fileName",
            "executionResult",
            "format",
        }
        
        class properties:
            executionResult = schemas.StrSchema
            fileName = schemas.StrSchema
            
            
            class format(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def CSV(cls):
                    return cls("CSV")
                
                @schemas.classproperty
                def XLSX(cls):
                    return cls("XLSX")
        
            @staticmethod
            def customOverride() -> typing.Type['CustomOverride']:
                return CustomOverride
        
            @staticmethod
            def settings() -> typing.Type['Settings']:
                return Settings
            __annotations__ = {
                "executionResult": executionResult,
                "fileName": fileName,
                "format": format,
                "customOverride": customOverride,
                "settings": settings,
            }
    
    fileName: MetaOapg.properties.fileName
    executionResult: MetaOapg.properties.executionResult
    format: MetaOapg.properties.format
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["executionResult"]) -> MetaOapg.properties.executionResult: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fileName"]) -> MetaOapg.properties.fileName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["format"]) -> MetaOapg.properties.format: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customOverride"]) -> 'CustomOverride': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["settings"]) -> 'Settings': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["executionResult", "fileName", "format", "customOverride", "settings", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["executionResult"]) -> MetaOapg.properties.executionResult: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fileName"]) -> MetaOapg.properties.fileName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["format"]) -> MetaOapg.properties.format: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customOverride"]) -> typing.Union['CustomOverride', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["settings"]) -> typing.Union['Settings', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["executionResult", "fileName", "format", "customOverride", "settings", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        fileName: typing.Union[MetaOapg.properties.fileName, str, ],
        executionResult: typing.Union[MetaOapg.properties.executionResult, str, ],
        format: typing.Union[MetaOapg.properties.format, str, ],
        customOverride: typing.Union['CustomOverride', schemas.Unset] = schemas.unset,
        settings: typing.Union['Settings', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TabularExportRequest':
        return super().__new__(
            cls,
            *_args,
            fileName=fileName,
            executionResult=executionResult,
            format=format,
            customOverride=customOverride,
            settings=settings,
            _configuration=_configuration,
            **kwargs,
        )

from gooddata_api_client.model.custom_override import CustomOverride
from gooddata_api_client.model.settings import Settings
