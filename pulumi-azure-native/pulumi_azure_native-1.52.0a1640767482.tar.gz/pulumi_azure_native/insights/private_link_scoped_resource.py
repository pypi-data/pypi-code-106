# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['PrivateLinkScopedResourceArgs', 'PrivateLinkScopedResource']

@pulumi.input_type
class PrivateLinkScopedResourceArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 scope_name: pulumi.Input[str],
                 linked_resource_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a PrivateLinkScopedResource resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] scope_name: The name of the Azure Monitor PrivateLinkScope resource.
        :param pulumi.Input[str] linked_resource_id: The resource id of the scoped Azure monitor resource.
        :param pulumi.Input[str] name: The name of the scoped resource object.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "scope_name", scope_name)
        if linked_resource_id is not None:
            pulumi.set(__self__, "linked_resource_id", linked_resource_id)
        if name is not None:
            pulumi.set(__self__, "name", name)

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
    @pulumi.getter(name="scopeName")
    def scope_name(self) -> pulumi.Input[str]:
        """
        The name of the Azure Monitor PrivateLinkScope resource.
        """
        return pulumi.get(self, "scope_name")

    @scope_name.setter
    def scope_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "scope_name", value)

    @property
    @pulumi.getter(name="linkedResourceId")
    def linked_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource id of the scoped Azure monitor resource.
        """
        return pulumi.get(self, "linked_resource_id")

    @linked_resource_id.setter
    def linked_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "linked_resource_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the scoped resource object.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class PrivateLinkScopedResource(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 linked_resource_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scope_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A private link scoped resource
        API Version: 2019-10-17-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] linked_resource_id: The resource id of the scoped Azure monitor resource.
        :param pulumi.Input[str] name: The name of the scoped resource object.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] scope_name: The name of the Azure Monitor PrivateLinkScope resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PrivateLinkScopedResourceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A private link scoped resource
        API Version: 2019-10-17-preview.

        :param str resource_name: The name of the resource.
        :param PrivateLinkScopedResourceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PrivateLinkScopedResourceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 linked_resource_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scope_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = PrivateLinkScopedResourceArgs.__new__(PrivateLinkScopedResourceArgs)

            __props__.__dict__["linked_resource_id"] = linked_resource_id
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if scope_name is None and not opts.urn:
                raise TypeError("Missing required property 'scope_name'")
            __props__.__dict__["scope_name"] = scope_name
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:insights/v20191017preview:PrivateLinkScopedResource"), pulumi.Alias(type_="azure-native:insights/v20210701preview:PrivateLinkScopedResource")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PrivateLinkScopedResource, __self__).__init__(
            'azure-native:insights:PrivateLinkScopedResource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PrivateLinkScopedResource':
        """
        Get an existing PrivateLinkScopedResource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PrivateLinkScopedResourceArgs.__new__(PrivateLinkScopedResourceArgs)

        __props__.__dict__["linked_resource_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["type"] = None
        return PrivateLinkScopedResource(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="linkedResourceId")
    def linked_resource_id(self) -> pulumi.Output[Optional[str]]:
        """
        The resource id of the scoped Azure monitor resource.
        """
        return pulumi.get(self, "linked_resource_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Azure resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        State of the private endpoint connection.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Azure resource type
        """
        return pulumi.get(self, "type")

