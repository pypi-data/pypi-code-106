# coding: utf-8

"""
    Cythereal Dashboard API

     The API used exclusively by the MAGIC Dashboard for populating charts, graphs, tables, etc... on the dashboard.  # API Conventions  **All responses** MUST be of type `APIResponse` and contain the following fields:  * `api_version` |  The current api version * `success` | Boolean value indicating if the operation succeeded. * `code` | Status code. Typically corresponds to the HTTP status code.  * `message` | A human readable message providing more details about the operation. Can be null or empty.  **Successful operations** MUST return a `SuccessResponse`, which extends `APIResponse` by adding:  * `data` | Properties containing the response object. * `success` | MUST equal True  When returning objects from a successful response, the `data` object SHOULD contain a property named after the requested object type. For example, the `/alerts` endpoint should return a response object with `data.alerts`. This property SHOULD  contain a list of the returned objects. For the `/alerts` endpoint, the `data.alerts` property contains a list of MagicAlerts objects. See the `/alerts` endpoint documentation for an example.  **Failed Operations** MUST return an `ErrorResponse`, which extends `APIResponse` by adding:  * `success` | MUST equal False.   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@cythereal.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cythereal_dashboard.api_client import ApiClient


class ChartsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_campaign_timeline_binaries(self, campaign_id, **kwargs):  # noqa: E501
        """Gets all the binaries in a specific campaign for the user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_campaign_timeline_binaries(campaign_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str campaign_id: The ID of a campaign. Equal to the binary_id of a random binary in the campaign. (required)
        :return: BinaryGraphListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_campaign_timeline_binaries_with_http_info(campaign_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_campaign_timeline_binaries_with_http_info(campaign_id, **kwargs)  # noqa: E501
            return data

    def get_campaign_timeline_binaries_with_http_info(self, campaign_id, **kwargs):  # noqa: E501
        """Gets all the binaries in a specific campaign for the user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_campaign_timeline_binaries_with_http_info(campaign_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str campaign_id: The ID of a campaign. Equal to the binary_id of a random binary in the campaign. (required)
        :return: BinaryGraphListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_campaign_timeline_binaries" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign_id' is set
        if ('campaign_id' not in params or
                params['campaign_id'] is None):
            raise ValueError("Missing the required parameter `campaign_id` when calling `get_campaign_timeline_binaries`")  # noqa: E501

        if 'campaign_id' in params and not re.search(r'^([a-fA-F0-9]{32}|[a-fA-F0-9]{40}|[a-fA-F0-9]{64}|[a-fA-F0-9]{128})$', params['campaign_id']):  # noqa: E501
            raise ValueError("Invalid value for parameter `campaign_id` when calling `get_campaign_timeline_binaries`, must conform to the pattern `/^([a-fA-F0-9]{32}|[a-fA-F0-9]{40}|[a-fA-F0-9]{64}|[a-fA-F0-9]{128})$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'campaign_id' in params:
            path_params['campaign_id'] = params['campaign_id']  # noqa: E501

        query_params = []

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
            '/charts/timeline/{campaign_id}/campaign/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BinaryGraphListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_campaigns_heatmap(self, **kwargs):  # noqa: E501
        """Gets all the user's collection info in heat map format  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_campaigns_heatmap(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: CampaignMapListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_campaigns_heatmap_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_campaigns_heatmap_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_campaigns_heatmap_with_http_info(self, **kwargs):  # noqa: E501
        """Gets all the user's collection info in heat map format  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_campaigns_heatmap_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: CampaignMapListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_campaigns_heatmap" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/charts/maps/campaigns/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CampaignMapListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_empty_yara_heatmap(self, **kwargs):  # noqa: E501
        """Get the users empty yara campaign in heatmap format  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_empty_yara_heatmap(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: CampaignMapListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_empty_yara_heatmap_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_empty_yara_heatmap_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_empty_yara_heatmap_with_http_info(self, **kwargs):  # noqa: E501
        """Get the users empty yara campaign in heatmap format  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_empty_yara_heatmap_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: CampaignMapListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_empty_yara_heatmap" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/charts/maps/empty_yara/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CampaignMapListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_singletons_heatmap(self, **kwargs):  # noqa: E501
        """Get all the user's singleton info in heat map format  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_singletons_heatmap(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: CampaignMapListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_singletons_heatmap_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_singletons_heatmap_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_singletons_heatmap_with_http_info(self, **kwargs):  # noqa: E501
        """Get all the user's singleton info in heat map format  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_singletons_heatmap_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: CampaignMapListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_singletons_heatmap" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/charts/maps/singletons/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CampaignMapListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_timeline_binaries(self, **kwargs):  # noqa: E501
        """Gets all of the user's binaries in timeline format  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_timeline_binaries(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: BinaryGraphListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_timeline_binaries_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_timeline_binaries_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_timeline_binaries_with_http_info(self, **kwargs):  # noqa: E501
        """Gets all of the user's binaries in timeline format  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_timeline_binaries_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: BinaryGraphListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_timeline_binaries" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/charts/timeline/binaries/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BinaryGraphListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_timeline_campaigns(self, **kwargs):  # noqa: E501
        """Gets all the user's campaigns in timeline format  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_timeline_campaigns(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: CampaignGraphListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_timeline_campaigns_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_timeline_campaigns_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_timeline_campaigns_with_http_info(self, **kwargs):  # noqa: E501
        """Gets all the user's campaigns in timeline format  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_timeline_campaigns_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: CampaignGraphListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_timeline_campaigns" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/charts/timeline/campaigns/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CampaignGraphListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_timeline_singletons(self, **kwargs):  # noqa: E501
        """Gets all of the user's singleton binaries in timeline format  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_timeline_singletons(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: BinaryGraphListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_timeline_singletons_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_timeline_singletons_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_timeline_singletons_with_http_info(self, **kwargs):  # noqa: E501
        """Gets all of the user's singleton binaries in timeline format  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_timeline_singletons_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: BinaryGraphListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_timeline_singletons" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/charts/timeline/singletons/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BinaryGraphListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
