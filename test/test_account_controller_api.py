# coding: utf-8

"""
    Mobile API

    All decimal values are accepted and returned with 2 decimal place precision, e.g., 150.21. All date fields are sent in ISO 8601 format YYYY-MM-DD, e.g., 2016-11-30.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import api_mobile
from api_mobile.api.account_controller_api import AccountControllerApi  # noqa: E501
from api_mobile.rest import ApiException


class TestAccountControllerApi(unittest.TestCase):
    """AccountControllerApi unit test stubs"""

    def setUp(self):
        self.api = api_mobile.api.account_controller_api.AccountControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_export_and_download_statement_as_json_using_post(self):
        """Test case for export_and_download_statement_as_json_using_post

        exportAndDownloadStatementAsJson  # noqa: E501
        """
        pass

    def test_export_and_download_statement_ios_using_post(self):
        """Test case for export_and_download_statement_ios_using_post

        exportAndDownloadStatementIOS  # noqa: E501
        """
        pass

    def test_export_and_download_statement_using_post(self):
        """Test case for export_and_download_statement_using_post

        exportAndDownloadStatement  # noqa: E501
        """
        pass

    def test_generate_tax_report_in_html_using_post(self):
        """Test case for generate_tax_report_in_html_using_post

        generateTaxReportInHtml  # noqa: E501
        """
        pass

    def test_generate_tax_report_in_pdf_using_post(self):
        """Test case for generate_tax_report_in_pdf_using_post

        generateTaxReportInPdf  # noqa: E501
        """
        pass

    def test_get_account_balance_using_get(self):
        """Test case for get_account_balance_using_get

        getAccountBalance  # noqa: E501
        """
        pass

    def test_get_account_statement_using_get(self):
        """Test case for get_account_statement_using_get

        getAccountStatement  # noqa: E501
        """
        pass

    def test_get_account_statement_using_post(self):
        """Test case for get_account_statement_using_post

        getAccountStatement  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
