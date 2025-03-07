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
from gooddata_api_client.model.data_source_schemata import DataSourceSchemata
from gooddata_api_client.model.scan_request import ScanRequest
from gooddata_api_client.model.scan_result_pdm import ScanResultPdm
from gooddata_api_client.model.scan_sql_request import ScanSqlRequest
from gooddata_api_client.model.scan_sql_response import ScanSqlResponse


class ScanningApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_data_source_schemata_endpoint = _Endpoint(
            settings={
                'response_type': (DataSourceSchemata,),
                'auth': [],
                'endpoint_path': '/api/v1/actions/dataSources/{dataSourceId}/scanSchemata',
                'operation_id': 'get_data_source_schemata',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'data_source_id',
                ],
                'required': [
                    'data_source_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'data_source_id',
                ]
            },
            root_map={
                'validations': {
                    ('data_source_id',): {

                        'regex': {
                            'pattern': r'^(?!\.)[.A-Za-z0-9_-]{1,255}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'data_source_id':
                        (str,),
                },
                'attribute_map': {
                    'data_source_id': 'dataSourceId',
                },
                'location_map': {
                    'data_source_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.scan_data_source_endpoint = _Endpoint(
            settings={
                'response_type': (ScanResultPdm,),
                'auth': [],
                'endpoint_path': '/api/v1/actions/dataSources/{dataSourceId}/scan',
                'operation_id': 'scan_data_source',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'data_source_id',
                    'scan_request',
                ],
                'required': [
                    'data_source_id',
                    'scan_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'data_source_id',
                ]
            },
            root_map={
                'validations': {
                    ('data_source_id',): {

                        'regex': {
                            'pattern': r'^(?!\.)[.A-Za-z0-9_-]{1,255}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'data_source_id':
                        (str,),
                    'scan_request':
                        (ScanRequest,),
                },
                'attribute_map': {
                    'data_source_id': 'dataSourceId',
                },
                'location_map': {
                    'data_source_id': 'path',
                    'scan_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.scan_sql_endpoint = _Endpoint(
            settings={
                'response_type': (ScanSqlResponse,),
                'auth': [],
                'endpoint_path': '/api/v1/actions/dataSources/{dataSourceId}/scanSql',
                'operation_id': 'scan_sql',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'data_source_id',
                    'scan_sql_request',
                ],
                'required': [
                    'data_source_id',
                    'scan_sql_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'data_source_id',
                ]
            },
            root_map={
                'validations': {
                    ('data_source_id',): {

                        'regex': {
                            'pattern': r'^(?!\.)[.A-Za-z0-9_-]{1,255}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'data_source_id':
                        (str,),
                    'scan_sql_request':
                        (ScanSqlRequest,),
                },
                'attribute_map': {
                    'data_source_id': 'dataSourceId',
                },
                'location_map': {
                    'data_source_id': 'path',
                    'scan_sql_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def get_data_source_schemata(
        self,
        data_source_id,
        **kwargs
    ):
        """Get a list of schema names of a database  # noqa: E501

        It scans a database and reads metadata. The result of the request contains a list of schema names of a database.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_data_source_schemata(data_source_id, async_req=True)
        >>> result = thread.get()

        Args:
            data_source_id (str): Data source id

        Keyword Args:
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
            DataSourceSchemata
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
        kwargs['data_source_id'] = \
            data_source_id
        return self.get_data_source_schemata_endpoint.call_with_http_info(**kwargs)

    def scan_data_source(
        self,
        data_source_id,
        scan_request,
        **kwargs
    ):
        """Scan a database to get a physical data model (PDM)  # noqa: E501

        It scans a database and transforms its metadata to a declarative definition of the physical data model (PDM). The result of the request contains the mentioned physical data model (PDM) of a database within warning, for example, about unsupported columns.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.scan_data_source(data_source_id, scan_request, async_req=True)
        >>> result = thread.get()

        Args:
            data_source_id (str): Data source id
            scan_request (ScanRequest):

        Keyword Args:
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
            ScanResultPdm
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
        kwargs['data_source_id'] = \
            data_source_id
        kwargs['scan_request'] = \
            scan_request
        return self.scan_data_source_endpoint.call_with_http_info(**kwargs)

    def scan_sql(
        self,
        data_source_id,
        scan_sql_request,
        **kwargs
    ):
        """Collect metadata about SQL query  # noqa: E501

        It executes SQL query against specified data source and extracts metadata. Metadata consist of column names and column data types. It can optionally provide also preview of data returned by SQL query  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.scan_sql(data_source_id, scan_sql_request, async_req=True)
        >>> result = thread.get()

        Args:
            data_source_id (str): Data source id
            scan_sql_request (ScanSqlRequest):

        Keyword Args:
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
            ScanSqlResponse
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
        kwargs['data_source_id'] = \
            data_source_id
        kwargs['scan_sql_request'] = \
            scan_sql_request
        return self.scan_sql_endpoint.call_with_http_info(**kwargs)

