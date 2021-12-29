# coding: utf-8

"""
    Cythereal Dashboard API

     The API used exclusively by the MAGIC Dashboard for populating charts, graphs, tables, etc... on the dashboard.  # API Conventions  **All responses** MUST be of type `APIResponse` and contain the following fields:  * `api_version` |  The current api version * `success` | Boolean value indicating if the operation succeeded. * `code` | Status code. Typically corresponds to the HTTP status code.  * `message` | A human readable message providing more details about the operation. Can be null or empty.  **Successful operations** MUST return a `SuccessResponse`, which extends `APIResponse` by adding:  * `data` | Properties containing the response object. * `success` | MUST equal True  When returning objects from a successful response, the `data` object SHOULD contain a property named after the requested object type. For example, the `/alerts` endpoint should return a response object with `data.alerts`. This property SHOULD  contain a list of the returned objects. For the `/alerts` endpoint, the `data.alerts` property contains a list of MagicAlerts objects. See the `/alerts` endpoint documentation for an example.  **Failed Operations** MUST return an `ErrorResponse`, which extends `APIResponse` by adding:  * `success` | MUST equal False.   # noqa: E501

    OpenAPI spec version: 0.41.0
    Contact: support@cythereal.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class FileBinaryDataListInner(object):
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
        'sha1': 'Sha1',
        'category': 'Category',
        'categories': 'Categories',
        'family': 'Family',
        'families': 'Families',
        'unmapped': 'Unmapped',
        'labels': 'OldCategories',
        'num_matches': 'int'
    }

    attribute_map = {
        'sha1': 'sha1',
        'category': 'category',
        'categories': 'categories',
        'family': 'family',
        'families': 'families',
        'unmapped': 'unmapped',
        'labels': 'labels',
        'num_matches': 'num_matches'
    }

    def __init__(self, sha1=None, category=None, categories=None, family=None, families=None, unmapped=None, labels=None, num_matches=None):  # noqa: E501
        """FileBinaryDataListInner - a model defined in Swagger"""  # noqa: E501

        self._sha1 = None
        self._category = None
        self._categories = None
        self._family = None
        self._families = None
        self._unmapped = None
        self._labels = None
        self._num_matches = None
        self.discriminator = None

        if sha1 is not None:
            self.sha1 = sha1
        if category is not None:
            self.category = category
        if categories is not None:
            self.categories = categories
        if family is not None:
            self.family = family
        if families is not None:
            self.families = families
        if unmapped is not None:
            self.unmapped = unmapped
        if labels is not None:
            self.labels = labels
        if num_matches is not None:
            self.num_matches = num_matches

    @property
    def sha1(self):
        """Gets the sha1 of this FileBinaryDataListInner.  # noqa: E501


        :return: The sha1 of this FileBinaryDataListInner.  # noqa: E501
        :rtype: Sha1
        """
        return self._sha1

    @sha1.setter
    def sha1(self, sha1):
        """Sets the sha1 of this FileBinaryDataListInner.


        :param sha1: The sha1 of this FileBinaryDataListInner.  # noqa: E501
        :type: Sha1
        """

        self._sha1 = sha1

    @property
    def category(self):
        """Gets the category of this FileBinaryDataListInner.  # noqa: E501


        :return: The category of this FileBinaryDataListInner.  # noqa: E501
        :rtype: Category
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this FileBinaryDataListInner.


        :param category: The category of this FileBinaryDataListInner.  # noqa: E501
        :type: Category
        """

        self._category = category

    @property
    def categories(self):
        """Gets the categories of this FileBinaryDataListInner.  # noqa: E501


        :return: The categories of this FileBinaryDataListInner.  # noqa: E501
        :rtype: Categories
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this FileBinaryDataListInner.


        :param categories: The categories of this FileBinaryDataListInner.  # noqa: E501
        :type: Categories
        """

        self._categories = categories

    @property
    def family(self):
        """Gets the family of this FileBinaryDataListInner.  # noqa: E501


        :return: The family of this FileBinaryDataListInner.  # noqa: E501
        :rtype: Family
        """
        return self._family

    @family.setter
    def family(self, family):
        """Sets the family of this FileBinaryDataListInner.


        :param family: The family of this FileBinaryDataListInner.  # noqa: E501
        :type: Family
        """

        self._family = family

    @property
    def families(self):
        """Gets the families of this FileBinaryDataListInner.  # noqa: E501


        :return: The families of this FileBinaryDataListInner.  # noqa: E501
        :rtype: Families
        """
        return self._families

    @families.setter
    def families(self, families):
        """Sets the families of this FileBinaryDataListInner.


        :param families: The families of this FileBinaryDataListInner.  # noqa: E501
        :type: Families
        """

        self._families = families

    @property
    def unmapped(self):
        """Gets the unmapped of this FileBinaryDataListInner.  # noqa: E501


        :return: The unmapped of this FileBinaryDataListInner.  # noqa: E501
        :rtype: Unmapped
        """
        return self._unmapped

    @unmapped.setter
    def unmapped(self, unmapped):
        """Sets the unmapped of this FileBinaryDataListInner.


        :param unmapped: The unmapped of this FileBinaryDataListInner.  # noqa: E501
        :type: Unmapped
        """

        self._unmapped = unmapped

    @property
    def labels(self):
        """Gets the labels of this FileBinaryDataListInner.  # noqa: E501


        :return: The labels of this FileBinaryDataListInner.  # noqa: E501
        :rtype: OldCategories
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this FileBinaryDataListInner.


        :param labels: The labels of this FileBinaryDataListInner.  # noqa: E501
        :type: OldCategories
        """

        self._labels = labels

    @property
    def num_matches(self):
        """Gets the num_matches of this FileBinaryDataListInner.  # noqa: E501

        The number of similar files to this one.  # noqa: E501

        :return: The num_matches of this FileBinaryDataListInner.  # noqa: E501
        :rtype: int
        """
        return self._num_matches

    @num_matches.setter
    def num_matches(self, num_matches):
        """Sets the num_matches of this FileBinaryDataListInner.

        The number of similar files to this one.  # noqa: E501

        :param num_matches: The num_matches of this FileBinaryDataListInner.  # noqa: E501
        :type: int
        """

        self._num_matches = num_matches

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
        if issubclass(FileBinaryDataListInner, dict):
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
        if not isinstance(other, FileBinaryDataListInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
