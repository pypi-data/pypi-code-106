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

__all__ = ['VolumeGroupArgs', 'VolumeGroup']

@pulumi.input_type
class VolumeGroupArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 group_meta_data: Optional[pulumi.Input['VolumeGroupMetaDataArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 volume_group_name: Optional[pulumi.Input[str]] = None,
                 volumes: Optional[pulumi.Input[Sequence[pulumi.Input['VolumeGroupVolumePropertiesArgs']]]] = None):
        """
        The set of arguments for constructing a VolumeGroup resource.
        :param pulumi.Input[str] account_name: The name of the NetApp account
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input['VolumeGroupMetaDataArgs'] group_meta_data: Volume group details
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] volume_group_name: The name of the volumeGroup
        :param pulumi.Input[Sequence[pulumi.Input['VolumeGroupVolumePropertiesArgs']]] volumes: List of volumes from group
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if group_meta_data is not None:
            pulumi.set(__self__, "group_meta_data", group_meta_data)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if volume_group_name is not None:
            pulumi.set(__self__, "volume_group_name", volume_group_name)
        if volumes is not None:
            pulumi.set(__self__, "volumes", volumes)

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
    @pulumi.getter(name="groupMetaData")
    def group_meta_data(self) -> Optional[pulumi.Input['VolumeGroupMetaDataArgs']]:
        """
        Volume group details
        """
        return pulumi.get(self, "group_meta_data")

    @group_meta_data.setter
    def group_meta_data(self, value: Optional[pulumi.Input['VolumeGroupMetaDataArgs']]):
        pulumi.set(self, "group_meta_data", value)

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
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="volumeGroupName")
    def volume_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the volumeGroup
        """
        return pulumi.get(self, "volume_group_name")

    @volume_group_name.setter
    def volume_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume_group_name", value)

    @property
    @pulumi.getter
    def volumes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VolumeGroupVolumePropertiesArgs']]]]:
        """
        List of volumes from group
        """
        return pulumi.get(self, "volumes")

    @volumes.setter
    def volumes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VolumeGroupVolumePropertiesArgs']]]]):
        pulumi.set(self, "volumes", value)


class VolumeGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 group_meta_data: Optional[pulumi.Input[pulumi.InputType['VolumeGroupMetaDataArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 volume_group_name: Optional[pulumi.Input[str]] = None,
                 volumes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VolumeGroupVolumePropertiesArgs']]]]] = None,
                 __props__=None):
        """
        Volume group resource for create

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the NetApp account
        :param pulumi.Input[pulumi.InputType['VolumeGroupMetaDataArgs']] group_meta_data: Volume group details
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] volume_group_name: The name of the volumeGroup
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VolumeGroupVolumePropertiesArgs']]]] volumes: List of volumes from group
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VolumeGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Volume group resource for create

        :param str resource_name: The name of the resource.
        :param VolumeGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VolumeGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 group_meta_data: Optional[pulumi.Input[pulumi.InputType['VolumeGroupMetaDataArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 volume_group_name: Optional[pulumi.Input[str]] = None,
                 volumes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VolumeGroupVolumePropertiesArgs']]]]] = None,
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
            __props__ = VolumeGroupArgs.__new__(VolumeGroupArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["group_meta_data"] = group_meta_data
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["volume_group_name"] = volume_group_name
            __props__.__dict__["volumes"] = volumes
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        super(VolumeGroup, __self__).__init__(
            'azure-native:netapp/v20210801:VolumeGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VolumeGroup':
        """
        Get an existing VolumeGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VolumeGroupArgs.__new__(VolumeGroupArgs)

        __props__.__dict__["group_meta_data"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["volumes"] = None
        return VolumeGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="groupMetaData")
    def group_meta_data(self) -> pulumi.Output[Optional['outputs.VolumeGroupMetaDataResponse']]:
        """
        Volume group details
        """
        return pulumi.get(self, "group_meta_data")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
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

    @property
    @pulumi.getter
    def volumes(self) -> pulumi.Output[Optional[Sequence['outputs.VolumeGroupVolumePropertiesResponse']]]:
        """
        List of volumes from group
        """
        return pulumi.get(self, "volumes")

