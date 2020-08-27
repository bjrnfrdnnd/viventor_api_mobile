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


class LoanPrimary(object):
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
        'attachments': 'list[LoanAttachment]',
        'available_capital_for_investment': 'float',
        'bank_guarantee': 'bool',
        'buyback': 'bool',
        'company': 'str',
        'country_code': 'str',
        'date_end': 'datetime',
        'extended': 'bool',
        'generic_collateral': 'Generic',
        'initial_capital': 'float',
        'interest': 'float',
        'investment_enabled': 'bool',
        'invoice_collateral': 'Invoice',
        'loan_rating': 'str',
        'loan_type': 'int',
        'loan_type_name': 'str',
        'loan_request_rid': 'int',
        'ltv': 'float',
        'ltv2': 'float',
        'original_start_date': 'datetime',
        'payment_guarantee': 'bool',
        'payments_status': 'int',
        'realty_collateral': 'Collateral',
        'remaing_capital_after_paid_quote': 'float',
        'remaining_capital_for_investment': 'float',
        'remaining_loan_term': 'int',
        'request_date': 'datetime',
        'request_term': 'int',
        't_presta_key': 'int',
        'total_invested': 'float',
        'total_percentage_invested': 'float'
    }

    attribute_map = {
        'attachments': 'attachments',
        'available_capital_for_investment': 'available_capital_forInvestment',
        'bank_guarantee': 'bank_guarantee',
        'buyback': 'buyback',
        'company': 'company',
        'country_code': 'country_code',
        'date_end': 'date_end',
        'extended': 'extended',
        'generic_collateral': 'generic_collateral',
        'initial_capital': 'initial_capital',
        'interest': 'interest',
        'investment_enabled': 'investment_enabled',
        'invoice_collateral': 'invoice_collateral',
        'loan_rating': 'loanRating',
        'loan_type': 'loanType',
        'loan_type_name': 'loanTypeName',
        'loan_request_rid': 'loan_request_rid',
        'ltv': 'ltv',
        'ltv2': 'ltv2',
        'original_start_date': 'original_start_date',
        'payment_guarantee': 'payment_guarantee',
        'payments_status': 'paymentsStatus',
        'realty_collateral': 'realty_collateral',
        'remaing_capital_after_paid_quote': 'remaing_capital_afterPaidQuote',
        'remaining_capital_for_investment': 'remaining_capital_forInvestment',
        'remaining_loan_term': 'remaining_loan_term',
        'request_date': 'request_date',
        'request_term': 'request_term',
        't_presta_key': 't_presta_key',
        'total_invested': 'totalInvested',
        'total_percentage_invested': 'total_percentage_invested'
    }

    def __init__(self, attachments=None, available_capital_for_investment=None, bank_guarantee=None, buyback=None, company=None, country_code=None, date_end=None, extended=None, generic_collateral=None, initial_capital=None, interest=None, investment_enabled=None, invoice_collateral=None, loan_rating=None, loan_type=None, loan_type_name=None, loan_request_rid=None, ltv=None, ltv2=None, original_start_date=None, payment_guarantee=None, payments_status=None, realty_collateral=None, remaing_capital_after_paid_quote=None, remaining_capital_for_investment=None, remaining_loan_term=None, request_date=None, request_term=None, t_presta_key=None, total_invested=None, total_percentage_invested=None):  # noqa: E501
        """LoanPrimary - a model defined in Swagger"""  # noqa: E501

        self._attachments = None
        self._available_capital_for_investment = None
        self._bank_guarantee = None
        self._buyback = None
        self._company = None
        self._country_code = None
        self._date_end = None
        self._extended = None
        self._generic_collateral = None
        self._initial_capital = None
        self._interest = None
        self._investment_enabled = None
        self._invoice_collateral = None
        self._loan_rating = None
        self._loan_type = None
        self._loan_type_name = None
        self._loan_request_rid = None
        self._ltv = None
        self._ltv2 = None
        self._original_start_date = None
        self._payment_guarantee = None
        self._payments_status = None
        self._realty_collateral = None
        self._remaing_capital_after_paid_quote = None
        self._remaining_capital_for_investment = None
        self._remaining_loan_term = None
        self._request_date = None
        self._request_term = None
        self._t_presta_key = None
        self._total_invested = None
        self._total_percentage_invested = None
        self.discriminator = None

        if attachments is not None:
            self.attachments = attachments
        if available_capital_for_investment is not None:
            self.available_capital_for_investment = available_capital_for_investment
        if bank_guarantee is not None:
            self.bank_guarantee = bank_guarantee
        if buyback is not None:
            self.buyback = buyback
        if company is not None:
            self.company = company
        if country_code is not None:
            self.country_code = country_code
        if date_end is not None:
            self.date_end = date_end
        if extended is not None:
            self.extended = extended
        if generic_collateral is not None:
            self.generic_collateral = generic_collateral
        if initial_capital is not None:
            self.initial_capital = initial_capital
        if interest is not None:
            self.interest = interest
        if investment_enabled is not None:
            self.investment_enabled = investment_enabled
        if invoice_collateral is not None:
            self.invoice_collateral = invoice_collateral
        if loan_rating is not None:
            self.loan_rating = loan_rating
        if loan_type is not None:
            self.loan_type = loan_type
        if loan_type_name is not None:
            self.loan_type_name = loan_type_name
        if loan_request_rid is not None:
            self.loan_request_rid = loan_request_rid
        if ltv is not None:
            self.ltv = ltv
        if ltv2 is not None:
            self.ltv2 = ltv2
        if original_start_date is not None:
            self.original_start_date = original_start_date
        if payment_guarantee is not None:
            self.payment_guarantee = payment_guarantee
        if payments_status is not None:
            self.payments_status = payments_status
        if realty_collateral is not None:
            self.realty_collateral = realty_collateral
        if remaing_capital_after_paid_quote is not None:
            self.remaing_capital_after_paid_quote = remaing_capital_after_paid_quote
        if remaining_capital_for_investment is not None:
            self.remaining_capital_for_investment = remaining_capital_for_investment
        if remaining_loan_term is not None:
            self.remaining_loan_term = remaining_loan_term
        if request_date is not None:
            self.request_date = request_date
        if request_term is not None:
            self.request_term = request_term
        if t_presta_key is not None:
            self.t_presta_key = t_presta_key
        if total_invested is not None:
            self.total_invested = total_invested
        if total_percentage_invested is not None:
            self.total_percentage_invested = total_percentage_invested

    @property
    def attachments(self):
        """Gets the attachments of this LoanPrimary.  # noqa: E501


        :return: The attachments of this LoanPrimary.  # noqa: E501
        :rtype: list[LoanAttachment]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this LoanPrimary.


        :param attachments: The attachments of this LoanPrimary.  # noqa: E501
        :type: list[LoanAttachment]
        """

        self._attachments = attachments

    @property
    def available_capital_for_investment(self):
        """Gets the available_capital_for_investment of this LoanPrimary.  # noqa: E501


        :return: The available_capital_for_investment of this LoanPrimary.  # noqa: E501
        :rtype: float
        """
        return self._available_capital_for_investment

    @available_capital_for_investment.setter
    def available_capital_for_investment(self, available_capital_for_investment):
        """Sets the available_capital_for_investment of this LoanPrimary.


        :param available_capital_for_investment: The available_capital_for_investment of this LoanPrimary.  # noqa: E501
        :type: float
        """

        self._available_capital_for_investment = available_capital_for_investment

    @property
    def bank_guarantee(self):
        """Gets the bank_guarantee of this LoanPrimary.  # noqa: E501


        :return: The bank_guarantee of this LoanPrimary.  # noqa: E501
        :rtype: bool
        """
        return self._bank_guarantee

    @bank_guarantee.setter
    def bank_guarantee(self, bank_guarantee):
        """Sets the bank_guarantee of this LoanPrimary.


        :param bank_guarantee: The bank_guarantee of this LoanPrimary.  # noqa: E501
        :type: bool
        """

        self._bank_guarantee = bank_guarantee

    @property
    def buyback(self):
        """Gets the buyback of this LoanPrimary.  # noqa: E501


        :return: The buyback of this LoanPrimary.  # noqa: E501
        :rtype: bool
        """
        return self._buyback

    @buyback.setter
    def buyback(self, buyback):
        """Sets the buyback of this LoanPrimary.


        :param buyback: The buyback of this LoanPrimary.  # noqa: E501
        :type: bool
        """

        self._buyback = buyback

    @property
    def company(self):
        """Gets the company of this LoanPrimary.  # noqa: E501


        :return: The company of this LoanPrimary.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this LoanPrimary.


        :param company: The company of this LoanPrimary.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def country_code(self):
        """Gets the country_code of this LoanPrimary.  # noqa: E501


        :return: The country_code of this LoanPrimary.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this LoanPrimary.


        :param country_code: The country_code of this LoanPrimary.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def date_end(self):
        """Gets the date_end of this LoanPrimary.  # noqa: E501


        :return: The date_end of this LoanPrimary.  # noqa: E501
        :rtype: datetime
        """
        return self._date_end

    @date_end.setter
    def date_end(self, date_end):
        """Sets the date_end of this LoanPrimary.


        :param date_end: The date_end of this LoanPrimary.  # noqa: E501
        :type: datetime
        """

        self._date_end = date_end

    @property
    def extended(self):
        """Gets the extended of this LoanPrimary.  # noqa: E501


        :return: The extended of this LoanPrimary.  # noqa: E501
        :rtype: bool
        """
        return self._extended

    @extended.setter
    def extended(self, extended):
        """Sets the extended of this LoanPrimary.


        :param extended: The extended of this LoanPrimary.  # noqa: E501
        :type: bool
        """

        self._extended = extended

    @property
    def generic_collateral(self):
        """Gets the generic_collateral of this LoanPrimary.  # noqa: E501


        :return: The generic_collateral of this LoanPrimary.  # noqa: E501
        :rtype: Generic
        """
        return self._generic_collateral

    @generic_collateral.setter
    def generic_collateral(self, generic_collateral):
        """Sets the generic_collateral of this LoanPrimary.


        :param generic_collateral: The generic_collateral of this LoanPrimary.  # noqa: E501
        :type: Generic
        """

        self._generic_collateral = generic_collateral

    @property
    def initial_capital(self):
        """Gets the initial_capital of this LoanPrimary.  # noqa: E501


        :return: The initial_capital of this LoanPrimary.  # noqa: E501
        :rtype: float
        """
        return self._initial_capital

    @initial_capital.setter
    def initial_capital(self, initial_capital):
        """Sets the initial_capital of this LoanPrimary.


        :param initial_capital: The initial_capital of this LoanPrimary.  # noqa: E501
        :type: float
        """

        self._initial_capital = initial_capital

    @property
    def interest(self):
        """Gets the interest of this LoanPrimary.  # noqa: E501


        :return: The interest of this LoanPrimary.  # noqa: E501
        :rtype: float
        """
        return self._interest

    @interest.setter
    def interest(self, interest):
        """Sets the interest of this LoanPrimary.


        :param interest: The interest of this LoanPrimary.  # noqa: E501
        :type: float
        """

        self._interest = interest

    @property
    def investment_enabled(self):
        """Gets the investment_enabled of this LoanPrimary.  # noqa: E501


        :return: The investment_enabled of this LoanPrimary.  # noqa: E501
        :rtype: bool
        """
        return self._investment_enabled

    @investment_enabled.setter
    def investment_enabled(self, investment_enabled):
        """Sets the investment_enabled of this LoanPrimary.


        :param investment_enabled: The investment_enabled of this LoanPrimary.  # noqa: E501
        :type: bool
        """

        self._investment_enabled = investment_enabled

    @property
    def invoice_collateral(self):
        """Gets the invoice_collateral of this LoanPrimary.  # noqa: E501


        :return: The invoice_collateral of this LoanPrimary.  # noqa: E501
        :rtype: Invoice
        """
        return self._invoice_collateral

    @invoice_collateral.setter
    def invoice_collateral(self, invoice_collateral):
        """Sets the invoice_collateral of this LoanPrimary.


        :param invoice_collateral: The invoice_collateral of this LoanPrimary.  # noqa: E501
        :type: Invoice
        """

        self._invoice_collateral = invoice_collateral

    @property
    def loan_rating(self):
        """Gets the loan_rating of this LoanPrimary.  # noqa: E501


        :return: The loan_rating of this LoanPrimary.  # noqa: E501
        :rtype: str
        """
        return self._loan_rating

    @loan_rating.setter
    def loan_rating(self, loan_rating):
        """Sets the loan_rating of this LoanPrimary.


        :param loan_rating: The loan_rating of this LoanPrimary.  # noqa: E501
        :type: str
        """
        allowed_values = ["NO_GUARANTEE", "BUYBACK", "PAYMENT_GUARANTEE", "BANK_GUARANTEE"]  # noqa: E501
        if loan_rating not in allowed_values:
            raise ValueError(
                "Invalid value for `loan_rating` ({0}), must be one of {1}"  # noqa: E501
                .format(loan_rating, allowed_values)
            )

        self._loan_rating = loan_rating

    @property
    def loan_type(self):
        """Gets the loan_type of this LoanPrimary.  # noqa: E501


        :return: The loan_type of this LoanPrimary.  # noqa: E501
        :rtype: int
        """
        return self._loan_type

    @loan_type.setter
    def loan_type(self, loan_type):
        """Sets the loan_type of this LoanPrimary.


        :param loan_type: The loan_type of this LoanPrimary.  # noqa: E501
        :type: int
        """

        self._loan_type = loan_type

    @property
    def loan_type_name(self):
        """Gets the loan_type_name of this LoanPrimary.  # noqa: E501


        :return: The loan_type_name of this LoanPrimary.  # noqa: E501
        :rtype: str
        """
        return self._loan_type_name

    @loan_type_name.setter
    def loan_type_name(self, loan_type_name):
        """Sets the loan_type_name of this LoanPrimary.


        :param loan_type_name: The loan_type_name of this LoanPrimary.  # noqa: E501
        :type: str
        """
        allowed_values = ["MORTGAGE", "CONSUMER", "INVOICE_FINANCING", "BUSINESS", "LINE_OF_CREDIT", "PAWNBROKING"]  # noqa: E501
        if loan_type_name not in allowed_values:
            raise ValueError(
                "Invalid value for `loan_type_name` ({0}), must be one of {1}"  # noqa: E501
                .format(loan_type_name, allowed_values)
            )

        self._loan_type_name = loan_type_name

    @property
    def loan_request_rid(self):
        """Gets the loan_request_rid of this LoanPrimary.  # noqa: E501


        :return: The loan_request_rid of this LoanPrimary.  # noqa: E501
        :rtype: int
        """
        return self._loan_request_rid

    @loan_request_rid.setter
    def loan_request_rid(self, loan_request_rid):
        """Sets the loan_request_rid of this LoanPrimary.


        :param loan_request_rid: The loan_request_rid of this LoanPrimary.  # noqa: E501
        :type: int
        """

        self._loan_request_rid = loan_request_rid

    @property
    def ltv(self):
        """Gets the ltv of this LoanPrimary.  # noqa: E501


        :return: The ltv of this LoanPrimary.  # noqa: E501
        :rtype: float
        """
        return self._ltv

    @ltv.setter
    def ltv(self, ltv):
        """Sets the ltv of this LoanPrimary.


        :param ltv: The ltv of this LoanPrimary.  # noqa: E501
        :type: float
        """

        self._ltv = ltv

    @property
    def ltv2(self):
        """Gets the ltv2 of this LoanPrimary.  # noqa: E501


        :return: The ltv2 of this LoanPrimary.  # noqa: E501
        :rtype: float
        """
        return self._ltv2

    @ltv2.setter
    def ltv2(self, ltv2):
        """Sets the ltv2 of this LoanPrimary.


        :param ltv2: The ltv2 of this LoanPrimary.  # noqa: E501
        :type: float
        """

        self._ltv2 = ltv2

    @property
    def original_start_date(self):
        """Gets the original_start_date of this LoanPrimary.  # noqa: E501


        :return: The original_start_date of this LoanPrimary.  # noqa: E501
        :rtype: datetime
        """
        return self._original_start_date

    @original_start_date.setter
    def original_start_date(self, original_start_date):
        """Sets the original_start_date of this LoanPrimary.


        :param original_start_date: The original_start_date of this LoanPrimary.  # noqa: E501
        :type: datetime
        """

        self._original_start_date = original_start_date

    @property
    def payment_guarantee(self):
        """Gets the payment_guarantee of this LoanPrimary.  # noqa: E501


        :return: The payment_guarantee of this LoanPrimary.  # noqa: E501
        :rtype: bool
        """
        return self._payment_guarantee

    @payment_guarantee.setter
    def payment_guarantee(self, payment_guarantee):
        """Sets the payment_guarantee of this LoanPrimary.


        :param payment_guarantee: The payment_guarantee of this LoanPrimary.  # noqa: E501
        :type: bool
        """

        self._payment_guarantee = payment_guarantee

    @property
    def payments_status(self):
        """Gets the payments_status of this LoanPrimary.  # noqa: E501


        :return: The payments_status of this LoanPrimary.  # noqa: E501
        :rtype: int
        """
        return self._payments_status

    @payments_status.setter
    def payments_status(self, payments_status):
        """Sets the payments_status of this LoanPrimary.


        :param payments_status: The payments_status of this LoanPrimary.  # noqa: E501
        :type: int
        """

        self._payments_status = payments_status

    @property
    def realty_collateral(self):
        """Gets the realty_collateral of this LoanPrimary.  # noqa: E501


        :return: The realty_collateral of this LoanPrimary.  # noqa: E501
        :rtype: Collateral
        """
        return self._realty_collateral

    @realty_collateral.setter
    def realty_collateral(self, realty_collateral):
        """Sets the realty_collateral of this LoanPrimary.


        :param realty_collateral: The realty_collateral of this LoanPrimary.  # noqa: E501
        :type: Collateral
        """

        self._realty_collateral = realty_collateral

    @property
    def remaing_capital_after_paid_quote(self):
        """Gets the remaing_capital_after_paid_quote of this LoanPrimary.  # noqa: E501


        :return: The remaing_capital_after_paid_quote of this LoanPrimary.  # noqa: E501
        :rtype: float
        """
        return self._remaing_capital_after_paid_quote

    @remaing_capital_after_paid_quote.setter
    def remaing_capital_after_paid_quote(self, remaing_capital_after_paid_quote):
        """Sets the remaing_capital_after_paid_quote of this LoanPrimary.


        :param remaing_capital_after_paid_quote: The remaing_capital_after_paid_quote of this LoanPrimary.  # noqa: E501
        :type: float
        """

        self._remaing_capital_after_paid_quote = remaing_capital_after_paid_quote

    @property
    def remaining_capital_for_investment(self):
        """Gets the remaining_capital_for_investment of this LoanPrimary.  # noqa: E501


        :return: The remaining_capital_for_investment of this LoanPrimary.  # noqa: E501
        :rtype: float
        """
        return self._remaining_capital_for_investment

    @remaining_capital_for_investment.setter
    def remaining_capital_for_investment(self, remaining_capital_for_investment):
        """Sets the remaining_capital_for_investment of this LoanPrimary.


        :param remaining_capital_for_investment: The remaining_capital_for_investment of this LoanPrimary.  # noqa: E501
        :type: float
        """

        self._remaining_capital_for_investment = remaining_capital_for_investment

    @property
    def remaining_loan_term(self):
        """Gets the remaining_loan_term of this LoanPrimary.  # noqa: E501


        :return: The remaining_loan_term of this LoanPrimary.  # noqa: E501
        :rtype: int
        """
        return self._remaining_loan_term

    @remaining_loan_term.setter
    def remaining_loan_term(self, remaining_loan_term):
        """Sets the remaining_loan_term of this LoanPrimary.


        :param remaining_loan_term: The remaining_loan_term of this LoanPrimary.  # noqa: E501
        :type: int
        """

        self._remaining_loan_term = remaining_loan_term

    @property
    def request_date(self):
        """Gets the request_date of this LoanPrimary.  # noqa: E501


        :return: The request_date of this LoanPrimary.  # noqa: E501
        :rtype: datetime
        """
        return self._request_date

    @request_date.setter
    def request_date(self, request_date):
        """Sets the request_date of this LoanPrimary.


        :param request_date: The request_date of this LoanPrimary.  # noqa: E501
        :type: datetime
        """

        self._request_date = request_date

    @property
    def request_term(self):
        """Gets the request_term of this LoanPrimary.  # noqa: E501


        :return: The request_term of this LoanPrimary.  # noqa: E501
        :rtype: int
        """
        return self._request_term

    @request_term.setter
    def request_term(self, request_term):
        """Sets the request_term of this LoanPrimary.


        :param request_term: The request_term of this LoanPrimary.  # noqa: E501
        :type: int
        """

        self._request_term = request_term

    @property
    def t_presta_key(self):
        """Gets the t_presta_key of this LoanPrimary.  # noqa: E501


        :return: The t_presta_key of this LoanPrimary.  # noqa: E501
        :rtype: int
        """
        return self._t_presta_key

    @t_presta_key.setter
    def t_presta_key(self, t_presta_key):
        """Sets the t_presta_key of this LoanPrimary.


        :param t_presta_key: The t_presta_key of this LoanPrimary.  # noqa: E501
        :type: int
        """

        self._t_presta_key = t_presta_key

    @property
    def total_invested(self):
        """Gets the total_invested of this LoanPrimary.  # noqa: E501


        :return: The total_invested of this LoanPrimary.  # noqa: E501
        :rtype: float
        """
        return self._total_invested

    @total_invested.setter
    def total_invested(self, total_invested):
        """Sets the total_invested of this LoanPrimary.


        :param total_invested: The total_invested of this LoanPrimary.  # noqa: E501
        :type: float
        """

        self._total_invested = total_invested

    @property
    def total_percentage_invested(self):
        """Gets the total_percentage_invested of this LoanPrimary.  # noqa: E501


        :return: The total_percentage_invested of this LoanPrimary.  # noqa: E501
        :rtype: float
        """
        return self._total_percentage_invested

    @total_percentage_invested.setter
    def total_percentage_invested(self, total_percentage_invested):
        """Sets the total_percentage_invested of this LoanPrimary.


        :param total_percentage_invested: The total_percentage_invested of this LoanPrimary.  # noqa: E501
        :type: float
        """

        self._total_percentage_invested = total_percentage_invested

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
        if issubclass(LoanPrimary, dict):
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
        if not isinstance(other, LoanPrimary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
