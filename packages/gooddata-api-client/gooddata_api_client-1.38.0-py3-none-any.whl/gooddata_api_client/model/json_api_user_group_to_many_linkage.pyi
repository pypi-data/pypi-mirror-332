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


class JsonApiUserGroupToManyLinkage(
    schemas.ListSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    References to other resource objects in a to-many (\"relationship\"). Relationships can be specified by including a member in a resource's links object.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['JsonApiUserGroupLinkage']:
            return JsonApiUserGroupLinkage

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple['JsonApiUserGroupLinkage'], typing.List['JsonApiUserGroupLinkage']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'JsonApiUserGroupToManyLinkage':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'JsonApiUserGroupLinkage':
        return super().__getitem__(i)

from gooddata_api_client.model.json_api_user_group_linkage import JsonApiUserGroupLinkage
