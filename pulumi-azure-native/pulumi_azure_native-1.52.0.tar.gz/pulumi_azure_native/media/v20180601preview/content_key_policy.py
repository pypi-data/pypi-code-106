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

__all__ = ['ContentKeyPolicyArgs', 'ContentKeyPolicy']

@pulumi.input_type
class ContentKeyPolicyArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 options: pulumi.Input[Sequence[pulumi.Input['ContentKeyPolicyOptionArgs']]],
                 resource_group_name: pulumi.Input[str],
                 content_key_policy_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ContentKeyPolicy resource.
        :param pulumi.Input[str] account_name: The Media Services account name.
        :param pulumi.Input[Sequence[pulumi.Input['ContentKeyPolicyOptionArgs']]] options: The Key Policy options.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the Azure subscription.
        :param pulumi.Input[str] content_key_policy_name: The Content Key Policy name.
        :param pulumi.Input[str] description: A description for the Policy.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "options", options)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if content_key_policy_name is not None:
            pulumi.set(__self__, "content_key_policy_name", content_key_policy_name)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        The Media Services account name.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter
    def options(self) -> pulumi.Input[Sequence[pulumi.Input['ContentKeyPolicyOptionArgs']]]:
        """
        The Key Policy options.
        """
        return pulumi.get(self, "options")

    @options.setter
    def options(self, value: pulumi.Input[Sequence[pulumi.Input['ContentKeyPolicyOptionArgs']]]):
        pulumi.set(self, "options", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group within the Azure subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="contentKeyPolicyName")
    def content_key_policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Content Key Policy name.
        """
        return pulumi.get(self, "content_key_policy_name")

    @content_key_policy_name.setter
    def content_key_policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content_key_policy_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for the Policy.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


class ContentKeyPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 content_key_policy_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContentKeyPolicyOptionArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A Content Key Policy resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The Media Services account name.
        :param pulumi.Input[str] content_key_policy_name: The Content Key Policy name.
        :param pulumi.Input[str] description: A description for the Policy.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContentKeyPolicyOptionArgs']]]] options: The Key Policy options.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the Azure subscription.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ContentKeyPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A Content Key Policy resource.

        :param str resource_name: The name of the resource.
        :param ContentKeyPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ContentKeyPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 content_key_policy_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContentKeyPolicyOptionArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = ContentKeyPolicyArgs.__new__(ContentKeyPolicyArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["content_key_policy_name"] = content_key_policy_name
            __props__.__dict__["description"] = description
            if options is None and not opts.urn:
                raise TypeError("Missing required property 'options'")
            __props__.__dict__["options"] = options
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["created"] = None
            __props__.__dict__["last_modified"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["policy_id"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:media:ContentKeyPolicy"), pulumi.Alias(type_="azure-native:media/v20180330preview:ContentKeyPolicy"), pulumi.Alias(type_="azure-native:media/v20180701:ContentKeyPolicy"), pulumi.Alias(type_="azure-native:media/v20200501:ContentKeyPolicy"), pulumi.Alias(type_="azure-native:media/v20210601:ContentKeyPolicy")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ContentKeyPolicy, __self__).__init__(
            'azure-native:media/v20180601preview:ContentKeyPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ContentKeyPolicy':
        """
        Get an existing ContentKeyPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ContentKeyPolicyArgs.__new__(ContentKeyPolicyArgs)

        __props__.__dict__["created"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["last_modified"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["options"] = None
        __props__.__dict__["policy_id"] = None
        __props__.__dict__["type"] = None
        return ContentKeyPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def created(self) -> pulumi.Output[str]:
        """
        The creation date of the Policy
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description for the Policy.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> pulumi.Output[str]:
        """
        The last modified date of the Policy
        """
        return pulumi.get(self, "last_modified")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def options(self) -> pulumi.Output[Sequence['outputs.ContentKeyPolicyOptionResponse']]:
        """
        The Key Policy options.
        """
        return pulumi.get(self, "options")

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Output[str]:
        """
        The legacy Policy ID.
        """
        return pulumi.get(self, "policy_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

