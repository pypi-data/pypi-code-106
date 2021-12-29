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

__all__ = ['CustomLocationArgs', 'CustomLocation']

@pulumi.input_type
class CustomLocationArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 authentication: Optional[pulumi.Input['CustomLocationPropertiesAuthenticationArgs']] = None,
                 cluster_extension_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 host_resource_id: Optional[pulumi.Input[str]] = None,
                 host_type: Optional[pulumi.Input[Union[str, 'HostType']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a CustomLocation resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['CustomLocationPropertiesAuthenticationArgs'] authentication: This is optional input that contains the authentication that should be used to generate the namespace.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] cluster_extension_ids: Contains the reference to the add-on that contains charts to deploy CRDs and operators.
        :param pulumi.Input[str] display_name: Display name for the Custom Locations location.
        :param pulumi.Input[str] host_resource_id: Connected Cluster or AKS Cluster. The Custom Locations RP will perform a checkAccess API for listAdminCredentials permissions.
        :param pulumi.Input[Union[str, 'HostType']] host_type: Type of host the Custom Locations is referencing (Kubernetes, etc...).
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] namespace: Kubernetes namespace that will be created on the specified cluster.
        :param pulumi.Input[str] provisioning_state: Provisioning State for the Custom Location.
        :param pulumi.Input[str] resource_name: Custom Locations name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if authentication is not None:
            pulumi.set(__self__, "authentication", authentication)
        if cluster_extension_ids is not None:
            pulumi.set(__self__, "cluster_extension_ids", cluster_extension_ids)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if host_resource_id is not None:
            pulumi.set(__self__, "host_resource_id", host_resource_id)
        if host_type is not None:
            pulumi.set(__self__, "host_type", host_type)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if resource_name is not None:
            pulumi.set(__self__, "resource_name", resource_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def authentication(self) -> Optional[pulumi.Input['CustomLocationPropertiesAuthenticationArgs']]:
        """
        This is optional input that contains the authentication that should be used to generate the namespace.
        """
        return pulumi.get(self, "authentication")

    @authentication.setter
    def authentication(self, value: Optional[pulumi.Input['CustomLocationPropertiesAuthenticationArgs']]):
        pulumi.set(self, "authentication", value)

    @property
    @pulumi.getter(name="clusterExtensionIds")
    def cluster_extension_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Contains the reference to the add-on that contains charts to deploy CRDs and operators.
        """
        return pulumi.get(self, "cluster_extension_ids")

    @cluster_extension_ids.setter
    def cluster_extension_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "cluster_extension_ids", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Display name for the Custom Locations location.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="hostResourceId")
    def host_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        Connected Cluster or AKS Cluster. The Custom Locations RP will perform a checkAccess API for listAdminCredentials permissions.
        """
        return pulumi.get(self, "host_resource_id")

    @host_resource_id.setter
    def host_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host_resource_id", value)

    @property
    @pulumi.getter(name="hostType")
    def host_type(self) -> Optional[pulumi.Input[Union[str, 'HostType']]]:
        """
        Type of host the Custom Locations is referencing (Kubernetes, etc...).
        """
        return pulumi.get(self, "host_type")

    @host_type.setter
    def host_type(self, value: Optional[pulumi.Input[Union[str, 'HostType']]]):
        pulumi.set(self, "host_type", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        Kubernetes namespace that will be created on the specified cluster.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[str]]:
        """
        Provisioning State for the Custom Location.
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        Custom Locations name.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_name", value)

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


class CustomLocation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication: Optional[pulumi.Input[pulumi.InputType['CustomLocationPropertiesAuthenticationArgs']]] = None,
                 cluster_extension_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 host_resource_id: Optional[pulumi.Input[str]] = None,
                 host_type: Optional[pulumi.Input[Union[str, 'HostType']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Custom Locations definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['CustomLocationPropertiesAuthenticationArgs']] authentication: This is optional input that contains the authentication that should be used to generate the namespace.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] cluster_extension_ids: Contains the reference to the add-on that contains charts to deploy CRDs and operators.
        :param pulumi.Input[str] display_name: Display name for the Custom Locations location.
        :param pulumi.Input[str] host_resource_id: Connected Cluster or AKS Cluster. The Custom Locations RP will perform a checkAccess API for listAdminCredentials permissions.
        :param pulumi.Input[Union[str, 'HostType']] host_type: Type of host the Custom Locations is referencing (Kubernetes, etc...).
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] namespace: Kubernetes namespace that will be created on the specified cluster.
        :param pulumi.Input[str] provisioning_state: Provisioning State for the Custom Location.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_name_: Custom Locations name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CustomLocationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Custom Locations definition.

        :param str resource_name: The name of the resource.
        :param CustomLocationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CustomLocationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication: Optional[pulumi.Input[pulumi.InputType['CustomLocationPropertiesAuthenticationArgs']]] = None,
                 cluster_extension_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 host_resource_id: Optional[pulumi.Input[str]] = None,
                 host_type: Optional[pulumi.Input[Union[str, 'HostType']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
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
            __props__ = CustomLocationArgs.__new__(CustomLocationArgs)

            __props__.__dict__["authentication"] = authentication
            __props__.__dict__["cluster_extension_ids"] = cluster_extension_ids
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["host_resource_id"] = host_resource_id
            __props__.__dict__["host_type"] = host_type
            __props__.__dict__["location"] = location
            __props__.__dict__["namespace"] = namespace
            __props__.__dict__["provisioning_state"] = provisioning_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:extendedlocation:CustomLocation"), pulumi.Alias(type_="azure-native:extendedlocation/v20210815:CustomLocation")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(CustomLocation, __self__).__init__(
            'azure-native:extendedlocation/v20210315preview:CustomLocation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CustomLocation':
        """
        Get an existing CustomLocation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CustomLocationArgs.__new__(CustomLocationArgs)

        __props__.__dict__["authentication"] = None
        __props__.__dict__["cluster_extension_ids"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["host_resource_id"] = None
        __props__.__dict__["host_type"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["namespace"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return CustomLocation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def authentication(self) -> pulumi.Output[Optional['outputs.CustomLocationPropertiesResponseAuthentication']]:
        """
        This is optional input that contains the authentication that should be used to generate the namespace.
        """
        return pulumi.get(self, "authentication")

    @property
    @pulumi.getter(name="clusterExtensionIds")
    def cluster_extension_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Contains the reference to the add-on that contains charts to deploy CRDs and operators.
        """
        return pulumi.get(self, "cluster_extension_ids")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        Display name for the Custom Locations location.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="hostResourceId")
    def host_resource_id(self) -> pulumi.Output[Optional[str]]:
        """
        Connected Cluster or AKS Cluster. The Custom Locations RP will perform a checkAccess API for listAdminCredentials permissions.
        """
        return pulumi.get(self, "host_resource_id")

    @property
    @pulumi.getter(name="hostType")
    def host_type(self) -> pulumi.Output[Optional[str]]:
        """
        Type of host the Custom Locations is referencing (Kubernetes, etc...).
        """
        return pulumi.get(self, "host_type")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Output[Optional[str]]:
        """
        Kubernetes namespace that will be created on the specified cluster.
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        Provisioning State for the Custom Location.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource
        """
        return pulumi.get(self, "system_data")

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
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

