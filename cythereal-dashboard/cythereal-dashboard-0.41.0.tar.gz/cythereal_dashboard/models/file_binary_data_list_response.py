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


class FileBinaryDataListResponse(object):
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
        'api_version': 'str',
        'success': 'bool',
        'code': 'object',
        'message': 'str',
        'data': 'FileBinaryDataList'
    }

    attribute_map = {
        'api_version': 'api_version',
        'success': 'success',
        'code': 'code',
        'message': 'message',
        'data': 'data'
    }

    def __init__(self, api_version=None, success=None, code=None, message=None, data=None):  # noqa: E501
        """FileBinaryDataListResponse - a model defined in Swagger"""  # noqa: E501

        self._api_version = None
        self._success = None
        self._code = None
        self._message = None
        self._data = None
        self.discriminator = None

        self.api_version = api_version
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    @property
    def api_version(self):
        """Gets the api_version of this FileBinaryDataListResponse.  # noqa: E501

        The current api version.  # noqa: E501

        :return: The api_version of this FileBinaryDataListResponse.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this FileBinaryDataListResponse.

        The current api version.  # noqa: E501

        :param api_version: The api_version of this FileBinaryDataListResponse.  # noqa: E501
        :type: str
        """
        if api_version is None:
            raise ValueError("Invalid value for `api_version`, must not be `None`")  # noqa: E501

        self._api_version = api_version

    @property
    def success(self):
        """Gets the success of this FileBinaryDataListResponse.  # noqa: E501

        MUST equal true.  # noqa: E501

        :return: The success of this FileBinaryDataListResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this FileBinaryDataListResponse.

        MUST equal true.  # noqa: E501

        :param success: The success of this FileBinaryDataListResponse.  # noqa: E501
        :type: bool
        """
        if success is None:
            raise ValueError("Invalid value for `success`, must not be `None`")  # noqa: E501

        self._success = success

    @property
    def code(self):
        """Gets the code of this FileBinaryDataListResponse.  # noqa: E501


        :return: The code of this FileBinaryDataListResponse.  # noqa: E501
        :rtype: object
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this FileBinaryDataListResponse.


        :param code: The code of this FileBinaryDataListResponse.  # noqa: E501
        :type: object
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def message(self):
        """Gets the message of this FileBinaryDataListResponse.  # noqa: E501

        A human readable message providing more details about the operation. Can be null or empty if no additional information is required.   # noqa: E501

        :return: The message of this FileBinaryDataListResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this FileBinaryDataListResponse.

        A human readable message providing more details about the operation. Can be null or empty if no additional information is required.   # noqa: E501

        :param message: The message of this FileBinaryDataListResponse.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def data(self):
        """Gets the data of this FileBinaryDataListResponse.  # noqa: E501


        :return: The data of this FileBinaryDataListResponse.  # noqa: E501
        :rtype: FileBinaryDataList
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this FileBinaryDataListResponse.


        :param data: The data of this FileBinaryDataListResponse.  # noqa: E501
        :type: FileBinaryDataList
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

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
        if issubclass(FileBinaryDataListResponse, dict):
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
        if not isinstance(other, FileBinaryDataListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
