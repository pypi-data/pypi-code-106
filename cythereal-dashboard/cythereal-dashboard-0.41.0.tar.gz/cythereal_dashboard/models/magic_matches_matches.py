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


class MagicMatchesMatches(object):
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
        'sha256': 'Sha256',
        'sha512': 'Sha512',
        'md5': 'Md5',
        'object_class': 'ObjectClass',
        'unix_filetype': 'Filetype',
        'first_seen': 'Timestamp',
        'filename': 'Filename',
        'tags': 'Tags',
        'status': 'Status',
        'analysis': 'Analysis',
        'is_public': 'IsPublic',
        'is_owned': 'IsOwned',
        'is_user': 'IsUser',
        'is_group': 'IsGroup',
        'tokens': 'Tokens',
        'av_names': 'AvNames',
        'unmapped': 'Unmapped',
        'categories': 'Categories',
        'families': 'Families',
        'category': 'Category',
        'family': 'Family',
        'labels': 'OldCategories',
        'detection_stats': 'DetectionStats',
        'num_matches': 'NumMatches',
        'match_type': 'str',
        'match_subtypes': 'list[MagicMatchesMatchSubtypes]',
        'max_similarity': 'float'
    }

    attribute_map = {
        'sha1': 'sha1',
        'sha256': 'sha256',
        'sha512': 'sha512',
        'md5': 'md5',
        'object_class': 'object_class',
        'unix_filetype': 'unix_filetype',
        'first_seen': 'first_seen',
        'filename': 'filename',
        'tags': 'tags',
        'status': 'status',
        'analysis': 'analysis',
        'is_public': 'is_public',
        'is_owned': 'is_owned',
        'is_user': 'is_user',
        'is_group': 'is_group',
        'tokens': 'tokens',
        'av_names': 'av_names',
        'unmapped': 'unmapped',
        'categories': 'categories',
        'families': 'families',
        'category': 'category',
        'family': 'family',
        'labels': 'labels',
        'detection_stats': 'detection_stats',
        'num_matches': 'num_matches',
        'match_type': 'match_type',
        'match_subtypes': 'match_subtypes',
        'max_similarity': 'max_similarity'
    }

    def __init__(self, sha1=None, sha256=None, sha512=None, md5=None, object_class=None, unix_filetype=None, first_seen=None, filename=None, tags=None, status=None, analysis=None, is_public=None, is_owned=None, is_user=None, is_group=None, tokens=None, av_names=None, unmapped=None, categories=None, families=None, category=None, family=None, labels=None, detection_stats=None, num_matches=None, match_type=None, match_subtypes=None, max_similarity=None):  # noqa: E501
        """MagicMatchesMatches - a model defined in Swagger"""  # noqa: E501

        self._sha1 = None
        self._sha256 = None
        self._sha512 = None
        self._md5 = None
        self._object_class = None
        self._unix_filetype = None
        self._first_seen = None
        self._filename = None
        self._tags = None
        self._status = None
        self._analysis = None
        self._is_public = None
        self._is_owned = None
        self._is_user = None
        self._is_group = None
        self._tokens = None
        self._av_names = None
        self._unmapped = None
        self._categories = None
        self._families = None
        self._category = None
        self._family = None
        self._labels = None
        self._detection_stats = None
        self._num_matches = None
        self._match_type = None
        self._match_subtypes = None
        self._max_similarity = None
        self.discriminator = None

        if sha1 is not None:
            self.sha1 = sha1
        if sha256 is not None:
            self.sha256 = sha256
        if sha512 is not None:
            self.sha512 = sha512
        if md5 is not None:
            self.md5 = md5
        if object_class is not None:
            self.object_class = object_class
        if unix_filetype is not None:
            self.unix_filetype = unix_filetype
        if first_seen is not None:
            self.first_seen = first_seen
        if filename is not None:
            self.filename = filename
        if tags is not None:
            self.tags = tags
        if status is not None:
            self.status = status
        if analysis is not None:
            self.analysis = analysis
        if is_public is not None:
            self.is_public = is_public
        if is_owned is not None:
            self.is_owned = is_owned
        if is_user is not None:
            self.is_user = is_user
        if is_group is not None:
            self.is_group = is_group
        if tokens is not None:
            self.tokens = tokens
        if av_names is not None:
            self.av_names = av_names
        if unmapped is not None:
            self.unmapped = unmapped
        if categories is not None:
            self.categories = categories
        if families is not None:
            self.families = families
        if category is not None:
            self.category = category
        if family is not None:
            self.family = family
        if labels is not None:
            self.labels = labels
        if detection_stats is not None:
            self.detection_stats = detection_stats
        if num_matches is not None:
            self.num_matches = num_matches
        if match_type is not None:
            self.match_type = match_type
        if match_subtypes is not None:
            self.match_subtypes = match_subtypes
        if max_similarity is not None:
            self.max_similarity = max_similarity

    @property
    def sha1(self):
        """Gets the sha1 of this MagicMatchesMatches.  # noqa: E501


        :return: The sha1 of this MagicMatchesMatches.  # noqa: E501
        :rtype: Sha1
        """
        return self._sha1

    @sha1.setter
    def sha1(self, sha1):
        """Sets the sha1 of this MagicMatchesMatches.


        :param sha1: The sha1 of this MagicMatchesMatches.  # noqa: E501
        :type: Sha1
        """

        self._sha1 = sha1

    @property
    def sha256(self):
        """Gets the sha256 of this MagicMatchesMatches.  # noqa: E501


        :return: The sha256 of this MagicMatchesMatches.  # noqa: E501
        :rtype: Sha256
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        """Sets the sha256 of this MagicMatchesMatches.


        :param sha256: The sha256 of this MagicMatchesMatches.  # noqa: E501
        :type: Sha256
        """

        self._sha256 = sha256

    @property
    def sha512(self):
        """Gets the sha512 of this MagicMatchesMatches.  # noqa: E501


        :return: The sha512 of this MagicMatchesMatches.  # noqa: E501
        :rtype: Sha512
        """
        return self._sha512

    @sha512.setter
    def sha512(self, sha512):
        """Sets the sha512 of this MagicMatchesMatches.


        :param sha512: The sha512 of this MagicMatchesMatches.  # noqa: E501
        :type: Sha512
        """

        self._sha512 = sha512

    @property
    def md5(self):
        """Gets the md5 of this MagicMatchesMatches.  # noqa: E501


        :return: The md5 of this MagicMatchesMatches.  # noqa: E501
        :rtype: Md5
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this MagicMatchesMatches.


        :param md5: The md5 of this MagicMatchesMatches.  # noqa: E501
        :type: Md5
        """

        self._md5 = md5

    @property
    def object_class(self):
        """Gets the object_class of this MagicMatchesMatches.  # noqa: E501


        :return: The object_class of this MagicMatchesMatches.  # noqa: E501
        :rtype: ObjectClass
        """
        return self._object_class

    @object_class.setter
    def object_class(self, object_class):
        """Sets the object_class of this MagicMatchesMatches.


        :param object_class: The object_class of this MagicMatchesMatches.  # noqa: E501
        :type: ObjectClass
        """

        self._object_class = object_class

    @property
    def unix_filetype(self):
        """Gets the unix_filetype of this MagicMatchesMatches.  # noqa: E501


        :return: The unix_filetype of this MagicMatchesMatches.  # noqa: E501
        :rtype: Filetype
        """
        return self._unix_filetype

    @unix_filetype.setter
    def unix_filetype(self, unix_filetype):
        """Sets the unix_filetype of this MagicMatchesMatches.


        :param unix_filetype: The unix_filetype of this MagicMatchesMatches.  # noqa: E501
        :type: Filetype
        """

        self._unix_filetype = unix_filetype

    @property
    def first_seen(self):
        """Gets the first_seen of this MagicMatchesMatches.  # noqa: E501


        :return: The first_seen of this MagicMatchesMatches.  # noqa: E501
        :rtype: Timestamp
        """
        return self._first_seen

    @first_seen.setter
    def first_seen(self, first_seen):
        """Sets the first_seen of this MagicMatchesMatches.


        :param first_seen: The first_seen of this MagicMatchesMatches.  # noqa: E501
        :type: Timestamp
        """

        self._first_seen = first_seen

    @property
    def filename(self):
        """Gets the filename of this MagicMatchesMatches.  # noqa: E501


        :return: The filename of this MagicMatchesMatches.  # noqa: E501
        :rtype: Filename
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this MagicMatchesMatches.


        :param filename: The filename of this MagicMatchesMatches.  # noqa: E501
        :type: Filename
        """

        self._filename = filename

    @property
    def tags(self):
        """Gets the tags of this MagicMatchesMatches.  # noqa: E501


        :return: The tags of this MagicMatchesMatches.  # noqa: E501
        :rtype: Tags
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this MagicMatchesMatches.


        :param tags: The tags of this MagicMatchesMatches.  # noqa: E501
        :type: Tags
        """

        self._tags = tags

    @property
    def status(self):
        """Gets the status of this MagicMatchesMatches.  # noqa: E501


        :return: The status of this MagicMatchesMatches.  # noqa: E501
        :rtype: Status
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MagicMatchesMatches.


        :param status: The status of this MagicMatchesMatches.  # noqa: E501
        :type: Status
        """

        self._status = status

    @property
    def analysis(self):
        """Gets the analysis of this MagicMatchesMatches.  # noqa: E501


        :return: The analysis of this MagicMatchesMatches.  # noqa: E501
        :rtype: Analysis
        """
        return self._analysis

    @analysis.setter
    def analysis(self, analysis):
        """Sets the analysis of this MagicMatchesMatches.


        :param analysis: The analysis of this MagicMatchesMatches.  # noqa: E501
        :type: Analysis
        """

        self._analysis = analysis

    @property
    def is_public(self):
        """Gets the is_public of this MagicMatchesMatches.  # noqa: E501


        :return: The is_public of this MagicMatchesMatches.  # noqa: E501
        :rtype: IsPublic
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this MagicMatchesMatches.


        :param is_public: The is_public of this MagicMatchesMatches.  # noqa: E501
        :type: IsPublic
        """

        self._is_public = is_public

    @property
    def is_owned(self):
        """Gets the is_owned of this MagicMatchesMatches.  # noqa: E501


        :return: The is_owned of this MagicMatchesMatches.  # noqa: E501
        :rtype: IsOwned
        """
        return self._is_owned

    @is_owned.setter
    def is_owned(self, is_owned):
        """Sets the is_owned of this MagicMatchesMatches.


        :param is_owned: The is_owned of this MagicMatchesMatches.  # noqa: E501
        :type: IsOwned
        """

        self._is_owned = is_owned

    @property
    def is_user(self):
        """Gets the is_user of this MagicMatchesMatches.  # noqa: E501


        :return: The is_user of this MagicMatchesMatches.  # noqa: E501
        :rtype: IsUser
        """
        return self._is_user

    @is_user.setter
    def is_user(self, is_user):
        """Sets the is_user of this MagicMatchesMatches.


        :param is_user: The is_user of this MagicMatchesMatches.  # noqa: E501
        :type: IsUser
        """

        self._is_user = is_user

    @property
    def is_group(self):
        """Gets the is_group of this MagicMatchesMatches.  # noqa: E501


        :return: The is_group of this MagicMatchesMatches.  # noqa: E501
        :rtype: IsGroup
        """
        return self._is_group

    @is_group.setter
    def is_group(self, is_group):
        """Sets the is_group of this MagicMatchesMatches.


        :param is_group: The is_group of this MagicMatchesMatches.  # noqa: E501
        :type: IsGroup
        """

        self._is_group = is_group

    @property
    def tokens(self):
        """Gets the tokens of this MagicMatchesMatches.  # noqa: E501


        :return: The tokens of this MagicMatchesMatches.  # noqa: E501
        :rtype: Tokens
        """
        return self._tokens

    @tokens.setter
    def tokens(self, tokens):
        """Sets the tokens of this MagicMatchesMatches.


        :param tokens: The tokens of this MagicMatchesMatches.  # noqa: E501
        :type: Tokens
        """

        self._tokens = tokens

    @property
    def av_names(self):
        """Gets the av_names of this MagicMatchesMatches.  # noqa: E501


        :return: The av_names of this MagicMatchesMatches.  # noqa: E501
        :rtype: AvNames
        """
        return self._av_names

    @av_names.setter
    def av_names(self, av_names):
        """Sets the av_names of this MagicMatchesMatches.


        :param av_names: The av_names of this MagicMatchesMatches.  # noqa: E501
        :type: AvNames
        """

        self._av_names = av_names

    @property
    def unmapped(self):
        """Gets the unmapped of this MagicMatchesMatches.  # noqa: E501


        :return: The unmapped of this MagicMatchesMatches.  # noqa: E501
        :rtype: Unmapped
        """
        return self._unmapped

    @unmapped.setter
    def unmapped(self, unmapped):
        """Sets the unmapped of this MagicMatchesMatches.


        :param unmapped: The unmapped of this MagicMatchesMatches.  # noqa: E501
        :type: Unmapped
        """

        self._unmapped = unmapped

    @property
    def categories(self):
        """Gets the categories of this MagicMatchesMatches.  # noqa: E501


        :return: The categories of this MagicMatchesMatches.  # noqa: E501
        :rtype: Categories
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this MagicMatchesMatches.


        :param categories: The categories of this MagicMatchesMatches.  # noqa: E501
        :type: Categories
        """

        self._categories = categories

    @property
    def families(self):
        """Gets the families of this MagicMatchesMatches.  # noqa: E501


        :return: The families of this MagicMatchesMatches.  # noqa: E501
        :rtype: Families
        """
        return self._families

    @families.setter
    def families(self, families):
        """Sets the families of this MagicMatchesMatches.


        :param families: The families of this MagicMatchesMatches.  # noqa: E501
        :type: Families
        """

        self._families = families

    @property
    def category(self):
        """Gets the category of this MagicMatchesMatches.  # noqa: E501


        :return: The category of this MagicMatchesMatches.  # noqa: E501
        :rtype: Category
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this MagicMatchesMatches.


        :param category: The category of this MagicMatchesMatches.  # noqa: E501
        :type: Category
        """

        self._category = category

    @property
    def family(self):
        """Gets the family of this MagicMatchesMatches.  # noqa: E501


        :return: The family of this MagicMatchesMatches.  # noqa: E501
        :rtype: Family
        """
        return self._family

    @family.setter
    def family(self, family):
        """Sets the family of this MagicMatchesMatches.


        :param family: The family of this MagicMatchesMatches.  # noqa: E501
        :type: Family
        """

        self._family = family

    @property
    def labels(self):
        """Gets the labels of this MagicMatchesMatches.  # noqa: E501


        :return: The labels of this MagicMatchesMatches.  # noqa: E501
        :rtype: OldCategories
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this MagicMatchesMatches.


        :param labels: The labels of this MagicMatchesMatches.  # noqa: E501
        :type: OldCategories
        """

        self._labels = labels

    @property
    def detection_stats(self):
        """Gets the detection_stats of this MagicMatchesMatches.  # noqa: E501


        :return: The detection_stats of this MagicMatchesMatches.  # noqa: E501
        :rtype: DetectionStats
        """
        return self._detection_stats

    @detection_stats.setter
    def detection_stats(self, detection_stats):
        """Sets the detection_stats of this MagicMatchesMatches.


        :param detection_stats: The detection_stats of this MagicMatchesMatches.  # noqa: E501
        :type: DetectionStats
        """

        self._detection_stats = detection_stats

    @property
    def num_matches(self):
        """Gets the num_matches of this MagicMatchesMatches.  # noqa: E501


        :return: The num_matches of this MagicMatchesMatches.  # noqa: E501
        :rtype: NumMatches
        """
        return self._num_matches

    @num_matches.setter
    def num_matches(self, num_matches):
        """Sets the num_matches of this MagicMatchesMatches.


        :param num_matches: The num_matches of this MagicMatchesMatches.  # noqa: E501
        :type: NumMatches
        """

        self._num_matches = num_matches

    @property
    def match_type(self):
        """Gets the match_type of this MagicMatchesMatches.  # noqa: E501

        The MAGIC classification for the match.  # noqa: E501

        :return: The match_type of this MagicMatchesMatches.  # noqa: E501
        :rtype: str
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        """Sets the match_type of this MagicMatchesMatches.

        The MAGIC classification for the match.  # noqa: E501

        :param match_type: The match_type of this MagicMatchesMatches.  # noqa: E501
        :type: str
        """
        allowed_values = ["similar_packer_similar_payload", "similar_packer_different_payload", "different_packer_similar_payload", "weak_similar"]  # noqa: E501
        if match_type not in allowed_values:
            raise ValueError(
                "Invalid value for `match_type` ({0}), must be one of {1}"  # noqa: E501
                .format(match_type, allowed_values)
            )

        self._match_type = match_type

    @property
    def match_subtypes(self):
        """Gets the match_subtypes of this MagicMatchesMatches.  # noqa: E501

        Finer grained identification of match types.  # noqa: E501

        :return: The match_subtypes of this MagicMatchesMatches.  # noqa: E501
        :rtype: list[MagicMatchesMatchSubtypes]
        """
        return self._match_subtypes

    @match_subtypes.setter
    def match_subtypes(self, match_subtypes):
        """Sets the match_subtypes of this MagicMatchesMatches.

        Finer grained identification of match types.  # noqa: E501

        :param match_subtypes: The match_subtypes of this MagicMatchesMatches.  # noqa: E501
        :type: list[MagicMatchesMatchSubtypes]
        """

        self._match_subtypes = match_subtypes

    @property
    def max_similarity(self):
        """Gets the max_similarity of this MagicMatchesMatches.  # noqa: E501

        The maximum similarity value from `match_subtypes`.  # noqa: E501

        :return: The max_similarity of this MagicMatchesMatches.  # noqa: E501
        :rtype: float
        """
        return self._max_similarity

    @max_similarity.setter
    def max_similarity(self, max_similarity):
        """Sets the max_similarity of this MagicMatchesMatches.

        The maximum similarity value from `match_subtypes`.  # noqa: E501

        :param max_similarity: The max_similarity of this MagicMatchesMatches.  # noqa: E501
        :type: float
        """

        self._max_similarity = max_similarity

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
        if issubclass(MagicMatchesMatches, dict):
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
        if not isinstance(other, MagicMatchesMatches):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
