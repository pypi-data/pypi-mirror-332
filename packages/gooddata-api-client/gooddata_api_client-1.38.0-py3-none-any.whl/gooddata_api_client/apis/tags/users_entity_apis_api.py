# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Contact: support@gooddata.com
    Generated by: https://openapi-generator.tech
"""

from gooddata_api_client.paths.api_v1_entities_users.post import CreateEntityUsers
from gooddata_api_client.paths.api_v1_entities_users_id.delete import DeleteEntityUsers
from gooddata_api_client.paths.api_v1_entities_users.get import GetAllEntitiesUsers
from gooddata_api_client.paths.api_v1_entities_users_id.get import GetEntityUsers
from gooddata_api_client.paths.api_v1_entities_users_id.patch import PatchEntityUsers
from gooddata_api_client.paths.api_v1_entities_users_id.put import UpdateEntityUsers


class UsersEntityAPIsApi(
    CreateEntityUsers,
    DeleteEntityUsers,
    GetAllEntitiesUsers,
    GetEntityUsers,
    PatchEntityUsers,
    UpdateEntityUsers,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
