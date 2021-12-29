# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *

__all__ = ['AgentPoolArgs', 'AgentPool']

@pulumi.input_type
class AgentPoolArgs:
    def __init__(__self__, *,
                 registry_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 agent_pool_name: Optional[pulumi.Input[str]] = None,
                 count: Optional[pulumi.Input[int]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 os: Optional[pulumi.Input[Union[str, 'OS']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tier: Optional[pulumi.Input[str]] = None,
                 virtual_network_subnet_resource_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AgentPool resource.
        :param pulumi.Input[str] registry_name: The name of the container registry.
        :param pulumi.Input[str] resource_group_name: The name of the resource group to which the container registry belongs.
        :param pulumi.Input[str] agent_pool_name: The name of the agent pool.
        :param pulumi.Input[int] count: The count of agent machine
        :param pulumi.Input[str] location: The location of the resource. This cannot be changed after the resource is created.
        :param pulumi.Input[Union[str, 'OS']] os: The OS of agent machine
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags of the resource.
        :param pulumi.Input[str] tier: The Tier of agent machine
        :param pulumi.Input[str] virtual_network_subnet_resource_id: The Virtual Network Subnet Resource Id of the agent machine
        """
        pulumi.set(__self__, "registry_name", registry_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if agent_pool_name is not None:
            pulumi.set(__self__, "agent_pool_name", agent_pool_name)
        if count is not None:
            pulumi.set(__self__, "count", count)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if os is not None:
            pulumi.set(__self__, "os", os)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)
        if virtual_network_subnet_resource_id is not None:
            pulumi.set(__self__, "virtual_network_subnet_resource_id", virtual_network_subnet_resource_id)

    @property
    @pulumi.getter(name="registryName")
    def registry_name(self) -> pulumi.Input[str]:
        """
        The name of the container registry.
        """
        return pulumi.get(self, "registry_name")

    @registry_name.setter
    def registry_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "registry_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group to which the container registry belongs.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="agentPoolName")
    def agent_pool_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the agent pool.
        """
        return pulumi.get(self, "agent_pool_name")

    @agent_pool_name.setter
    def agent_pool_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "agent_pool_name", value)

    @property
    @pulumi.getter
    def count(self) -> Optional[pulumi.Input[int]]:
        """
        The count of agent machine
        """
        return pulumi.get(self, "count")

    @count.setter
    def count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "count", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the resource. This cannot be changed after the resource is created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def os(self) -> Optional[pulumi.Input[Union[str, 'OS']]]:
        """
        The OS of agent machine
        """
        return pulumi.get(self, "os")

    @os.setter
    def os(self, value: Optional[pulumi.Input[Union[str, 'OS']]]):
        pulumi.set(self, "os", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[str]]:
        """
        The Tier of agent machine
        """
        return pulumi.get(self, "tier")

    @tier.setter
    def tier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tier", value)

    @property
    @pulumi.getter(name="virtualNetworkSubnetResourceId")
    def virtual_network_subnet_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Virtual Network Subnet Resource Id of the agent machine
        """
        return pulumi.get(self, "virtual_network_subnet_resource_id")

    @virtual_network_subnet_resource_id.setter
    def virtual_network_subnet_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "virtual_network_subnet_resource_id", value)


class AgentPool(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_pool_name: Optional[pulumi.Input[str]] = None,
                 count: Optional[pulumi.Input[int]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 os: Optional[pulumi.Input[Union[str, 'OS']]] = None,
                 registry_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tier: Optional[pulumi.Input[str]] = None,
                 virtual_network_subnet_resource_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The agentpool that has the ARM resource and properties.
        The agentpool will have all information to create an agent pool.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] agent_pool_name: The name of the agent pool.
        :param pulumi.Input[int] count: The count of agent machine
        :param pulumi.Input[str] location: The location of the resource. This cannot be changed after the resource is created.
        :param pulumi.Input[Union[str, 'OS']] os: The OS of agent machine
        :param pulumi.Input[str] registry_name: The name of the container registry.
        :param pulumi.Input[str] resource_group_name: The name of the resource group to which the container registry belongs.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags of the resource.
        :param pulumi.Input[str] tier: The Tier of agent machine
        :param pulumi.Input[str] virtual_network_subnet_resource_id: The Virtual Network Subnet Resource Id of the agent machine
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AgentPoolArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The agentpool that has the ARM resource and properties.
        The agentpool will have all information to create an agent pool.

        :param str resource_name: The name of the resource.
        :param AgentPoolArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AgentPoolArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_pool_name: Optional[pulumi.Input[str]] = None,
                 count: Optional[pulumi.Input[int]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 os: Optional[pulumi.Input[Union[str, 'OS']]] = None,
                 registry_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tier: Optional[pulumi.Input[str]] = None,
                 virtual_network_subnet_resource_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = AgentPoolArgs.__new__(AgentPoolArgs)

            __props__.__dict__["agent_pool_name"] = agent_pool_name
            __props__.__dict__["count"] = count
            __props__.__dict__["location"] = location
            __props__.__dict__["os"] = os
            if registry_name is None and not opts.urn:
                raise TypeError("Missing required property 'registry_name'")
            __props__.__dict__["registry_name"] = registry_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["tier"] = tier
            __props__.__dict__["virtual_network_subnet_resource_id"] = virtual_network_subnet_resource_id
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:containerregistry:AgentPool")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AgentPool, __self__).__init__(
            'azure-native:containerregistry/v20190601preview:AgentPool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AgentPool':
        """
        Get an existing AgentPool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AgentPoolArgs.__new__(AgentPoolArgs)

        __props__.__dict__["count"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["os"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["tier"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["virtual_network_subnet_resource_id"] = None
        return AgentPool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def count(self) -> pulumi.Output[Optional[int]]:
        """
        The count of agent machine
        """
        return pulumi.get(self, "count")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The location of the resource. This cannot be changed after the resource is created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def os(self) -> pulumi.Output[Optional[str]]:
        """
        The OS of agent machine
        """
        return pulumi.get(self, "os")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of this agent pool
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def tier(self) -> pulumi.Output[Optional[str]]:
        """
        The Tier of agent machine
        """
        return pulumi.get(self, "tier")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualNetworkSubnetResourceId")
    def virtual_network_subnet_resource_id(self) -> pulumi.Output[Optional[str]]:
        """
        The Virtual Network Subnet Resource Id of the agent machine
        """
        return pulumi.get(self, "virtual_network_subnet_resource_id")

