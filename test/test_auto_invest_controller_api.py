# coding: utf-8

"""
    Mobile API

    All decimal values are accepted and returned with 2 decimal place precision, e.g., 150.21. All date fields are sent in ISO 8601 format YYYY-MM-DD, e.g., 2016-11-30.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.auto_invest_controller_api import AutoInvestControllerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAutoInvestControllerApi(unittest.TestCase):
    """AutoInvestControllerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.auto_invest_controller_api.AutoInvestControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_activate_using_get(self):
        """Test case for activate_using_get

        activate  # noqa: E501
        """
        pass

    def test_add_auto_investment_using_post(self):
        """Test case for add_auto_investment_using_post

        addAutoInvestment  # noqa: E501
        """
        pass

    def test_delete_using_get(self):
        """Test case for delete_using_get

        delete  # noqa: E501
        """
        pass

    def test_edit_auto_investment_using_post(self):
        """Test case for edit_auto_investment_using_post

        editAutoInvestment  # noqa: E501
        """
        pass

    def test_get_auto_investment_list_using_get(self):
        """Test case for get_auto_investment_list_using_get

        getAutoInvestmentList  # noqa: E501
        """
        pass

    def test_get_auto_investment_view_using_get(self):
        """Test case for get_auto_investment_view_using_get

        getAutoInvestmentView  # noqa: E501
        """
        pass

    def test_stop_using_get(self):
        """Test case for stop_using_get

        stop  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()