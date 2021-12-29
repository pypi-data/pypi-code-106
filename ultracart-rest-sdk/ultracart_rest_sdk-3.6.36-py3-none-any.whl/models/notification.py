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


class Notification(object):
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
        'can_filter_by_distribution_centers': 'bool',
        'can_include_affiliate': 'bool',
        'can_include_order': 'bool',
        'can_include_order_plain_text': 'bool',
        'distribution_center_filters': 'list[str]',
        'include_affiliate': 'bool',
        'include_order': 'bool',
        'include_order_plain_text': 'bool',
        'name': 'str',
        'notification_group': 'str',
        'selected': 'bool'
    }

    attribute_map = {
        'can_filter_by_distribution_centers': 'can_filter_by_distribution_centers',
        'can_include_affiliate': 'can_include_affiliate',
        'can_include_order': 'can_include_order',
        'can_include_order_plain_text': 'can_include_order_plain_text',
        'distribution_center_filters': 'distribution_center_filters',
        'include_affiliate': 'include_affiliate',
        'include_order': 'include_order',
        'include_order_plain_text': 'include_order_plain_text',
        'name': 'name',
        'notification_group': 'notification_group',
        'selected': 'selected'
    }

    def __init__(self, can_filter_by_distribution_centers=None, can_include_affiliate=None, can_include_order=None, can_include_order_plain_text=None, distribution_center_filters=None, include_affiliate=None, include_order=None, include_order_plain_text=None, name=None, notification_group=None, selected=None):  # noqa: E501
        """Notification - a model defined in Swagger"""  # noqa: E501

        self._can_filter_by_distribution_centers = None
        self._can_include_affiliate = None
        self._can_include_order = None
        self._can_include_order_plain_text = None
        self._distribution_center_filters = None
        self._include_affiliate = None
        self._include_order = None
        self._include_order_plain_text = None
        self._name = None
        self._notification_group = None
        self._selected = None
        self.discriminator = None

        if can_filter_by_distribution_centers is not None:
            self.can_filter_by_distribution_centers = can_filter_by_distribution_centers
        if can_include_affiliate is not None:
            self.can_include_affiliate = can_include_affiliate
        if can_include_order is not None:
            self.can_include_order = can_include_order
        if can_include_order_plain_text is not None:
            self.can_include_order_plain_text = can_include_order_plain_text
        if distribution_center_filters is not None:
            self.distribution_center_filters = distribution_center_filters
        if include_affiliate is not None:
            self.include_affiliate = include_affiliate
        if include_order is not None:
            self.include_order = include_order
        if include_order_plain_text is not None:
            self.include_order_plain_text = include_order_plain_text
        if name is not None:
            self.name = name
        if notification_group is not None:
            self.notification_group = notification_group
        if selected is not None:
            self.selected = selected

    @property
    def can_filter_by_distribution_centers(self):
        """Gets the can_filter_by_distribution_centers of this Notification.  # noqa: E501

        True if this notification can be filtered to only send for one or more distribution centers.  # noqa: E501

        :return: The can_filter_by_distribution_centers of this Notification.  # noqa: E501
        :rtype: bool
        """
        return self._can_filter_by_distribution_centers

    @can_filter_by_distribution_centers.setter
    def can_filter_by_distribution_centers(self, can_filter_by_distribution_centers):
        """Sets the can_filter_by_distribution_centers of this Notification.

        True if this notification can be filtered to only send for one or more distribution centers.  # noqa: E501

        :param can_filter_by_distribution_centers: The can_filter_by_distribution_centers of this Notification.  # noqa: E501
        :type: bool
        """

        self._can_filter_by_distribution_centers = can_filter_by_distribution_centers

    @property
    def can_include_affiliate(self):
        """Gets the can_include_affiliate of this Notification.  # noqa: E501

        True if this notification can include an affiliate information.  # noqa: E501

        :return: The can_include_affiliate of this Notification.  # noqa: E501
        :rtype: bool
        """
        return self._can_include_affiliate

    @can_include_affiliate.setter
    def can_include_affiliate(self, can_include_affiliate):
        """Sets the can_include_affiliate of this Notification.

        True if this notification can include an affiliate information.  # noqa: E501

        :param can_include_affiliate: The can_include_affiliate of this Notification.  # noqa: E501
        :type: bool
        """

        self._can_include_affiliate = can_include_affiliate

    @property
    def can_include_order(self):
        """Gets the can_include_order of this Notification.  # noqa: E501

        True if this notification can include an order attachment.  # noqa: E501

        :return: The can_include_order of this Notification.  # noqa: E501
        :rtype: bool
        """
        return self._can_include_order

    @can_include_order.setter
    def can_include_order(self, can_include_order):
        """Sets the can_include_order of this Notification.

        True if this notification can include an order attachment.  # noqa: E501

        :param can_include_order: The can_include_order of this Notification.  # noqa: E501
        :type: bool
        """

        self._can_include_order = can_include_order

    @property
    def can_include_order_plain_text(self):
        """Gets the can_include_order_plain_text of this Notification.  # noqa: E501

        True if this notification can include a plain text rendering of an order directly within an email.  Some desire this over an attachment  # noqa: E501

        :return: The can_include_order_plain_text of this Notification.  # noqa: E501
        :rtype: bool
        """
        return self._can_include_order_plain_text

    @can_include_order_plain_text.setter
    def can_include_order_plain_text(self, can_include_order_plain_text):
        """Sets the can_include_order_plain_text of this Notification.

        True if this notification can include a plain text rendering of an order directly within an email.  Some desire this over an attachment  # noqa: E501

        :param can_include_order_plain_text: The can_include_order_plain_text of this Notification.  # noqa: E501
        :type: bool
        """

        self._can_include_order_plain_text = can_include_order_plain_text

    @property
    def distribution_center_filters(self):
        """Gets the distribution_center_filters of this Notification.  # noqa: E501

        If this notification supports it, this list of distribution center CODES will filter the notification to just those distribution centers.  # noqa: E501

        :return: The distribution_center_filters of this Notification.  # noqa: E501
        :rtype: list[str]
        """
        return self._distribution_center_filters

    @distribution_center_filters.setter
    def distribution_center_filters(self, distribution_center_filters):
        """Sets the distribution_center_filters of this Notification.

        If this notification supports it, this list of distribution center CODES will filter the notification to just those distribution centers.  # noqa: E501

        :param distribution_center_filters: The distribution_center_filters of this Notification.  # noqa: E501
        :type: list[str]
        """

        self._distribution_center_filters = distribution_center_filters

    @property
    def include_affiliate(self):
        """Gets the include_affiliate of this Notification.  # noqa: E501

        If true, and this notification supports it, affiliate information will be attached to all notifications of this type  # noqa: E501

        :return: The include_affiliate of this Notification.  # noqa: E501
        :rtype: bool
        """
        return self._include_affiliate

    @include_affiliate.setter
    def include_affiliate(self, include_affiliate):
        """Sets the include_affiliate of this Notification.

        If true, and this notification supports it, affiliate information will be attached to all notifications of this type  # noqa: E501

        :param include_affiliate: The include_affiliate of this Notification.  # noqa: E501
        :type: bool
        """

        self._include_affiliate = include_affiliate

    @property
    def include_order(self):
        """Gets the include_order of this Notification.  # noqa: E501

        If true, and this notification supports it, the order will be attached to all notifications of this type  # noqa: E501

        :return: The include_order of this Notification.  # noqa: E501
        :rtype: bool
        """
        return self._include_order

    @include_order.setter
    def include_order(self, include_order):
        """Sets the include_order of this Notification.

        If true, and this notification supports it, the order will be attached to all notifications of this type  # noqa: E501

        :param include_order: The include_order of this Notification.  # noqa: E501
        :type: bool
        """

        self._include_order = include_order

    @property
    def include_order_plain_text(self):
        """Gets the include_order_plain_text of this Notification.  # noqa: E501

        If true, and this notification supports it, a plain text order will be directly inserted into all notifications of this type  # noqa: E501

        :return: The include_order_plain_text of this Notification.  # noqa: E501
        :rtype: bool
        """
        return self._include_order_plain_text

    @include_order_plain_text.setter
    def include_order_plain_text(self, include_order_plain_text):
        """Sets the include_order_plain_text of this Notification.

        If true, and this notification supports it, a plain text order will be directly inserted into all notifications of this type  # noqa: E501

        :param include_order_plain_text: The include_order_plain_text of this Notification.  # noqa: E501
        :type: bool
        """

        self._include_order_plain_text = include_order_plain_text

    @property
    def name(self):
        """Gets the name of this Notification.  # noqa: E501

        The name of this notification.  # noqa: E501

        :return: The name of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Notification.

        The name of this notification.  # noqa: E501

        :param name: The name of this Notification.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def notification_group(self):
        """Gets the notification_group of this Notification.  # noqa: E501

        A group for this notification.  This name is only used for visual grouping within interfaces.  # noqa: E501

        :return: The notification_group of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._notification_group

    @notification_group.setter
    def notification_group(self, notification_group):
        """Sets the notification_group of this Notification.

        A group for this notification.  This name is only used for visual grouping within interfaces.  # noqa: E501

        :param notification_group: The notification_group of this Notification.  # noqa: E501
        :type: str
        """

        self._notification_group = notification_group

    @property
    def selected(self):
        """Gets the selected of this Notification.  # noqa: E501

        True if this user wishes to receive this email notification.  # noqa: E501

        :return: The selected of this Notification.  # noqa: E501
        :rtype: bool
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        """Sets the selected of this Notification.

        True if this user wishes to receive this email notification.  # noqa: E501

        :param selected: The selected of this Notification.  # noqa: E501
        :type: bool
        """

        self._selected = selected

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
        if issubclass(Notification, dict):
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
        if not isinstance(other, Notification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
