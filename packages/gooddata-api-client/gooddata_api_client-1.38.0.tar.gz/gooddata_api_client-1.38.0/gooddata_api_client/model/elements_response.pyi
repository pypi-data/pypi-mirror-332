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


class ElementsResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Entity holding list of sorted & filtered label elements, related primary label of attribute owning requested label and paging.
    """


    class MetaOapg:
        required = {
            "primaryLabel",
            "elements",
            "paging",
        }
        
        class properties:
            
            
            class elements(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Element']:
                        return Element
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Element'], typing.List['Element']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'elements':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Element':
                    return super().__getitem__(i)
        
            @staticmethod
            def paging() -> typing.Type['Paging']:
                return Paging
        
            @staticmethod
            def primaryLabel() -> typing.Type['RestApiIdentifier']:
                return RestApiIdentifier
        
            @staticmethod
            def format() -> typing.Type['AttributeFormat']:
                return AttributeFormat
            
            
            class granularity(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def MINUTE(cls):
                    return cls("MINUTE")
                
                @schemas.classproperty
                def HOUR(cls):
                    return cls("HOUR")
                
                @schemas.classproperty
                def DAY(cls):
                    return cls("DAY")
                
                @schemas.classproperty
                def WEEK(cls):
                    return cls("WEEK")
                
                @schemas.classproperty
                def MONTH(cls):
                    return cls("MONTH")
                
                @schemas.classproperty
                def QUARTER(cls):
                    return cls("QUARTER")
                
                @schemas.classproperty
                def YEAR(cls):
                    return cls("YEAR")
                
                @schemas.classproperty
                def MINUTE_OF_HOUR(cls):
                    return cls("MINUTE_OF_HOUR")
                
                @schemas.classproperty
                def HOUR_OF_DAY(cls):
                    return cls("HOUR_OF_DAY")
                
                @schemas.classproperty
                def DAY_OF_WEEK(cls):
                    return cls("DAY_OF_WEEK")
                
                @schemas.classproperty
                def DAY_OF_MONTH(cls):
                    return cls("DAY_OF_MONTH")
                
                @schemas.classproperty
                def DAY_OF_YEAR(cls):
                    return cls("DAY_OF_YEAR")
                
                @schemas.classproperty
                def WEEK_OF_YEAR(cls):
                    return cls("WEEK_OF_YEAR")
                
                @schemas.classproperty
                def MONTH_OF_YEAR(cls):
                    return cls("MONTH_OF_YEAR")
                
                @schemas.classproperty
                def QUARTER_OF_YEAR(cls):
                    return cls("QUARTER_OF_YEAR")
            __annotations__ = {
                "elements": elements,
                "paging": paging,
                "primaryLabel": primaryLabel,
                "format": format,
                "granularity": granularity,
            }
    
    primaryLabel: 'RestApiIdentifier'
    elements: MetaOapg.properties.elements
    paging: 'Paging'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["elements"]) -> MetaOapg.properties.elements: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paging"]) -> 'Paging': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["primaryLabel"]) -> 'RestApiIdentifier': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["format"]) -> 'AttributeFormat': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["granularity"]) -> MetaOapg.properties.granularity: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["elements", "paging", "primaryLabel", "format", "granularity", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["elements"]) -> MetaOapg.properties.elements: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paging"]) -> 'Paging': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["primaryLabel"]) -> 'RestApiIdentifier': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["format"]) -> typing.Union['AttributeFormat', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["granularity"]) -> typing.Union[MetaOapg.properties.granularity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["elements", "paging", "primaryLabel", "format", "granularity", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        primaryLabel: 'RestApiIdentifier',
        elements: typing.Union[MetaOapg.properties.elements, list, tuple, ],
        paging: 'Paging',
        format: typing.Union['AttributeFormat', schemas.Unset] = schemas.unset,
        granularity: typing.Union[MetaOapg.properties.granularity, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ElementsResponse':
        return super().__new__(
            cls,
            *_args,
            primaryLabel=primaryLabel,
            elements=elements,
            paging=paging,
            format=format,
            granularity=granularity,
            _configuration=_configuration,
            **kwargs,
        )

from gooddata_api_client.model.attribute_format import AttributeFormat
from gooddata_api_client.model.element import Element
from gooddata_api_client.model.paging import Paging
from gooddata_api_client.model.rest_api_identifier import RestApiIdentifier
