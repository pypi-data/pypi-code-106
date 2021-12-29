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


class EmailDomain(object):
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
        'comment': 'str',
        'dkim': 'list[VerificationRecord]',
        'dkim_status': 'str',
        'domain': 'str',
        'esp_domain_uuid': 'str',
        'identity_status': 'str',
        'merchant_id': 'str',
        'provider': 'str',
        'start_dkim_dts': 'str',
        'start_identity_dts': 'str',
        'verification': 'VerificationRecord'
    }

    attribute_map = {
        'comment': 'comment',
        'dkim': 'dkim',
        'dkim_status': 'dkim_status',
        'domain': 'domain',
        'esp_domain_uuid': 'esp_domain_uuid',
        'identity_status': 'identity_status',
        'merchant_id': 'merchant_id',
        'provider': 'provider',
        'start_dkim_dts': 'start_dkim_dts',
        'start_identity_dts': 'start_identity_dts',
        'verification': 'verification'
    }

    def __init__(self, comment=None, dkim=None, dkim_status=None, domain=None, esp_domain_uuid=None, identity_status=None, merchant_id=None, provider=None, start_dkim_dts=None, start_identity_dts=None, verification=None):  # noqa: E501
        """EmailDomain - a model defined in Swagger"""  # noqa: E501

        self._comment = None
        self._dkim = None
        self._dkim_status = None
        self._domain = None
        self._esp_domain_uuid = None
        self._identity_status = None
        self._merchant_id = None
        self._provider = None
        self._start_dkim_dts = None
        self._start_identity_dts = None
        self._verification = None
        self.discriminator = None

        if comment is not None:
            self.comment = comment
        if dkim is not None:
            self.dkim = dkim
        if dkim_status is not None:
            self.dkim_status = dkim_status
        if domain is not None:
            self.domain = domain
        if esp_domain_uuid is not None:
            self.esp_domain_uuid = esp_domain_uuid
        if identity_status is not None:
            self.identity_status = identity_status
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if provider is not None:
            self.provider = provider
        if start_dkim_dts is not None:
            self.start_dkim_dts = start_dkim_dts
        if start_identity_dts is not None:
            self.start_identity_dts = start_identity_dts
        if verification is not None:
            self.verification = verification

    @property
    def comment(self):
        """Gets the comment of this EmailDomain.  # noqa: E501


        :return: The comment of this EmailDomain.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this EmailDomain.


        :param comment: The comment of this EmailDomain.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def dkim(self):
        """Gets the dkim of this EmailDomain.  # noqa: E501


        :return: The dkim of this EmailDomain.  # noqa: E501
        :rtype: list[VerificationRecord]
        """
        return self._dkim

    @dkim.setter
    def dkim(self, dkim):
        """Sets the dkim of this EmailDomain.


        :param dkim: The dkim of this EmailDomain.  # noqa: E501
        :type: list[VerificationRecord]
        """

        self._dkim = dkim

    @property
    def dkim_status(self):
        """Gets the dkim_status of this EmailDomain.  # noqa: E501


        :return: The dkim_status of this EmailDomain.  # noqa: E501
        :rtype: str
        """
        return self._dkim_status

    @dkim_status.setter
    def dkim_status(self, dkim_status):
        """Sets the dkim_status of this EmailDomain.


        :param dkim_status: The dkim_status of this EmailDomain.  # noqa: E501
        :type: str
        """

        self._dkim_status = dkim_status

    @property
    def domain(self):
        """Gets the domain of this EmailDomain.  # noqa: E501


        :return: The domain of this EmailDomain.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this EmailDomain.


        :param domain: The domain of this EmailDomain.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def esp_domain_uuid(self):
        """Gets the esp_domain_uuid of this EmailDomain.  # noqa: E501


        :return: The esp_domain_uuid of this EmailDomain.  # noqa: E501
        :rtype: str
        """
        return self._esp_domain_uuid

    @esp_domain_uuid.setter
    def esp_domain_uuid(self, esp_domain_uuid):
        """Sets the esp_domain_uuid of this EmailDomain.


        :param esp_domain_uuid: The esp_domain_uuid of this EmailDomain.  # noqa: E501
        :type: str
        """

        self._esp_domain_uuid = esp_domain_uuid

    @property
    def identity_status(self):
        """Gets the identity_status of this EmailDomain.  # noqa: E501


        :return: The identity_status of this EmailDomain.  # noqa: E501
        :rtype: str
        """
        return self._identity_status

    @identity_status.setter
    def identity_status(self, identity_status):
        """Sets the identity_status of this EmailDomain.


        :param identity_status: The identity_status of this EmailDomain.  # noqa: E501
        :type: str
        """

        self._identity_status = identity_status

    @property
    def merchant_id(self):
        """Gets the merchant_id of this EmailDomain.  # noqa: E501


        :return: The merchant_id of this EmailDomain.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this EmailDomain.


        :param merchant_id: The merchant_id of this EmailDomain.  # noqa: E501
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def provider(self):
        """Gets the provider of this EmailDomain.  # noqa: E501


        :return: The provider of this EmailDomain.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this EmailDomain.


        :param provider: The provider of this EmailDomain.  # noqa: E501
        :type: str
        """

        self._provider = provider

    @property
    def start_dkim_dts(self):
        """Gets the start_dkim_dts of this EmailDomain.  # noqa: E501


        :return: The start_dkim_dts of this EmailDomain.  # noqa: E501
        :rtype: str
        """
        return self._start_dkim_dts

    @start_dkim_dts.setter
    def start_dkim_dts(self, start_dkim_dts):
        """Sets the start_dkim_dts of this EmailDomain.


        :param start_dkim_dts: The start_dkim_dts of this EmailDomain.  # noqa: E501
        :type: str
        """

        self._start_dkim_dts = start_dkim_dts

    @property
    def start_identity_dts(self):
        """Gets the start_identity_dts of this EmailDomain.  # noqa: E501


        :return: The start_identity_dts of this EmailDomain.  # noqa: E501
        :rtype: str
        """
        return self._start_identity_dts

    @start_identity_dts.setter
    def start_identity_dts(self, start_identity_dts):
        """Sets the start_identity_dts of this EmailDomain.


        :param start_identity_dts: The start_identity_dts of this EmailDomain.  # noqa: E501
        :type: str
        """

        self._start_identity_dts = start_identity_dts

    @property
    def verification(self):
        """Gets the verification of this EmailDomain.  # noqa: E501


        :return: The verification of this EmailDomain.  # noqa: E501
        :rtype: VerificationRecord
        """
        return self._verification

    @verification.setter
    def verification(self, verification):
        """Sets the verification of this EmailDomain.


        :param verification: The verification of this EmailDomain.  # noqa: E501
        :type: VerificationRecord
        """

        self._verification = verification

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
        if issubclass(EmailDomain, dict):
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
        if not isinstance(other, EmailDomain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
