# coding: utf-8

"""
    UltraCart Rest API V2

    UltraCart REST API Version 2  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CartSettingsPaymentPayPal(object):
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
        'paypal_button_alt_text': 'str',
        'paypal_button_url': 'str',
        'paypal_credit_button_url': 'str',
        'paypal_credit_legal_image_url': 'str',
        'paypal_credit_legal_url': 'str'
    }

    attribute_map = {
        'paypal_button_alt_text': 'paypal_button_alt_text',
        'paypal_button_url': 'paypal_button_url',
        'paypal_credit_button_url': 'paypal_credit_button_url',
        'paypal_credit_legal_image_url': 'paypal_credit_legal_image_url',
        'paypal_credit_legal_url': 'paypal_credit_legal_url'
    }

    def __init__(self, paypal_button_alt_text=None, paypal_button_url=None, paypal_credit_button_url=None, paypal_credit_legal_image_url=None, paypal_credit_legal_url=None):  # noqa: E501
        """CartSettingsPaymentPayPal - a model defined in Swagger"""  # noqa: E501

        self._paypal_button_alt_text = None
        self._paypal_button_url = None
        self._paypal_credit_button_url = None
        self._paypal_credit_legal_image_url = None
        self._paypal_credit_legal_url = None
        self.discriminator = None

        if paypal_button_alt_text is not None:
            self.paypal_button_alt_text = paypal_button_alt_text
        if paypal_button_url is not None:
            self.paypal_button_url = paypal_button_url
        if paypal_credit_button_url is not None:
            self.paypal_credit_button_url = paypal_credit_button_url
        if paypal_credit_legal_image_url is not None:
            self.paypal_credit_legal_image_url = paypal_credit_legal_image_url
        if paypal_credit_legal_url is not None:
            self.paypal_credit_legal_url = paypal_credit_legal_url

    @property
    def paypal_button_alt_text(self):
        """Gets the paypal_button_alt_text of this CartSettingsPaymentPayPal.  # noqa: E501

        PayPal button alt text  # noqa: E501

        :return: The paypal_button_alt_text of this CartSettingsPaymentPayPal.  # noqa: E501
        :rtype: str
        """
        return self._paypal_button_alt_text

    @paypal_button_alt_text.setter
    def paypal_button_alt_text(self, paypal_button_alt_text):
        """Sets the paypal_button_alt_text of this CartSettingsPaymentPayPal.

        PayPal button alt text  # noqa: E501

        :param paypal_button_alt_text: The paypal_button_alt_text of this CartSettingsPaymentPayPal.  # noqa: E501
        :type: str
        """

        self._paypal_button_alt_text = paypal_button_alt_text

    @property
    def paypal_button_url(self):
        """Gets the paypal_button_url of this CartSettingsPaymentPayPal.  # noqa: E501

        PayPal button URL  # noqa: E501

        :return: The paypal_button_url of this CartSettingsPaymentPayPal.  # noqa: E501
        :rtype: str
        """
        return self._paypal_button_url

    @paypal_button_url.setter
    def paypal_button_url(self, paypal_button_url):
        """Sets the paypal_button_url of this CartSettingsPaymentPayPal.

        PayPal button URL  # noqa: E501

        :param paypal_button_url: The paypal_button_url of this CartSettingsPaymentPayPal.  # noqa: E501
        :type: str
        """

        self._paypal_button_url = paypal_button_url

    @property
    def paypal_credit_button_url(self):
        """Gets the paypal_credit_button_url of this CartSettingsPaymentPayPal.  # noqa: E501

        PayPal Credit button URL  # noqa: E501

        :return: The paypal_credit_button_url of this CartSettingsPaymentPayPal.  # noqa: E501
        :rtype: str
        """
        return self._paypal_credit_button_url

    @paypal_credit_button_url.setter
    def paypal_credit_button_url(self, paypal_credit_button_url):
        """Sets the paypal_credit_button_url of this CartSettingsPaymentPayPal.

        PayPal Credit button URL  # noqa: E501

        :param paypal_credit_button_url: The paypal_credit_button_url of this CartSettingsPaymentPayPal.  # noqa: E501
        :type: str
        """

        self._paypal_credit_button_url = paypal_credit_button_url

    @property
    def paypal_credit_legal_image_url(self):
        """Gets the paypal_credit_legal_image_url of this CartSettingsPaymentPayPal.  # noqa: E501

        PayPal Credit legal image URL  # noqa: E501

        :return: The paypal_credit_legal_image_url of this CartSettingsPaymentPayPal.  # noqa: E501
        :rtype: str
        """
        return self._paypal_credit_legal_image_url

    @paypal_credit_legal_image_url.setter
    def paypal_credit_legal_image_url(self, paypal_credit_legal_image_url):
        """Sets the paypal_credit_legal_image_url of this CartSettingsPaymentPayPal.

        PayPal Credit legal image URL  # noqa: E501

        :param paypal_credit_legal_image_url: The paypal_credit_legal_image_url of this CartSettingsPaymentPayPal.  # noqa: E501
        :type: str
        """

        self._paypal_credit_legal_image_url = paypal_credit_legal_image_url

    @property
    def paypal_credit_legal_url(self):
        """Gets the paypal_credit_legal_url of this CartSettingsPaymentPayPal.  # noqa: E501

        PayPal Credit legal URL  # noqa: E501

        :return: The paypal_credit_legal_url of this CartSettingsPaymentPayPal.  # noqa: E501
        :rtype: str
        """
        return self._paypal_credit_legal_url

    @paypal_credit_legal_url.setter
    def paypal_credit_legal_url(self, paypal_credit_legal_url):
        """Sets the paypal_credit_legal_url of this CartSettingsPaymentPayPal.

        PayPal Credit legal URL  # noqa: E501

        :param paypal_credit_legal_url: The paypal_credit_legal_url of this CartSettingsPaymentPayPal.  # noqa: E501
        :type: str
        """

        self._paypal_credit_legal_url = paypal_credit_legal_url

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
        if issubclass(CartSettingsPaymentPayPal, dict):
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
        if not isinstance(other, CartSettingsPaymentPayPal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
