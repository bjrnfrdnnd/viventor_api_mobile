# coding: utf-8

"""
    Mobile API

    All decimal values are accepted and returned with 2 decimal place precision, e.g., 150.21. All date fields are sent in ISO 8601 format YYYY-MM-DD, e.g., 2016-11-30.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class StatisticsModel(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'business_interest_rates': 'list[StatisticsEntryModel]',
        'client_count': 'int',
        'consumer_interest_rates': 'list[StatisticsEntryModel]',
        'interest_paid': 'list[StatisticsEntryModel]',
        'investments': 'list[StatisticsEntryModel]',
        'invoice_financing_interest_rates': 'list[StatisticsEntryModel]',
        'line_of_credit_interest_rates': 'list[StatisticsEntryModel]',
        'mortgage_interest_rates': 'list[StatisticsEntryModel]',
        'pawnbroking_interest_rates': 'list[StatisticsEntryModel]',
        'total_business_investments': 'float',
        'total_consumer_investments': 'float',
        'total_interest_paid': 'float',
        'total_investments': 'float',
        'total_invoice_financing_investments': 'float',
        'total_line_of_credit_investments': 'float',
        'total_mortgage_investments': 'float',
        'total_pawnbroking_investments': 'float'
    }

    attribute_map = {
        'business_interest_rates': 'business_interest_rates',
        'client_count': 'client_count',
        'consumer_interest_rates': 'consumer_interest_rates',
        'interest_paid': 'interest_paid',
        'investments': 'investments',
        'invoice_financing_interest_rates': 'invoice_financing_interest_rates',
        'line_of_credit_interest_rates': 'line_of_credit_interest_rates',
        'mortgage_interest_rates': 'mortgage_interest_rates',
        'pawnbroking_interest_rates': 'pawnbroking_interest_rates',
        'total_business_investments': 'total_business_investments',
        'total_consumer_investments': 'total_consumer_investments',
        'total_interest_paid': 'total_interest_paid',
        'total_investments': 'total_investments',
        'total_invoice_financing_investments': 'total_invoice_financing_investments',
        'total_line_of_credit_investments': 'total_line_of_credit_investments',
        'total_mortgage_investments': 'total_mortgage_investments',
        'total_pawnbroking_investments': 'total_pawnbroking_investments'
    }

    def __init__(self, business_interest_rates=None, client_count=None, consumer_interest_rates=None, interest_paid=None, investments=None, invoice_financing_interest_rates=None, line_of_credit_interest_rates=None, mortgage_interest_rates=None, pawnbroking_interest_rates=None, total_business_investments=None, total_consumer_investments=None, total_interest_paid=None, total_investments=None, total_invoice_financing_investments=None, total_line_of_credit_investments=None, total_mortgage_investments=None, total_pawnbroking_investments=None):  # noqa: E501
        """StatisticsModel - a model defined in Swagger"""  # noqa: E501

        self._business_interest_rates = None
        self._client_count = None
        self._consumer_interest_rates = None
        self._interest_paid = None
        self._investments = None
        self._invoice_financing_interest_rates = None
        self._line_of_credit_interest_rates = None
        self._mortgage_interest_rates = None
        self._pawnbroking_interest_rates = None
        self._total_business_investments = None
        self._total_consumer_investments = None
        self._total_interest_paid = None
        self._total_investments = None
        self._total_invoice_financing_investments = None
        self._total_line_of_credit_investments = None
        self._total_mortgage_investments = None
        self._total_pawnbroking_investments = None
        self.discriminator = None

        if business_interest_rates is not None:
            self.business_interest_rates = business_interest_rates
        if client_count is not None:
            self.client_count = client_count
        if consumer_interest_rates is not None:
            self.consumer_interest_rates = consumer_interest_rates
        if interest_paid is not None:
            self.interest_paid = interest_paid
        if investments is not None:
            self.investments = investments
        if invoice_financing_interest_rates is not None:
            self.invoice_financing_interest_rates = invoice_financing_interest_rates
        if line_of_credit_interest_rates is not None:
            self.line_of_credit_interest_rates = line_of_credit_interest_rates
        if mortgage_interest_rates is not None:
            self.mortgage_interest_rates = mortgage_interest_rates
        if pawnbroking_interest_rates is not None:
            self.pawnbroking_interest_rates = pawnbroking_interest_rates
        if total_business_investments is not None:
            self.total_business_investments = total_business_investments
        if total_consumer_investments is not None:
            self.total_consumer_investments = total_consumer_investments
        if total_interest_paid is not None:
            self.total_interest_paid = total_interest_paid
        if total_investments is not None:
            self.total_investments = total_investments
        if total_invoice_financing_investments is not None:
            self.total_invoice_financing_investments = total_invoice_financing_investments
        if total_line_of_credit_investments is not None:
            self.total_line_of_credit_investments = total_line_of_credit_investments
        if total_mortgage_investments is not None:
            self.total_mortgage_investments = total_mortgage_investments
        if total_pawnbroking_investments is not None:
            self.total_pawnbroking_investments = total_pawnbroking_investments

    @property
    def business_interest_rates(self):
        """Gets the business_interest_rates of this StatisticsModel.  # noqa: E501


        :return: The business_interest_rates of this StatisticsModel.  # noqa: E501
        :rtype: list[StatisticsEntryModel]
        """
        return self._business_interest_rates

    @business_interest_rates.setter
    def business_interest_rates(self, business_interest_rates):
        """Sets the business_interest_rates of this StatisticsModel.


        :param business_interest_rates: The business_interest_rates of this StatisticsModel.  # noqa: E501
        :type: list[StatisticsEntryModel]
        """

        self._business_interest_rates = business_interest_rates

    @property
    def client_count(self):
        """Gets the client_count of this StatisticsModel.  # noqa: E501


        :return: The client_count of this StatisticsModel.  # noqa: E501
        :rtype: int
        """
        return self._client_count

    @client_count.setter
    def client_count(self, client_count):
        """Sets the client_count of this StatisticsModel.


        :param client_count: The client_count of this StatisticsModel.  # noqa: E501
        :type: int
        """

        self._client_count = client_count

    @property
    def consumer_interest_rates(self):
        """Gets the consumer_interest_rates of this StatisticsModel.  # noqa: E501


        :return: The consumer_interest_rates of this StatisticsModel.  # noqa: E501
        :rtype: list[StatisticsEntryModel]
        """
        return self._consumer_interest_rates

    @consumer_interest_rates.setter
    def consumer_interest_rates(self, consumer_interest_rates):
        """Sets the consumer_interest_rates of this StatisticsModel.


        :param consumer_interest_rates: The consumer_interest_rates of this StatisticsModel.  # noqa: E501
        :type: list[StatisticsEntryModel]
        """

        self._consumer_interest_rates = consumer_interest_rates

    @property
    def interest_paid(self):
        """Gets the interest_paid of this StatisticsModel.  # noqa: E501


        :return: The interest_paid of this StatisticsModel.  # noqa: E501
        :rtype: list[StatisticsEntryModel]
        """
        return self._interest_paid

    @interest_paid.setter
    def interest_paid(self, interest_paid):
        """Sets the interest_paid of this StatisticsModel.


        :param interest_paid: The interest_paid of this StatisticsModel.  # noqa: E501
        :type: list[StatisticsEntryModel]
        """

        self._interest_paid = interest_paid

    @property
    def investments(self):
        """Gets the investments of this StatisticsModel.  # noqa: E501


        :return: The investments of this StatisticsModel.  # noqa: E501
        :rtype: list[StatisticsEntryModel]
        """
        return self._investments

    @investments.setter
    def investments(self, investments):
        """Sets the investments of this StatisticsModel.


        :param investments: The investments of this StatisticsModel.  # noqa: E501
        :type: list[StatisticsEntryModel]
        """

        self._investments = investments

    @property
    def invoice_financing_interest_rates(self):
        """Gets the invoice_financing_interest_rates of this StatisticsModel.  # noqa: E501


        :return: The invoice_financing_interest_rates of this StatisticsModel.  # noqa: E501
        :rtype: list[StatisticsEntryModel]
        """
        return self._invoice_financing_interest_rates

    @invoice_financing_interest_rates.setter
    def invoice_financing_interest_rates(self, invoice_financing_interest_rates):
        """Sets the invoice_financing_interest_rates of this StatisticsModel.


        :param invoice_financing_interest_rates: The invoice_financing_interest_rates of this StatisticsModel.  # noqa: E501
        :type: list[StatisticsEntryModel]
        """

        self._invoice_financing_interest_rates = invoice_financing_interest_rates

    @property
    def line_of_credit_interest_rates(self):
        """Gets the line_of_credit_interest_rates of this StatisticsModel.  # noqa: E501


        :return: The line_of_credit_interest_rates of this StatisticsModel.  # noqa: E501
        :rtype: list[StatisticsEntryModel]
        """
        return self._line_of_credit_interest_rates

    @line_of_credit_interest_rates.setter
    def line_of_credit_interest_rates(self, line_of_credit_interest_rates):
        """Sets the line_of_credit_interest_rates of this StatisticsModel.


        :param line_of_credit_interest_rates: The line_of_credit_interest_rates of this StatisticsModel.  # noqa: E501
        :type: list[StatisticsEntryModel]
        """

        self._line_of_credit_interest_rates = line_of_credit_interest_rates

    @property
    def mortgage_interest_rates(self):
        """Gets the mortgage_interest_rates of this StatisticsModel.  # noqa: E501


        :return: The mortgage_interest_rates of this StatisticsModel.  # noqa: E501
        :rtype: list[StatisticsEntryModel]
        """
        return self._mortgage_interest_rates

    @mortgage_interest_rates.setter
    def mortgage_interest_rates(self, mortgage_interest_rates):
        """Sets the mortgage_interest_rates of this StatisticsModel.


        :param mortgage_interest_rates: The mortgage_interest_rates of this StatisticsModel.  # noqa: E501
        :type: list[StatisticsEntryModel]
        """

        self._mortgage_interest_rates = mortgage_interest_rates

    @property
    def pawnbroking_interest_rates(self):
        """Gets the pawnbroking_interest_rates of this StatisticsModel.  # noqa: E501


        :return: The pawnbroking_interest_rates of this StatisticsModel.  # noqa: E501
        :rtype: list[StatisticsEntryModel]
        """
        return self._pawnbroking_interest_rates

    @pawnbroking_interest_rates.setter
    def pawnbroking_interest_rates(self, pawnbroking_interest_rates):
        """Sets the pawnbroking_interest_rates of this StatisticsModel.


        :param pawnbroking_interest_rates: The pawnbroking_interest_rates of this StatisticsModel.  # noqa: E501
        :type: list[StatisticsEntryModel]
        """

        self._pawnbroking_interest_rates = pawnbroking_interest_rates

    @property
    def total_business_investments(self):
        """Gets the total_business_investments of this StatisticsModel.  # noqa: E501


        :return: The total_business_investments of this StatisticsModel.  # noqa: E501
        :rtype: float
        """
        return self._total_business_investments

    @total_business_investments.setter
    def total_business_investments(self, total_business_investments):
        """Sets the total_business_investments of this StatisticsModel.


        :param total_business_investments: The total_business_investments of this StatisticsModel.  # noqa: E501
        :type: float
        """

        self._total_business_investments = total_business_investments

    @property
    def total_consumer_investments(self):
        """Gets the total_consumer_investments of this StatisticsModel.  # noqa: E501


        :return: The total_consumer_investments of this StatisticsModel.  # noqa: E501
        :rtype: float
        """
        return self._total_consumer_investments

    @total_consumer_investments.setter
    def total_consumer_investments(self, total_consumer_investments):
        """Sets the total_consumer_investments of this StatisticsModel.


        :param total_consumer_investments: The total_consumer_investments of this StatisticsModel.  # noqa: E501
        :type: float
        """

        self._total_consumer_investments = total_consumer_investments

    @property
    def total_interest_paid(self):
        """Gets the total_interest_paid of this StatisticsModel.  # noqa: E501


        :return: The total_interest_paid of this StatisticsModel.  # noqa: E501
        :rtype: float
        """
        return self._total_interest_paid

    @total_interest_paid.setter
    def total_interest_paid(self, total_interest_paid):
        """Sets the total_interest_paid of this StatisticsModel.


        :param total_interest_paid: The total_interest_paid of this StatisticsModel.  # noqa: E501
        :type: float
        """

        self._total_interest_paid = total_interest_paid

    @property
    def total_investments(self):
        """Gets the total_investments of this StatisticsModel.  # noqa: E501


        :return: The total_investments of this StatisticsModel.  # noqa: E501
        :rtype: float
        """
        return self._total_investments

    @total_investments.setter
    def total_investments(self, total_investments):
        """Sets the total_investments of this StatisticsModel.


        :param total_investments: The total_investments of this StatisticsModel.  # noqa: E501
        :type: float
        """

        self._total_investments = total_investments

    @property
    def total_invoice_financing_investments(self):
        """Gets the total_invoice_financing_investments of this StatisticsModel.  # noqa: E501


        :return: The total_invoice_financing_investments of this StatisticsModel.  # noqa: E501
        :rtype: float
        """
        return self._total_invoice_financing_investments

    @total_invoice_financing_investments.setter
    def total_invoice_financing_investments(self, total_invoice_financing_investments):
        """Sets the total_invoice_financing_investments of this StatisticsModel.


        :param total_invoice_financing_investments: The total_invoice_financing_investments of this StatisticsModel.  # noqa: E501
        :type: float
        """

        self._total_invoice_financing_investments = total_invoice_financing_investments

    @property
    def total_line_of_credit_investments(self):
        """Gets the total_line_of_credit_investments of this StatisticsModel.  # noqa: E501


        :return: The total_line_of_credit_investments of this StatisticsModel.  # noqa: E501
        :rtype: float
        """
        return self._total_line_of_credit_investments

    @total_line_of_credit_investments.setter
    def total_line_of_credit_investments(self, total_line_of_credit_investments):
        """Sets the total_line_of_credit_investments of this StatisticsModel.


        :param total_line_of_credit_investments: The total_line_of_credit_investments of this StatisticsModel.  # noqa: E501
        :type: float
        """

        self._total_line_of_credit_investments = total_line_of_credit_investments

    @property
    def total_mortgage_investments(self):
        """Gets the total_mortgage_investments of this StatisticsModel.  # noqa: E501


        :return: The total_mortgage_investments of this StatisticsModel.  # noqa: E501
        :rtype: float
        """
        return self._total_mortgage_investments

    @total_mortgage_investments.setter
    def total_mortgage_investments(self, total_mortgage_investments):
        """Sets the total_mortgage_investments of this StatisticsModel.


        :param total_mortgage_investments: The total_mortgage_investments of this StatisticsModel.  # noqa: E501
        :type: float
        """

        self._total_mortgage_investments = total_mortgage_investments

    @property
    def total_pawnbroking_investments(self):
        """Gets the total_pawnbroking_investments of this StatisticsModel.  # noqa: E501


        :return: The total_pawnbroking_investments of this StatisticsModel.  # noqa: E501
        :rtype: float
        """
        return self._total_pawnbroking_investments

    @total_pawnbroking_investments.setter
    def total_pawnbroking_investments(self, total_pawnbroking_investments):
        """Sets the total_pawnbroking_investments of this StatisticsModel.


        :param total_pawnbroking_investments: The total_pawnbroking_investments of this StatisticsModel.  # noqa: E501
        :type: float
        """

        self._total_pawnbroking_investments = total_pawnbroking_investments

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(StatisticsModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StatisticsModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other