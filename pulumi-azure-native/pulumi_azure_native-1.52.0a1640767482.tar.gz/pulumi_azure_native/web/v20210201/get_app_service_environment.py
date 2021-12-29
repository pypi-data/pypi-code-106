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
    'GetAppServiceEnvironmentResult',
    'AwaitableGetAppServiceEnvironmentResult',
    'get_app_service_environment',
    'get_app_service_environment_output',
]

@pulumi.output_type
class GetAppServiceEnvironmentResult:
    """
    App Service Environment ARM resource.
    """
    def __init__(__self__, cluster_settings=None, dedicated_host_count=None, dns_suffix=None, front_end_scale_factor=None, has_linux_workers=None, id=None, internal_load_balancing_mode=None, ipssl_address_count=None, kind=None, location=None, maximum_number_of_machines=None, multi_role_count=None, multi_size=None, name=None, provisioning_state=None, status=None, suspended=None, tags=None, type=None, user_whitelisted_ip_ranges=None, virtual_network=None, zone_redundant=None):
        if cluster_settings and not isinstance(cluster_settings, list):
            raise TypeError("Expected argument 'cluster_settings' to be a list")
        pulumi.set(__self__, "cluster_settings", cluster_settings)
        if dedicated_host_count and not isinstance(dedicated_host_count, int):
            raise TypeError("Expected argument 'dedicated_host_count' to be a int")
        pulumi.set(__self__, "dedicated_host_count", dedicated_host_count)
        if dns_suffix and not isinstance(dns_suffix, str):
            raise TypeError("Expected argument 'dns_suffix' to be a str")
        pulumi.set(__self__, "dns_suffix", dns_suffix)
        if front_end_scale_factor and not isinstance(front_end_scale_factor, int):
            raise TypeError("Expected argument 'front_end_scale_factor' to be a int")
        pulumi.set(__self__, "front_end_scale_factor", front_end_scale_factor)
        if has_linux_workers and not isinstance(has_linux_workers, bool):
            raise TypeError("Expected argument 'has_linux_workers' to be a bool")
        pulumi.set(__self__, "has_linux_workers", has_linux_workers)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if internal_load_balancing_mode and not isinstance(internal_load_balancing_mode, str):
            raise TypeError("Expected argument 'internal_load_balancing_mode' to be a str")
        pulumi.set(__self__, "internal_load_balancing_mode", internal_load_balancing_mode)
        if ipssl_address_count and not isinstance(ipssl_address_count, int):
            raise TypeError("Expected argument 'ipssl_address_count' to be a int")
        pulumi.set(__self__, "ipssl_address_count", ipssl_address_count)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if maximum_number_of_machines and not isinstance(maximum_number_of_machines, int):
            raise TypeError("Expected argument 'maximum_number_of_machines' to be a int")
        pulumi.set(__self__, "maximum_number_of_machines", maximum_number_of_machines)
        if multi_role_count and not isinstance(multi_role_count, int):
            raise TypeError("Expected argument 'multi_role_count' to be a int")
        pulumi.set(__self__, "multi_role_count", multi_role_count)
        if multi_size and not isinstance(multi_size, str):
            raise TypeError("Expected argument 'multi_size' to be a str")
        pulumi.set(__self__, "multi_size", multi_size)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if suspended and not isinstance(suspended, bool):
            raise TypeError("Expected argument 'suspended' to be a bool")
        pulumi.set(__self__, "suspended", suspended)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if user_whitelisted_ip_ranges and not isinstance(user_whitelisted_ip_ranges, list):
            raise TypeError("Expected argument 'user_whitelisted_ip_ranges' to be a list")
        pulumi.set(__self__, "user_whitelisted_ip_ranges", user_whitelisted_ip_ranges)
        if virtual_network and not isinstance(virtual_network, dict):
            raise TypeError("Expected argument 'virtual_network' to be a dict")
        pulumi.set(__self__, "virtual_network", virtual_network)
        if zone_redundant and not isinstance(zone_redundant, bool):
            raise TypeError("Expected argument 'zone_redundant' to be a bool")
        pulumi.set(__self__, "zone_redundant", zone_redundant)

    @property
    @pulumi.getter(name="clusterSettings")
    def cluster_settings(self) -> Optional[Sequence['outputs.NameValuePairResponse']]:
        """
        Custom settings for changing the behavior of the App Service Environment.
        """
        return pulumi.get(self, "cluster_settings")

    @property
    @pulumi.getter(name="dedicatedHostCount")
    def dedicated_host_count(self) -> Optional[int]:
        """
        Dedicated Host Count
        """
        return pulumi.get(self, "dedicated_host_count")

    @property
    @pulumi.getter(name="dnsSuffix")
    def dns_suffix(self) -> Optional[str]:
        """
        DNS suffix of the App Service Environment.
        """
        return pulumi.get(self, "dns_suffix")

    @property
    @pulumi.getter(name="frontEndScaleFactor")
    def front_end_scale_factor(self) -> Optional[int]:
        """
        Scale factor for front-ends.
        """
        return pulumi.get(self, "front_end_scale_factor")

    @property
    @pulumi.getter(name="hasLinuxWorkers")
    def has_linux_workers(self) -> bool:
        """
        Flag that displays whether an ASE has linux workers or not
        """
        return pulumi.get(self, "has_linux_workers")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="internalLoadBalancingMode")
    def internal_load_balancing_mode(self) -> Optional[str]:
        """
        Specifies which endpoints to serve internally in the Virtual Network for the App Service Environment.
        """
        return pulumi.get(self, "internal_load_balancing_mode")

    @property
    @pulumi.getter(name="ipsslAddressCount")
    def ipssl_address_count(self) -> Optional[int]:
        """
        Number of IP SSL addresses reserved for the App Service Environment.
        """
        return pulumi.get(self, "ipssl_address_count")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource Location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maximumNumberOfMachines")
    def maximum_number_of_machines(self) -> int:
        """
        Maximum number of VMs in the App Service Environment.
        """
        return pulumi.get(self, "maximum_number_of_machines")

    @property
    @pulumi.getter(name="multiRoleCount")
    def multi_role_count(self) -> int:
        """
        Number of front-end instances.
        """
        return pulumi.get(self, "multi_role_count")

    @property
    @pulumi.getter(name="multiSize")
    def multi_size(self) -> Optional[str]:
        """
        Front-end VM size, e.g. "Medium", "Large".
        """
        return pulumi.get(self, "multi_size")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the App Service Environment.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Current status of the App Service Environment.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def suspended(self) -> bool:
        """
        <code>true</code> if the App Service Environment is suspended; otherwise, <code>false</code>. The environment can be suspended, e.g. when the management endpoint is no longer available
         (most likely because NSG blocked the incoming traffic).
        """
        return pulumi.get(self, "suspended")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userWhitelistedIpRanges")
    def user_whitelisted_ip_ranges(self) -> Optional[Sequence[str]]:
        """
        User added ip ranges to whitelist on ASE db
        """
        return pulumi.get(self, "user_whitelisted_ip_ranges")

    @property
    @pulumi.getter(name="virtualNetwork")
    def virtual_network(self) -> 'outputs.VirtualNetworkProfileResponse':
        """
        Description of the Virtual Network.
        """
        return pulumi.get(self, "virtual_network")

    @property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> Optional[bool]:
        """
        Whether or not this App Service Environment is zone-redundant.
        """
        return pulumi.get(self, "zone_redundant")


class AwaitableGetAppServiceEnvironmentResult(GetAppServiceEnvironmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAppServiceEnvironmentResult(
            cluster_settings=self.cluster_settings,
            dedicated_host_count=self.dedicated_host_count,
            dns_suffix=self.dns_suffix,
            front_end_scale_factor=self.front_end_scale_factor,
            has_linux_workers=self.has_linux_workers,
            id=self.id,
            internal_load_balancing_mode=self.internal_load_balancing_mode,
            ipssl_address_count=self.ipssl_address_count,
            kind=self.kind,
            location=self.location,
            maximum_number_of_machines=self.maximum_number_of_machines,
            multi_role_count=self.multi_role_count,
            multi_size=self.multi_size,
            name=self.name,
            provisioning_state=self.provisioning_state,
            status=self.status,
            suspended=self.suspended,
            tags=self.tags,
            type=self.type,
            user_whitelisted_ip_ranges=self.user_whitelisted_ip_ranges,
            virtual_network=self.virtual_network,
            zone_redundant=self.zone_redundant)


def get_app_service_environment(name: Optional[str] = None,
                                resource_group_name: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAppServiceEnvironmentResult:
    """
    App Service Environment ARM resource.


    :param str name: Name of the App Service Environment.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:web/v20210201:getAppServiceEnvironment', __args__, opts=opts, typ=GetAppServiceEnvironmentResult).value

    return AwaitableGetAppServiceEnvironmentResult(
        cluster_settings=__ret__.cluster_settings,
        dedicated_host_count=__ret__.dedicated_host_count,
        dns_suffix=__ret__.dns_suffix,
        front_end_scale_factor=__ret__.front_end_scale_factor,
        has_linux_workers=__ret__.has_linux_workers,
        id=__ret__.id,
        internal_load_balancing_mode=__ret__.internal_load_balancing_mode,
        ipssl_address_count=__ret__.ipssl_address_count,
        kind=__ret__.kind,
        location=__ret__.location,
        maximum_number_of_machines=__ret__.maximum_number_of_machines,
        multi_role_count=__ret__.multi_role_count,
        multi_size=__ret__.multi_size,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        status=__ret__.status,
        suspended=__ret__.suspended,
        tags=__ret__.tags,
        type=__ret__.type,
        user_whitelisted_ip_ranges=__ret__.user_whitelisted_ip_ranges,
        virtual_network=__ret__.virtual_network,
        zone_redundant=__ret__.zone_redundant)


@_utilities.lift_output_func(get_app_service_environment)
def get_app_service_environment_output(name: Optional[pulumi.Input[str]] = None,
                                       resource_group_name: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAppServiceEnvironmentResult]:
    """
    App Service Environment ARM resource.


    :param str name: Name of the App Service Environment.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    ...
