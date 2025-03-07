# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Contact: support@gooddata.com
    Generated by: https://openapi-generator.tech
"""

from gooddata_api_client.paths.api_v1_actions_workspaces_workspace_id_execution_collect_label_elements.post import ComputeLabelElementsPost
from gooddata_api_client.paths.api_v1_actions_workspaces_workspace_id_execution_afm_execute.post import ComputeReport
from gooddata_api_client.paths.api_v1_actions_workspaces_workspace_id_execution_afm_compute_valid_objects.post import ComputeValidObjects
from gooddata_api_client.paths.api_v1_actions_workspaces_workspace_id_export_tabular.post import CreateTabularExport
from gooddata_api_client.paths.api_v1_actions_workspaces_workspace_id_execution_afm_explain.post import ExplainAfm
from gooddata_api_client.paths.api_v1_actions_workspaces_workspace_id_export_tabular_export_id.get import GetTabularExport
from gooddata_api_client.paths.api_v1_actions_workspaces_workspace_id_execution_afm_execute_result_result_id_metadata.get import RetrieveExecutionMetadata
from gooddata_api_client.paths.api_v1_actions_workspaces_workspace_id_execution_afm_execute_result_result_id.get import RetrieveResult


class ComputationApi(
    ComputeLabelElementsPost,
    ComputeReport,
    ComputeValidObjects,
    CreateTabularExport,
    ExplainAfm,
    GetTabularExport,
    RetrieveExecutionMetadata,
    RetrieveResult,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
