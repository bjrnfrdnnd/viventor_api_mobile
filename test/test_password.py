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
from viventor_api_mobile.models.password import Password  # noqa: E501
from viventor_api_mobile.rest import ApiException


class TestPassword(unittest.TestCase):
    """Password unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPassword(self):
        """Test Password"""
        # FIXME: construct object with mandatory attributes with example values
        # model = viventor_api_mobile.models.password.Password()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
