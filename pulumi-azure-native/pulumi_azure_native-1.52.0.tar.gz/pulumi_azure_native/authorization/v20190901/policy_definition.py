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

__all__ = ['PolicyDefinitionArgs', 'PolicyDefinition']

@pulumi.input_type
class PolicyDefinitionArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input['ParameterDefinitionsValueArgs']]]] = None,
                 policy_definition_name: Optional[pulumi.Input[str]] = None,
                 policy_rule: Optional[Any] = None,
                 policy_type: Optional[pulumi.Input[Union[str, 'PolicyType']]] = None):
        """
        The set of arguments for constructing a PolicyDefinition resource.
        :param pulumi.Input[str] description: The policy definition description.
        :param pulumi.Input[str] display_name: The display name of the policy definition.
        :param Any metadata: The policy definition metadata.  Metadata is an open ended object and is typically a collection of key value pairs.
        :param pulumi.Input[str] mode: The policy definition mode. Some examples are All, Indexed, Microsoft.KeyVault.Data.
        :param pulumi.Input[Mapping[str, pulumi.Input['ParameterDefinitionsValueArgs']]] parameters: The parameter definitions for parameters used in the policy rule. The keys are the parameter names.
        :param pulumi.Input[str] policy_definition_name: The name of the policy definition to create.
        :param Any policy_rule: The policy rule.
        :param pulumi.Input[Union[str, 'PolicyType']] policy_type: The type of policy definition. Possible values are NotSpecified, BuiltIn, Custom, and Static.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if mode is not None:
            pulumi.set(__self__, "mode", mode)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if policy_definition_name is not None:
            pulumi.set(__self__, "policy_definition_name", policy_definition_name)
        if policy_rule is not None:
            pulumi.set(__self__, "policy_rule", policy_rule)
        if policy_type is not None:
            pulumi.set(__self__, "policy_type", policy_type)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The policy definition description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of the policy definition.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        """
        The policy definition metadata.  Metadata is an open ended object and is typically a collection of key value pairs.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[Any]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[str]]:
        """
        The policy definition mode. Some examples are All, Indexed, Microsoft.KeyVault.Data.
        """
        return pulumi.get(self, "mode")

    @mode.setter
    def mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mode", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['ParameterDefinitionsValueArgs']]]]:
        """
        The parameter definitions for parameters used in the policy rule. The keys are the parameter names.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['ParameterDefinitionsValueArgs']]]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="policyDefinitionName")
    def policy_definition_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the policy definition to create.
        """
        return pulumi.get(self, "policy_definition_name")

    @policy_definition_name.setter
    def policy_definition_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_definition_name", value)

    @property
    @pulumi.getter(name="policyRule")
    def policy_rule(self) -> Optional[Any]:
        """
        The policy rule.
        """
        return pulumi.get(self, "policy_rule")

    @policy_rule.setter
    def policy_rule(self, value: Optional[Any]):
        pulumi.set(self, "policy_rule", value)

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[pulumi.Input[Union[str, 'PolicyType']]]:
        """
        The type of policy definition. Possible values are NotSpecified, BuiltIn, Custom, and Static.
        """
        return pulumi.get(self, "policy_type")

    @policy_type.setter
    def policy_type(self, value: Optional[pulumi.Input[Union[str, 'PolicyType']]]):
        pulumi.set(self, "policy_type", value)


class PolicyDefinition(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['ParameterDefinitionsValueArgs']]]]] = None,
                 policy_definition_name: Optional[pulumi.Input[str]] = None,
                 policy_rule: Optional[Any] = None,
                 policy_type: Optional[pulumi.Input[Union[str, 'PolicyType']]] = None,
                 __props__=None):
        """
        The policy definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The policy definition description.
        :param pulumi.Input[str] display_name: The display name of the policy definition.
        :param Any metadata: The policy definition metadata.  Metadata is an open ended object and is typically a collection of key value pairs.
        :param pulumi.Input[str] mode: The policy definition mode. Some examples are All, Indexed, Microsoft.KeyVault.Data.
        :param pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['ParameterDefinitionsValueArgs']]]] parameters: The parameter definitions for parameters used in the policy rule. The keys are the parameter names.
        :param pulumi.Input[str] policy_definition_name: The name of the policy definition to create.
        :param Any policy_rule: The policy rule.
        :param pulumi.Input[Union[str, 'PolicyType']] policy_type: The type of policy definition. Possible values are NotSpecified, BuiltIn, Custom, and Static.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[PolicyDefinitionArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The policy definition.

        :param str resource_name: The name of the resource.
        :param PolicyDefinitionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PolicyDefinitionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['ParameterDefinitionsValueArgs']]]]] = None,
                 policy_definition_name: Optional[pulumi.Input[str]] = None,
                 policy_rule: Optional[Any] = None,
                 policy_type: Optional[pulumi.Input[Union[str, 'PolicyType']]] = None,
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
            __props__ = PolicyDefinitionArgs.__new__(PolicyDefinitionArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["mode"] = mode
            __props__.__dict__["parameters"] = parameters
            __props__.__dict__["policy_definition_name"] = policy_definition_name
            __props__.__dict__["policy_rule"] = policy_rule
            __props__.__dict__["policy_type"] = policy_type
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:authorization:PolicyDefinition"), pulumi.Alias(type_="azure-native:authorization/v20151001preview:PolicyDefinition"), pulumi.Alias(type_="azure-native:authorization/v20160401:PolicyDefinition"), pulumi.Alias(type_="azure-native:authorization/v20161201:PolicyDefinition"), pulumi.Alias(type_="azure-native:authorization/v20180301:PolicyDefinition"), pulumi.Alias(type_="azure-native:authorization/v20180501:PolicyDefinition"), pulumi.Alias(type_="azure-native:authorization/v20190101:PolicyDefinition"), pulumi.Alias(type_="azure-native:authorization/v20190601:PolicyDefinition"), pulumi.Alias(type_="azure-native:authorization/v20200301:PolicyDefinition"), pulumi.Alias(type_="azure-native:authorization/v20200901:PolicyDefinition"), pulumi.Alias(type_="azure-native:authorization/v20210601:PolicyDefinition")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PolicyDefinition, __self__).__init__(
            'azure-native:authorization/v20190901:PolicyDefinition',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PolicyDefinition':
        """
        Get an existing PolicyDefinition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PolicyDefinitionArgs.__new__(PolicyDefinitionArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["metadata"] = None
        __props__.__dict__["mode"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["policy_rule"] = None
        __props__.__dict__["policy_type"] = None
        __props__.__dict__["type"] = None
        return PolicyDefinition(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The policy definition description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        The display name of the policy definition.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Any]]:
        """
        The policy definition metadata.  Metadata is an open ended object and is typically a collection of key value pairs.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def mode(self) -> pulumi.Output[Optional[str]]:
        """
        The policy definition mode. Some examples are All, Indexed, Microsoft.KeyVault.Data.
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the policy definition.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Mapping[str, 'outputs.ParameterDefinitionsValueResponse']]]:
        """
        The parameter definitions for parameters used in the policy rule. The keys are the parameter names.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="policyRule")
    def policy_rule(self) -> pulumi.Output[Optional[Any]]:
        """
        The policy rule.
        """
        return pulumi.get(self, "policy_rule")

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of policy definition. Possible values are NotSpecified, BuiltIn, Custom, and Static.
        """
        return pulumi.get(self, "policy_type")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource (Microsoft.Authorization/policyDefinitions).
        """
        return pulumi.get(self, "type")

