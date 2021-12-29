# coding: utf-8

"""
    Cythereal Dashboard API

     The API used exclusively by the MAGIC Dashboard for populating charts, graphs, tables, etc... on the dashboard.  # API Conventions  **All responses** MUST be of type `APIResponse` and contain the following fields:  * `api_version` |  The current api version * `success` | Boolean value indicating if the operation succeeded. * `code` | Status code. Typically corresponds to the HTTP status code.  * `message` | A human readable message providing more details about the operation. Can be null or empty.  **Successful operations** MUST return a `SuccessResponse`, which extends `APIResponse` by adding:  * `data` | Properties containing the response object. * `success` | MUST equal True  When returning objects from a successful response, the `data` object SHOULD contain a property named after the requested object type. For example, the `/alerts` endpoint should return a response object with `data.alerts`. This property SHOULD  contain a list of the returned objects. For the `/alerts` endpoint, the `data.alerts` property contains a list of MagicAlerts objects. See the `/alerts` endpoint documentation for an example.  **Failed Operations** MUST return an `ErrorResponse`, which extends `APIResponse` by adding:  * `success` | MUST equal False.   # noqa: E501

    OpenAPI spec version: 0.41.0
    Contact: support@cythereal.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cythereal_dashboard.api_client import ApiClient


class SignaturesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_magic_yara(self, binary_id, **kwargs):  # noqa: E501
        """\"Generate a yara rule, and campaign information for  the provided binaries.\"   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_magic_yara(binary_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] binary_id: The SHA1 of the binary to get yara for.  Specify parameter multiple  times to include multiple binaries in the rule.  The generated rule  will attempt to cover all included binaries.  (required)
        :param str name: The custom name to give the yara rule. The rule name will always take the form of:   CythMAGIC_\\<name>_\\<config> 
        :param str config: The name of the config file to use when creating the yara rule. The config files will determine what criteria to use when creating the rule, and are predefined at this time. 
        :param bool unpacked: If true, return the yara rule for the unpacked binaries.
        :param bool debug: If true, add rejected signatures as yara rule metadata. 
        :return: MagicYaraResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_magic_yara_with_http_info(binary_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_magic_yara_with_http_info(binary_id, **kwargs)  # noqa: E501
            return data

    def get_magic_yara_with_http_info(self, binary_id, **kwargs):  # noqa: E501
        """\"Generate a yara rule, and campaign information for  the provided binaries.\"   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_magic_yara_with_http_info(binary_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] binary_id: The SHA1 of the binary to get yara for.  Specify parameter multiple  times to include multiple binaries in the rule.  The generated rule  will attempt to cover all included binaries.  (required)
        :param str name: The custom name to give the yara rule. The rule name will always take the form of:   CythMAGIC_\\<name>_\\<config> 
        :param str config: The name of the config file to use when creating the yara rule. The config files will determine what criteria to use when creating the rule, and are predefined at this time. 
        :param bool unpacked: If true, return the yara rule for the unpacked binaries.
        :param bool debug: If true, add rejected signatures as yara rule metadata. 
        :return: MagicYaraResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['binary_id', 'name', 'config', 'unpacked', 'debug']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_magic_yara" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'binary_id' is set
        if ('binary_id' not in params or
                params['binary_id'] is None):
            raise ValueError("Missing the required parameter `binary_id` when calling `get_magic_yara`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'binary_id' in params:
            query_params.append(('binary_id', params['binary_id']))  # noqa: E501
            collection_formats['binary_id'] = 'multi'  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'config' in params:
            query_params.append(('config', params['config']))  # noqa: E501
        if 'unpacked' in params:
            query_params.append(('unpacked', params['unpacked']))  # noqa: E501
        if 'debug' in params:
            query_params.append(('debug', params['debug']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key_query_param']  # noqa: E501

        return self.api_client.call_api(
            '/signatures/magic_yara/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MagicYaraResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_procedure_signatures(self, binary_id, **kwargs):  # noqa: E501
        """Generate procedure signatures for provided binaries.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_procedure_signatures(binary_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] binary_id: The SHA1 of the binary to get yara for.  Specify parameter multiple  times to include multiple binaries in the rule.  The generated rule  will attempt to cover all included binaries.  (required)
        :param bool unpacked: If true, return the procedures for the unpacked binaries.
        :param int limit: Number of procedures to return per call
        :param int page: Number of pages per (limit) to skip
        :return: ProcedureSignaturesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_procedure_signatures_with_http_info(binary_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_procedure_signatures_with_http_info(binary_id, **kwargs)  # noqa: E501
            return data

    def get_procedure_signatures_with_http_info(self, binary_id, **kwargs):  # noqa: E501
        """Generate procedure signatures for provided binaries.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_procedure_signatures_with_http_info(binary_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] binary_id: The SHA1 of the binary to get yara for.  Specify parameter multiple  times to include multiple binaries in the rule.  The generated rule  will attempt to cover all included binaries.  (required)
        :param bool unpacked: If true, return the procedures for the unpacked binaries.
        :param int limit: Number of procedures to return per call
        :param int page: Number of pages per (limit) to skip
        :return: ProcedureSignaturesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['binary_id', 'unpacked', 'limit', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_procedure_signatures" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'binary_id' is set
        if ('binary_id' not in params or
                params['binary_id'] is None):
            raise ValueError("Missing the required parameter `binary_id` when calling `get_procedure_signatures`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'binary_id' in params:
            query_params.append(('binary_id', params['binary_id']))  # noqa: E501
            collection_formats['binary_id'] = 'multi'  # noqa: E501
        if 'unpacked' in params:
            query_params.append(('unpacked', params['unpacked']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key_query_param']  # noqa: E501

        return self.api_client.call_api(
            '/signatures/procedures/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProcedureSignaturesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
