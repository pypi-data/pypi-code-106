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

__all__ = ['SaasSubscriptionLevelArgs', 'SaasSubscriptionLevel']

@pulumi.input_type
class SaasSubscriptionLevelArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input['SaasCreationPropertiesArgs']] = None,
                 resource_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a SaasSubscriptionLevel resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] location: Resource location. Only value allowed for SaaS is 'global'
        :param pulumi.Input[str] name: The resource name
        :param pulumi.Input['SaasCreationPropertiesArgs'] properties: Properties of the SaaS resource that are relevant for creation.
        :param pulumi.Input[str] resource_name: The name of the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: the resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if resource_name is not None:
            pulumi.set(__self__, "resource_name", resource_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location. Only value allowed for SaaS is 'global'
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The resource name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['SaasCreationPropertiesArgs']]:
        """
        Properties of the SaaS resource that are relevant for creation.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['SaasCreationPropertiesArgs']]):
        pulumi.set(self, "properties", value)

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
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        the resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class SaasSubscriptionLevel(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['SaasCreationPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        SaaS REST API resource definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: Resource location. Only value allowed for SaaS is 'global'
        :param pulumi.Input[str] name: The resource name
        :param pulumi.Input[pulumi.InputType['SaasCreationPropertiesArgs']] properties: Properties of the SaaS resource that are relevant for creation.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] resource_name_: The name of the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: the resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SaasSubscriptionLevelArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        SaaS REST API resource definition.

        :param str resource_name: The name of the resource.
        :param SaasSubscriptionLevelArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SaasSubscriptionLevelArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['SaasCreationPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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
            __props__ = SaasSubscriptionLevelArgs.__new__(SaasSubscriptionLevelArgs)

            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["tags"] = tags
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:saas:SaasSubscriptionLevel")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SaasSubscriptionLevel, __self__).__init__(
            'azure-native:saas/v20180301beta:SaasSubscriptionLevel',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SaasSubscriptionLevel':
        """
        Get an existing SaasSubscriptionLevel resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SaasSubscriptionLevelArgs.__new__(SaasSubscriptionLevelArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return SaasSubscriptionLevel(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.SaasResourceResponseProperties']:
        """
        saas properties
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        the resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

