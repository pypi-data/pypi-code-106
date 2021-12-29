# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetContainerResult',
    'AwaitableGetContainerResult',
    'get_container',
    'get_container_output',
]

@pulumi.output_type
class GetContainerResult:
    """
    Represents a container on the  Data Box Edge/Gateway device.
    """
    def __init__(__self__, container_status=None, created_date_time=None, data_format=None, id=None, name=None, refresh_details=None, type=None):
        if container_status and not isinstance(container_status, str):
            raise TypeError("Expected argument 'container_status' to be a str")
        pulumi.set(__self__, "container_status", container_status)
        if created_date_time and not isinstance(created_date_time, str):
            raise TypeError("Expected argument 'created_date_time' to be a str")
        pulumi.set(__self__, "created_date_time", created_date_time)
        if data_format and not isinstance(data_format, str):
            raise TypeError("Expected argument 'data_format' to be a str")
        pulumi.set(__self__, "data_format", data_format)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if refresh_details and not isinstance(refresh_details, dict):
            raise TypeError("Expected argument 'refresh_details' to be a dict")
        pulumi.set(__self__, "refresh_details", refresh_details)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="containerStatus")
    def container_status(self) -> str:
        """
        Current status of the container.
        """
        return pulumi.get(self, "container_status")

    @property
    @pulumi.getter(name="createdDateTime")
    def created_date_time(self) -> str:
        """
        The UTC time when container got created.
        """
        return pulumi.get(self, "created_date_time")

    @property
    @pulumi.getter(name="dataFormat")
    def data_format(self) -> str:
        """
        DataFormat for Container
        """
        return pulumi.get(self, "data_format")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The path ID that uniquely identifies the object.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The object name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="refreshDetails")
    def refresh_details(self) -> 'outputs.RefreshDetailsResponse':
        """
        Details of the refresh job on this container.
        """
        return pulumi.get(self, "refresh_details")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The hierarchical type of the object.
        """
        return pulumi.get(self, "type")


class AwaitableGetContainerResult(GetContainerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetContainerResult(
            container_status=self.container_status,
            created_date_time=self.created_date_time,
            data_format=self.data_format,
            id=self.id,
            name=self.name,
            refresh_details=self.refresh_details,
            type=self.type)


def get_container(container_name: Optional[str] = None,
                  device_name: Optional[str] = None,
                  resource_group_name: Optional[str] = None,
                  storage_account_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetContainerResult:
    """
    Represents a container on the  Data Box Edge/Gateway device.


    :param str container_name: The container Name
    :param str device_name: The device name.
    :param str resource_group_name: The resource group name.
    :param str storage_account_name: The Storage Account Name
    """
    __args__ = dict()
    __args__['containerName'] = container_name
    __args__['deviceName'] = device_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['storageAccountName'] = storage_account_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:databoxedge/v20190801:getContainer', __args__, opts=opts, typ=GetContainerResult).value

    return AwaitableGetContainerResult(
        container_status=__ret__.container_status,
        created_date_time=__ret__.created_date_time,
        data_format=__ret__.data_format,
        id=__ret__.id,
        name=__ret__.name,
        refresh_details=__ret__.refresh_details,
        type=__ret__.type)


@_utilities.lift_output_func(get_container)
def get_container_output(container_name: Optional[pulumi.Input[str]] = None,
                         device_name: Optional[pulumi.Input[str]] = None,
                         resource_group_name: Optional[pulumi.Input[str]] = None,
                         storage_account_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetContainerResult]:
    """
    Represents a container on the  Data Box Edge/Gateway device.


    :param str container_name: The container Name
    :param str device_name: The device name.
    :param str resource_group_name: The resource group name.
    :param str storage_account_name: The Storage Account Name
    """
    ...
