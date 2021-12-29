# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['CustomResourceProviderArgs', 'CustomResourceProvider']

@pulumi.input_type
class CustomResourceProviderArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input['CustomRPActionRouteDefinitionArgs']]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_provider_name: Optional[pulumi.Input[str]] = None,
                 resource_types: Optional[pulumi.Input[Sequence[pulumi.Input['CustomRPResourceTypeRouteDefinitionArgs']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 validations: Optional[pulumi.Input[Sequence[pulumi.Input['CustomRPValidationsArgs']]]] = None):
        """
        The set of arguments for constructing a CustomResourceProvider resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Sequence[pulumi.Input['CustomRPActionRouteDefinitionArgs']]] actions: A list of actions that the custom resource provider implements.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] resource_provider_name: The name of the resource provider.
        :param pulumi.Input[Sequence[pulumi.Input['CustomRPResourceTypeRouteDefinitionArgs']]] resource_types: A list of resource types that the custom resource provider implements.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[Sequence[pulumi.Input['CustomRPValidationsArgs']]] validations: A list of validations to run on the custom resource provider's requests.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if actions is not None:
            pulumi.set(__self__, "actions", actions)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if resource_provider_name is not None:
            pulumi.set(__self__, "resource_provider_name", resource_provider_name)
        if resource_types is not None:
            pulumi.set(__self__, "resource_types", resource_types)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if validations is not None:
            pulumi.set(__self__, "validations", validations)

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
    def actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CustomRPActionRouteDefinitionArgs']]]]:
        """
        A list of actions that the custom resource provider implements.
        """
        return pulumi.get(self, "actions")

    @actions.setter
    def actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CustomRPActionRouteDefinitionArgs']]]]):
        pulumi.set(self, "actions", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="resourceProviderName")
    def resource_provider_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource provider.
        """
        return pulumi.get(self, "resource_provider_name")

    @resource_provider_name.setter
    def resource_provider_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_provider_name", value)

    @property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CustomRPResourceTypeRouteDefinitionArgs']]]]:
        """
        A list of resource types that the custom resource provider implements.
        """
        return pulumi.get(self, "resource_types")

    @resource_types.setter
    def resource_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CustomRPResourceTypeRouteDefinitionArgs']]]]):
        pulumi.set(self, "resource_types", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def validations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CustomRPValidationsArgs']]]]:
        """
        A list of validations to run on the custom resource provider's requests.
        """
        return pulumi.get(self, "validations")

    @validations.setter
    def validations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CustomRPValidationsArgs']]]]):
        pulumi.set(self, "validations", value)


class CustomResourceProvider(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomRPActionRouteDefinitionArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_provider_name: Optional[pulumi.Input[str]] = None,
                 resource_types: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomRPResourceTypeRouteDefinitionArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 validations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomRPValidationsArgs']]]]] = None,
                 __props__=None):
        """
        A manifest file that defines the custom resource provider resources.
        API Version: 2018-09-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomRPActionRouteDefinitionArgs']]]] actions: A list of actions that the custom resource provider implements.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] resource_provider_name: The name of the resource provider.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomRPResourceTypeRouteDefinitionArgs']]]] resource_types: A list of resource types that the custom resource provider implements.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomRPValidationsArgs']]]] validations: A list of validations to run on the custom resource provider's requests.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CustomResourceProviderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A manifest file that defines the custom resource provider resources.
        API Version: 2018-09-01-preview.

        :param str resource_name: The name of the resource.
        :param CustomResourceProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CustomResourceProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomRPActionRouteDefinitionArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_provider_name: Optional[pulumi.Input[str]] = None,
                 resource_types: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomRPResourceTypeRouteDefinitionArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 validations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomRPValidationsArgs']]]]] = None,
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
            __props__ = CustomResourceProviderArgs.__new__(CustomResourceProviderArgs)

            __props__.__dict__["actions"] = actions
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_provider_name"] = resource_provider_name
            __props__.__dict__["resource_types"] = resource_types
            __props__.__dict__["tags"] = tags
            __props__.__dict__["validations"] = validations
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:customproviders/v20180901preview:CustomResourceProvider")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(CustomResourceProvider, __self__).__init__(
            'azure-native:customproviders:CustomResourceProvider',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CustomResourceProvider':
        """
        Get an existing CustomResourceProvider resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CustomResourceProviderArgs.__new__(CustomResourceProviderArgs)

        __props__.__dict__["actions"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resource_types"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["validations"] = None
        return CustomResourceProvider(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Output[Optional[Sequence['outputs.CustomRPActionRouteDefinitionResponse']]]:
        """
        A list of actions that the custom resource provider implements.
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the resource provider.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> pulumi.Output[Optional[Sequence['outputs.CustomRPResourceTypeRouteDefinitionResponse']]]:
        """
        A list of resource types that the custom resource provider implements.
        """
        return pulumi.get(self, "resource_types")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def validations(self) -> pulumi.Output[Optional[Sequence['outputs.CustomRPValidationsResponse']]]:
        """
        A list of validations to run on the custom resource provider's requests.
        """
        return pulumi.get(self, "validations")

