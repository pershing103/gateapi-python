# coding: utf-8

"""
    Gate API v4

    APIv4 provides spot, margin and futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    OpenAPI spec version: 4.7.3
    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class FuturesOrderBook(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'asks': 'list[FuturesOrderBookItem]',
        'bids': 'list[FuturesOrderBookItem]'
    }

    attribute_map = {
        'asks': 'asks',
        'bids': 'bids'
    }

    def __init__(self, asks=None, bids=None):  # noqa: E501
        """FuturesOrderBook - a model defined in OpenAPI"""  # noqa: E501

        self._asks = None
        self._bids = None
        self.discriminator = None

        self.asks = asks
        self.bids = bids

    @property
    def asks(self):
        """Gets the asks of this FuturesOrderBook.  # noqa: E501

        Asks order depth  # noqa: E501

        :return: The asks of this FuturesOrderBook.  # noqa: E501
        :rtype: list[FuturesOrderBookItem]
        """
        return self._asks

    @asks.setter
    def asks(self, asks):
        """Sets the asks of this FuturesOrderBook.

        Asks order depth  # noqa: E501

        :param asks: The asks of this FuturesOrderBook.  # noqa: E501
        :type: list[FuturesOrderBookItem]
        """
        if asks is None:
            raise ValueError("Invalid value for `asks`, must not be `None`")  # noqa: E501

        self._asks = asks

    @property
    def bids(self):
        """Gets the bids of this FuturesOrderBook.  # noqa: E501

        Bids order depth  # noqa: E501

        :return: The bids of this FuturesOrderBook.  # noqa: E501
        :rtype: list[FuturesOrderBookItem]
        """
        return self._bids

    @bids.setter
    def bids(self, bids):
        """Sets the bids of this FuturesOrderBook.

        Bids order depth  # noqa: E501

        :param bids: The bids of this FuturesOrderBook.  # noqa: E501
        :type: list[FuturesOrderBookItem]
        """
        if bids is None:
            raise ValueError("Invalid value for `bids`, must not be `None`")  # noqa: E501

        self._bids = bids

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FuturesOrderBook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
