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

__all__ = ['VolumeArgs', 'Volume']

@pulumi.input_type
class VolumeArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 creation_token: pulumi.Input[str],
                 pool_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 service_level: pulumi.Input[Union[str, 'ServiceLevel']],
                 export_policy: Optional[pulumi.Input['VolumePropertiesExportPolicyArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[Any] = None,
                 usage_threshold: Optional[pulumi.Input[float]] = None,
                 volume_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Volume resource.
        :param pulumi.Input[str] account_name: The name of the NetApp account
        :param pulumi.Input[str] creation_token: A unique file path for the volume. Used when creating mount targets
        :param pulumi.Input[str] pool_name: The name of the capacity pool
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Union[str, 'ServiceLevel']] service_level: The service level of the file system
        :param pulumi.Input['VolumePropertiesExportPolicyArgs'] export_policy: Export policy rule
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] subnet_id: The Azure Resource URI for a delegated subnet. Must have the delegation Microsoft.NetApp/volumes
        :param Any tags: Resource tags
        :param pulumi.Input[float] usage_threshold: Maximum storage quota allowed for a file system in bytes. This is a soft quota used for alerting only. Minimum size is 100 GiB. Upper limit is 100TiB.
        :param pulumi.Input[str] volume_name: The name of the volume
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "creation_token", creation_token)
        pulumi.set(__self__, "pool_name", pool_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if service_level is None:
            service_level = 'Premium'
        pulumi.set(__self__, "service_level", service_level)
        if export_policy is not None:
            pulumi.set(__self__, "export_policy", export_policy)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if subnet_id is not None:
            pulumi.set(__self__, "subnet_id", subnet_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if usage_threshold is None:
            usage_threshold = 107374182400
        if usage_threshold is not None:
            pulumi.set(__self__, "usage_threshold", usage_threshold)
        if volume_name is not None:
            pulumi.set(__self__, "volume_name", volume_name)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        The name of the NetApp account
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="creationToken")
    def creation_token(self) -> pulumi.Input[str]:
        """
        A unique file path for the volume. Used when creating mount targets
        """
        return pulumi.get(self, "creation_token")

    @creation_token.setter
    def creation_token(self, value: pulumi.Input[str]):
        pulumi.set(self, "creation_token", value)

    @property
    @pulumi.getter(name="poolName")
    def pool_name(self) -> pulumi.Input[str]:
        """
        The name of the capacity pool
        """
        return pulumi.get(self, "pool_name")

    @pool_name.setter
    def pool_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "pool_name", value)

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
    @pulumi.getter(name="serviceLevel")
    def service_level(self) -> pulumi.Input[Union[str, 'ServiceLevel']]:
        """
        The service level of the file system
        """
        return pulumi.get(self, "service_level")

    @service_level.setter
    def service_level(self, value: pulumi.Input[Union[str, 'ServiceLevel']]):
        pulumi.set(self, "service_level", value)

    @property
    @pulumi.getter(name="exportPolicy")
    def export_policy(self) -> Optional[pulumi.Input['VolumePropertiesExportPolicyArgs']]:
        """
        Export policy rule
        """
        return pulumi.get(self, "export_policy")

    @export_policy.setter
    def export_policy(self, value: Optional[pulumi.Input['VolumePropertiesExportPolicyArgs']]):
        pulumi.set(self, "export_policy", value)

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
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Azure Resource URI for a delegated subnet. Must have the delegation Microsoft.NetApp/volumes
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subnet_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[Any]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="usageThreshold")
    def usage_threshold(self) -> Optional[pulumi.Input[float]]:
        """
        Maximum storage quota allowed for a file system in bytes. This is a soft quota used for alerting only. Minimum size is 100 GiB. Upper limit is 100TiB.
        """
        return pulumi.get(self, "usage_threshold")

    @usage_threshold.setter
    def usage_threshold(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "usage_threshold", value)

    @property
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the volume
        """
        return pulumi.get(self, "volume_name")

    @volume_name.setter
    def volume_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume_name", value)


class Volume(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 creation_token: Optional[pulumi.Input[str]] = None,
                 export_policy: Optional[pulumi.Input[pulumi.InputType['VolumePropertiesExportPolicyArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 pool_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_level: Optional[pulumi.Input[Union[str, 'ServiceLevel']]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[Any] = None,
                 usage_threshold: Optional[pulumi.Input[float]] = None,
                 volume_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Volume resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the NetApp account
        :param pulumi.Input[str] creation_token: A unique file path for the volume. Used when creating mount targets
        :param pulumi.Input[pulumi.InputType['VolumePropertiesExportPolicyArgs']] export_policy: Export policy rule
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] pool_name: The name of the capacity pool
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Union[str, 'ServiceLevel']] service_level: The service level of the file system
        :param pulumi.Input[str] subnet_id: The Azure Resource URI for a delegated subnet. Must have the delegation Microsoft.NetApp/volumes
        :param Any tags: Resource tags
        :param pulumi.Input[float] usage_threshold: Maximum storage quota allowed for a file system in bytes. This is a soft quota used for alerting only. Minimum size is 100 GiB. Upper limit is 100TiB.
        :param pulumi.Input[str] volume_name: The name of the volume
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VolumeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Volume resource

        :param str resource_name: The name of the resource.
        :param VolumeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VolumeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 creation_token: Optional[pulumi.Input[str]] = None,
                 export_policy: Optional[pulumi.Input[pulumi.InputType['VolumePropertiesExportPolicyArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 pool_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_level: Optional[pulumi.Input[Union[str, 'ServiceLevel']]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[Any] = None,
                 usage_threshold: Optional[pulumi.Input[float]] = None,
                 volume_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = VolumeArgs.__new__(VolumeArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            if creation_token is None and not opts.urn:
                raise TypeError("Missing required property 'creation_token'")
            __props__.__dict__["creation_token"] = creation_token
            __props__.__dict__["export_policy"] = export_policy
            __props__.__dict__["location"] = location
            if pool_name is None and not opts.urn:
                raise TypeError("Missing required property 'pool_name'")
            __props__.__dict__["pool_name"] = pool_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_level is None:
                service_level = 'Premium'
            if service_level is None and not opts.urn:
                raise TypeError("Missing required property 'service_level'")
            __props__.__dict__["service_level"] = service_level
            __props__.__dict__["subnet_id"] = subnet_id
            __props__.__dict__["tags"] = tags
            if usage_threshold is None:
                usage_threshold = 107374182400
            __props__.__dict__["usage_threshold"] = usage_threshold
            __props__.__dict__["volume_name"] = volume_name
            __props__.__dict__["file_system_id"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:netapp:Volume"), pulumi.Alias(type_="azure-native:netapp/v20190501:Volume"), pulumi.Alias(type_="azure-native:netapp/v20190601:Volume"), pulumi.Alias(type_="azure-native:netapp/v20190701:Volume"), pulumi.Alias(type_="azure-native:netapp/v20190801:Volume"), pulumi.Alias(type_="azure-native:netapp/v20191001:Volume"), pulumi.Alias(type_="azure-native:netapp/v20191101:Volume"), pulumi.Alias(type_="azure-native:netapp/v20200201:Volume"), pulumi.Alias(type_="azure-native:netapp/v20200301:Volume"), pulumi.Alias(type_="azure-native:netapp/v20200501:Volume"), pulumi.Alias(type_="azure-native:netapp/v20200601:Volume"), pulumi.Alias(type_="azure-native:netapp/v20200701:Volume"), pulumi.Alias(type_="azure-native:netapp/v20200801:Volume"), pulumi.Alias(type_="azure-native:netapp/v20200901:Volume"), pulumi.Alias(type_="azure-native:netapp/v20201101:Volume"), pulumi.Alias(type_="azure-native:netapp/v20201201:Volume"), pulumi.Alias(type_="azure-native:netapp/v20210201:Volume"), pulumi.Alias(type_="azure-native:netapp/v20210401:Volume"), pulumi.Alias(type_="azure-native:netapp/v20210401preview:Volume"), pulumi.Alias(type_="azure-native:netapp/v20210601:Volume"), pulumi.Alias(type_="azure-native:netapp/v20210801:Volume")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Volume, __self__).__init__(
            'azure-native:netapp/v20170815:Volume',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Volume':
        """
        Get an existing Volume resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VolumeArgs.__new__(VolumeArgs)

        __props__.__dict__["creation_token"] = None
        __props__.__dict__["export_policy"] = None
        __props__.__dict__["file_system_id"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["service_level"] = None
        __props__.__dict__["subnet_id"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["usage_threshold"] = None
        return Volume(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationToken")
    def creation_token(self) -> pulumi.Output[str]:
        """
        A unique file path for the volume. Used when creating mount targets
        """
        return pulumi.get(self, "creation_token")

    @property
    @pulumi.getter(name="exportPolicy")
    def export_policy(self) -> pulumi.Output[Optional['outputs.VolumePropertiesResponseExportPolicy']]:
        """
        Export policy rule
        """
        return pulumi.get(self, "export_policy")

    @property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> pulumi.Output[str]:
        """
        Unique FileSystem Identifier.
        """
        return pulumi.get(self, "file_system_id")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Azure lifecycle management
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="serviceLevel")
    def service_level(self) -> pulumi.Output[str]:
        """
        The service level of the file system
        """
        return pulumi.get(self, "service_level")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[Optional[str]]:
        """
        The Azure Resource URI for a delegated subnet. Must have the delegation Microsoft.NetApp/volumes
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Any]]:
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

    @property
    @pulumi.getter(name="usageThreshold")
    def usage_threshold(self) -> pulumi.Output[Optional[float]]:
        """
        Maximum storage quota allowed for a file system in bytes. This is a soft quota used for alerting only. Minimum size is 100 GiB. Upper limit is 100TiB.
        """
        return pulumi.get(self, "usage_threshold")

