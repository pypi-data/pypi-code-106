# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *

__all__ = ['ContainerArgs', 'Container']

@pulumi.input_type
class ContainerArgs:
    def __init__(__self__, *,
                 data_format: pulumi.Input[Union[str, 'AzureContainerDataFormat']],
                 device_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 storage_account_name: pulumi.Input[str],
                 container_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Container resource.
        :param pulumi.Input[Union[str, 'AzureContainerDataFormat']] data_format: DataFormat for Container
        :param pulumi.Input[str] device_name: The device name.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] storage_account_name: The Storage Account Name
        :param pulumi.Input[str] container_name: The container name.
        """
        pulumi.set(__self__, "data_format", data_format)
        pulumi.set(__self__, "device_name", device_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "storage_account_name", storage_account_name)
        if container_name is not None:
            pulumi.set(__self__, "container_name", container_name)

    @property
    @pulumi.getter(name="dataFormat")
    def data_format(self) -> pulumi.Input[Union[str, 'AzureContainerDataFormat']]:
        """
        DataFormat for Container
        """
        return pulumi.get(self, "data_format")

    @data_format.setter
    def data_format(self, value: pulumi.Input[Union[str, 'AzureContainerDataFormat']]):
        pulumi.set(self, "data_format", value)

    @property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Input[str]:
        """
        The device name.
        """
        return pulumi.get(self, "device_name")

    @device_name.setter
    def device_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "device_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> pulumi.Input[str]:
        """
        The Storage Account Name
        """
        return pulumi.get(self, "storage_account_name")

    @storage_account_name.setter
    def storage_account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "storage_account_name", value)

    @property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[pulumi.Input[str]]:
        """
        The container name.
        """
        return pulumi.get(self, "container_name")

    @container_name.setter
    def container_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "container_name", value)


class Container(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 container_name: Optional[pulumi.Input[str]] = None,
                 data_format: Optional[pulumi.Input[Union[str, 'AzureContainerDataFormat']]] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_account_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Represents a container on the  Data Box Edge/Gateway device.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] container_name: The container name.
        :param pulumi.Input[Union[str, 'AzureContainerDataFormat']] data_format: DataFormat for Container
        :param pulumi.Input[str] device_name: The device name.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] storage_account_name: The Storage Account Name
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ContainerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a container on the  Data Box Edge/Gateway device.

        :param str resource_name: The name of the resource.
        :param ContainerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ContainerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 container_name: Optional[pulumi.Input[str]] = None,
                 data_format: Optional[pulumi.Input[Union[str, 'AzureContainerDataFormat']]] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_account_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ContainerArgs.__new__(ContainerArgs)

            __props__.__dict__["container_name"] = container_name
            if data_format is None and not opts.urn:
                raise TypeError("Missing required property 'data_format'")
            __props__.__dict__["data_format"] = data_format
            if device_name is None and not opts.urn:
                raise TypeError("Missing required property 'device_name'")
            __props__.__dict__["device_name"] = device_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if storage_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'storage_account_name'")
            __props__.__dict__["storage_account_name"] = storage_account_name
            __props__.__dict__["container_status"] = None
            __props__.__dict__["created_date_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["refresh_details"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:databoxedge:Container"), pulumi.Alias(type_="azure-native:databoxedge/v20190801:Container"), pulumi.Alias(type_="azure-native:databoxedge/v20200501preview:Container"), pulumi.Alias(type_="azure-native:databoxedge/v20200901:Container"), pulumi.Alias(type_="azure-native:databoxedge/v20200901preview:Container"), pulumi.Alias(type_="azure-native:databoxedge/v20201201:Container"), pulumi.Alias(type_="azure-native:databoxedge/v20210201:Container"), pulumi.Alias(type_="azure-native:databoxedge/v20210201preview:Container"), pulumi.Alias(type_="azure-native:databoxedge/v20210601:Container")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Container, __self__).__init__(
            'azure-native:databoxedge/v20210601preview:Container',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Container':
        """
        Get an existing Container resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ContainerArgs.__new__(ContainerArgs)

        __props__.__dict__["container_status"] = None
        __props__.__dict__["created_date_time"] = None
        __props__.__dict__["data_format"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["refresh_details"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return Container(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="containerStatus")
    def container_status(self) -> pulumi.Output[str]:
        """
        Current status of the container.
        """
        return pulumi.get(self, "container_status")

    @property
    @pulumi.getter(name="createdDateTime")
    def created_date_time(self) -> pulumi.Output[str]:
        """
        The UTC time when container got created.
        """
        return pulumi.get(self, "created_date_time")

    @property
    @pulumi.getter(name="dataFormat")
    def data_format(self) -> pulumi.Output[str]:
        """
        DataFormat for Container
        """
        return pulumi.get(self, "data_format")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The object name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="refreshDetails")
    def refresh_details(self) -> pulumi.Output['outputs.RefreshDetailsResponse']:
        """
        Details of the refresh job on this container.
        """
        return pulumi.get(self, "refresh_details")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Container in DataBoxEdge Resource
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The hierarchical type of the object.
        """
        return pulumi.get(self, "type")

