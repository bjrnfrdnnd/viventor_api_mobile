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


class AccountResult(object):
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
        '_date': 'datetime',
        'descr': 'str',
        'funds_in_transit': 'float',
        'funds_received_date': 'datetime',
        'id_type': 'int',
        'investor': 'int',
        'residual': 'float',
        'row_number': 'int',
        'sub_type': 'str',
        'type': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        '_date': 'date',
        'descr': 'descr',
        'funds_in_transit': 'fundsInTransit',
        'funds_received_date': 'fundsReceivedDate',
        'id_type': 'idType',
        'investor': 'investor',
        'residual': 'residual',
        'row_number': 'rowNumber',
        'sub_type': 'subType',
        'type': 'type'
    }

    def __init__(self, amount=None, _date=None, descr=None, funds_in_transit=None, funds_received_date=None, id_type=None, investor=None, residual=None, row_number=None, sub_type=None, type=None):  # noqa: E501
        """AccountResult - a model defined in Swagger"""  # noqa: E501

        self._amount = None
        self.__date = None
        self._descr = None
        self._funds_in_transit = None
        self._funds_received_date = None
        self._id_type = None
        self._investor = None
        self._residual = None
        self._row_number = None
        self._sub_type = None
        self._type = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if _date is not None:
            self._date = _date
        if descr is not None:
            self.descr = descr
        if funds_in_transit is not None:
            self.funds_in_transit = funds_in_transit
        if funds_received_date is not None:
            self.funds_received_date = funds_received_date
        if id_type is not None:
            self.id_type = id_type
        if investor is not None:
            self.investor = investor
        if residual is not None:
            self.residual = residual
        if row_number is not None:
            self.row_number = row_number
        if sub_type is not None:
            self.sub_type = sub_type
        if type is not None:
            self.type = type

    @property
    def amount(self):
        """Gets the amount of this AccountResult.  # noqa: E501


        :return: The amount of this AccountResult.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this AccountResult.


        :param amount: The amount of this AccountResult.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def _date(self):
        """Gets the _date of this AccountResult.  # noqa: E501


        :return: The _date of this AccountResult.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this AccountResult.


        :param _date: The _date of this AccountResult.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def descr(self):
        """Gets the descr of this AccountResult.  # noqa: E501


        :return: The descr of this AccountResult.  # noqa: E501
        :rtype: str
        """
        return self._descr

    @descr.setter
    def descr(self, descr):
        """Sets the descr of this AccountResult.


        :param descr: The descr of this AccountResult.  # noqa: E501
        :type: str
        """

        self._descr = descr

    @property
    def funds_in_transit(self):
        """Gets the funds_in_transit of this AccountResult.  # noqa: E501


        :return: The funds_in_transit of this AccountResult.  # noqa: E501
        :rtype: float
        """
        return self._funds_in_transit

    @funds_in_transit.setter
    def funds_in_transit(self, funds_in_transit):
        """Sets the funds_in_transit of this AccountResult.


        :param funds_in_transit: The funds_in_transit of this AccountResult.  # noqa: E501
        :type: float
        """

        self._funds_in_transit = funds_in_transit

    @property
    def funds_received_date(self):
        """Gets the funds_received_date of this AccountResult.  # noqa: E501


        :return: The funds_received_date of this AccountResult.  # noqa: E501
        :rtype: datetime
        """
        return self._funds_received_date

    @funds_received_date.setter
    def funds_received_date(self, funds_received_date):
        """Sets the funds_received_date of this AccountResult.


        :param funds_received_date: The funds_received_date of this AccountResult.  # noqa: E501
        :type: datetime
        """

        self._funds_received_date = funds_received_date

    @property
    def id_type(self):
        """Gets the id_type of this AccountResult.  # noqa: E501


        :return: The id_type of this AccountResult.  # noqa: E501
        :rtype: int
        """
        return self._id_type

    @id_type.setter
    def id_type(self, id_type):
        """Sets the id_type of this AccountResult.


        :param id_type: The id_type of this AccountResult.  # noqa: E501
        :type: int
        """

        self._id_type = id_type

    @property
    def investor(self):
        """Gets the investor of this AccountResult.  # noqa: E501


        :return: The investor of this AccountResult.  # noqa: E501
        :rtype: int
        """
        return self._investor

    @investor.setter
    def investor(self, investor):
        """Sets the investor of this AccountResult.


        :param investor: The investor of this AccountResult.  # noqa: E501
        :type: int
        """

        self._investor = investor

    @property
    def residual(self):
        """Gets the residual of this AccountResult.  # noqa: E501


        :return: The residual of this AccountResult.  # noqa: E501
        :rtype: float
        """
        return self._residual

    @residual.setter
    def residual(self, residual):
        """Sets the residual of this AccountResult.


        :param residual: The residual of this AccountResult.  # noqa: E501
        :type: float
        """

        self._residual = residual

    @property
    def row_number(self):
        """Gets the row_number of this AccountResult.  # noqa: E501


        :return: The row_number of this AccountResult.  # noqa: E501
        :rtype: int
        """
        return self._row_number

    @row_number.setter
    def row_number(self, row_number):
        """Sets the row_number of this AccountResult.


        :param row_number: The row_number of this AccountResult.  # noqa: E501
        :type: int
        """

        self._row_number = row_number

    @property
    def sub_type(self):
        """Gets the sub_type of this AccountResult.  # noqa: E501


        :return: The sub_type of this AccountResult.  # noqa: E501
        :rtype: str
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        """Sets the sub_type of this AccountResult.


        :param sub_type: The sub_type of this AccountResult.  # noqa: E501
        :type: str
        """

        self._sub_type = sub_type

    @property
    def type(self):
        """Gets the type of this AccountResult.  # noqa: E501


        :return: The type of this AccountResult.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AccountResult.


        :param type: The type of this AccountResult.  # noqa: E501
        :type: str
        """
        allowed_values = ["LISTING", "DEPOSIT", "WITHDRAWAL", "BUY_NOTE", "SELL_NOTE", "BUY_NOTE_SECONDARY_MARKET", "SELL_NOTE_SECONDARY_MARKET", "SECONDARY_MARKET_BUY_COMMISSION", "SECONDARY_MARKET_SELL_COMMISSION", "REPAYMENT_PRINCIPAL", "REPAYMENT_INTEREST", "REPAYMENT_FEE", "BUYBACK_PRINCIPAL", "BUYBACK_INTEREST", "BUYBACK_FEE", "PRINCIPAL_RECEIVED", "INTEREST_RECEIVED", "FEE_RECEIVED", "FIT_INTEREST", "CORRECTION", "RESERVED_FUNDS", "BONUS_CASHBACK", "BONUS_REFERRAL_CLIENT", "BONUS_REFERRAL_COUNTERPARTY"]  # noqa: E501
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
        if issubclass(AccountResult, dict):
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
        if not isinstance(other, AccountResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
