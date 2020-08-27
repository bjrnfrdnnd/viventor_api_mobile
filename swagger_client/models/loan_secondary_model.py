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


class LoanSecondaryModel(object):
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
        'available': 'float',
        'bank_guarantee': 'bool',
        'buyback': 'bool',
        'country_code': 'str',
        'discount': 'float',
        'due_date': 'date',
        'id': 'int',
        'interest_rate': 'float',
        'listing_date': 'date',
        'ltv': 'float',
        'note_id': 'int',
        'originator': 'str',
        'payment_guarantee': 'bool',
        'premium': 'float',
        'price': 'float',
        'remaining_term': 'int',
        'request_term': 'int'
    }

    attribute_map = {
        'available': 'available',
        'bank_guarantee': 'bank_guarantee',
        'buyback': 'buyback',
        'country_code': 'country_code',
        'discount': 'discount',
        'due_date': 'due_date',
        'id': 'id',
        'interest_rate': 'interest_rate',
        'listing_date': 'listing_date',
        'ltv': 'ltv',
        'note_id': 'note_id',
        'originator': 'originator',
        'payment_guarantee': 'payment_guarantee',
        'premium': 'premium',
        'price': 'price',
        'remaining_term': 'remaining_term',
        'request_term': 'request_term'
    }

    def __init__(self, available=None, bank_guarantee=None, buyback=None, country_code=None, discount=None, due_date=None, id=None, interest_rate=None, listing_date=None, ltv=None, note_id=None, originator=None, payment_guarantee=None, premium=None, price=None, remaining_term=None, request_term=None):  # noqa: E501
        """LoanSecondaryModel - a model defined in Swagger"""  # noqa: E501

        self._available = None
        self._bank_guarantee = None
        self._buyback = None
        self._country_code = None
        self._discount = None
        self._due_date = None
        self._id = None
        self._interest_rate = None
        self._listing_date = None
        self._ltv = None
        self._note_id = None
        self._originator = None
        self._payment_guarantee = None
        self._premium = None
        self._price = None
        self._remaining_term = None
        self._request_term = None
        self.discriminator = None

        if available is not None:
            self.available = available
        if bank_guarantee is not None:
            self.bank_guarantee = bank_guarantee
        if buyback is not None:
            self.buyback = buyback
        if country_code is not None:
            self.country_code = country_code
        if discount is not None:
            self.discount = discount
        if due_date is not None:
            self.due_date = due_date
        if id is not None:
            self.id = id
        if interest_rate is not None:
            self.interest_rate = interest_rate
        if listing_date is not None:
            self.listing_date = listing_date
        if ltv is not None:
            self.ltv = ltv
        if note_id is not None:
            self.note_id = note_id
        if originator is not None:
            self.originator = originator
        if payment_guarantee is not None:
            self.payment_guarantee = payment_guarantee
        if premium is not None:
            self.premium = premium
        if price is not None:
            self.price = price
        if remaining_term is not None:
            self.remaining_term = remaining_term
        if request_term is not None:
            self.request_term = request_term

    @property
    def available(self):
        """Gets the available of this LoanSecondaryModel.  # noqa: E501


        :return: The available of this LoanSecondaryModel.  # noqa: E501
        :rtype: float
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this LoanSecondaryModel.


        :param available: The available of this LoanSecondaryModel.  # noqa: E501
        :type: float
        """

        self._available = available

    @property
    def bank_guarantee(self):
        """Gets the bank_guarantee of this LoanSecondaryModel.  # noqa: E501


        :return: The bank_guarantee of this LoanSecondaryModel.  # noqa: E501
        :rtype: bool
        """
        return self._bank_guarantee

    @bank_guarantee.setter
    def bank_guarantee(self, bank_guarantee):
        """Sets the bank_guarantee of this LoanSecondaryModel.


        :param bank_guarantee: The bank_guarantee of this LoanSecondaryModel.  # noqa: E501
        :type: bool
        """

        self._bank_guarantee = bank_guarantee

    @property
    def buyback(self):
        """Gets the buyback of this LoanSecondaryModel.  # noqa: E501


        :return: The buyback of this LoanSecondaryModel.  # noqa: E501
        :rtype: bool
        """
        return self._buyback

    @buyback.setter
    def buyback(self, buyback):
        """Sets the buyback of this LoanSecondaryModel.


        :param buyback: The buyback of this LoanSecondaryModel.  # noqa: E501
        :type: bool
        """

        self._buyback = buyback

    @property
    def country_code(self):
        """Gets the country_code of this LoanSecondaryModel.  # noqa: E501


        :return: The country_code of this LoanSecondaryModel.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this LoanSecondaryModel.


        :param country_code: The country_code of this LoanSecondaryModel.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def discount(self):
        """Gets the discount of this LoanSecondaryModel.  # noqa: E501


        :return: The discount of this LoanSecondaryModel.  # noqa: E501
        :rtype: float
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """Sets the discount of this LoanSecondaryModel.


        :param discount: The discount of this LoanSecondaryModel.  # noqa: E501
        :type: float
        """

        self._discount = discount

    @property
    def due_date(self):
        """Gets the due_date of this LoanSecondaryModel.  # noqa: E501


        :return: The due_date of this LoanSecondaryModel.  # noqa: E501
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this LoanSecondaryModel.


        :param due_date: The due_date of this LoanSecondaryModel.  # noqa: E501
        :type: date
        """

        self._due_date = due_date

    @property
    def id(self):
        """Gets the id of this LoanSecondaryModel.  # noqa: E501


        :return: The id of this LoanSecondaryModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LoanSecondaryModel.


        :param id: The id of this LoanSecondaryModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def interest_rate(self):
        """Gets the interest_rate of this LoanSecondaryModel.  # noqa: E501


        :return: The interest_rate of this LoanSecondaryModel.  # noqa: E501
        :rtype: float
        """
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, interest_rate):
        """Sets the interest_rate of this LoanSecondaryModel.


        :param interest_rate: The interest_rate of this LoanSecondaryModel.  # noqa: E501
        :type: float
        """

        self._interest_rate = interest_rate

    @property
    def listing_date(self):
        """Gets the listing_date of this LoanSecondaryModel.  # noqa: E501


        :return: The listing_date of this LoanSecondaryModel.  # noqa: E501
        :rtype: date
        """
        return self._listing_date

    @listing_date.setter
    def listing_date(self, listing_date):
        """Sets the listing_date of this LoanSecondaryModel.


        :param listing_date: The listing_date of this LoanSecondaryModel.  # noqa: E501
        :type: date
        """

        self._listing_date = listing_date

    @property
    def ltv(self):
        """Gets the ltv of this LoanSecondaryModel.  # noqa: E501


        :return: The ltv of this LoanSecondaryModel.  # noqa: E501
        :rtype: float
        """
        return self._ltv

    @ltv.setter
    def ltv(self, ltv):
        """Sets the ltv of this LoanSecondaryModel.


        :param ltv: The ltv of this LoanSecondaryModel.  # noqa: E501
        :type: float
        """

        self._ltv = ltv

    @property
    def note_id(self):
        """Gets the note_id of this LoanSecondaryModel.  # noqa: E501


        :return: The note_id of this LoanSecondaryModel.  # noqa: E501
        :rtype: int
        """
        return self._note_id

    @note_id.setter
    def note_id(self, note_id):
        """Sets the note_id of this LoanSecondaryModel.


        :param note_id: The note_id of this LoanSecondaryModel.  # noqa: E501
        :type: int
        """

        self._note_id = note_id

    @property
    def originator(self):
        """Gets the originator of this LoanSecondaryModel.  # noqa: E501


        :return: The originator of this LoanSecondaryModel.  # noqa: E501
        :rtype: str
        """
        return self._originator

    @originator.setter
    def originator(self, originator):
        """Sets the originator of this LoanSecondaryModel.


        :param originator: The originator of this LoanSecondaryModel.  # noqa: E501
        :type: str
        """

        self._originator = originator

    @property
    def payment_guarantee(self):
        """Gets the payment_guarantee of this LoanSecondaryModel.  # noqa: E501


        :return: The payment_guarantee of this LoanSecondaryModel.  # noqa: E501
        :rtype: bool
        """
        return self._payment_guarantee

    @payment_guarantee.setter
    def payment_guarantee(self, payment_guarantee):
        """Sets the payment_guarantee of this LoanSecondaryModel.


        :param payment_guarantee: The payment_guarantee of this LoanSecondaryModel.  # noqa: E501
        :type: bool
        """

        self._payment_guarantee = payment_guarantee

    @property
    def premium(self):
        """Gets the premium of this LoanSecondaryModel.  # noqa: E501


        :return: The premium of this LoanSecondaryModel.  # noqa: E501
        :rtype: float
        """
        return self._premium

    @premium.setter
    def premium(self, premium):
        """Sets the premium of this LoanSecondaryModel.


        :param premium: The premium of this LoanSecondaryModel.  # noqa: E501
        :type: float
        """

        self._premium = premium

    @property
    def price(self):
        """Gets the price of this LoanSecondaryModel.  # noqa: E501


        :return: The price of this LoanSecondaryModel.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this LoanSecondaryModel.


        :param price: The price of this LoanSecondaryModel.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def remaining_term(self):
        """Gets the remaining_term of this LoanSecondaryModel.  # noqa: E501


        :return: The remaining_term of this LoanSecondaryModel.  # noqa: E501
        :rtype: int
        """
        return self._remaining_term

    @remaining_term.setter
    def remaining_term(self, remaining_term):
        """Sets the remaining_term of this LoanSecondaryModel.


        :param remaining_term: The remaining_term of this LoanSecondaryModel.  # noqa: E501
        :type: int
        """

        self._remaining_term = remaining_term

    @property
    def request_term(self):
        """Gets the request_term of this LoanSecondaryModel.  # noqa: E501


        :return: The request_term of this LoanSecondaryModel.  # noqa: E501
        :rtype: int
        """
        return self._request_term

    @request_term.setter
    def request_term(self, request_term):
        """Sets the request_term of this LoanSecondaryModel.


        :param request_term: The request_term of this LoanSecondaryModel.  # noqa: E501
        :type: int
        """

        self._request_term = request_term

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
        if issubclass(LoanSecondaryModel, dict):
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
        if not isinstance(other, LoanSecondaryModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other