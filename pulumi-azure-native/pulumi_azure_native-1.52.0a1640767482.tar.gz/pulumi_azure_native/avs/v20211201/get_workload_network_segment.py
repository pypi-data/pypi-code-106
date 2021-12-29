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
    'GetWorkloadNetworkSegmentResult',
    'AwaitableGetWorkloadNetworkSegmentResult',
    'get_workload_network_segment',
    'get_workload_network_segment_output',
]

@pulumi.output_type
class GetWorkloadNetworkSegmentResult:
    """
    NSX Segment
    """
    def __init__(__self__, connected_gateway=None, display_name=None, id=None, name=None, port_vif=None, provisioning_state=None, revision=None, status=None, subnet=None, type=None):
        if connected_gateway and not isinstance(connected_gateway, str):
            raise TypeError("Expected argument 'connected_gateway' to be a str")
        pulumi.set(__self__, "connected_gateway", connected_gateway)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if port_vif and not isinstance(port_vif, list):
            raise TypeError("Expected argument 'port_vif' to be a list")
        pulumi.set(__self__, "port_vif", port_vif)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if revision and not isinstance(revision, float):
            raise TypeError("Expected argument 'revision' to be a float")
        pulumi.set(__self__, "revision", revision)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if subnet and not isinstance(subnet, dict):
            raise TypeError("Expected argument 'subnet' to be a dict")
        pulumi.set(__self__, "subnet", subnet)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="connectedGateway")
    def connected_gateway(self) -> Optional[str]:
        """
        Gateway which to connect segment to.
        """
        return pulumi.get(self, "connected_gateway")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        Display name of the segment.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="portVif")
    def port_vif(self) -> Sequence['outputs.WorkloadNetworkSegmentPortVifResponse']:
        """
        Port Vif which segment is associated with.
        """
        return pulumi.get(self, "port_vif")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def revision(self) -> Optional[float]:
        """
        NSX revision number.
        """
        return pulumi.get(self, "revision")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Segment status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def subnet(self) -> Optional['outputs.WorkloadNetworkSegmentSubnetResponse']:
        """
        Subnet which to connect segment to.
        """
        return pulumi.get(self, "subnet")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetWorkloadNetworkSegmentResult(GetWorkloadNetworkSegmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkloadNetworkSegmentResult(
            connected_gateway=self.connected_gateway,
            display_name=self.display_name,
            id=self.id,
            name=self.name,
            port_vif=self.port_vif,
            provisioning_state=self.provisioning_state,
            revision=self.revision,
            status=self.status,
            subnet=self.subnet,
            type=self.type)


def get_workload_network_segment(private_cloud_name: Optional[str] = None,
                                 resource_group_name: Optional[str] = None,
                                 segment_id: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkloadNetworkSegmentResult:
    """
    NSX Segment


    :param str private_cloud_name: Name of the private cloud
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str segment_id: NSX Segment identifier. Generally the same as the Segment's display name
    """
    __args__ = dict()
    __args__['privateCloudName'] = private_cloud_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['segmentId'] = segment_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:avs/v20211201:getWorkloadNetworkSegment', __args__, opts=opts, typ=GetWorkloadNetworkSegmentResult).value

    return AwaitableGetWorkloadNetworkSegmentResult(
        connected_gateway=__ret__.connected_gateway,
        display_name=__ret__.display_name,
        id=__ret__.id,
        name=__ret__.name,
        port_vif=__ret__.port_vif,
        provisioning_state=__ret__.provisioning_state,
        revision=__ret__.revision,
        status=__ret__.status,
        subnet=__ret__.subnet,
        type=__ret__.type)


@_utilities.lift_output_func(get_workload_network_segment)
def get_workload_network_segment_output(private_cloud_name: Optional[pulumi.Input[str]] = None,
                                        resource_group_name: Optional[pulumi.Input[str]] = None,
                                        segment_id: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkloadNetworkSegmentResult]:
    """
    NSX Segment


    :param str private_cloud_name: Name of the private cloud
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str segment_id: NSX Segment identifier. Generally the same as the Segment's display name
    """
    ...
