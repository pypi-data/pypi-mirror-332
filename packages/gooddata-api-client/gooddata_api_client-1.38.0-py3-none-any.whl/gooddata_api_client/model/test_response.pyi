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


class TestResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Response from data source testing.
    """


    class MetaOapg:
        required = {
            "successful",
        }
        
        class properties:
            successful = schemas.BoolSchema
            error = schemas.StrSchema
        
            @staticmethod
            def queryDurationMillis() -> typing.Type['TestQueryDuration']:
                return TestQueryDuration
            __annotations__ = {
                "successful": successful,
                "error": error,
                "queryDurationMillis": queryDurationMillis,
            }
    
    successful: MetaOapg.properties.successful
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["successful"]) -> MetaOapg.properties.successful: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["queryDurationMillis"]) -> 'TestQueryDuration': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["successful", "error", "queryDurationMillis", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["successful"]) -> MetaOapg.properties.successful: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> typing.Union[MetaOapg.properties.error, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["queryDurationMillis"]) -> typing.Union['TestQueryDuration', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["successful", "error", "queryDurationMillis", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        successful: typing.Union[MetaOapg.properties.successful, bool, ],
        error: typing.Union[MetaOapg.properties.error, str, schemas.Unset] = schemas.unset,
        queryDurationMillis: typing.Union['TestQueryDuration', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TestResponse':
        return super().__new__(
            cls,
            *_args,
            successful=successful,
            error=error,
            queryDurationMillis=queryDurationMillis,
            _configuration=_configuration,
            **kwargs,
        )

from gooddata_api_client.model.test_query_duration import TestQueryDuration
