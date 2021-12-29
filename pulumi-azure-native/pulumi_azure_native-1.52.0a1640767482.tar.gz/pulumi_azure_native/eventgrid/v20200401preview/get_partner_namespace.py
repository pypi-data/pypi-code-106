# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetPartnerNamespaceResult',
    'AwaitableGetPartnerNamespaceResult',
    'get_partner_namespace',
    'get_partner_namespace_output',
]

@pulumi.output_type
class GetPartnerNamespaceResult:
    """
    EventGrid Partner Namespace.
    """
    def __init__(__self__, endpoint=None, id=None, location=None, name=None, partner_registration_fully_qualified_id=None, provisioning_state=None, system_data=None, tags=None, type=None):
        if endpoint and not isinstance(endpoint, str):
            raise TypeError("Expected argument 'endpoint' to be a str")
        pulumi.set(__self__, "endpoint", endpoint)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if partner_registration_fully_qualified_id and not isinstance(partner_registration_fully_qualified_id, str):
            raise TypeError("Expected argument 'partner_registration_fully_qualified_id' to be a str")
        pulumi.set(__self__, "partner_registration_fully_qualified_id", partner_registration_fully_qualified_id)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def endpoint(self) -> str:
        """
        Endpoint for the partner namespace.
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified identifier of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partnerRegistrationFullyQualifiedId")
    def partner_registration_fully_qualified_id(self) -> Optional[str]:
        """
        The fully qualified ARM Id of the partner registration that should be associated with this partner namespace. This takes the following format:
        /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerRegistrations/{partnerRegistrationName}.
        """
        return pulumi.get(self, "partner_registration_fully_qualified_id")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the partner namespace.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system metadata relating to Partner Namespace resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetPartnerNamespaceResult(GetPartnerNamespaceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPartnerNamespaceResult(
            endpoint=self.endpoint,
            id=self.id,
            location=self.location,
            name=self.name,
            partner_registration_fully_qualified_id=self.partner_registration_fully_qualified_id,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_partner_namespace(partner_namespace_name: Optional[str] = None,
                          resource_group_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPartnerNamespaceResult:
    """
    EventGrid Partner Namespace.


    :param str partner_namespace_name: Name of the partner namespace.
    :param str resource_group_name: The name of the resource group within the user's subscription.
    """
    __args__ = dict()
    __args__['partnerNamespaceName'] = partner_namespace_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:eventgrid/v20200401preview:getPartnerNamespace', __args__, opts=opts, typ=GetPartnerNamespaceResult).value

    return AwaitableGetPartnerNamespaceResult(
        endpoint=__ret__.endpoint,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        partner_registration_fully_qualified_id=__ret__.partner_registration_fully_qualified_id,
        provisioning_state=__ret__.provisioning_state,
        system_data=__ret__.system_data,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_partner_namespace)
def get_partner_namespace_output(partner_namespace_name: Optional[pulumi.Input[str]] = None,
                                 resource_group_name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPartnerNamespaceResult]:
    """
    EventGrid Partner Namespace.


    :param str partner_namespace_name: Name of the partner namespace.
    :param str resource_group_name: The name of the resource group within the user's subscription.
    """
    ...
