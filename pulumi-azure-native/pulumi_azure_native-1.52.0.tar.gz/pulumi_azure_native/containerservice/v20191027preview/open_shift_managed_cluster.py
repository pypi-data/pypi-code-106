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
from ._inputs import *

__all__ = ['OpenShiftManagedClusterArgs', 'OpenShiftManagedCluster']

@pulumi.input_type
class OpenShiftManagedClusterArgs:
    def __init__(__self__, *,
                 open_shift_version: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 agent_pool_profiles: Optional[pulumi.Input[Sequence[pulumi.Input['OpenShiftManagedClusterAgentPoolProfileArgs']]]] = None,
                 auth_profile: Optional[pulumi.Input['OpenShiftManagedClusterAuthProfileArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 master_pool_profile: Optional[pulumi.Input['OpenShiftManagedClusterMasterPoolProfileArgs']] = None,
                 monitor_profile: Optional[pulumi.Input['OpenShiftManagedClusterMonitorProfileArgs']] = None,
                 network_profile: Optional[pulumi.Input['NetworkProfileArgs']] = None,
                 plan: Optional[pulumi.Input['PurchasePlanArgs']] = None,
                 refresh_cluster: Optional[pulumi.Input[bool]] = None,
                 resource_name: Optional[pulumi.Input[str]] = None,
                 router_profiles: Optional[pulumi.Input[Sequence[pulumi.Input['OpenShiftRouterProfileArgs']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a OpenShiftManagedCluster resource.
        :param pulumi.Input[str] open_shift_version: Version of OpenShift specified when creating the cluster.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Sequence[pulumi.Input['OpenShiftManagedClusterAgentPoolProfileArgs']]] agent_pool_profiles: Configuration of OpenShift cluster VMs.
        :param pulumi.Input['OpenShiftManagedClusterAuthProfileArgs'] auth_profile: Configures OpenShift authentication.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input['OpenShiftManagedClusterMasterPoolProfileArgs'] master_pool_profile: Configuration for OpenShift master VMs.
        :param pulumi.Input['OpenShiftManagedClusterMonitorProfileArgs'] monitor_profile: Configures Log Analytics integration.
        :param pulumi.Input['NetworkProfileArgs'] network_profile: Configuration for OpenShift networking.
        :param pulumi.Input['PurchasePlanArgs'] plan: Define the resource plan as required by ARM for billing purposes
        :param pulumi.Input[bool] refresh_cluster: Allows node rotation
        :param pulumi.Input[str] resource_name: The name of the OpenShift managed cluster resource.
        :param pulumi.Input[Sequence[pulumi.Input['OpenShiftRouterProfileArgs']]] router_profiles: Configuration for OpenShift router(s).
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        pulumi.set(__self__, "open_shift_version", open_shift_version)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if agent_pool_profiles is not None:
            pulumi.set(__self__, "agent_pool_profiles", agent_pool_profiles)
        if auth_profile is not None:
            pulumi.set(__self__, "auth_profile", auth_profile)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if master_pool_profile is not None:
            pulumi.set(__self__, "master_pool_profile", master_pool_profile)
        if monitor_profile is not None:
            pulumi.set(__self__, "monitor_profile", monitor_profile)
        if network_profile is not None:
            pulumi.set(__self__, "network_profile", network_profile)
        if plan is not None:
            pulumi.set(__self__, "plan", plan)
        if refresh_cluster is not None:
            pulumi.set(__self__, "refresh_cluster", refresh_cluster)
        if resource_name is not None:
            pulumi.set(__self__, "resource_name", resource_name)
        if router_profiles is not None:
            pulumi.set(__self__, "router_profiles", router_profiles)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="openShiftVersion")
    def open_shift_version(self) -> pulumi.Input[str]:
        """
        Version of OpenShift specified when creating the cluster.
        """
        return pulumi.get(self, "open_shift_version")

    @open_shift_version.setter
    def open_shift_version(self, value: pulumi.Input[str]):
        pulumi.set(self, "open_shift_version", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="agentPoolProfiles")
    def agent_pool_profiles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['OpenShiftManagedClusterAgentPoolProfileArgs']]]]:
        """
        Configuration of OpenShift cluster VMs.
        """
        return pulumi.get(self, "agent_pool_profiles")

    @agent_pool_profiles.setter
    def agent_pool_profiles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['OpenShiftManagedClusterAgentPoolProfileArgs']]]]):
        pulumi.set(self, "agent_pool_profiles", value)

    @property
    @pulumi.getter(name="authProfile")
    def auth_profile(self) -> Optional[pulumi.Input['OpenShiftManagedClusterAuthProfileArgs']]:
        """
        Configures OpenShift authentication.
        """
        return pulumi.get(self, "auth_profile")

    @auth_profile.setter
    def auth_profile(self, value: Optional[pulumi.Input['OpenShiftManagedClusterAuthProfileArgs']]):
        pulumi.set(self, "auth_profile", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="masterPoolProfile")
    def master_pool_profile(self) -> Optional[pulumi.Input['OpenShiftManagedClusterMasterPoolProfileArgs']]:
        """
        Configuration for OpenShift master VMs.
        """
        return pulumi.get(self, "master_pool_profile")

    @master_pool_profile.setter
    def master_pool_profile(self, value: Optional[pulumi.Input['OpenShiftManagedClusterMasterPoolProfileArgs']]):
        pulumi.set(self, "master_pool_profile", value)

    @property
    @pulumi.getter(name="monitorProfile")
    def monitor_profile(self) -> Optional[pulumi.Input['OpenShiftManagedClusterMonitorProfileArgs']]:
        """
        Configures Log Analytics integration.
        """
        return pulumi.get(self, "monitor_profile")

    @monitor_profile.setter
    def monitor_profile(self, value: Optional[pulumi.Input['OpenShiftManagedClusterMonitorProfileArgs']]):
        pulumi.set(self, "monitor_profile", value)

    @property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[pulumi.Input['NetworkProfileArgs']]:
        """
        Configuration for OpenShift networking.
        """
        return pulumi.get(self, "network_profile")

    @network_profile.setter
    def network_profile(self, value: Optional[pulumi.Input['NetworkProfileArgs']]):
        pulumi.set(self, "network_profile", value)

    @property
    @pulumi.getter
    def plan(self) -> Optional[pulumi.Input['PurchasePlanArgs']]:
        """
        Define the resource plan as required by ARM for billing purposes
        """
        return pulumi.get(self, "plan")

    @plan.setter
    def plan(self, value: Optional[pulumi.Input['PurchasePlanArgs']]):
        pulumi.set(self, "plan", value)

    @property
    @pulumi.getter(name="refreshCluster")
    def refresh_cluster(self) -> Optional[pulumi.Input[bool]]:
        """
        Allows node rotation
        """
        return pulumi.get(self, "refresh_cluster")

    @refresh_cluster.setter
    def refresh_cluster(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "refresh_cluster", value)

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the OpenShift managed cluster resource.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter(name="routerProfiles")
    def router_profiles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['OpenShiftRouterProfileArgs']]]]:
        """
        Configuration for OpenShift router(s).
        """
        return pulumi.get(self, "router_profiles")

    @router_profiles.setter
    def router_profiles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['OpenShiftRouterProfileArgs']]]]):
        pulumi.set(self, "router_profiles", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class OpenShiftManagedCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_pool_profiles: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OpenShiftManagedClusterAgentPoolProfileArgs']]]]] = None,
                 auth_profile: Optional[pulumi.Input[pulumi.InputType['OpenShiftManagedClusterAuthProfileArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 master_pool_profile: Optional[pulumi.Input[pulumi.InputType['OpenShiftManagedClusterMasterPoolProfileArgs']]] = None,
                 monitor_profile: Optional[pulumi.Input[pulumi.InputType['OpenShiftManagedClusterMonitorProfileArgs']]] = None,
                 network_profile: Optional[pulumi.Input[pulumi.InputType['NetworkProfileArgs']]] = None,
                 open_shift_version: Optional[pulumi.Input[str]] = None,
                 plan: Optional[pulumi.Input[pulumi.InputType['PurchasePlanArgs']]] = None,
                 refresh_cluster: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 router_profiles: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OpenShiftRouterProfileArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        OpenShift Managed cluster.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OpenShiftManagedClusterAgentPoolProfileArgs']]]] agent_pool_profiles: Configuration of OpenShift cluster VMs.
        :param pulumi.Input[pulumi.InputType['OpenShiftManagedClusterAuthProfileArgs']] auth_profile: Configures OpenShift authentication.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[pulumi.InputType['OpenShiftManagedClusterMasterPoolProfileArgs']] master_pool_profile: Configuration for OpenShift master VMs.
        :param pulumi.Input[pulumi.InputType['OpenShiftManagedClusterMonitorProfileArgs']] monitor_profile: Configures Log Analytics integration.
        :param pulumi.Input[pulumi.InputType['NetworkProfileArgs']] network_profile: Configuration for OpenShift networking.
        :param pulumi.Input[str] open_shift_version: Version of OpenShift specified when creating the cluster.
        :param pulumi.Input[pulumi.InputType['PurchasePlanArgs']] plan: Define the resource plan as required by ARM for billing purposes
        :param pulumi.Input[bool] refresh_cluster: Allows node rotation
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] resource_name_: The name of the OpenShift managed cluster resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OpenShiftRouterProfileArgs']]]] router_profiles: Configuration for OpenShift router(s).
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OpenShiftManagedClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        OpenShift Managed cluster.

        :param str resource_name: The name of the resource.
        :param OpenShiftManagedClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OpenShiftManagedClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_pool_profiles: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OpenShiftManagedClusterAgentPoolProfileArgs']]]]] = None,
                 auth_profile: Optional[pulumi.Input[pulumi.InputType['OpenShiftManagedClusterAuthProfileArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 master_pool_profile: Optional[pulumi.Input[pulumi.InputType['OpenShiftManagedClusterMasterPoolProfileArgs']]] = None,
                 monitor_profile: Optional[pulumi.Input[pulumi.InputType['OpenShiftManagedClusterMonitorProfileArgs']]] = None,
                 network_profile: Optional[pulumi.Input[pulumi.InputType['NetworkProfileArgs']]] = None,
                 open_shift_version: Optional[pulumi.Input[str]] = None,
                 plan: Optional[pulumi.Input[pulumi.InputType['PurchasePlanArgs']]] = None,
                 refresh_cluster: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 router_profiles: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OpenShiftRouterProfileArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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
            __props__ = OpenShiftManagedClusterArgs.__new__(OpenShiftManagedClusterArgs)

            __props__.__dict__["agent_pool_profiles"] = agent_pool_profiles
            __props__.__dict__["auth_profile"] = auth_profile
            __props__.__dict__["location"] = location
            __props__.__dict__["master_pool_profile"] = master_pool_profile
            __props__.__dict__["monitor_profile"] = monitor_profile
            __props__.__dict__["network_profile"] = network_profile
            if open_shift_version is None and not opts.urn:
                raise TypeError("Missing required property 'open_shift_version'")
            __props__.__dict__["open_shift_version"] = open_shift_version
            __props__.__dict__["plan"] = plan
            __props__.__dict__["refresh_cluster"] = refresh_cluster
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["router_profiles"] = router_profiles
            __props__.__dict__["tags"] = tags
            __props__.__dict__["cluster_version"] = None
            __props__.__dict__["fqdn"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["public_hostname"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:containerservice:OpenShiftManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20180930preview:OpenShiftManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20190430:OpenShiftManagedCluster"), pulumi.Alias(type_="azure-native:containerservice/v20190930preview:OpenShiftManagedCluster")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(OpenShiftManagedCluster, __self__).__init__(
            'azure-native:containerservice/v20191027preview:OpenShiftManagedCluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'OpenShiftManagedCluster':
        """
        Get an existing OpenShiftManagedCluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OpenShiftManagedClusterArgs.__new__(OpenShiftManagedClusterArgs)

        __props__.__dict__["agent_pool_profiles"] = None
        __props__.__dict__["auth_profile"] = None
        __props__.__dict__["cluster_version"] = None
        __props__.__dict__["fqdn"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["master_pool_profile"] = None
        __props__.__dict__["monitor_profile"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_profile"] = None
        __props__.__dict__["open_shift_version"] = None
        __props__.__dict__["plan"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["public_hostname"] = None
        __props__.__dict__["refresh_cluster"] = None
        __props__.__dict__["router_profiles"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return OpenShiftManagedCluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="agentPoolProfiles")
    def agent_pool_profiles(self) -> pulumi.Output[Optional[Sequence['outputs.OpenShiftManagedClusterAgentPoolProfileResponse']]]:
        """
        Configuration of OpenShift cluster VMs.
        """
        return pulumi.get(self, "agent_pool_profiles")

    @property
    @pulumi.getter(name="authProfile")
    def auth_profile(self) -> pulumi.Output[Optional['outputs.OpenShiftManagedClusterAuthProfileResponse']]:
        """
        Configures OpenShift authentication.
        """
        return pulumi.get(self, "auth_profile")

    @property
    @pulumi.getter(name="clusterVersion")
    def cluster_version(self) -> pulumi.Output[str]:
        """
        Version of OpenShift specified when creating the cluster.
        """
        return pulumi.get(self, "cluster_version")

    @property
    @pulumi.getter
    def fqdn(self) -> pulumi.Output[str]:
        """
        Service generated FQDN for OpenShift API server loadbalancer internal hostname.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="masterPoolProfile")
    def master_pool_profile(self) -> pulumi.Output[Optional['outputs.OpenShiftManagedClusterMasterPoolProfileResponse']]:
        """
        Configuration for OpenShift master VMs.
        """
        return pulumi.get(self, "master_pool_profile")

    @property
    @pulumi.getter(name="monitorProfile")
    def monitor_profile(self) -> pulumi.Output[Optional['outputs.OpenShiftManagedClusterMonitorProfileResponse']]:
        """
        Configures Log Analytics integration.
        """
        return pulumi.get(self, "monitor_profile")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> pulumi.Output[Optional['outputs.NetworkProfileResponse']]:
        """
        Configuration for OpenShift networking.
        """
        return pulumi.get(self, "network_profile")

    @property
    @pulumi.getter(name="openShiftVersion")
    def open_shift_version(self) -> pulumi.Output[str]:
        """
        Version of OpenShift specified when creating the cluster.
        """
        return pulumi.get(self, "open_shift_version")

    @property
    @pulumi.getter
    def plan(self) -> pulumi.Output[Optional['outputs.PurchasePlanResponse']]:
        """
        Define the resource plan as required by ARM for billing purposes
        """
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The current deployment or provisioning state, which only appears in the response.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicHostname")
    def public_hostname(self) -> pulumi.Output[str]:
        """
        Service generated FQDN or private IP for OpenShift API server.
        """
        return pulumi.get(self, "public_hostname")

    @property
    @pulumi.getter(name="refreshCluster")
    def refresh_cluster(self) -> pulumi.Output[Optional[bool]]:
        """
        Allows node rotation
        """
        return pulumi.get(self, "refresh_cluster")

    @property
    @pulumi.getter(name="routerProfiles")
    def router_profiles(self) -> pulumi.Output[Optional[Sequence['outputs.OpenShiftRouterProfileResponse']]]:
        """
        Configuration for OpenShift router(s).
        """
        return pulumi.get(self, "router_profiles")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

