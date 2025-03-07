# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Contact: support@gooddata.com
    Generated by: https://openapi-generator.tech
"""

from gooddata_api_client.paths.api_v1_entities_organization_settings.post import CreateEntityOrganizationSettings
from gooddata_api_client.paths.api_v1_entities_organization_settings_id.delete import DeleteEntityOrganizationSettings
from gooddata_api_client.paths.api_v1_entities_organization_settings.get import GetAllEntitiesOrganizationSettings
from gooddata_api_client.paths.api_v1_entities_organization_settings_id.get import GetEntityOrganizationSettings
from gooddata_api_client.paths.api_v1_entities_admin_organizations_id.get import GetEntityOrganizations
from gooddata_api_client.paths.api_v1_entities_organization.get import GetOrganization
from gooddata_api_client.paths.api_v1_entities_organization_settings_id.patch import PatchEntityOrganizationSettings
from gooddata_api_client.paths.api_v1_entities_admin_organizations_id.patch import PatchEntityOrganizations
from gooddata_api_client.paths.api_v1_entities_organization_settings_id.put import UpdateEntityOrganizationSettings
from gooddata_api_client.paths.api_v1_entities_admin_organizations_id.put import UpdateEntityOrganizations


class OrganizationEntityAPIsApi(
    CreateEntityOrganizationSettings,
    DeleteEntityOrganizationSettings,
    GetAllEntitiesOrganizationSettings,
    GetEntityOrganizationSettings,
    GetEntityOrganizations,
    GetOrganization,
    PatchEntityOrganizationSettings,
    PatchEntityOrganizations,
    UpdateEntityOrganizationSettings,
    UpdateEntityOrganizations,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
