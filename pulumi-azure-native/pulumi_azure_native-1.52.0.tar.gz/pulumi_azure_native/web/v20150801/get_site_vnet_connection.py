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
    'GetSiteVNETConnectionResult',
    'AwaitableGetSiteVNETConnectionResult',
    'get_site_vnet_connection',
    'get_site_vnet_connection_output',
]

@pulumi.output_type
class GetSiteVNETConnectionResult:
    """
    VNETInfo contract. This contract is public and is a stripped down version of VNETInfoInternal
    """
    def __init__(__self__, cert_blob=None, cert_thumbprint=None, dns_servers=None, id=None, kind=None, location=None, name=None, resync_required=None, routes=None, tags=None, type=None, vnet_resource_id=None):
        if cert_blob and not isinstance(cert_blob, str):
            raise TypeError("Expected argument 'cert_blob' to be a str")
        pulumi.set(__self__, "cert_blob", cert_blob)
        if cert_thumbprint and not isinstance(cert_thumbprint, str):
            raise TypeError("Expected argument 'cert_thumbprint' to be a str")
        pulumi.set(__self__, "cert_thumbprint", cert_thumbprint)
        if dns_servers and not isinstance(dns_servers, str):
            raise TypeError("Expected argument 'dns_servers' to be a str")
        pulumi.set(__self__, "dns_servers", dns_servers)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resync_required and not isinstance(resync_required, bool):
            raise TypeError("Expected argument 'resync_required' to be a bool")
        pulumi.set(__self__, "resync_required", resync_required)
        if routes and not isinstance(routes, list):
            raise TypeError("Expected argument 'routes' to be a list")
        pulumi.set(__self__, "routes", routes)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if vnet_resource_id and not isinstance(vnet_resource_id, str):
            raise TypeError("Expected argument 'vnet_resource_id' to be a str")
        pulumi.set(__self__, "vnet_resource_id", vnet_resource_id)

    @property
    @pulumi.getter(name="certBlob")
    def cert_blob(self) -> Optional[str]:
        """
        A certificate file (.cer) blob containing the public key of the private key used to authenticate a 
                    Point-To-Site VPN connection.
        """
        return pulumi.get(self, "cert_blob")

    @property
    @pulumi.getter(name="certThumbprint")
    def cert_thumbprint(self) -> Optional[str]:
        """
        The client certificate thumbprint
        """
        return pulumi.get(self, "cert_thumbprint")

    @property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> Optional[str]:
        """
        Dns servers to be used by this VNET. This should be a comma-separated list of IP addresses.
        """
        return pulumi.get(self, "dns_servers")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind of resource
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource Location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Resource Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resyncRequired")
    def resync_required(self) -> Optional[bool]:
        """
        Flag to determine if a resync is required
        """
        return pulumi.get(self, "resync_required")

    @property
    @pulumi.getter
    def routes(self) -> Optional[Sequence['outputs.VnetRouteResponse']]:
        """
        The routes that this virtual network connection uses.
        """
        return pulumi.get(self, "routes")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vnetResourceId")
    def vnet_resource_id(self) -> Optional[str]:
        """
        The vnet resource id
        """
        return pulumi.get(self, "vnet_resource_id")


class AwaitableGetSiteVNETConnectionResult(GetSiteVNETConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSiteVNETConnectionResult(
            cert_blob=self.cert_blob,
            cert_thumbprint=self.cert_thumbprint,
            dns_servers=self.dns_servers,
            id=self.id,
            kind=self.kind,
            location=self.location,
            name=self.name,
            resync_required=self.resync_required,
            routes=self.routes,
            tags=self.tags,
            type=self.type,
            vnet_resource_id=self.vnet_resource_id)


def get_site_vnet_connection(name: Optional[str] = None,
                             resource_group_name: Optional[str] = None,
                             vnet_name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSiteVNETConnectionResult:
    """
    VNETInfo contract. This contract is public and is a stripped down version of VNETInfoInternal


    :param str name: The name of the web app
    :param str resource_group_name: The resource group name
    :param str vnet_name: The name of the Virtual Network
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __args__['vnetName'] = vnet_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:web/v20150801:getSiteVNETConnection', __args__, opts=opts, typ=GetSiteVNETConnectionResult).value

    return AwaitableGetSiteVNETConnectionResult(
        cert_blob=__ret__.cert_blob,
        cert_thumbprint=__ret__.cert_thumbprint,
        dns_servers=__ret__.dns_servers,
        id=__ret__.id,
        kind=__ret__.kind,
        location=__ret__.location,
        name=__ret__.name,
        resync_required=__ret__.resync_required,
        routes=__ret__.routes,
        tags=__ret__.tags,
        type=__ret__.type,
        vnet_resource_id=__ret__.vnet_resource_id)


@_utilities.lift_output_func(get_site_vnet_connection)
def get_site_vnet_connection_output(name: Optional[pulumi.Input[str]] = None,
                                    resource_group_name: Optional[pulumi.Input[str]] = None,
                                    vnet_name: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSiteVNETConnectionResult]:
    """
    VNETInfo contract. This contract is public and is a stripped down version of VNETInfoInternal


    :param str name: The name of the web app
    :param str resource_group_name: The resource group name
    :param str vnet_name: The name of the Virtual Network
    """
    ...
