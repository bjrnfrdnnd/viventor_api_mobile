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


class ErrorBody(object):
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
        'code': 'int',
        'message': 'str',
        'property_path': 'str'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'property_path': 'property_path'
    }

    def __init__(self, code=None, message=None, property_path=None):  # noqa: E501
        """ErrorBody - a model defined in Swagger"""  # noqa: E501

        self._code = None
        self._message = None
        self._property_path = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if property_path is not None:
            self.property_path = property_path

    @property
    def code(self):
        """Gets the code of this ErrorBody.  # noqa: E501


        :return: The code of this ErrorBody.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ErrorBody.


        :param code: The code of this ErrorBody.  # noqa: E501
        :type: int
        """

        self._code = code

    @property
    def message(self):
        """Gets the message of this ErrorBody.  # noqa: E501


        :return: The message of this ErrorBody.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ErrorBody.


        :param message: The message of this ErrorBody.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def property_path(self):
        """Gets the property_path of this ErrorBody.  # noqa: E501


        :return: The property_path of this ErrorBody.  # noqa: E501
        :rtype: str
        """
        return self._property_path

    @property_path.setter
    def property_path(self, property_path):
        """Sets the property_path of this ErrorBody.


        :param property_path: The property_path of this ErrorBody.  # noqa: E501
        :type: str
        """

        self._property_path = property_path

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
        if issubclass(ErrorBody, dict):
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
        if not isinstance(other, ErrorBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other