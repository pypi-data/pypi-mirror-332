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


class ArithmeticMeasureDefinition(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Metric representing arithmetics between metrics.
    """


    class MetaOapg:
        required = {
            "arithmeticMeasure",
        }
        
        class properties:
            
            
            class arithmeticMeasure(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "measureIdentifiers",
                        "operator",
                    }
                    
                    class properties:
                        
                        
                        class measureIdentifiers(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                @staticmethod
                                def items() -> typing.Type['AfmLocalIdentifier']:
                                    return AfmLocalIdentifier
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple['AfmLocalIdentifier'], typing.List['AfmLocalIdentifier']],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'measureIdentifiers':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> 'AfmLocalIdentifier':
                                return super().__getitem__(i)
                        
                        
                        class operator(
                            schemas.EnumBase,
                            schemas.StrSchema
                        ):
                            
                            @schemas.classproperty
                            def SUM(cls):
                                return cls("SUM")
                            
                            @schemas.classproperty
                            def DIFFERENCE(cls):
                                return cls("DIFFERENCE")
                            
                            @schemas.classproperty
                            def MULTIPLICATION(cls):
                                return cls("MULTIPLICATION")
                            
                            @schemas.classproperty
                            def RATIO(cls):
                                return cls("RATIO")
                            
                            @schemas.classproperty
                            def CHANGE(cls):
                                return cls("CHANGE")
                        __annotations__ = {
                            "measureIdentifiers": measureIdentifiers,
                            "operator": operator,
                        }
                
                measureIdentifiers: MetaOapg.properties.measureIdentifiers
                operator: MetaOapg.properties.operator
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["measureIdentifiers"]) -> MetaOapg.properties.measureIdentifiers: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["operator"]) -> MetaOapg.properties.operator: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["measureIdentifiers", "operator", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["measureIdentifiers"]) -> MetaOapg.properties.measureIdentifiers: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["operator"]) -> MetaOapg.properties.operator: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["measureIdentifiers", "operator", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    measureIdentifiers: typing.Union[MetaOapg.properties.measureIdentifiers, list, tuple, ],
                    operator: typing.Union[MetaOapg.properties.operator, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'arithmeticMeasure':
                    return super().__new__(
                        cls,
                        *_args,
                        measureIdentifiers=measureIdentifiers,
                        operator=operator,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "arithmeticMeasure": arithmeticMeasure,
            }
    
    arithmeticMeasure: MetaOapg.properties.arithmeticMeasure
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["arithmeticMeasure"]) -> MetaOapg.properties.arithmeticMeasure: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["arithmeticMeasure", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["arithmeticMeasure"]) -> MetaOapg.properties.arithmeticMeasure: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["arithmeticMeasure", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        arithmeticMeasure: typing.Union[MetaOapg.properties.arithmeticMeasure, dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ArithmeticMeasureDefinition':
        return super().__new__(
            cls,
            *_args,
            arithmeticMeasure=arithmeticMeasure,
            _configuration=_configuration,
            **kwargs,
        )

from gooddata_api_client.model.afm_local_identifier import AfmLocalIdentifier
