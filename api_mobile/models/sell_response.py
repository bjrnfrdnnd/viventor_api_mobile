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


class SellResponse(object):
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
        'message': 'str',
        'my_investment_view': 'MyInvestmentView',
        'success': 'bool'
    }

    attribute_map = {
        'message': 'message',
        'my_investment_view': 'my_investment_view',
        'success': 'success'
    }

    def __init__(self, message=None, my_investment_view=None, success=None):  # noqa: E501
        """SellResponse - a model defined in Swagger"""  # noqa: E501

        self._message = None
        self._my_investment_view = None
        self._success = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if my_investment_view is not None:
            self.my_investment_view = my_investment_view
        if success is not None:
            self.success = success

    @property
    def message(self):
        """Gets the message of this SellResponse.  # noqa: E501


        :return: The message of this SellResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this SellResponse.


        :param message: The message of this SellResponse.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def my_investment_view(self):
        """Gets the my_investment_view of this SellResponse.  # noqa: E501


        :return: The my_investment_view of this SellResponse.  # noqa: E501
        :rtype: MyInvestmentView
        """
        return self._my_investment_view

    @my_investment_view.setter
    def my_investment_view(self, my_investment_view):
        """Sets the my_investment_view of this SellResponse.


        :param my_investment_view: The my_investment_view of this SellResponse.  # noqa: E501
        :type: MyInvestmentView
        """

        self._my_investment_view = my_investment_view

    @property
    def success(self):
        """Gets the success of this SellResponse.  # noqa: E501


        :return: The success of this SellResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this SellResponse.


        :param success: The success of this SellResponse.  # noqa: E501
        :type: bool
        """

        self._success = success

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
        if issubclass(SellResponse, dict):
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
        if not isinstance(other, SellResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other