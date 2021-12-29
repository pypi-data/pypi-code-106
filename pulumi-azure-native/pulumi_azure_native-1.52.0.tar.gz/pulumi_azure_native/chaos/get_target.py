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
    'GetTargetResult',
    'AwaitableGetTargetResult',
    'get_target',
    'get_target_output',
]

@pulumi.output_type
class GetTargetResult:
    """
    Model that represents a Target resource.
    """
    def __init__(__self__, id=None, location=None, name=None, properties=None, system_data=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Location of the target resource.
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
    @pulumi.getter
    def properties(self) -> Any:
        """
        The properties of the target resource.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system metadata of the target resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetTargetResult(GetTargetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTargetResult(
            id=self.id,
            location=self.location,
            name=self.name,
            properties=self.properties,
            system_data=self.system_data,
            type=self.type)


def get_target(parent_provider_namespace: Optional[str] = None,
               parent_resource_name: Optional[str] = None,
               parent_resource_type: Optional[str] = None,
               resource_group_name: Optional[str] = None,
               target_name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTargetResult:
    """
    Model that represents a Target resource.
    API Version: 2021-09-15-preview.


    :param str parent_provider_namespace: String that represents a resource provider namespace.
    :param str parent_resource_name: String that represents a resource name.
    :param str parent_resource_type: String that represents a resource type.
    :param str resource_group_name: String that represents an Azure resource group.
    :param str target_name: String that represents a Target resource name.
    """
    __args__ = dict()
    __args__['parentProviderNamespace'] = parent_provider_namespace
    __args__['parentResourceName'] = parent_resource_name
    __args__['parentResourceType'] = parent_resource_type
    __args__['resourceGroupName'] = resource_group_name
    __args__['targetName'] = target_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:chaos:getTarget', __args__, opts=opts, typ=GetTargetResult).value

    return AwaitableGetTargetResult(
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        properties=__ret__.properties,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_target)
def get_target_output(parent_provider_namespace: Optional[pulumi.Input[str]] = None,
                      parent_resource_name: Optional[pulumi.Input[str]] = None,
                      parent_resource_type: Optional[pulumi.Input[str]] = None,
                      resource_group_name: Optional[pulumi.Input[str]] = None,
                      target_name: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTargetResult]:
    """
    Model that represents a Target resource.
    API Version: 2021-09-15-preview.


    :param str parent_provider_namespace: String that represents a resource provider namespace.
    :param str parent_resource_name: String that represents a resource name.
    :param str parent_resource_type: String that represents a resource type.
    :param str resource_group_name: String that represents an Azure resource group.
    :param str target_name: String that represents a Target resource name.
    """
    ...
