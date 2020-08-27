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


class LoanPrimaryModel(object):
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
        'amount': 'float',
        'attachments': 'list[LoanAttachment]',
        'available': 'float',
        'balance': 'float',
        'bank_guarantee': 'bool',
        'buyback': 'bool',
        'country_code': 'str',
        'generic_collateral': 'Generic',
        'id': 'int',
        'interest_rate': 'float',
        'invoice_collateral': 'Invoice',
        'ltv': 'float',
        'originator': 'str',
        'payment_guarantee': 'bool',
        'realty_collateral': 'Collateral',
        'remaining_term': 'int',
        'request_term': 'int',
        'start_date': 'date',
        'total_percentage_invested': 'float',
        'type': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'attachments': 'attachments',
        'available': 'available',
        'balance': 'balance',
        'bank_guarantee': 'bank_guarantee',
        'buyback': 'buyback',
        'country_code': 'country_code',
        'generic_collateral': 'generic_collateral',
        'id': 'id',
        'interest_rate': 'interest_rate',
        'invoice_collateral': 'invoice_collateral',
        'ltv': 'ltv',
        'originator': 'originator',
        'payment_guarantee': 'payment_guarantee',
        'realty_collateral': 'realty_collateral',
        'remaining_term': 'remaining_term',
        'request_term': 'request_term',
        'start_date': 'start_date',
        'total_percentage_invested': 'total_percentage_invested',
        'type': 'type'
    }

    def __init__(self, amount=None, attachments=None, available=None, balance=None, bank_guarantee=None, buyback=None, country_code=None, generic_collateral=None, id=None, interest_rate=None, invoice_collateral=None, ltv=None, originator=None, payment_guarantee=None, realty_collateral=None, remaining_term=None, request_term=None, start_date=None, total_percentage_invested=None, type=None):  # noqa: E501
        """LoanPrimaryModel - a model defined in Swagger"""  # noqa: E501

        self._amount = None
        self._attachments = None
        self._available = None
        self._balance = None
        self._bank_guarantee = None
        self._buyback = None
        self._country_code = None
        self._generic_collateral = None
        self._id = None
        self._interest_rate = None
        self._invoice_collateral = None
        self._ltv = None
        self._originator = None
        self._payment_guarantee = None
        self._realty_collateral = None
        self._remaining_term = None
        self._request_term = None
        self._start_date = None
        self._total_percentage_invested = None
        self._type = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if attachments is not None:
            self.attachments = attachments
        if available is not None:
            self.available = available
        if balance is not None:
            self.balance = balance
        if bank_guarantee is not None:
            self.bank_guarantee = bank_guarantee
        if buyback is not None:
            self.buyback = buyback
        if country_code is not None:
            self.country_code = country_code
        if generic_collateral is not None:
            self.generic_collateral = generic_collateral
        if id is not None:
            self.id = id
        if interest_rate is not None:
            self.interest_rate = interest_rate
        if invoice_collateral is not None:
            self.invoice_collateral = invoice_collateral
        if ltv is not None:
            self.ltv = ltv
        if originator is not None:
            self.originator = originator
        if payment_guarantee is not None:
            self.payment_guarantee = payment_guarantee
        if realty_collateral is not None:
            self.realty_collateral = realty_collateral
        if remaining_term is not None:
            self.remaining_term = remaining_term
        if request_term is not None:
            self.request_term = request_term
        if start_date is not None:
            self.start_date = start_date
        if total_percentage_invested is not None:
            self.total_percentage_invested = total_percentage_invested
        if type is not None:
            self.type = type

    @property
    def amount(self):
        """Gets the amount of this LoanPrimaryModel.  # noqa: E501


        :return: The amount of this LoanPrimaryModel.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this LoanPrimaryModel.


        :param amount: The amount of this LoanPrimaryModel.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def attachments(self):
        """Gets the attachments of this LoanPrimaryModel.  # noqa: E501


        :return: The attachments of this LoanPrimaryModel.  # noqa: E501
        :rtype: list[LoanAttachment]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this LoanPrimaryModel.


        :param attachments: The attachments of this LoanPrimaryModel.  # noqa: E501
        :type: list[LoanAttachment]
        """

        self._attachments = attachments

    @property
    def available(self):
        """Gets the available of this LoanPrimaryModel.  # noqa: E501


        :return: The available of this LoanPrimaryModel.  # noqa: E501
        :rtype: float
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this LoanPrimaryModel.


        :param available: The available of this LoanPrimaryModel.  # noqa: E501
        :type: float
        """

        self._available = available

    @property
    def balance(self):
        """Gets the balance of this LoanPrimaryModel.  # noqa: E501


        :return: The balance of this LoanPrimaryModel.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this LoanPrimaryModel.


        :param balance: The balance of this LoanPrimaryModel.  # noqa: E501
        :type: float
        """

        self._balance = balance

    @property
    def bank_guarantee(self):
        """Gets the bank_guarantee of this LoanPrimaryModel.  # noqa: E501


        :return: The bank_guarantee of this LoanPrimaryModel.  # noqa: E501
        :rtype: bool
        """
        return self._bank_guarantee

    @bank_guarantee.setter
    def bank_guarantee(self, bank_guarantee):
        """Sets the bank_guarantee of this LoanPrimaryModel.


        :param bank_guarantee: The bank_guarantee of this LoanPrimaryModel.  # noqa: E501
        :type: bool
        """

        self._bank_guarantee = bank_guarantee

    @property
    def buyback(self):
        """Gets the buyback of this LoanPrimaryModel.  # noqa: E501


        :return: The buyback of this LoanPrimaryModel.  # noqa: E501
        :rtype: bool
        """
        return self._buyback

    @buyback.setter
    def buyback(self, buyback):
        """Sets the buyback of this LoanPrimaryModel.


        :param buyback: The buyback of this LoanPrimaryModel.  # noqa: E501
        :type: bool
        """

        self._buyback = buyback

    @property
    def country_code(self):
        """Gets the country_code of this LoanPrimaryModel.  # noqa: E501


        :return: The country_code of this LoanPrimaryModel.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this LoanPrimaryModel.


        :param country_code: The country_code of this LoanPrimaryModel.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def generic_collateral(self):
        """Gets the generic_collateral of this LoanPrimaryModel.  # noqa: E501


        :return: The generic_collateral of this LoanPrimaryModel.  # noqa: E501
        :rtype: Generic
        """
        return self._generic_collateral

    @generic_collateral.setter
    def generic_collateral(self, generic_collateral):
        """Sets the generic_collateral of this LoanPrimaryModel.


        :param generic_collateral: The generic_collateral of this LoanPrimaryModel.  # noqa: E501
        :type: Generic
        """

        self._generic_collateral = generic_collateral

    @property
    def id(self):
        """Gets the id of this LoanPrimaryModel.  # noqa: E501


        :return: The id of this LoanPrimaryModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LoanPrimaryModel.


        :param id: The id of this LoanPrimaryModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def interest_rate(self):
        """Gets the interest_rate of this LoanPrimaryModel.  # noqa: E501


        :return: The interest_rate of this LoanPrimaryModel.  # noqa: E501
        :rtype: float
        """
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, interest_rate):
        """Sets the interest_rate of this LoanPrimaryModel.


        :param interest_rate: The interest_rate of this LoanPrimaryModel.  # noqa: E501
        :type: float
        """

        self._interest_rate = interest_rate

    @property
    def invoice_collateral(self):
        """Gets the invoice_collateral of this LoanPrimaryModel.  # noqa: E501


        :return: The invoice_collateral of this LoanPrimaryModel.  # noqa: E501
        :rtype: Invoice
        """
        return self._invoice_collateral

    @invoice_collateral.setter
    def invoice_collateral(self, invoice_collateral):
        """Sets the invoice_collateral of this LoanPrimaryModel.


        :param invoice_collateral: The invoice_collateral of this LoanPrimaryModel.  # noqa: E501
        :type: Invoice
        """

        self._invoice_collateral = invoice_collateral

    @property
    def ltv(self):
        """Gets the ltv of this LoanPrimaryModel.  # noqa: E501


        :return: The ltv of this LoanPrimaryModel.  # noqa: E501
        :rtype: float
        """
        return self._ltv

    @ltv.setter
    def ltv(self, ltv):
        """Sets the ltv of this LoanPrimaryModel.


        :param ltv: The ltv of this LoanPrimaryModel.  # noqa: E501
        :type: float
        """

        self._ltv = ltv

    @property
    def originator(self):
        """Gets the originator of this LoanPrimaryModel.  # noqa: E501


        :return: The originator of this LoanPrimaryModel.  # noqa: E501
        :rtype: str
        """
        return self._originator

    @originator.setter
    def originator(self, originator):
        """Sets the originator of this LoanPrimaryModel.


        :param originator: The originator of this LoanPrimaryModel.  # noqa: E501
        :type: str
        """

        self._originator = originator

    @property
    def payment_guarantee(self):
        """Gets the payment_guarantee of this LoanPrimaryModel.  # noqa: E501


        :return: The payment_guarantee of this LoanPrimaryModel.  # noqa: E501
        :rtype: bool
        """
        return self._payment_guarantee

    @payment_guarantee.setter
    def payment_guarantee(self, payment_guarantee):
        """Sets the payment_guarantee of this LoanPrimaryModel.


        :param payment_guarantee: The payment_guarantee of this LoanPrimaryModel.  # noqa: E501
        :type: bool
        """

        self._payment_guarantee = payment_guarantee

    @property
    def realty_collateral(self):
        """Gets the realty_collateral of this LoanPrimaryModel.  # noqa: E501


        :return: The realty_collateral of this LoanPrimaryModel.  # noqa: E501
        :rtype: Collateral
        """
        return self._realty_collateral

    @realty_collateral.setter
    def realty_collateral(self, realty_collateral):
        """Sets the realty_collateral of this LoanPrimaryModel.


        :param realty_collateral: The realty_collateral of this LoanPrimaryModel.  # noqa: E501
        :type: Collateral
        """

        self._realty_collateral = realty_collateral

    @property
    def remaining_term(self):
        """Gets the remaining_term of this LoanPrimaryModel.  # noqa: E501


        :return: The remaining_term of this LoanPrimaryModel.  # noqa: E501
        :rtype: int
        """
        return self._remaining_term

    @remaining_term.setter
    def remaining_term(self, remaining_term):
        """Sets the remaining_term of this LoanPrimaryModel.


        :param remaining_term: The remaining_term of this LoanPrimaryModel.  # noqa: E501
        :type: int
        """

        self._remaining_term = remaining_term

    @property
    def request_term(self):
        """Gets the request_term of this LoanPrimaryModel.  # noqa: E501


        :return: The request_term of this LoanPrimaryModel.  # noqa: E501
        :rtype: int
        """
        return self._request_term

    @request_term.setter
    def request_term(self, request_term):
        """Sets the request_term of this LoanPrimaryModel.


        :param request_term: The request_term of this LoanPrimaryModel.  # noqa: E501
        :type: int
        """

        self._request_term = request_term

    @property
    def start_date(self):
        """Gets the start_date of this LoanPrimaryModel.  # noqa: E501


        :return: The start_date of this LoanPrimaryModel.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this LoanPrimaryModel.


        :param start_date: The start_date of this LoanPrimaryModel.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

    @property
    def total_percentage_invested(self):
        """Gets the total_percentage_invested of this LoanPrimaryModel.  # noqa: E501


        :return: The total_percentage_invested of this LoanPrimaryModel.  # noqa: E501
        :rtype: float
        """
        return self._total_percentage_invested

    @total_percentage_invested.setter
    def total_percentage_invested(self, total_percentage_invested):
        """Sets the total_percentage_invested of this LoanPrimaryModel.


        :param total_percentage_invested: The total_percentage_invested of this LoanPrimaryModel.  # noqa: E501
        :type: float
        """

        self._total_percentage_invested = total_percentage_invested

    @property
    def type(self):
        """Gets the type of this LoanPrimaryModel.  # noqa: E501


        :return: The type of this LoanPrimaryModel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LoanPrimaryModel.


        :param type: The type of this LoanPrimaryModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["MORTGAGE", "CONSUMER", "INVOICE_FINANCING", "BUSINESS", "LINE_OF_CREDIT", "PAWNBROKING"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(LoanPrimaryModel, dict):
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
        if not isinstance(other, LoanPrimaryModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other