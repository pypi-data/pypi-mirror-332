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


class DeclarativeReference(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A dataset reference.
    """


    class MetaOapg:
        required = {
            "identifier",
            "sourceColumns",
            "multivalue",
        }
        
        class properties:
        
            @staticmethod
            def identifier() -> typing.Type['ReferenceIdentifier']:
                return ReferenceIdentifier
            multivalue = schemas.BoolSchema
            
            
            class sourceColumns(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'sourceColumns':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class sourceColumnDataTypes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'sourceColumnDataTypes':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "identifier": identifier,
                "multivalue": multivalue,
                "sourceColumns": sourceColumns,
                "sourceColumnDataTypes": sourceColumnDataTypes,
            }
    
    identifier: 'ReferenceIdentifier'
    sourceColumns: MetaOapg.properties.sourceColumns
    multivalue: MetaOapg.properties.multivalue
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["identifier"]) -> 'ReferenceIdentifier': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["multivalue"]) -> MetaOapg.properties.multivalue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceColumns"]) -> MetaOapg.properties.sourceColumns: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceColumnDataTypes"]) -> MetaOapg.properties.sourceColumnDataTypes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["identifier", "multivalue", "sourceColumns", "sourceColumnDataTypes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["identifier"]) -> 'ReferenceIdentifier': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["multivalue"]) -> MetaOapg.properties.multivalue: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceColumns"]) -> MetaOapg.properties.sourceColumns: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceColumnDataTypes"]) -> typing.Union[MetaOapg.properties.sourceColumnDataTypes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["identifier", "multivalue", "sourceColumns", "sourceColumnDataTypes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        identifier: 'ReferenceIdentifier',
        sourceColumns: typing.Union[MetaOapg.properties.sourceColumns, list, tuple, ],
        multivalue: typing.Union[MetaOapg.properties.multivalue, bool, ],
        sourceColumnDataTypes: typing.Union[MetaOapg.properties.sourceColumnDataTypes, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DeclarativeReference':
        return super().__new__(
            cls,
            *_args,
            identifier=identifier,
            sourceColumns=sourceColumns,
            multivalue=multivalue,
            sourceColumnDataTypes=sourceColumnDataTypes,
            _configuration=_configuration,
            **kwargs,
        )

from gooddata_api_client.model.reference_identifier import ReferenceIdentifier
