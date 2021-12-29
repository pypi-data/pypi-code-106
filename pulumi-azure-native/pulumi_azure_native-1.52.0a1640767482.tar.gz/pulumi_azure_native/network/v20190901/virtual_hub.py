# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._inputs import *

__all__ = ['VirtualHubArgs', 'VirtualHub']

@pulumi.input_type
class VirtualHubArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 address_prefix: Optional[pulumi.Input[str]] = None,
                 azure_firewall: Optional[pulumi.Input['SubResourceArgs']] = None,
                 express_route_gateway: Optional[pulumi.Input['SubResourceArgs']] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 p2_s_vpn_gateway: Optional[pulumi.Input['SubResourceArgs']] = None,
                 route_table: Optional[pulumi.Input['VirtualHubRouteTableArgs']] = None,
                 security_provider_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_hub_name: Optional[pulumi.Input[str]] = None,
                 virtual_hub_route_table_v2s: Optional[pulumi.Input[Sequence[pulumi.Input['VirtualHubRouteTableV2Args']]]] = None,
                 virtual_network_connections: Optional[pulumi.Input[Sequence[pulumi.Input['HubVirtualNetworkConnectionArgs']]]] = None,
                 virtual_wan: Optional[pulumi.Input['SubResourceArgs']] = None,
                 vpn_gateway: Optional[pulumi.Input['SubResourceArgs']] = None):
        """
        The set of arguments for constructing a VirtualHub resource.
        :param pulumi.Input[str] resource_group_name: The resource group name of the VirtualHub.
        :param pulumi.Input[str] address_prefix: Address-prefix for this VirtualHub.
        :param pulumi.Input['SubResourceArgs'] azure_firewall: The azureFirewall associated with this VirtualHub.
        :param pulumi.Input['SubResourceArgs'] express_route_gateway: The expressRouteGateway associated with this VirtualHub.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input['SubResourceArgs'] p2_s_vpn_gateway: The P2SVpnGateway associated with this VirtualHub.
        :param pulumi.Input['VirtualHubRouteTableArgs'] route_table: The routeTable associated with this virtual hub.
        :param pulumi.Input[str] security_provider_name: The Security Provider name.
        :param pulumi.Input[str] sku: The sku of this VirtualHub.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] virtual_hub_name: The name of the VirtualHub.
        :param pulumi.Input[Sequence[pulumi.Input['VirtualHubRouteTableV2Args']]] virtual_hub_route_table_v2s: List of all virtual hub route table v2s associated with this VirtualHub.
        :param pulumi.Input[Sequence[pulumi.Input['HubVirtualNetworkConnectionArgs']]] virtual_network_connections: List of all vnet connections with this VirtualHub.
        :param pulumi.Input['SubResourceArgs'] virtual_wan: The VirtualWAN to which the VirtualHub belongs.
        :param pulumi.Input['SubResourceArgs'] vpn_gateway: The VpnGateway associated with this VirtualHub.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if address_prefix is not None:
            pulumi.set(__self__, "address_prefix", address_prefix)
        if azure_firewall is not None:
            pulumi.set(__self__, "azure_firewall", azure_firewall)
        if express_route_gateway is not None:
            pulumi.set(__self__, "express_route_gateway", express_route_gateway)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if p2_s_vpn_gateway is not None:
            pulumi.set(__self__, "p2_s_vpn_gateway", p2_s_vpn_gateway)
        if route_table is not None:
            pulumi.set(__self__, "route_table", route_table)
        if security_provider_name is not None:
            pulumi.set(__self__, "security_provider_name", security_provider_name)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if virtual_hub_name is not None:
            pulumi.set(__self__, "virtual_hub_name", virtual_hub_name)
        if virtual_hub_route_table_v2s is not None:
            pulumi.set(__self__, "virtual_hub_route_table_v2s", virtual_hub_route_table_v2s)
        if virtual_network_connections is not None:
            pulumi.set(__self__, "virtual_network_connections", virtual_network_connections)
        if virtual_wan is not None:
            pulumi.set(__self__, "virtual_wan", virtual_wan)
        if vpn_gateway is not None:
            pulumi.set(__self__, "vpn_gateway", vpn_gateway)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name of the VirtualHub.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        Address-prefix for this VirtualHub.
        """
        return pulumi.get(self, "address_prefix")

    @address_prefix.setter
    def address_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address_prefix", value)

    @property
    @pulumi.getter(name="azureFirewall")
    def azure_firewall(self) -> Optional[pulumi.Input['SubResourceArgs']]:
        """
        The azureFirewall associated with this VirtualHub.
        """
        return pulumi.get(self, "azure_firewall")

    @azure_firewall.setter
    def azure_firewall(self, value: Optional[pulumi.Input['SubResourceArgs']]):
        pulumi.set(self, "azure_firewall", value)

    @property
    @pulumi.getter(name="expressRouteGateway")
    def express_route_gateway(self) -> Optional[pulumi.Input['SubResourceArgs']]:
        """
        The expressRouteGateway associated with this VirtualHub.
        """
        return pulumi.get(self, "express_route_gateway")

    @express_route_gateway.setter
    def express_route_gateway(self, value: Optional[pulumi.Input['SubResourceArgs']]):
        pulumi.set(self, "express_route_gateway", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="p2SVpnGateway")
    def p2_s_vpn_gateway(self) -> Optional[pulumi.Input['SubResourceArgs']]:
        """
        The P2SVpnGateway associated with this VirtualHub.
        """
        return pulumi.get(self, "p2_s_vpn_gateway")

    @p2_s_vpn_gateway.setter
    def p2_s_vpn_gateway(self, value: Optional[pulumi.Input['SubResourceArgs']]):
        pulumi.set(self, "p2_s_vpn_gateway", value)

    @property
    @pulumi.getter(name="routeTable")
    def route_table(self) -> Optional[pulumi.Input['VirtualHubRouteTableArgs']]:
        """
        The routeTable associated with this virtual hub.
        """
        return pulumi.get(self, "route_table")

    @route_table.setter
    def route_table(self, value: Optional[pulumi.Input['VirtualHubRouteTableArgs']]):
        pulumi.set(self, "route_table", value)

    @property
    @pulumi.getter(name="securityProviderName")
    def security_provider_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Security Provider name.
        """
        return pulumi.get(self, "security_provider_name")

    @security_provider_name.setter
    def security_provider_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "security_provider_name", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[str]]:
        """
        The sku of this VirtualHub.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="virtualHubName")
    def virtual_hub_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the VirtualHub.
        """
        return pulumi.get(self, "virtual_hub_name")

    @virtual_hub_name.setter
    def virtual_hub_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "virtual_hub_name", value)

    @property
    @pulumi.getter(name="virtualHubRouteTableV2s")
    def virtual_hub_route_table_v2s(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VirtualHubRouteTableV2Args']]]]:
        """
        List of all virtual hub route table v2s associated with this VirtualHub.
        """
        return pulumi.get(self, "virtual_hub_route_table_v2s")

    @virtual_hub_route_table_v2s.setter
    def virtual_hub_route_table_v2s(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VirtualHubRouteTableV2Args']]]]):
        pulumi.set(self, "virtual_hub_route_table_v2s", value)

    @property
    @pulumi.getter(name="virtualNetworkConnections")
    def virtual_network_connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['HubVirtualNetworkConnectionArgs']]]]:
        """
        List of all vnet connections with this VirtualHub.
        """
        return pulumi.get(self, "virtual_network_connections")

    @virtual_network_connections.setter
    def virtual_network_connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['HubVirtualNetworkConnectionArgs']]]]):
        pulumi.set(self, "virtual_network_connections", value)

    @property
    @pulumi.getter(name="virtualWan")
    def virtual_wan(self) -> Optional[pulumi.Input['SubResourceArgs']]:
        """
        The VirtualWAN to which the VirtualHub belongs.
        """
        return pulumi.get(self, "virtual_wan")

    @virtual_wan.setter
    def virtual_wan(self, value: Optional[pulumi.Input['SubResourceArgs']]):
        pulumi.set(self, "virtual_wan", value)

    @property
    @pulumi.getter(name="vpnGateway")
    def vpn_gateway(self) -> Optional[pulumi.Input['SubResourceArgs']]:
        """
        The VpnGateway associated with this VirtualHub.
        """
        return pulumi.get(self, "vpn_gateway")

    @vpn_gateway.setter
    def vpn_gateway(self, value: Optional[pulumi.Input['SubResourceArgs']]):
        pulumi.set(self, "vpn_gateway", value)


class VirtualHub(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address_prefix: Optional[pulumi.Input[str]] = None,
                 azure_firewall: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 express_route_gateway: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 p2_s_vpn_gateway: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 route_table: Optional[pulumi.Input[pulumi.InputType['VirtualHubRouteTableArgs']]] = None,
                 security_provider_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_hub_name: Optional[pulumi.Input[str]] = None,
                 virtual_hub_route_table_v2s: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VirtualHubRouteTableV2Args']]]]] = None,
                 virtual_network_connections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HubVirtualNetworkConnectionArgs']]]]] = None,
                 virtual_wan: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 vpn_gateway: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 __props__=None):
        """
        VirtualHub Resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address_prefix: Address-prefix for this VirtualHub.
        :param pulumi.Input[pulumi.InputType['SubResourceArgs']] azure_firewall: The azureFirewall associated with this VirtualHub.
        :param pulumi.Input[pulumi.InputType['SubResourceArgs']] express_route_gateway: The expressRouteGateway associated with this VirtualHub.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[pulumi.InputType['SubResourceArgs']] p2_s_vpn_gateway: The P2SVpnGateway associated with this VirtualHub.
        :param pulumi.Input[str] resource_group_name: The resource group name of the VirtualHub.
        :param pulumi.Input[pulumi.InputType['VirtualHubRouteTableArgs']] route_table: The routeTable associated with this virtual hub.
        :param pulumi.Input[str] security_provider_name: The Security Provider name.
        :param pulumi.Input[str] sku: The sku of this VirtualHub.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] virtual_hub_name: The name of the VirtualHub.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VirtualHubRouteTableV2Args']]]] virtual_hub_route_table_v2s: List of all virtual hub route table v2s associated with this VirtualHub.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HubVirtualNetworkConnectionArgs']]]] virtual_network_connections: List of all vnet connections with this VirtualHub.
        :param pulumi.Input[pulumi.InputType['SubResourceArgs']] virtual_wan: The VirtualWAN to which the VirtualHub belongs.
        :param pulumi.Input[pulumi.InputType['SubResourceArgs']] vpn_gateway: The VpnGateway associated with this VirtualHub.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VirtualHubArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        VirtualHub Resource.

        :param str resource_name: The name of the resource.
        :param VirtualHubArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VirtualHubArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address_prefix: Optional[pulumi.Input[str]] = None,
                 azure_firewall: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 express_route_gateway: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 p2_s_vpn_gateway: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 route_table: Optional[pulumi.Input[pulumi.InputType['VirtualHubRouteTableArgs']]] = None,
                 security_provider_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_hub_name: Optional[pulumi.Input[str]] = None,
                 virtual_hub_route_table_v2s: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VirtualHubRouteTableV2Args']]]]] = None,
                 virtual_network_connections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HubVirtualNetworkConnectionArgs']]]]] = None,
                 virtual_wan: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 vpn_gateway: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VirtualHubArgs.__new__(VirtualHubArgs)

            __props__.__dict__["address_prefix"] = address_prefix
            __props__.__dict__["azure_firewall"] = azure_firewall
            __props__.__dict__["express_route_gateway"] = express_route_gateway
            __props__.__dict__["id"] = id
            __props__.__dict__["location"] = location
            __props__.__dict__["p2_s_vpn_gateway"] = p2_s_vpn_gateway
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["route_table"] = route_table
            __props__.__dict__["security_provider_name"] = security_provider_name
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["virtual_hub_name"] = virtual_hub_name
            __props__.__dict__["virtual_hub_route_table_v2s"] = virtual_hub_route_table_v2s
            __props__.__dict__["virtual_network_connections"] = virtual_network_connections
            __props__.__dict__["virtual_wan"] = virtual_wan
            __props__.__dict__["vpn_gateway"] = vpn_gateway
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:VirtualHub"), pulumi.Alias(type_="azure-native:network/v20180401:VirtualHub"), pulumi.Alias(type_="azure-native:network/v20180601:VirtualHub"), pulumi.Alias(type_="azure-native:network/v20180701:VirtualHub"), pulumi.Alias(type_="azure-native:network/v20180801:VirtualHub"), pulumi.Alias(type_="azure-native:network/v20181001:VirtualHub"), pulumi.Alias(type_="azure-native:network/v20181101:VirtualHub"), pulumi.Alias(type_="azure-native:network/v20181201:VirtualHub"), pulumi.Alias(type_="azure-native:network/v20190201:VirtualHub"), pulumi.Alias(type_="azure-native:network/v20190401:VirtualHub"), pulumi.Alias(type_="azure-native:network/v20190601:VirtualHub"), pulumi.Alias(type_="azure-native:network/v20190701:VirtualHub"), pulumi.Alias(type_="azure-native:network/v20190801:VirtualHub"), pulumi.Alias(type_="azure-native:network/v20191101:VirtualHub"), pulumi.Alias(type_="azure-native:network/v20191201:VirtualHub"), pulumi.Alias(type_="azure-native:network/v20200301:VirtualHub"), pulumi.Alias(type_="azure-native:network/v20200401:VirtualHub"), pulumi.Alias(type_="azure-native:network/v20200501:VirtualHub"), pulumi.Alias(type_="azure-native:network/v20200601:VirtualHub"), pulumi.Alias(type_="azure-native:network/v20200701:VirtualHub"), pulumi.Alias(type_="azure-native:network/v20200801:VirtualHub"), pulumi.Alias(type_="azure-native:network/v20201101:VirtualHub"), pulumi.Alias(type_="azure-native:network/v20210201:VirtualHub"), pulumi.Alias(type_="azure-native:network/v20210301:VirtualHub"), pulumi.Alias(type_="azure-native:network/v20210501:VirtualHub")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VirtualHub, __self__).__init__(
            'azure-native:network/v20190901:VirtualHub',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VirtualHub':
        """
        Get an existing VirtualHub resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VirtualHubArgs.__new__(VirtualHubArgs)

        __props__.__dict__["address_prefix"] = None
        __props__.__dict__["azure_firewall"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["express_route_gateway"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["p2_s_vpn_gateway"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["route_table"] = None
        __props__.__dict__["security_provider_name"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["virtual_hub_route_table_v2s"] = None
        __props__.__dict__["virtual_network_connections"] = None
        __props__.__dict__["virtual_wan"] = None
        __props__.__dict__["vpn_gateway"] = None
        return VirtualHub(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> pulumi.Output[Optional[str]]:
        """
        Address-prefix for this VirtualHub.
        """
        return pulumi.get(self, "address_prefix")

    @property
    @pulumi.getter(name="azureFirewall")
    def azure_firewall(self) -> pulumi.Output[Optional['outputs.SubResourceResponse']]:
        """
        The azureFirewall associated with this VirtualHub.
        """
        return pulumi.get(self, "azure_firewall")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="expressRouteGateway")
    def express_route_gateway(self) -> pulumi.Output[Optional['outputs.SubResourceResponse']]:
        """
        The expressRouteGateway associated with this VirtualHub.
        """
        return pulumi.get(self, "express_route_gateway")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="p2SVpnGateway")
    def p2_s_vpn_gateway(self) -> pulumi.Output[Optional['outputs.SubResourceResponse']]:
        """
        The P2SVpnGateway associated with this VirtualHub.
        """
        return pulumi.get(self, "p2_s_vpn_gateway")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the virtual hub resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="routeTable")
    def route_table(self) -> pulumi.Output[Optional['outputs.VirtualHubRouteTableResponse']]:
        """
        The routeTable associated with this virtual hub.
        """
        return pulumi.get(self, "route_table")

    @property
    @pulumi.getter(name="securityProviderName")
    def security_provider_name(self) -> pulumi.Output[Optional[str]]:
        """
        The Security Provider name.
        """
        return pulumi.get(self, "security_provider_name")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[str]]:
        """
        The sku of this VirtualHub.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualHubRouteTableV2s")
    def virtual_hub_route_table_v2s(self) -> pulumi.Output[Optional[Sequence['outputs.VirtualHubRouteTableV2Response']]]:
        """
        List of all virtual hub route table v2s associated with this VirtualHub.
        """
        return pulumi.get(self, "virtual_hub_route_table_v2s")

    @property
    @pulumi.getter(name="virtualNetworkConnections")
    def virtual_network_connections(self) -> pulumi.Output[Optional[Sequence['outputs.HubVirtualNetworkConnectionResponse']]]:
        """
        List of all vnet connections with this VirtualHub.
        """
        return pulumi.get(self, "virtual_network_connections")

    @property
    @pulumi.getter(name="virtualWan")
    def virtual_wan(self) -> pulumi.Output[Optional['outputs.SubResourceResponse']]:
        """
        The VirtualWAN to which the VirtualHub belongs.
        """
        return pulumi.get(self, "virtual_wan")

    @property
    @pulumi.getter(name="vpnGateway")
    def vpn_gateway(self) -> pulumi.Output[Optional['outputs.SubResourceResponse']]:
        """
        The VpnGateway associated with this VirtualHub.
        """
        return pulumi.get(self, "vpn_gateway")

