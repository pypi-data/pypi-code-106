# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['NotebookProxyArgs', 'NotebookProxy']

@pulumi.input_type
class NotebookProxyArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 hostname: Optional[pulumi.Input[str]] = None,
                 public_dns: Optional[pulumi.Input[str]] = None,
                 public_network_access: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 resource_name: Optional[pulumi.Input[str]] = None,
                 secondary_app_id: Optional[pulumi.Input[str]] = None,
                 system_data: Optional[pulumi.Input['NotebookResourceSystemDataArgs']] = None):
        """
        The set of arguments for constructing a NotebookProxy resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] hostname: The friendly string identifier of the creator of the NotebookProxy resource.
        :param pulumi.Input[str] public_dns: The public DNS name
        :param pulumi.Input[str] public_network_access: Allow public network access on a V-Net locked notebook resource
        :param pulumi.Input[str] region: The region of the NotebookProxy resource.
        :param pulumi.Input[str] resource_name: The name of the resource.
        :param pulumi.Input[str] secondary_app_id: The alternate application ID used for auth token request in the data plane
        :param pulumi.Input['NotebookResourceSystemDataArgs'] system_data: System data for notebook resource
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if hostname is not None:
            pulumi.set(__self__, "hostname", hostname)
        if public_dns is not None:
            pulumi.set(__self__, "public_dns", public_dns)
        if public_network_access is not None:
            pulumi.set(__self__, "public_network_access", public_network_access)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if resource_name is not None:
            pulumi.set(__self__, "resource_name", resource_name)
        if secondary_app_id is not None:
            pulumi.set(__self__, "secondary_app_id", secondary_app_id)
        if system_data is not None:
            pulumi.set(__self__, "system_data", system_data)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[str]]:
        """
        The friendly string identifier of the creator of the NotebookProxy resource.
        """
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hostname", value)

    @property
    @pulumi.getter(name="publicDns")
    def public_dns(self) -> Optional[pulumi.Input[str]]:
        """
        The public DNS name
        """
        return pulumi.get(self, "public_dns")

    @public_dns.setter
    def public_dns(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_dns", value)

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[str]]:
        """
        Allow public network access on a V-Net locked notebook resource
        """
        return pulumi.get(self, "public_network_access")

    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_network_access", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region of the NotebookProxy resource.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter(name="secondaryAppId")
    def secondary_app_id(self) -> Optional[pulumi.Input[str]]:
        """
        The alternate application ID used for auth token request in the data plane
        """
        return pulumi.get(self, "secondary_app_id")

    @secondary_app_id.setter
    def secondary_app_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secondary_app_id", value)

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> Optional[pulumi.Input['NotebookResourceSystemDataArgs']]:
        """
        System data for notebook resource
        """
        return pulumi.get(self, "system_data")

    @system_data.setter
    def system_data(self, value: Optional[pulumi.Input['NotebookResourceSystemDataArgs']]):
        pulumi.set(self, "system_data", value)


class NotebookProxy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 public_dns: Optional[pulumi.Input[str]] = None,
                 public_network_access: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 secondary_app_id: Optional[pulumi.Input[str]] = None,
                 system_data: Optional[pulumi.Input[pulumi.InputType['NotebookResourceSystemDataArgs']]] = None,
                 __props__=None):
        """
        A NotebookProxy resource.
        API Version: 2019-10-11-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] hostname: The friendly string identifier of the creator of the NotebookProxy resource.
        :param pulumi.Input[str] public_dns: The public DNS name
        :param pulumi.Input[str] public_network_access: Allow public network access on a V-Net locked notebook resource
        :param pulumi.Input[str] region: The region of the NotebookProxy resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_name_: The name of the resource.
        :param pulumi.Input[str] secondary_app_id: The alternate application ID used for auth token request in the data plane
        :param pulumi.Input[pulumi.InputType['NotebookResourceSystemDataArgs']] system_data: System data for notebook resource
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NotebookProxyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A NotebookProxy resource.
        API Version: 2019-10-11-preview.

        :param str resource_name: The name of the resource.
        :param NotebookProxyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NotebookProxyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 public_dns: Optional[pulumi.Input[str]] = None,
                 public_network_access: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 secondary_app_id: Optional[pulumi.Input[str]] = None,
                 system_data: Optional[pulumi.Input[pulumi.InputType['NotebookResourceSystemDataArgs']]] = None,
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
            __props__ = NotebookProxyArgs.__new__(NotebookProxyArgs)

            __props__.__dict__["hostname"] = hostname
            __props__.__dict__["public_dns"] = public_dns
            __props__.__dict__["public_network_access"] = public_network_access
            __props__.__dict__["region"] = region
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["secondary_app_id"] = secondary_app_id
            __props__.__dict__["system_data"] = system_data
            __props__.__dict__["name"] = None
            __props__.__dict__["resource_id"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:notebooks/v20191011preview:NotebookProxy")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(NotebookProxy, __self__).__init__(
            'azure-native:notebooks:NotebookProxy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NotebookProxy':
        """
        Get an existing NotebookProxy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NotebookProxyArgs.__new__(NotebookProxyArgs)

        __props__.__dict__["hostname"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["public_dns"] = None
        __props__.__dict__["public_network_access"] = None
        __props__.__dict__["region"] = None
        __props__.__dict__["resource_id"] = None
        __props__.__dict__["secondary_app_id"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return NotebookProxy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def hostname(self) -> pulumi.Output[Optional[str]]:
        """
        The friendly string identifier of the creator of the NotebookProxy resource.
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="publicDns")
    def public_dns(self) -> pulumi.Output[Optional[str]]:
        """
        The public DNS name
        """
        return pulumi.get(self, "public_dns")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[str]]:
        """
        Allow public network access on a V-Net locked notebook resource
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[Optional[str]]:
        """
        The region of the NotebookProxy resource.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[str]:
        """
        The unique identifier (a GUID) generated for every resource.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="secondaryAppId")
    def secondary_app_id(self) -> pulumi.Output[Optional[str]]:
        """
        The alternate application ID used for auth token request in the data plane
        """
        return pulumi.get(self, "secondary_app_id")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[Optional['outputs.NotebookResourceSystemDataResponse']]:
        """
        System data for notebook resource
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. Ex- Microsoft.Storage/storageAccounts or Microsoft.Notebooks/notebookProxies.
        """
        return pulumi.get(self, "type")

