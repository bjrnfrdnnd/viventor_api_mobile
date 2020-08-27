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


class CommonOperationResponse(object):
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
        'funds_available': 'float',
        'message': 'str',
        'success': 'bool',
        'token_expire_timestamp': 'int',
        'token_lifetime': 'int',
        'upload_token': 'str'
    }

    attribute_map = {
        'code': 'code',
        'funds_available': 'funds_available',
        'message': 'message',
        'success': 'success',
        'token_expire_timestamp': 'token_expire_timestamp',
        'token_lifetime': 'token_lifetime',
        'upload_token': 'upload_token'
    }

    def __init__(self, code=None, funds_available=None, message=None, success=None, token_expire_timestamp=None, token_lifetime=None, upload_token=None):  # noqa: E501
        """CommonOperationResponse - a model defined in Swagger"""  # noqa: E501

        self._code = None
        self._funds_available = None
        self._message = None
        self._success = None
        self._token_expire_timestamp = None
        self._token_lifetime = None
        self._upload_token = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if funds_available is not None:
            self.funds_available = funds_available
        if message is not None:
            self.message = message
        if success is not None:
            self.success = success
        if token_expire_timestamp is not None:
            self.token_expire_timestamp = token_expire_timestamp
        if token_lifetime is not None:
            self.token_lifetime = token_lifetime
        if upload_token is not None:
            self.upload_token = upload_token

    @property
    def code(self):
        """Gets the code of this CommonOperationResponse.  # noqa: E501


        :return: The code of this CommonOperationResponse.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CommonOperationResponse.


        :param code: The code of this CommonOperationResponse.  # noqa: E501
        :type: int
        """

        self._code = code

    @property
    def funds_available(self):
        """Gets the funds_available of this CommonOperationResponse.  # noqa: E501


        :return: The funds_available of this CommonOperationResponse.  # noqa: E501
        :rtype: float
        """
        return self._funds_available

    @funds_available.setter
    def funds_available(self, funds_available):
        """Sets the funds_available of this CommonOperationResponse.


        :param funds_available: The funds_available of this CommonOperationResponse.  # noqa: E501
        :type: float
        """

        self._funds_available = funds_available

    @property
    def message(self):
        """Gets the message of this CommonOperationResponse.  # noqa: E501


        :return: The message of this CommonOperationResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CommonOperationResponse.


        :param message: The message of this CommonOperationResponse.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def success(self):
        """Gets the success of this CommonOperationResponse.  # noqa: E501


        :return: The success of this CommonOperationResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this CommonOperationResponse.


        :param success: The success of this CommonOperationResponse.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def token_expire_timestamp(self):
        """Gets the token_expire_timestamp of this CommonOperationResponse.  # noqa: E501


        :return: The token_expire_timestamp of this CommonOperationResponse.  # noqa: E501
        :rtype: int
        """
        return self._token_expire_timestamp

    @token_expire_timestamp.setter
    def token_expire_timestamp(self, token_expire_timestamp):
        """Sets the token_expire_timestamp of this CommonOperationResponse.


        :param token_expire_timestamp: The token_expire_timestamp of this CommonOperationResponse.  # noqa: E501
        :type: int
        """

        self._token_expire_timestamp = token_expire_timestamp

    @property
    def token_lifetime(self):
        """Gets the token_lifetime of this CommonOperationResponse.  # noqa: E501


        :return: The token_lifetime of this CommonOperationResponse.  # noqa: E501
        :rtype: int
        """
        return self._token_lifetime

    @token_lifetime.setter
    def token_lifetime(self, token_lifetime):
        """Sets the token_lifetime of this CommonOperationResponse.


        :param token_lifetime: The token_lifetime of this CommonOperationResponse.  # noqa: E501
        :type: int
        """

        self._token_lifetime = token_lifetime

    @property
    def upload_token(self):
        """Gets the upload_token of this CommonOperationResponse.  # noqa: E501


        :return: The upload_token of this CommonOperationResponse.  # noqa: E501
        :rtype: str
        """
        return self._upload_token

    @upload_token.setter
    def upload_token(self, upload_token):
        """Sets the upload_token of this CommonOperationResponse.


        :param upload_token: The upload_token of this CommonOperationResponse.  # noqa: E501
        :type: str
        """

        self._upload_token = upload_token

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
        if issubclass(CommonOperationResponse, dict):
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
        if not isinstance(other, CommonOperationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
