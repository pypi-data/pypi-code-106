# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetDatabaseAccountTableResult',
    'AwaitableGetDatabaseAccountTableResult',
    'get_database_account_table',
    'get_database_account_table_output',
]

@pulumi.output_type
class GetDatabaseAccountTableResult:
    """
    An Azure Cosmos DB Table.
    """
    def __init__(__self__, id=None, location=None, name=None, tags=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The unique resource identifier of the database account.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The location of the resource group to which the resource belongs.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the database account.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of Azure resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetDatabaseAccountTableResult(GetDatabaseAccountTableResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatabaseAccountTableResult(
            id=self.id,
            location=self.location,
            name=self.name,
            tags=self.tags,
            type=self.type)


def get_database_account_table(account_name: Optional[str] = None,
                               resource_group_name: Optional[str] = None,
                               table_name: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatabaseAccountTableResult:
    """
    An Azure Cosmos DB Table.


    :param str account_name: Cosmos DB database account name.
    :param str resource_group_name: Name of an Azure resource group.
    :param str table_name: Cosmos DB table name.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['tableName'] = table_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:documentdb/v20150401:getDatabaseAccountTable', __args__, opts=opts, typ=GetDatabaseAccountTableResult).value

    return AwaitableGetDatabaseAccountTableResult(
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_database_account_table)
def get_database_account_table_output(account_name: Optional[pulumi.Input[str]] = None,
                                      resource_group_name: Optional[pulumi.Input[str]] = None,
                                      table_name: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatabaseAccountTableResult]:
    """
    An Azure Cosmos DB Table.


    :param str account_name: Cosmos DB database account name.
    :param str resource_group_name: Name of an Azure resource group.
    :param str table_name: Cosmos DB table name.
    """
    ...
