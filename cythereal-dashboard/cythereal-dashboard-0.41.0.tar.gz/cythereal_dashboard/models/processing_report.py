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


class ProcessingReport(object):
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
        'report_date': 'Timestamp',
        'bin_count': 'int',
        'est_success_bin_count': 'int',
        'binhash_count': 'int',
        'proc_count': 'int',
        'prochash_count': 'int',
        'sims_nodes_count': 'int',
        'sims_rel_count': 'int',
        'binhash_compression': 'float',
        'prochash_compression': 'float',
        'obj_counts': 'object',
        'processed_counts': 'object',
        'time_stats': 'list[TimeStat]'
    }

    attribute_map = {
        'report_date': 'report_date',
        'bin_count': 'bin_count',
        'est_success_bin_count': 'est_success_bin_count',
        'binhash_count': 'binhash_count',
        'proc_count': 'proc_count',
        'prochash_count': 'prochash_count',
        'sims_nodes_count': 'sims_nodes_count',
        'sims_rel_count': 'sims_rel_count',
        'binhash_compression': 'binhash_compression',
        'prochash_compression': 'prochash_compression',
        'obj_counts': 'obj_counts',
        'processed_counts': 'processed_counts',
        'time_stats': 'time_stats'
    }

    def __init__(self, report_date=None, bin_count=None, est_success_bin_count=None, binhash_count=None, proc_count=None, prochash_count=None, sims_nodes_count=None, sims_rel_count=None, binhash_compression=None, prochash_compression=None, obj_counts=None, processed_counts=None, time_stats=None):  # noqa: E501
        """ProcessingReport - a model defined in Swagger"""  # noqa: E501

        self._report_date = None
        self._bin_count = None
        self._est_success_bin_count = None
        self._binhash_count = None
        self._proc_count = None
        self._prochash_count = None
        self._sims_nodes_count = None
        self._sims_rel_count = None
        self._binhash_compression = None
        self._prochash_compression = None
        self._obj_counts = None
        self._processed_counts = None
        self._time_stats = None
        self.discriminator = None

        if report_date is not None:
            self.report_date = report_date
        if bin_count is not None:
            self.bin_count = bin_count
        if est_success_bin_count is not None:
            self.est_success_bin_count = est_success_bin_count
        if binhash_count is not None:
            self.binhash_count = binhash_count
        if proc_count is not None:
            self.proc_count = proc_count
        if prochash_count is not None:
            self.prochash_count = prochash_count
        if sims_nodes_count is not None:
            self.sims_nodes_count = sims_nodes_count
        if sims_rel_count is not None:
            self.sims_rel_count = sims_rel_count
        if binhash_compression is not None:
            self.binhash_compression = binhash_compression
        if prochash_compression is not None:
            self.prochash_compression = prochash_compression
        if obj_counts is not None:
            self.obj_counts = obj_counts
        if processed_counts is not None:
            self.processed_counts = processed_counts
        if time_stats is not None:
            self.time_stats = time_stats

    @property
    def report_date(self):
        """Gets the report_date of this ProcessingReport.  # noqa: E501


        :return: The report_date of this ProcessingReport.  # noqa: E501
        :rtype: Timestamp
        """
        return self._report_date

    @report_date.setter
    def report_date(self, report_date):
        """Sets the report_date of this ProcessingReport.


        :param report_date: The report_date of this ProcessingReport.  # noqa: E501
        :type: Timestamp
        """

        self._report_date = report_date

    @property
    def bin_count(self):
        """Gets the bin_count of this ProcessingReport.  # noqa: E501


        :return: The bin_count of this ProcessingReport.  # noqa: E501
        :rtype: int
        """
        return self._bin_count

    @bin_count.setter
    def bin_count(self, bin_count):
        """Sets the bin_count of this ProcessingReport.


        :param bin_count: The bin_count of this ProcessingReport.  # noqa: E501
        :type: int
        """

        self._bin_count = bin_count

    @property
    def est_success_bin_count(self):
        """Gets the est_success_bin_count of this ProcessingReport.  # noqa: E501


        :return: The est_success_bin_count of this ProcessingReport.  # noqa: E501
        :rtype: int
        """
        return self._est_success_bin_count

    @est_success_bin_count.setter
    def est_success_bin_count(self, est_success_bin_count):
        """Sets the est_success_bin_count of this ProcessingReport.


        :param est_success_bin_count: The est_success_bin_count of this ProcessingReport.  # noqa: E501
        :type: int
        """

        self._est_success_bin_count = est_success_bin_count

    @property
    def binhash_count(self):
        """Gets the binhash_count of this ProcessingReport.  # noqa: E501


        :return: The binhash_count of this ProcessingReport.  # noqa: E501
        :rtype: int
        """
        return self._binhash_count

    @binhash_count.setter
    def binhash_count(self, binhash_count):
        """Sets the binhash_count of this ProcessingReport.


        :param binhash_count: The binhash_count of this ProcessingReport.  # noqa: E501
        :type: int
        """

        self._binhash_count = binhash_count

    @property
    def proc_count(self):
        """Gets the proc_count of this ProcessingReport.  # noqa: E501


        :return: The proc_count of this ProcessingReport.  # noqa: E501
        :rtype: int
        """
        return self._proc_count

    @proc_count.setter
    def proc_count(self, proc_count):
        """Sets the proc_count of this ProcessingReport.


        :param proc_count: The proc_count of this ProcessingReport.  # noqa: E501
        :type: int
        """

        self._proc_count = proc_count

    @property
    def prochash_count(self):
        """Gets the prochash_count of this ProcessingReport.  # noqa: E501


        :return: The prochash_count of this ProcessingReport.  # noqa: E501
        :rtype: int
        """
        return self._prochash_count

    @prochash_count.setter
    def prochash_count(self, prochash_count):
        """Sets the prochash_count of this ProcessingReport.


        :param prochash_count: The prochash_count of this ProcessingReport.  # noqa: E501
        :type: int
        """

        self._prochash_count = prochash_count

    @property
    def sims_nodes_count(self):
        """Gets the sims_nodes_count of this ProcessingReport.  # noqa: E501


        :return: The sims_nodes_count of this ProcessingReport.  # noqa: E501
        :rtype: int
        """
        return self._sims_nodes_count

    @sims_nodes_count.setter
    def sims_nodes_count(self, sims_nodes_count):
        """Sets the sims_nodes_count of this ProcessingReport.


        :param sims_nodes_count: The sims_nodes_count of this ProcessingReport.  # noqa: E501
        :type: int
        """

        self._sims_nodes_count = sims_nodes_count

    @property
    def sims_rel_count(self):
        """Gets the sims_rel_count of this ProcessingReport.  # noqa: E501


        :return: The sims_rel_count of this ProcessingReport.  # noqa: E501
        :rtype: int
        """
        return self._sims_rel_count

    @sims_rel_count.setter
    def sims_rel_count(self, sims_rel_count):
        """Sets the sims_rel_count of this ProcessingReport.


        :param sims_rel_count: The sims_rel_count of this ProcessingReport.  # noqa: E501
        :type: int
        """

        self._sims_rel_count = sims_rel_count

    @property
    def binhash_compression(self):
        """Gets the binhash_compression of this ProcessingReport.  # noqa: E501


        :return: The binhash_compression of this ProcessingReport.  # noqa: E501
        :rtype: float
        """
        return self._binhash_compression

    @binhash_compression.setter
    def binhash_compression(self, binhash_compression):
        """Sets the binhash_compression of this ProcessingReport.


        :param binhash_compression: The binhash_compression of this ProcessingReport.  # noqa: E501
        :type: float
        """

        self._binhash_compression = binhash_compression

    @property
    def prochash_compression(self):
        """Gets the prochash_compression of this ProcessingReport.  # noqa: E501


        :return: The prochash_compression of this ProcessingReport.  # noqa: E501
        :rtype: float
        """
        return self._prochash_compression

    @prochash_compression.setter
    def prochash_compression(self, prochash_compression):
        """Sets the prochash_compression of this ProcessingReport.


        :param prochash_compression: The prochash_compression of this ProcessingReport.  # noqa: E501
        :type: float
        """

        self._prochash_compression = prochash_compression

    @property
    def obj_counts(self):
        """Gets the obj_counts of this ProcessingReport.  # noqa: E501


        :return: The obj_counts of this ProcessingReport.  # noqa: E501
        :rtype: object
        """
        return self._obj_counts

    @obj_counts.setter
    def obj_counts(self, obj_counts):
        """Sets the obj_counts of this ProcessingReport.


        :param obj_counts: The obj_counts of this ProcessingReport.  # noqa: E501
        :type: object
        """

        self._obj_counts = obj_counts

    @property
    def processed_counts(self):
        """Gets the processed_counts of this ProcessingReport.  # noqa: E501


        :return: The processed_counts of this ProcessingReport.  # noqa: E501
        :rtype: object
        """
        return self._processed_counts

    @processed_counts.setter
    def processed_counts(self, processed_counts):
        """Sets the processed_counts of this ProcessingReport.


        :param processed_counts: The processed_counts of this ProcessingReport.  # noqa: E501
        :type: object
        """

        self._processed_counts = processed_counts

    @property
    def time_stats(self):
        """Gets the time_stats of this ProcessingReport.  # noqa: E501


        :return: The time_stats of this ProcessingReport.  # noqa: E501
        :rtype: list[TimeStat]
        """
        return self._time_stats

    @time_stats.setter
    def time_stats(self, time_stats):
        """Sets the time_stats of this ProcessingReport.


        :param time_stats: The time_stats of this ProcessingReport.  # noqa: E501
        :type: list[TimeStat]
        """

        self._time_stats = time_stats

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
        if issubclass(ProcessingReport, dict):
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
        if not isinstance(other, ProcessingReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
