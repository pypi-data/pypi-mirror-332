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


class DeclarativeWorkspaceModel(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A declarative form of a model and analytics for a workspace.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def analytics() -> typing.Type['DeclarativeAnalyticsLayer']:
                return DeclarativeAnalyticsLayer
        
            @staticmethod
            def ldm() -> typing.Type['DeclarativeLdm']:
                return DeclarativeLdm
            __annotations__ = {
                "analytics": analytics,
                "ldm": ldm,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["analytics"]) -> 'DeclarativeAnalyticsLayer': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ldm"]) -> 'DeclarativeLdm': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["analytics", "ldm", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["analytics"]) -> typing.Union['DeclarativeAnalyticsLayer', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ldm"]) -> typing.Union['DeclarativeLdm', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["analytics", "ldm", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        analytics: typing.Union['DeclarativeAnalyticsLayer', schemas.Unset] = schemas.unset,
        ldm: typing.Union['DeclarativeLdm', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DeclarativeWorkspaceModel':
        return super().__new__(
            cls,
            *_args,
            analytics=analytics,
            ldm=ldm,
            _configuration=_configuration,
            **kwargs,
        )

from gooddata_api_client.model.declarative_analytics_layer import DeclarativeAnalyticsLayer
from gooddata_api_client.model.declarative_ldm import DeclarativeLdm
