# coding: utf-8

"""
    Mobile API

    All decimal values are accepted and returned with 2 decimal place precision, e.g., 150.21. All date fields are sent in ISO 8601 format YYYY-MM-DD, e.g., 2016-11-30.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import viventor_api_mobile
from viventor_api_mobile.api.filter_controller_api import FilterControllerApi  # noqa: E501
from viventor_api_mobile.rest import ApiException


class TestFilterControllerApi(unittest.TestCase):
    """FilterControllerApi unit test stubs"""

    def setUp(self):
        self.api = viventor_api_mobile.api.filter_controller_api.FilterControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_using_post5(self):
        """Test case for create_using_post5

        create  # noqa: E501
        """
        pass

    def test_delete_using_post1(self):
        """Test case for delete_using_post1

        delete  # noqa: E501
        """
        pass

    def test_read_using_get4(self):
        """Test case for read_using_get4

        read  # noqa: E501
        """
        pass

    def test_read_using_get5(self):
        """Test case for read_using_get5

        read  # noqa: E501
        """
        pass

    def test_update_using_post1(self):
        """Test case for update_using_post1

        update  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
