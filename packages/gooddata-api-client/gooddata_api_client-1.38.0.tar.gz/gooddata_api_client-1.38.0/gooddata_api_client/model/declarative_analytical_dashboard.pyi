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


class DeclarativeAnalyticalDashboard(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "id",
            "title",
            "content",
        }
        
        class properties:
            content = schemas.DictSchema
            
            
            class id(
                schemas.StrSchema
            ):
                pass
            
            
            class title(
                schemas.StrSchema
            ):
                pass
            
            
            class description(
                schemas.StrSchema
            ):
                pass
            
            
            class permissions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['DeclarativeAnalyticalDashboardPermission']:
                        return DeclarativeAnalyticalDashboardPermission
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['DeclarativeAnalyticalDashboardPermission'], typing.List['DeclarativeAnalyticalDashboardPermission']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'permissions':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'DeclarativeAnalyticalDashboardPermission':
                    return super().__getitem__(i)
            
            
            class tags(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tags':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "content": content,
                "id": id,
                "title": title,
                "description": description,
                "permissions": permissions,
                "tags": tags,
            }
    
    id: MetaOapg.properties.id
    title: MetaOapg.properties.title
    content: MetaOapg.properties.content
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["content"]) -> MetaOapg.properties.content: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["permissions"]) -> MetaOapg.properties.permissions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> MetaOapg.properties.tags: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["content", "id", "title", "description", "permissions", "tags", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["content"]) -> MetaOapg.properties.content: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["permissions"]) -> typing.Union[MetaOapg.properties.permissions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> typing.Union[MetaOapg.properties.tags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["content", "id", "title", "description", "permissions", "tags", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        title: typing.Union[MetaOapg.properties.title, str, ],
        content: typing.Union[MetaOapg.properties.content, dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        permissions: typing.Union[MetaOapg.properties.permissions, list, tuple, schemas.Unset] = schemas.unset,
        tags: typing.Union[MetaOapg.properties.tags, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DeclarativeAnalyticalDashboard':
        return super().__new__(
            cls,
            *_args,
            id=id,
            title=title,
            content=content,
            description=description,
            permissions=permissions,
            tags=tags,
            _configuration=_configuration,
            **kwargs,
        )

from gooddata_api_client.model.declarative_analytical_dashboard_permission import DeclarativeAnalyticalDashboardPermission
