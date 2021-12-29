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
    'GetIotDpsResourcePrivateEndpointConnectionResult',
    'AwaitableGetIotDpsResourcePrivateEndpointConnectionResult',
    'get_iot_dps_resource_private_endpoint_connection',
    'get_iot_dps_resource_private_endpoint_connection_output',
]

@pulumi.output_type
class GetIotDpsResourcePrivateEndpointConnectionResult:
    """
    The private endpoint connection of a provisioning service
    """
    def __init__(__self__, id=None, name=None, properties=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource identifier.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.PrivateEndpointConnectionPropertiesResponse':
        """
        The properties of a private endpoint connection
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetIotDpsResourcePrivateEndpointConnectionResult(GetIotDpsResourcePrivateEndpointConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIotDpsResourcePrivateEndpointConnectionResult(
            id=self.id,
            name=self.name,
            properties=self.properties,
            type=self.type)


def get_iot_dps_resource_private_endpoint_connection(private_endpoint_connection_name: Optional[str] = None,
                                                     resource_group_name: Optional[str] = None,
                                                     resource_name: Optional[str] = None,
                                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIotDpsResourcePrivateEndpointConnectionResult:
    """
    The private endpoint connection of a provisioning service


    :param str private_endpoint_connection_name: The name of the private endpoint connection
    :param str resource_group_name: The name of the resource group that contains the provisioning service.
    :param str resource_name: The name of the provisioning service.
    """
    __args__ = dict()
    __args__['privateEndpointConnectionName'] = private_endpoint_connection_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:devices/v20200301:getIotDpsResourcePrivateEndpointConnection', __args__, opts=opts, typ=GetIotDpsResourcePrivateEndpointConnectionResult).value

    return AwaitableGetIotDpsResourcePrivateEndpointConnectionResult(
        id=__ret__.id,
        name=__ret__.name,
        properties=__ret__.properties,
        type=__ret__.type)


@_utilities.lift_output_func(get_iot_dps_resource_private_endpoint_connection)
def get_iot_dps_resource_private_endpoint_connection_output(private_endpoint_connection_name: Optional[pulumi.Input[str]] = None,
                                                            resource_group_name: Optional[pulumi.Input[str]] = None,
                                                            resource_name: Optional[pulumi.Input[str]] = None,
                                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIotDpsResourcePrivateEndpointConnectionResult]:
    """
    The private endpoint connection of a provisioning service


    :param str private_endpoint_connection_name: The name of the private endpoint connection
    :param str resource_group_name: The name of the resource group that contains the provisioning service.
    :param str resource_name: The name of the provisioning service.
    """
    ...
