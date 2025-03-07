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


class ScanResultPdm(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Result of scan of data source physical model.
    """


    class MetaOapg:
        required = {
            "warnings",
            "pdm",
        }
        
        class properties:
        
            @staticmethod
            def pdm() -> typing.Type['DeclarativeTables']:
                return DeclarativeTables
            
            
            class warnings(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TableWarning']:
                        return TableWarning
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['TableWarning'], typing.List['TableWarning']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'warnings':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TableWarning':
                    return super().__getitem__(i)
            __annotations__ = {
                "pdm": pdm,
                "warnings": warnings,
            }
    
    warnings: MetaOapg.properties.warnings
    pdm: 'DeclarativeTables'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pdm"]) -> 'DeclarativeTables': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["warnings"]) -> MetaOapg.properties.warnings: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["pdm", "warnings", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pdm"]) -> 'DeclarativeTables': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["warnings"]) -> MetaOapg.properties.warnings: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["pdm", "warnings", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        warnings: typing.Union[MetaOapg.properties.warnings, list, tuple, ],
        pdm: 'DeclarativeTables',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ScanResultPdm':
        return super().__new__(
            cls,
            *_args,
            warnings=warnings,
            pdm=pdm,
            _configuration=_configuration,
            **kwargs,
        )

from gooddata_api_client.model.declarative_tables import DeclarativeTables
from gooddata_api_client.model.table_warning import TableWarning
