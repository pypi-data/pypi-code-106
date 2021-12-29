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
from ._inputs import *

__all__ = ['IoTRoleArgs', 'IoTRole']

@pulumi.input_type
class IoTRoleArgs:
    def __init__(__self__, *,
                 device_name: pulumi.Input[str],
                 host_platform: pulumi.Input[Union[str, 'PlatformType']],
                 io_t_device_details: pulumi.Input['IoTDeviceInfoArgs'],
                 io_t_edge_device_details: pulumi.Input['IoTDeviceInfoArgs'],
                 kind: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 role_status: pulumi.Input[Union[str, 'RoleStatus']],
                 compute_resource: Optional[pulumi.Input['ComputeResourceArgs']] = None,
                 io_t_edge_agent_info: Optional[pulumi.Input['IoTEdgeAgentInfoArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 share_mappings: Optional[pulumi.Input[Sequence[pulumi.Input['MountPointMapArgs']]]] = None):
        """
        The set of arguments for constructing a IoTRole resource.
        :param pulumi.Input[str] device_name: The device name.
        :param pulumi.Input[Union[str, 'PlatformType']] host_platform: Host OS supported by the IoT role.
        :param pulumi.Input['IoTDeviceInfoArgs'] io_t_device_details: IoT device metadata to which data box edge device needs to be connected.
        :param pulumi.Input['IoTDeviceInfoArgs'] io_t_edge_device_details: IoT edge device to which the IoT role needs to be configured.
        :param pulumi.Input[str] kind: Role type.
               Expected value is 'IOT'.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[Union[str, 'RoleStatus']] role_status: Role status.
        :param pulumi.Input['ComputeResourceArgs'] compute_resource: Resource allocation
        :param pulumi.Input['IoTEdgeAgentInfoArgs'] io_t_edge_agent_info: Iot edge agent details to download the agent and bootstrap iot runtime.
        :param pulumi.Input[str] name: The role name.
        :param pulumi.Input[Sequence[pulumi.Input['MountPointMapArgs']]] share_mappings: Mount points of shares in role(s).
        """
        pulumi.set(__self__, "device_name", device_name)
        pulumi.set(__self__, "host_platform", host_platform)
        pulumi.set(__self__, "io_t_device_details", io_t_device_details)
        pulumi.set(__self__, "io_t_edge_device_details", io_t_edge_device_details)
        pulumi.set(__self__, "kind", 'IOT')
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "role_status", role_status)
        if compute_resource is not None:
            pulumi.set(__self__, "compute_resource", compute_resource)
        if io_t_edge_agent_info is not None:
            pulumi.set(__self__, "io_t_edge_agent_info", io_t_edge_agent_info)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if share_mappings is not None:
            pulumi.set(__self__, "share_mappings", share_mappings)

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
    @pulumi.getter(name="hostPlatform")
    def host_platform(self) -> pulumi.Input[Union[str, 'PlatformType']]:
        """
        Host OS supported by the IoT role.
        """
        return pulumi.get(self, "host_platform")

    @host_platform.setter
    def host_platform(self, value: pulumi.Input[Union[str, 'PlatformType']]):
        pulumi.set(self, "host_platform", value)

    @property
    @pulumi.getter(name="ioTDeviceDetails")
    def io_t_device_details(self) -> pulumi.Input['IoTDeviceInfoArgs']:
        """
        IoT device metadata to which data box edge device needs to be connected.
        """
        return pulumi.get(self, "io_t_device_details")

    @io_t_device_details.setter
    def io_t_device_details(self, value: pulumi.Input['IoTDeviceInfoArgs']):
        pulumi.set(self, "io_t_device_details", value)

    @property
    @pulumi.getter(name="ioTEdgeDeviceDetails")
    def io_t_edge_device_details(self) -> pulumi.Input['IoTDeviceInfoArgs']:
        """
        IoT edge device to which the IoT role needs to be configured.
        """
        return pulumi.get(self, "io_t_edge_device_details")

    @io_t_edge_device_details.setter
    def io_t_edge_device_details(self, value: pulumi.Input['IoTDeviceInfoArgs']):
        pulumi.set(self, "io_t_edge_device_details", value)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        Role type.
        Expected value is 'IOT'.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)

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
    @pulumi.getter(name="roleStatus")
    def role_status(self) -> pulumi.Input[Union[str, 'RoleStatus']]:
        """
        Role status.
        """
        return pulumi.get(self, "role_status")

    @role_status.setter
    def role_status(self, value: pulumi.Input[Union[str, 'RoleStatus']]):
        pulumi.set(self, "role_status", value)

    @property
    @pulumi.getter(name="computeResource")
    def compute_resource(self) -> Optional[pulumi.Input['ComputeResourceArgs']]:
        """
        Resource allocation
        """
        return pulumi.get(self, "compute_resource")

    @compute_resource.setter
    def compute_resource(self, value: Optional[pulumi.Input['ComputeResourceArgs']]):
        pulumi.set(self, "compute_resource", value)

    @property
    @pulumi.getter(name="ioTEdgeAgentInfo")
    def io_t_edge_agent_info(self) -> Optional[pulumi.Input['IoTEdgeAgentInfoArgs']]:
        """
        Iot edge agent details to download the agent and bootstrap iot runtime.
        """
        return pulumi.get(self, "io_t_edge_agent_info")

    @io_t_edge_agent_info.setter
    def io_t_edge_agent_info(self, value: Optional[pulumi.Input['IoTEdgeAgentInfoArgs']]):
        pulumi.set(self, "io_t_edge_agent_info", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The role name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="shareMappings")
    def share_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MountPointMapArgs']]]]:
        """
        Mount points of shares in role(s).
        """
        return pulumi.get(self, "share_mappings")

    @share_mappings.setter
    def share_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MountPointMapArgs']]]]):
        pulumi.set(self, "share_mappings", value)


class IoTRole(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compute_resource: Optional[pulumi.Input[pulumi.InputType['ComputeResourceArgs']]] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 host_platform: Optional[pulumi.Input[Union[str, 'PlatformType']]] = None,
                 io_t_device_details: Optional[pulumi.Input[pulumi.InputType['IoTDeviceInfoArgs']]] = None,
                 io_t_edge_agent_info: Optional[pulumi.Input[pulumi.InputType['IoTEdgeAgentInfoArgs']]] = None,
                 io_t_edge_device_details: Optional[pulumi.Input[pulumi.InputType['IoTDeviceInfoArgs']]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 role_status: Optional[pulumi.Input[Union[str, 'RoleStatus']]] = None,
                 share_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MountPointMapArgs']]]]] = None,
                 __props__=None):
        """
        Compute role.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ComputeResourceArgs']] compute_resource: Resource allocation
        :param pulumi.Input[str] device_name: The device name.
        :param pulumi.Input[Union[str, 'PlatformType']] host_platform: Host OS supported by the IoT role.
        :param pulumi.Input[pulumi.InputType['IoTDeviceInfoArgs']] io_t_device_details: IoT device metadata to which data box edge device needs to be connected.
        :param pulumi.Input[pulumi.InputType['IoTEdgeAgentInfoArgs']] io_t_edge_agent_info: Iot edge agent details to download the agent and bootstrap iot runtime.
        :param pulumi.Input[pulumi.InputType['IoTDeviceInfoArgs']] io_t_edge_device_details: IoT edge device to which the IoT role needs to be configured.
        :param pulumi.Input[str] kind: Role type.
               Expected value is 'IOT'.
        :param pulumi.Input[str] name: The role name.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[Union[str, 'RoleStatus']] role_status: Role status.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MountPointMapArgs']]]] share_mappings: Mount points of shares in role(s).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IoTRoleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Compute role.

        :param str resource_name: The name of the resource.
        :param IoTRoleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IoTRoleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compute_resource: Optional[pulumi.Input[pulumi.InputType['ComputeResourceArgs']]] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 host_platform: Optional[pulumi.Input[Union[str, 'PlatformType']]] = None,
                 io_t_device_details: Optional[pulumi.Input[pulumi.InputType['IoTDeviceInfoArgs']]] = None,
                 io_t_edge_agent_info: Optional[pulumi.Input[pulumi.InputType['IoTEdgeAgentInfoArgs']]] = None,
                 io_t_edge_device_details: Optional[pulumi.Input[pulumi.InputType['IoTDeviceInfoArgs']]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 role_status: Optional[pulumi.Input[Union[str, 'RoleStatus']]] = None,
                 share_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MountPointMapArgs']]]]] = None,
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
            __props__ = IoTRoleArgs.__new__(IoTRoleArgs)

            __props__.__dict__["compute_resource"] = compute_resource
            if device_name is None and not opts.urn:
                raise TypeError("Missing required property 'device_name'")
            __props__.__dict__["device_name"] = device_name
            if host_platform is None and not opts.urn:
                raise TypeError("Missing required property 'host_platform'")
            __props__.__dict__["host_platform"] = host_platform
            if io_t_device_details is None and not opts.urn:
                raise TypeError("Missing required property 'io_t_device_details'")
            __props__.__dict__["io_t_device_details"] = io_t_device_details
            __props__.__dict__["io_t_edge_agent_info"] = io_t_edge_agent_info
            if io_t_edge_device_details is None and not opts.urn:
                raise TypeError("Missing required property 'io_t_edge_device_details'")
            __props__.__dict__["io_t_edge_device_details"] = io_t_edge_device_details
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = 'IOT'
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if role_status is None and not opts.urn:
                raise TypeError("Missing required property 'role_status'")
            __props__.__dict__["role_status"] = role_status
            __props__.__dict__["share_mappings"] = share_mappings
            __props__.__dict__["host_platform_type"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:databoxedge:IoTRole"), pulumi.Alias(type_="azure-native:databoxedge/v20190301:IoTRole"), pulumi.Alias(type_="azure-native:databoxedge/v20190701:IoTRole"), pulumi.Alias(type_="azure-native:databoxedge/v20190801:IoTRole"), pulumi.Alias(type_="azure-native:databoxedge/v20200501preview:IoTRole"), pulumi.Alias(type_="azure-native:databoxedge/v20200901preview:IoTRole"), pulumi.Alias(type_="azure-native:databoxedge/v20201201:IoTRole"), pulumi.Alias(type_="azure-native:databoxedge/v20210201:IoTRole"), pulumi.Alias(type_="azure-native:databoxedge/v20210201preview:IoTRole"), pulumi.Alias(type_="azure-native:databoxedge/v20210601:IoTRole"), pulumi.Alias(type_="azure-native:databoxedge/v20210601preview:IoTRole")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(IoTRole, __self__).__init__(
            'azure-native:databoxedge/v20200901:IoTRole',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'IoTRole':
        """
        Get an existing IoTRole resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IoTRoleArgs.__new__(IoTRoleArgs)

        __props__.__dict__["compute_resource"] = None
        __props__.__dict__["host_platform"] = None
        __props__.__dict__["host_platform_type"] = None
        __props__.__dict__["io_t_device_details"] = None
        __props__.__dict__["io_t_edge_agent_info"] = None
        __props__.__dict__["io_t_edge_device_details"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["role_status"] = None
        __props__.__dict__["share_mappings"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return IoTRole(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="computeResource")
    def compute_resource(self) -> pulumi.Output[Optional['outputs.ComputeResourceResponse']]:
        """
        Resource allocation
        """
        return pulumi.get(self, "compute_resource")

    @property
    @pulumi.getter(name="hostPlatform")
    def host_platform(self) -> pulumi.Output[str]:
        """
        Host OS supported by the IoT role.
        """
        return pulumi.get(self, "host_platform")

    @property
    @pulumi.getter(name="hostPlatformType")
    def host_platform_type(self) -> pulumi.Output[str]:
        """
        Platform where the Iot runtime is hosted.
        """
        return pulumi.get(self, "host_platform_type")

    @property
    @pulumi.getter(name="ioTDeviceDetails")
    def io_t_device_details(self) -> pulumi.Output['outputs.IoTDeviceInfoResponse']:
        """
        IoT device metadata to which data box edge device needs to be connected.
        """
        return pulumi.get(self, "io_t_device_details")

    @property
    @pulumi.getter(name="ioTEdgeAgentInfo")
    def io_t_edge_agent_info(self) -> pulumi.Output[Optional['outputs.IoTEdgeAgentInfoResponse']]:
        """
        Iot edge agent details to download the agent and bootstrap iot runtime.
        """
        return pulumi.get(self, "io_t_edge_agent_info")

    @property
    @pulumi.getter(name="ioTEdgeDeviceDetails")
    def io_t_edge_device_details(self) -> pulumi.Output['outputs.IoTDeviceInfoResponse']:
        """
        IoT edge device to which the IoT role needs to be configured.
        """
        return pulumi.get(self, "io_t_edge_device_details")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Role type.
        Expected value is 'IOT'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The object name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="roleStatus")
    def role_status(self) -> pulumi.Output[str]:
        """
        Role status.
        """
        return pulumi.get(self, "role_status")

    @property
    @pulumi.getter(name="shareMappings")
    def share_mappings(self) -> pulumi.Output[Optional[Sequence['outputs.MountPointMapResponse']]]:
        """
        Mount points of shares in role(s).
        """
        return pulumi.get(self, "share_mappings")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Role configured on ASE resource
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The hierarchical type of the object.
        """
        return pulumi.get(self, "type")

