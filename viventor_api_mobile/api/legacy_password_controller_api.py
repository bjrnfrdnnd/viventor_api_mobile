# coding: utf-8

"""
    Mobile API

    All decimal values are accepted and returned with 2 decimal place precision, e.g., 150.21. All date fields are sent in ISO 8601 format YYYY-MM-DD, e.g., 2016-11-30.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from viventor_api_mobile.api_client import ApiClient


class LegacyPasswordControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def change_password_using_post1(self, change_password_info, **kwargs):  # noqa: E501
        """changePassword  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_password_using_post1(change_password_info, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ChangePasswordInfo change_password_info: changePasswordInfo (required)
        :return: CommonOperationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.change_password_using_post1_with_http_info(change_password_info, **kwargs)  # noqa: E501
        else:
            (data) = self.change_password_using_post1_with_http_info(change_password_info, **kwargs)  # noqa: E501
            return data

    def change_password_using_post1_with_http_info(self, change_password_info, **kwargs):  # noqa: E501
        """changePassword  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_password_using_post1_with_http_info(change_password_info, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ChangePasswordInfo change_password_info: changePasswordInfo (required)
        :return: CommonOperationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['change_password_info']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method change_password_using_post1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'change_password_info' is set
        if ('change_password_info' not in params or
                params['change_password_info'] is None):
            raise ValueError("Missing the required parameter `change_password_info` when calling `change_password_using_post1`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'change_password_info' in params:
            body_params = params['change_password_info']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/app/v1/user/settings/change-password.json', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CommonOperationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def confirm_password_reset_using_post(self, reset_password_info, **kwargs):  # noqa: E501
        """confirmPasswordReset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.confirm_password_reset_using_post(reset_password_info, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ResetPasswordInfo reset_password_info: resetPasswordInfo (required)
        :return: CommonOperationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.confirm_password_reset_using_post_with_http_info(reset_password_info, **kwargs)  # noqa: E501
        else:
            (data) = self.confirm_password_reset_using_post_with_http_info(reset_password_info, **kwargs)  # noqa: E501
            return data

    def confirm_password_reset_using_post_with_http_info(self, reset_password_info, **kwargs):  # noqa: E501
        """confirmPasswordReset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.confirm_password_reset_using_post_with_http_info(reset_password_info, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ResetPasswordInfo reset_password_info: resetPasswordInfo (required)
        :return: CommonOperationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['reset_password_info']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method confirm_password_reset_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'reset_password_info' is set
        if ('reset_password_info' not in params or
                params['reset_password_info'] is None):
            raise ValueError("Missing the required parameter `reset_password_info` when calling `confirm_password_reset_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'reset_password_info' in params:
            body_params = params['reset_password_info']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/app/v1/user/recover/second.json', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CommonOperationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def request_password_reset_using_post(self, email, **kwargs):  # noqa: E501
        """requestPasswordReset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_password_reset_using_post(email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str email: email (required)
        :return: CommonOperationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.request_password_reset_using_post_with_http_info(email, **kwargs)  # noqa: E501
        else:
            (data) = self.request_password_reset_using_post_with_http_info(email, **kwargs)  # noqa: E501
            return data

    def request_password_reset_using_post_with_http_info(self, email, **kwargs):  # noqa: E501
        """requestPasswordReset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_password_reset_using_post_with_http_info(email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str email: email (required)
        :return: CommonOperationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['email']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method request_password_reset_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'email' is set
        if ('email' not in params or
                params['email'] is None):
            raise ValueError("Missing the required parameter `email` when calling `request_password_reset_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'email' in params:
            query_params.append(('email', params['email']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/app/v1/user/recover/first.json', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CommonOperationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
