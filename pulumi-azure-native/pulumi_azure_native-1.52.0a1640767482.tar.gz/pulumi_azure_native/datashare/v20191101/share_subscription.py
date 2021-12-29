# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['ShareSubscriptionArgs', 'ShareSubscription']

@pulumi.input_type
class ShareSubscriptionArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 invitation_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 source_share_location: pulumi.Input[str],
                 share_subscription_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ShareSubscription resource.
        :param pulumi.Input[str] account_name: The name of the share account.
        :param pulumi.Input[str] invitation_id: The invitation id.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] source_share_location: Source share location.
        :param pulumi.Input[str] share_subscription_name: The name of the shareSubscription.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "invitation_id", invitation_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "source_share_location", source_share_location)
        if share_subscription_name is not None:
            pulumi.set(__self__, "share_subscription_name", share_subscription_name)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        The name of the share account.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="invitationId")
    def invitation_id(self) -> pulumi.Input[str]:
        """
        The invitation id.
        """
        return pulumi.get(self, "invitation_id")

    @invitation_id.setter
    def invitation_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "invitation_id", value)

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
    @pulumi.getter(name="sourceShareLocation")
    def source_share_location(self) -> pulumi.Input[str]:
        """
        Source share location.
        """
        return pulumi.get(self, "source_share_location")

    @source_share_location.setter
    def source_share_location(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_share_location", value)

    @property
    @pulumi.getter(name="shareSubscriptionName")
    def share_subscription_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the shareSubscription.
        """
        return pulumi.get(self, "share_subscription_name")

    @share_subscription_name.setter
    def share_subscription_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "share_subscription_name", value)


class ShareSubscription(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 invitation_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 share_subscription_name: Optional[pulumi.Input[str]] = None,
                 source_share_location: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A share subscription data transfer object.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the share account.
        :param pulumi.Input[str] invitation_id: The invitation id.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] share_subscription_name: The name of the shareSubscription.
        :param pulumi.Input[str] source_share_location: Source share location.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ShareSubscriptionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A share subscription data transfer object.

        :param str resource_name: The name of the resource.
        :param ShareSubscriptionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ShareSubscriptionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 invitation_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 share_subscription_name: Optional[pulumi.Input[str]] = None,
                 source_share_location: Optional[pulumi.Input[str]] = None,
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
            __props__ = ShareSubscriptionArgs.__new__(ShareSubscriptionArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            if invitation_id is None and not opts.urn:
                raise TypeError("Missing required property 'invitation_id'")
            __props__.__dict__["invitation_id"] = invitation_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["share_subscription_name"] = share_subscription_name
            if source_share_location is None and not opts.urn:
                raise TypeError("Missing required property 'source_share_location'")
            __props__.__dict__["source_share_location"] = source_share_location
            __props__.__dict__["created_at"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provider_email"] = None
            __props__.__dict__["provider_name"] = None
            __props__.__dict__["provider_tenant_name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["share_description"] = None
            __props__.__dict__["share_kind"] = None
            __props__.__dict__["share_name"] = None
            __props__.__dict__["share_subscription_status"] = None
            __props__.__dict__["share_terms"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["user_email"] = None
            __props__.__dict__["user_name"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:datashare:ShareSubscription"), pulumi.Alias(type_="azure-native:datashare/v20181101preview:ShareSubscription"), pulumi.Alias(type_="azure-native:datashare/v20200901:ShareSubscription"), pulumi.Alias(type_="azure-native:datashare/v20201001preview:ShareSubscription"), pulumi.Alias(type_="azure-native:datashare/v20210801:ShareSubscription")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ShareSubscription, __self__).__init__(
            'azure-native:datashare/v20191101:ShareSubscription',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ShareSubscription':
        """
        Get an existing ShareSubscription resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ShareSubscriptionArgs.__new__(ShareSubscriptionArgs)

        __props__.__dict__["created_at"] = None
        __props__.__dict__["invitation_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provider_email"] = None
        __props__.__dict__["provider_name"] = None
        __props__.__dict__["provider_tenant_name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["share_description"] = None
        __props__.__dict__["share_kind"] = None
        __props__.__dict__["share_name"] = None
        __props__.__dict__["share_subscription_status"] = None
        __props__.__dict__["share_terms"] = None
        __props__.__dict__["source_share_location"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["user_email"] = None
        __props__.__dict__["user_name"] = None
        return ShareSubscription(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Time at which the share subscription was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="invitationId")
    def invitation_id(self) -> pulumi.Output[str]:
        """
        The invitation id.
        """
        return pulumi.get(self, "invitation_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the azure resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="providerEmail")
    def provider_email(self) -> pulumi.Output[str]:
        """
        Email of the provider who created the resource
        """
        return pulumi.get(self, "provider_email")

    @property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> pulumi.Output[str]:
        """
        Name of the provider who created the resource
        """
        return pulumi.get(self, "provider_name")

    @property
    @pulumi.getter(name="providerTenantName")
    def provider_tenant_name(self) -> pulumi.Output[str]:
        """
        Tenant name of the provider who created the resource
        """
        return pulumi.get(self, "provider_tenant_name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the share subscription
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="shareDescription")
    def share_description(self) -> pulumi.Output[str]:
        """
        Description of share
        """
        return pulumi.get(self, "share_description")

    @property
    @pulumi.getter(name="shareKind")
    def share_kind(self) -> pulumi.Output[str]:
        """
        Kind of share
        """
        return pulumi.get(self, "share_kind")

    @property
    @pulumi.getter(name="shareName")
    def share_name(self) -> pulumi.Output[str]:
        """
        Name of the share
        """
        return pulumi.get(self, "share_name")

    @property
    @pulumi.getter(name="shareSubscriptionStatus")
    def share_subscription_status(self) -> pulumi.Output[str]:
        """
        Gets the current status of share subscription.
        """
        return pulumi.get(self, "share_subscription_status")

    @property
    @pulumi.getter(name="shareTerms")
    def share_terms(self) -> pulumi.Output[str]:
        """
        Terms of a share
        """
        return pulumi.get(self, "share_terms")

    @property
    @pulumi.getter(name="sourceShareLocation")
    def source_share_location(self) -> pulumi.Output[str]:
        """
        Source share location.
        """
        return pulumi.get(self, "source_share_location")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the azure resource
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userEmail")
    def user_email(self) -> pulumi.Output[str]:
        """
        Email of the user who created the resource
        """
        return pulumi.get(self, "user_email")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Output[str]:
        """
        Name of the user who created the resource
        """
        return pulumi.get(self, "user_name")

