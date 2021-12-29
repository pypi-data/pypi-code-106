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
    'GetCloudEdgeManagementRoleResult',
    'AwaitableGetCloudEdgeManagementRoleResult',
    'get_cloud_edge_management_role',
    'get_cloud_edge_management_role_output',
]

@pulumi.output_type
class GetCloudEdgeManagementRoleResult:
    """
    CloudEdgeManagementRole role.
    """
    def __init__(__self__, edge_profile=None, id=None, kind=None, local_management_status=None, name=None, role_status=None, system_data=None, type=None):
        if edge_profile and not isinstance(edge_profile, dict):
            raise TypeError("Expected argument 'edge_profile' to be a dict")
        pulumi.set(__self__, "edge_profile", edge_profile)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if local_management_status and not isinstance(local_management_status, str):
            raise TypeError("Expected argument 'local_management_status' to be a str")
        pulumi.set(__self__, "local_management_status", local_management_status)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if role_status and not isinstance(role_status, str):
            raise TypeError("Expected argument 'role_status' to be a str")
        pulumi.set(__self__, "role_status", role_status)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="edgeProfile")
    def edge_profile(self) -> 'outputs.EdgeProfileResponse':
        """
        Edge Profile of the resource
        """
        return pulumi.get(self, "edge_profile")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The path ID that uniquely identifies the object.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Role type.
        Expected value is 'CloudEdgeManagement'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="localManagementStatus")
    def local_management_status(self) -> str:
        """
        Local Edge Management Status
        """
        return pulumi.get(self, "local_management_status")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The object name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="roleStatus")
    def role_status(self) -> str:
        """
        Role status.
        """
        return pulumi.get(self, "role_status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Role configured on ASE resource
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The hierarchical type of the object.
        """
        return pulumi.get(self, "type")


class AwaitableGetCloudEdgeManagementRoleResult(GetCloudEdgeManagementRoleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCloudEdgeManagementRoleResult(
            edge_profile=self.edge_profile,
            id=self.id,
            kind=self.kind,
            local_management_status=self.local_management_status,
            name=self.name,
            role_status=self.role_status,
            system_data=self.system_data,
            type=self.type)


def get_cloud_edge_management_role(device_name: Optional[str] = None,
                                   name: Optional[str] = None,
                                   resource_group_name: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCloudEdgeManagementRoleResult:
    """
    CloudEdgeManagementRole role.


    :param str device_name: The device name.
    :param str name: The role name.
    :param str resource_group_name: The resource group name.
    """
    __args__ = dict()
    __args__['deviceName'] = device_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:databoxedge/v20210601:getCloudEdgeManagementRole', __args__, opts=opts, typ=GetCloudEdgeManagementRoleResult).value

    return AwaitableGetCloudEdgeManagementRoleResult(
        edge_profile=__ret__.edge_profile,
        id=__ret__.id,
        kind=__ret__.kind,
        local_management_status=__ret__.local_management_status,
        name=__ret__.name,
        role_status=__ret__.role_status,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_cloud_edge_management_role)
def get_cloud_edge_management_role_output(device_name: Optional[pulumi.Input[str]] = None,
                                          name: Optional[pulumi.Input[str]] = None,
                                          resource_group_name: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCloudEdgeManagementRoleResult]:
    """
    CloudEdgeManagementRole role.


    :param str device_name: The device name.
    :param str name: The role name.
    :param str resource_group_name: The resource group name.
    """
    ...
