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
    'GetAttestationProviderResult',
    'AwaitableGetAttestationProviderResult',
    'get_attestation_provider',
    'get_attestation_provider_output',
]

@pulumi.output_type
class GetAttestationProviderResult:
    """
    Attestation service response message.
    """
    def __init__(__self__, attest_uri=None, id=None, location=None, name=None, private_endpoint_connections=None, public_network_access=None, status=None, system_data=None, tags=None, trust_model=None, type=None):
        if attest_uri and not isinstance(attest_uri, str):
            raise TypeError("Expected argument 'attest_uri' to be a str")
        pulumi.set(__self__, "attest_uri", attest_uri)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if private_endpoint_connections and not isinstance(private_endpoint_connections, list):
            raise TypeError("Expected argument 'private_endpoint_connections' to be a list")
        pulumi.set(__self__, "private_endpoint_connections", private_endpoint_connections)
        if public_network_access and not isinstance(public_network_access, str):
            raise TypeError("Expected argument 'public_network_access' to be a str")
        pulumi.set(__self__, "public_network_access", public_network_access)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if trust_model and not isinstance(trust_model, str):
            raise TypeError("Expected argument 'trust_model' to be a str")
        pulumi.set(__self__, "trust_model", trust_model)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="attestUri")
    def attest_uri(self) -> Optional[str]:
        """
        Gets the uri of attestation service
        """
        return pulumi.get(self, "attest_uri")

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
        The geo-location where the resource lives
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
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence['outputs.PrivateEndpointConnectionResponse']:
        """
        List of private endpoint connections associated with the attestation provider.
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[str]:
        """
        Controls whether traffic from the public network is allowed to access the Attestation Provider APIs.
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        Status of attestation service.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system metadata relating to this resource
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="trustModel")
    def trust_model(self) -> Optional[str]:
        """
        Trust model for the attestation provider.
        """
        return pulumi.get(self, "trust_model")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetAttestationProviderResult(GetAttestationProviderResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAttestationProviderResult(
            attest_uri=self.attest_uri,
            id=self.id,
            location=self.location,
            name=self.name,
            private_endpoint_connections=self.private_endpoint_connections,
            public_network_access=self.public_network_access,
            status=self.status,
            system_data=self.system_data,
            tags=self.tags,
            trust_model=self.trust_model,
            type=self.type)


def get_attestation_provider(provider_name: Optional[str] = None,
                             resource_group_name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAttestationProviderResult:
    """
    Attestation service response message.


    :param str provider_name: Name of the attestation provider.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['providerName'] = provider_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:attestation/v20210601preview:getAttestationProvider', __args__, opts=opts, typ=GetAttestationProviderResult).value

    return AwaitableGetAttestationProviderResult(
        attest_uri=__ret__.attest_uri,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        private_endpoint_connections=__ret__.private_endpoint_connections,
        public_network_access=__ret__.public_network_access,
        status=__ret__.status,
        system_data=__ret__.system_data,
        tags=__ret__.tags,
        trust_model=__ret__.trust_model,
        type=__ret__.type)


@_utilities.lift_output_func(get_attestation_provider)
def get_attestation_provider_output(provider_name: Optional[pulumi.Input[str]] = None,
                                    resource_group_name: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAttestationProviderResult]:
    """
    Attestation service response message.


    :param str provider_name: Name of the attestation provider.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
