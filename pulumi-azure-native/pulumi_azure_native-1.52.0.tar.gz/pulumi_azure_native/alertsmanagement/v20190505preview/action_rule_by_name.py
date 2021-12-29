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

__all__ = ['ActionRuleByNameArgs', 'ActionRuleByName']

@pulumi.input_type
class ActionRuleByNameArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 action_rule_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['ActionGroupArgs', 'DiagnosticsArgs', 'SuppressionArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ActionRuleByName resource.
        :param pulumi.Input[str] resource_group_name: Resource group name where the resource is created.
        :param pulumi.Input[str] action_rule_name: The name of action rule that needs to be created/updated
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[Union['ActionGroupArgs', 'DiagnosticsArgs', 'SuppressionArgs']] properties: action rule properties
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if action_rule_name is not None:
            pulumi.set(__self__, "action_rule_name", action_rule_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Resource group name where the resource is created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="actionRuleName")
    def action_rule_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of action rule that needs to be created/updated
        """
        return pulumi.get(self, "action_rule_name")

    @action_rule_name.setter
    def action_rule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action_rule_name", value)

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
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Union['ActionGroupArgs', 'DiagnosticsArgs', 'SuppressionArgs']]]:
        """
        action rule properties
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Union['ActionGroupArgs', 'DiagnosticsArgs', 'SuppressionArgs']]]):
        pulumi.set(self, "properties", value)

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


class ActionRuleByName(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action_rule_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union[pulumi.InputType['ActionGroupArgs'], pulumi.InputType['DiagnosticsArgs'], pulumi.InputType['SuppressionArgs']]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Action rule object containing target scope, conditions and suppression logic

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action_rule_name: The name of action rule that needs to be created/updated
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[Union[pulumi.InputType['ActionGroupArgs'], pulumi.InputType['DiagnosticsArgs'], pulumi.InputType['SuppressionArgs']]] properties: action rule properties
        :param pulumi.Input[str] resource_group_name: Resource group name where the resource is created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ActionRuleByNameArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Action rule object containing target scope, conditions and suppression logic

        :param str resource_name: The name of the resource.
        :param ActionRuleByNameArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ActionRuleByNameArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action_rule_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union[pulumi.InputType['ActionGroupArgs'], pulumi.InputType['DiagnosticsArgs'], pulumi.InputType['SuppressionArgs']]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = ActionRuleByNameArgs.__new__(ActionRuleByNameArgs)

            __props__.__dict__["action_rule_name"] = action_rule_name
            __props__.__dict__["location"] = location
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:alertsmanagement:ActionRuleByName"), pulumi.Alias(type_="azure-native:alertsmanagement/v20181102privatepreview:ActionRuleByName"), pulumi.Alias(type_="azure-native:alertsmanagement/v20210808preview:ActionRuleByName")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ActionRuleByName, __self__).__init__(
            'azure-native:alertsmanagement/v20190505preview:ActionRuleByName',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ActionRuleByName':
        """
        Get an existing ActionRuleByName resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ActionRuleByNameArgs.__new__(ActionRuleByNameArgs)

        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return ActionRuleByName(resource_name, opts=opts, __props__=__props__)

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
        Azure resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Any]:
        """
        action rule properties
        """
        return pulumi.get(self, "properties")

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
        Azure resource type
        """
        return pulumi.get(self, "type")

