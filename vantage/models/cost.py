# coding: utf-8

"""
    Vantage

    Vantage API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@vantage.sh
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from vantage.configuration import Configuration


class Cost(object):
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
        'accrued_at': 'str',
        'amount': 'str',
        'provider': 'str',
        'service': 'str'
    }

    attribute_map = {
        'accrued_at': 'accrued_at',
        'amount': 'amount',
        'provider': 'provider',
        'service': 'service'
    }

    def __init__(self, accrued_at=None, amount=None, provider=None, service=None, _configuration=None):  # noqa: E501
        """Cost - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._accrued_at = None
        self._amount = None
        self._provider = None
        self._service = None
        self.discriminator = None

        if accrued_at is not None:
            self.accrued_at = accrued_at
        if amount is not None:
            self.amount = amount
        if provider is not None:
            self.provider = provider
        if service is not None:
            self.service = service

    @property
    def accrued_at(self):
        """Gets the accrued_at of this Cost.  # noqa: E501

        The date the cost was accrued. ISO 8601 Formatted - 2021-07-15 or 2021-07-15T19:20:48+00:00.  # noqa: E501

        :return: The accrued_at of this Cost.  # noqa: E501
        :rtype: str
        """
        return self._accrued_at

    @accrued_at.setter
    def accrued_at(self, accrued_at):
        """Sets the accrued_at of this Cost.

        The date the cost was accrued. ISO 8601 Formatted - 2021-07-15 or 2021-07-15T19:20:48+00:00.  # noqa: E501

        :param accrued_at: The accrued_at of this Cost.  # noqa: E501
        :type: str
        """

        self._accrued_at = accrued_at

    @property
    def amount(self):
        """Gets the amount of this Cost.  # noqa: E501

        The amount of the cost.  # noqa: E501

        :return: The amount of this Cost.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Cost.

        The amount of the cost.  # noqa: E501

        :param amount: The amount of this Cost.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def provider(self):
        """Gets the provider of this Cost.  # noqa: E501

        The service provider where the cost was incurred. e.g. AWS  # noqa: E501

        :return: The provider of this Cost.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this Cost.

        The service provider where the cost was incurred. e.g. AWS  # noqa: E501

        :param provider: The provider of this Cost.  # noqa: E501
        :type: str
        """

        self._provider = provider

    @property
    def service(self):
        """Gets the service of this Cost.  # noqa: E501

        The service which incurred the cost. e.g. Amazon ElastiCache  # noqa: E501

        :return: The service of this Cost.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this Cost.

        The service which incurred the cost. e.g. Amazon ElastiCache  # noqa: E501

        :param service: The service of this Cost.  # noqa: E501
        :type: str
        """

        self._service = service

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
        if issubclass(Cost, dict):
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
        if not isinstance(other, Cost):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Cost):
            return True

        return self.to_dict() != other.to_dict()
