# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Contact: support@gooddata.com
    Generated by: https://openapi-generator.tech
"""

from gooddata_api_client.paths.api_v1_entities_user_groups.post import CreateEntityUserGroups
from gooddata_api_client.paths.api_v1_entities_user_groups_id.delete import DeleteEntityUserGroups
from gooddata_api_client.paths.api_v1_entities_user_groups.get import GetAllEntitiesUserGroups
from gooddata_api_client.paths.api_v1_entities_user_groups_id.get import GetEntityUserGroups
from gooddata_api_client.paths.api_v1_entities_user_groups_id.patch import PatchEntityUserGroups
from gooddata_api_client.paths.api_v1_entities_user_groups_id.put import UpdateEntityUserGroups


class UserGroupsEntityAPIsApi(
    CreateEntityUserGroups,
    DeleteEntityUserGroups,
    GetAllEntitiesUserGroups,
    GetEntityUserGroups,
    PatchEntityUserGroups,
    UpdateEntityUserGroups,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
