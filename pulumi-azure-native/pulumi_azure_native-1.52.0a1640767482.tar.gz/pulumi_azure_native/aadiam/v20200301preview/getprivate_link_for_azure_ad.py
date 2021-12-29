# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetprivateLinkForAzureAdResult',
    'AwaitableGetprivateLinkForAzureAdResult',
    'getprivate_link_for_azure_ad',
    'getprivate_link_for_azure_ad_output',
]

@pulumi.output_type
class GetprivateLinkForAzureAdResult:
    """
    PrivateLink Policy configuration object.
    """
    def __init__(__self__, all_tenants=None, id=None, name=None, owner_tenant_id=None, resource_group=None, resource_name=None, subscription_id=None, tags=None, tenants=None, type=None):
        if all_tenants and not isinstance(all_tenants, bool):
            raise TypeError("Expected argument 'all_tenants' to be a bool")
        pulumi.set(__self__, "all_tenants", all_tenants)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if owner_tenant_id and not isinstance(owner_tenant_id, str):
            raise TypeError("Expected argument 'owner_tenant_id' to be a str")
        pulumi.set(__self__, "owner_tenant_id", owner_tenant_id)
        if resource_group and not isinstance(resource_group, str):
            raise TypeError("Expected argument 'resource_group' to be a str")
        pulumi.set(__self__, "resource_group", resource_group)
        if resource_name and not isinstance(resource_name, str):
            raise TypeError("Expected argument 'resource_name' to be a str")
        pulumi.set(__self__, "resource_name", resource_name)
        if subscription_id and not isinstance(subscription_id, str):
            raise TypeError("Expected argument 'subscription_id' to be a str")
        pulumi.set(__self__, "subscription_id", subscription_id)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if tenants and not isinstance(tenants, list):
            raise TypeError("Expected argument 'tenants' to be a list")
        pulumi.set(__self__, "tenants", tenants)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="allTenants")
    def all_tenants(self) -> Optional[bool]:
        """
        Flag indicating whether all tenants are allowed
        """
        return pulumi.get(self, "all_tenants")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        String Id used to locate any resource on Azure.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of this resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="ownerTenantId")
    def owner_tenant_id(self) -> Optional[str]:
        """
        Guid of the owner tenant
        """
        return pulumi.get(self, "owner_tenant_id")

    @property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[str]:
        """
        Name of the resource group
        """
        return pulumi.get(self, "resource_group")

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[str]:
        """
        Name of the private link policy resource
        """
        return pulumi.get(self, "resource_name")

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[str]:
        """
        Subscription Identifier
        """
        return pulumi.get(self, "subscription_id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def tenants(self) -> Optional[Sequence[str]]:
        """
        The list of tenantIds.
        """
        return pulumi.get(self, "tenants")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of this resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetprivateLinkForAzureAdResult(GetprivateLinkForAzureAdResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetprivateLinkForAzureAdResult(
            all_tenants=self.all_tenants,
            id=self.id,
            name=self.name,
            owner_tenant_id=self.owner_tenant_id,
            resource_group=self.resource_group,
            resource_name=self.resource_name,
            subscription_id=self.subscription_id,
            tags=self.tags,
            tenants=self.tenants,
            type=self.type)


def getprivate_link_for_azure_ad(policy_name: Optional[str] = None,
                                 resource_group_name: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetprivateLinkForAzureAdResult:
    """
    PrivateLink Policy configuration object.


    :param str policy_name: The name of the private link policy in Azure AD.
    :param str resource_group_name: Name of an Azure resource group.
    """
    __args__ = dict()
    __args__['policyName'] = policy_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:aadiam/v20200301preview:getprivateLinkForAzureAd', __args__, opts=opts, typ=GetprivateLinkForAzureAdResult).value

    return AwaitableGetprivateLinkForAzureAdResult(
        all_tenants=__ret__.all_tenants,
        id=__ret__.id,
        name=__ret__.name,
        owner_tenant_id=__ret__.owner_tenant_id,
        resource_group=__ret__.resource_group,
        resource_name=__ret__.resource_name,
        subscription_id=__ret__.subscription_id,
        tags=__ret__.tags,
        tenants=__ret__.tenants,
        type=__ret__.type)


@_utilities.lift_output_func(getprivate_link_for_azure_ad)
def getprivate_link_for_azure_ad_output(policy_name: Optional[pulumi.Input[str]] = None,
                                        resource_group_name: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetprivateLinkForAzureAdResult]:
    """
    PrivateLink Policy configuration object.


    :param str policy_name: The name of the private link policy in Azure AD.
    :param str resource_group_name: Name of an Azure resource group.
    """
    ...
