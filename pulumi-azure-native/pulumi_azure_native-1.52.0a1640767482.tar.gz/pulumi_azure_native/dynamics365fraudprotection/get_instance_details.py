# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetInstanceDetailsResult',
    'AwaitableGetInstanceDetailsResult',
    'get_instance_details',
    'get_instance_details_output',
]

@pulumi.output_type
class GetInstanceDetailsResult:
    """
    Represents an instance of a DFP instance resource.
    """
    def __init__(__self__, administration=None, id=None, location=None, name=None, provisioning_state=None, system_data=None, tags=None, type=None):
        if administration and not isinstance(administration, dict):
            raise TypeError("Expected argument 'administration' to be a dict")
        pulumi.set(__self__, "administration", administration)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
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
    def administration(self) -> Optional['outputs.DFPInstanceAdministratorsResponse']:
        """
        A collection of DFP instance administrators
        """
        return pulumi.get(self, "administration")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Location of the DFP resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The current deployment state of DFP resource. The provisioningState is to indicate states for resource provisioning.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Key-value pairs of additional resource provisioning properties.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetInstanceDetailsResult(GetInstanceDetailsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstanceDetailsResult(
            administration=self.administration,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_instance_details(instance_name: Optional[str] = None,
                         resource_group_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstanceDetailsResult:
    """
    Represents an instance of a DFP instance resource.
    API Version: 2021-02-01-preview.


    :param str instance_name: The name of the instance. It must be a minimum of 3 characters, and a maximum of 63.
    :param str resource_group_name: The name of the Azure Resource group of which a given DFP instance is part. This name must be at least 1 character in length, and no more than 90.
    """
    __args__ = dict()
    __args__['instanceName'] = instance_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:dynamics365fraudprotection:getInstanceDetails', __args__, opts=opts, typ=GetInstanceDetailsResult).value

    return AwaitableGetInstanceDetailsResult(
        administration=__ret__.administration,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        system_data=__ret__.system_data,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_instance_details)
def get_instance_details_output(instance_name: Optional[pulumi.Input[str]] = None,
                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstanceDetailsResult]:
    """
    Represents an instance of a DFP instance resource.
    API Version: 2021-02-01-preview.


    :param str instance_name: The name of the instance. It must be a minimum of 3 characters, and a maximum of 63.
    :param str resource_group_name: The name of the Azure Resource group of which a given DFP instance is part. This name must be at least 1 character in length, and no more than 90.
    """
    ...
