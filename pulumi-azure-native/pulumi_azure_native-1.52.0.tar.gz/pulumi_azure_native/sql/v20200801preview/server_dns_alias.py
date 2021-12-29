# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['ServerDnsAliasArgs', 'ServerDnsAlias']

@pulumi.input_type
class ServerDnsAliasArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 server_name: pulumi.Input[str],
                 dns_alias_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ServerDnsAlias resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] server_name: The name of the server that the alias is pointing to.
        :param pulumi.Input[str] dns_alias_name: The name of the server dns alias.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "server_name", server_name)
        if dns_alias_name is not None:
            pulumi.set(__self__, "dns_alias_name", dns_alias_name)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[str]:
        """
        The name of the server that the alias is pointing to.
        """
        return pulumi.get(self, "server_name")

    @server_name.setter
    def server_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "server_name", value)

    @property
    @pulumi.getter(name="dnsAliasName")
    def dns_alias_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the server dns alias.
        """
        return pulumi.get(self, "dns_alias_name")

    @dns_alias_name.setter
    def dns_alias_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dns_alias_name", value)


class ServerDnsAlias(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dns_alias_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A server DNS alias.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dns_alias_name: The name of the server dns alias.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] server_name: The name of the server that the alias is pointing to.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServerDnsAliasArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A server DNS alias.

        :param str resource_name: The name of the resource.
        :param ServerDnsAliasArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServerDnsAliasArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dns_alias_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = ServerDnsAliasArgs.__new__(ServerDnsAliasArgs)

            __props__.__dict__["dns_alias_name"] = dns_alias_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if server_name is None and not opts.urn:
                raise TypeError("Missing required property 'server_name'")
            __props__.__dict__["server_name"] = server_name
            __props__.__dict__["azure_dns_record"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:sql:ServerDnsAlias"), pulumi.Alias(type_="azure-native:sql/v20170301preview:ServerDnsAlias"), pulumi.Alias(type_="azure-native:sql/v20200202preview:ServerDnsAlias"), pulumi.Alias(type_="azure-native:sql/v20201101preview:ServerDnsAlias"), pulumi.Alias(type_="azure-native:sql/v20210201preview:ServerDnsAlias"), pulumi.Alias(type_="azure-native:sql/v20210501preview:ServerDnsAlias"), pulumi.Alias(type_="azure-native:sql/v20210801preview:ServerDnsAlias")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ServerDnsAlias, __self__).__init__(
            'azure-native:sql/v20200801preview:ServerDnsAlias',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ServerDnsAlias':
        """
        Get an existing ServerDnsAlias resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServerDnsAliasArgs.__new__(ServerDnsAliasArgs)

        __props__.__dict__["azure_dns_record"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        return ServerDnsAlias(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="azureDnsRecord")
    def azure_dns_record(self) -> pulumi.Output[str]:
        """
        The fully qualified DNS record for alias
        """
        return pulumi.get(self, "azure_dns_record")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

