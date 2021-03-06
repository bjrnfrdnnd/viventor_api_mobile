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
from viventor_api_mobile.api.statistics_controller_api import StatisticsControllerApi  # noqa: E501
from viventor_api_mobile.rest import ApiException


class TestStatisticsControllerApi(unittest.TestCase):
    """StatisticsControllerApi unit test stubs"""

    def setUp(self):
        self.api = viventor_api_mobile.api.statistics_controller_api.StatisticsControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_statistic_xirr_using_get(self):
        """Test case for statistic_xirr_using_get

        statisticXirr  # noqa: E501
        """
        pass

    def test_statistics_using_get(self):
        """Test case for statistics_using_get

        statistics  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
