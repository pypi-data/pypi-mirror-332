"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Contact: support@gooddata.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from gooddata_api_client.api_client import ApiClient, Endpoint as _Endpoint
from gooddata_api_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from gooddata_api_client.model.json_api_dataset_out_document import JsonApiDatasetOutDocument
from gooddata_api_client.model.json_api_dataset_out_list import JsonApiDatasetOutList


class DatasetsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_all_entities_datasets_endpoint = _Endpoint(
            settings={
                'response_type': (JsonApiDatasetOutList,),
                'auth': [],
                'endpoint_path': '/api/v1/entities/workspaces/{workspaceId}/datasets',
                'operation_id': 'get_all_entities_datasets',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace_id',
                    'origin',
                    'filter',
                    'include',
                    'page',
                    'size',
                    'sort',
                    'x_gdc_validate_relations',
                    'meta_include',
                ],
                'required': [
                    'workspace_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'origin',
                    'include',
                    'meta_include',
                ],
                'validation': [
                    'meta_include',
                ]
            },
            root_map={
                'validations': {
                    ('meta_include',): {

                    },
                },
                'allowed_values': {
                    ('origin',): {

                        "ALL": "ALL",
                        "PARENTS": "PARENTS",
                        "NATIVE": "NATIVE"
                    },
                    ('include',): {

                        "ATTRIBUTES": "attributes",
                        "FACTS": "facts",
                        "DATASETS": "datasets",
                        "WORKSPACEDATAFILTERS": "workspaceDataFilters",
                        "REFERENCES": "references",
                        "ALL": "ALL"
                    },
                    ('meta_include',): {

                        "ORIGIN": "origin",
                        "PAGE": "page",
                        "ALL": "all",
                        "ALL": "ALL"
                    },
                },
                'openapi_types': {
                    'workspace_id':
                        (str,),
                    'origin':
                        (str,),
                    'filter':
                        (str,),
                    'include':
                        ([str],),
                    'page':
                        (int,),
                    'size':
                        (int,),
                    'sort':
                        ([str],),
                    'x_gdc_validate_relations':
                        (bool,),
                    'meta_include':
                        ([str],),
                },
                'attribute_map': {
                    'workspace_id': 'workspaceId',
                    'origin': 'origin',
                    'filter': 'filter',
                    'include': 'include',
                    'page': 'page',
                    'size': 'size',
                    'sort': 'sort',
                    'x_gdc_validate_relations': 'X-GDC-VALIDATE-RELATIONS',
                    'meta_include': 'metaInclude',
                },
                'location_map': {
                    'workspace_id': 'path',
                    'origin': 'query',
                    'filter': 'query',
                    'include': 'query',
                    'page': 'query',
                    'size': 'query',
                    'sort': 'query',
                    'x_gdc_validate_relations': 'header',
                    'meta_include': 'query',
                },
                'collection_format_map': {
                    'include': 'csv',
                    'sort': 'multi',
                    'meta_include': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.gooddata.api+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_entity_datasets_endpoint = _Endpoint(
            settings={
                'response_type': (JsonApiDatasetOutDocument,),
                'auth': [],
                'endpoint_path': '/api/v1/entities/workspaces/{workspaceId}/datasets/{objectId}',
                'operation_id': 'get_entity_datasets',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace_id',
                    'object_id',
                    'filter',
                    'include',
                    'x_gdc_validate_relations',
                    'meta_include',
                ],
                'required': [
                    'workspace_id',
                    'object_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'include',
                    'meta_include',
                ],
                'validation': [
                    'meta_include',
                ]
            },
            root_map={
                'validations': {
                    ('meta_include',): {

                    },
                },
                'allowed_values': {
                    ('include',): {

                        "ATTRIBUTES": "attributes",
                        "FACTS": "facts",
                        "DATASETS": "datasets",
                        "WORKSPACEDATAFILTERS": "workspaceDataFilters",
                        "REFERENCES": "references",
                        "ALL": "ALL"
                    },
                    ('meta_include',): {

                        "ORIGIN": "origin",
                        "ALL": "all",
                        "ALL": "ALL"
                    },
                },
                'openapi_types': {
                    'workspace_id':
                        (str,),
                    'object_id':
                        (str,),
                    'filter':
                        (str,),
                    'include':
                        ([str],),
                    'x_gdc_validate_relations':
                        (bool,),
                    'meta_include':
                        ([str],),
                },
                'attribute_map': {
                    'workspace_id': 'workspaceId',
                    'object_id': 'objectId',
                    'filter': 'filter',
                    'include': 'include',
                    'x_gdc_validate_relations': 'X-GDC-VALIDATE-RELATIONS',
                    'meta_include': 'metaInclude',
                },
                'location_map': {
                    'workspace_id': 'path',
                    'object_id': 'path',
                    'filter': 'query',
                    'include': 'query',
                    'x_gdc_validate_relations': 'header',
                    'meta_include': 'query',
                },
                'collection_format_map': {
                    'include': 'csv',
                    'meta_include': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.gooddata.api+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def get_all_entities_datasets(
        self,
        workspace_id,
        **kwargs
    ):
        """Get all Datasets  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_all_entities_datasets(workspace_id, async_req=True)
        >>> result = thread.get()

        Args:
            workspace_id (str):

        Keyword Args:
            origin (str): [optional] if omitted the server will use the default value of "ALL"
            filter (str): Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title=='Some Title';description=='desc'). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty=='Value 123').. [optional]
            include ([str]): Array of included collections or individual relationships. Includes are separated by commas (e.g. include=entity1s,entity2s). Collection include represents the inclusion of every relationship between this entity and the given collection. Relationship include represents the inclusion of the particular relationships only. If single parameter \"ALL\" is present, all possible includes are used (include=ALL).  __WARNING:__ Individual include types (collection, relationship or ALL) cannot be combined together.. [optional]
            page (int): Zero-based page index (0..N). [optional] if omitted the server will use the default value of 0
            size (int): The size of the page to be returned. [optional] if omitted the server will use the default value of 20
            sort ([str]): Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.. [optional]
            x_gdc_validate_relations (bool): [optional] if omitted the server will use the default value of False
            meta_include ([str]): Include Meta objects.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            JsonApiDatasetOutList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['workspace_id'] = \
            workspace_id
        return self.get_all_entities_datasets_endpoint.call_with_http_info(**kwargs)

    def get_entity_datasets(
        self,
        workspace_id,
        object_id,
        **kwargs
    ):
        """Get a Dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_entity_datasets(workspace_id, object_id, async_req=True)
        >>> result = thread.get()

        Args:
            workspace_id (str):
            object_id (str):

        Keyword Args:
            filter (str): Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title=='Some Title';description=='desc'). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty=='Value 123').. [optional]
            include ([str]): Array of included collections or individual relationships. Includes are separated by commas (e.g. include=entity1s,entity2s). Collection include represents the inclusion of every relationship between this entity and the given collection. Relationship include represents the inclusion of the particular relationships only. If single parameter \"ALL\" is present, all possible includes are used (include=ALL).  __WARNING:__ Individual include types (collection, relationship or ALL) cannot be combined together.. [optional]
            x_gdc_validate_relations (bool): [optional] if omitted the server will use the default value of False
            meta_include ([str]): Include Meta objects.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            JsonApiDatasetOutDocument
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['workspace_id'] = \
            workspace_id
        kwargs['object_id'] = \
            object_id
        return self.get_entity_datasets_endpoint.call_with_http_info(**kwargs)

