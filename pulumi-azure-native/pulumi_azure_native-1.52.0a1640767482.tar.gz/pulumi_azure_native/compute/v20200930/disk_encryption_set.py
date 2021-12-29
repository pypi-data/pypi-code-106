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

__all__ = ['DiskEncryptionSetArgs', 'DiskEncryptionSet']

@pulumi.input_type
class DiskEncryptionSetArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 active_key: Optional[pulumi.Input['KeyForDiskEncryptionSetArgs']] = None,
                 disk_encryption_set_name: Optional[pulumi.Input[str]] = None,
                 encryption_type: Optional[pulumi.Input[Union[str, 'DiskEncryptionSetType']]] = None,
                 identity: Optional[pulumi.Input['EncryptionSetIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a DiskEncryptionSet resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input['KeyForDiskEncryptionSetArgs'] active_key: The key vault key which is currently used by this disk encryption set.
        :param pulumi.Input[str] disk_encryption_set_name: The name of the disk encryption set that is being created. The name can't be changed after the disk encryption set is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters.
        :param pulumi.Input[Union[str, 'DiskEncryptionSetType']] encryption_type: The type of key used to encrypt the data of the disk.
        :param pulumi.Input['EncryptionSetIdentityArgs'] identity: The managed identity for the disk encryption set. It should be given permission on the key vault before it can be used to encrypt disks.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if active_key is not None:
            pulumi.set(__self__, "active_key", active_key)
        if disk_encryption_set_name is not None:
            pulumi.set(__self__, "disk_encryption_set_name", disk_encryption_set_name)
        if encryption_type is not None:
            pulumi.set(__self__, "encryption_type", encryption_type)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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
    @pulumi.getter(name="activeKey")
    def active_key(self) -> Optional[pulumi.Input['KeyForDiskEncryptionSetArgs']]:
        """
        The key vault key which is currently used by this disk encryption set.
        """
        return pulumi.get(self, "active_key")

    @active_key.setter
    def active_key(self, value: Optional[pulumi.Input['KeyForDiskEncryptionSetArgs']]):
        pulumi.set(self, "active_key", value)

    @property
    @pulumi.getter(name="diskEncryptionSetName")
    def disk_encryption_set_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the disk encryption set that is being created. The name can't be changed after the disk encryption set is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters.
        """
        return pulumi.get(self, "disk_encryption_set_name")

    @disk_encryption_set_name.setter
    def disk_encryption_set_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "disk_encryption_set_name", value)

    @property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> Optional[pulumi.Input[Union[str, 'DiskEncryptionSetType']]]:
        """
        The type of key used to encrypt the data of the disk.
        """
        return pulumi.get(self, "encryption_type")

    @encryption_type.setter
    def encryption_type(self, value: Optional[pulumi.Input[Union[str, 'DiskEncryptionSetType']]]):
        pulumi.set(self, "encryption_type", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['EncryptionSetIdentityArgs']]:
        """
        The managed identity for the disk encryption set. It should be given permission on the key vault before it can be used to encrypt disks.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['EncryptionSetIdentityArgs']]):
        pulumi.set(self, "identity", value)

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


class DiskEncryptionSet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active_key: Optional[pulumi.Input[pulumi.InputType['KeyForDiskEncryptionSetArgs']]] = None,
                 disk_encryption_set_name: Optional[pulumi.Input[str]] = None,
                 encryption_type: Optional[pulumi.Input[Union[str, 'DiskEncryptionSetType']]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['EncryptionSetIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        disk encryption set resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['KeyForDiskEncryptionSetArgs']] active_key: The key vault key which is currently used by this disk encryption set.
        :param pulumi.Input[str] disk_encryption_set_name: The name of the disk encryption set that is being created. The name can't be changed after the disk encryption set is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters.
        :param pulumi.Input[Union[str, 'DiskEncryptionSetType']] encryption_type: The type of key used to encrypt the data of the disk.
        :param pulumi.Input[pulumi.InputType['EncryptionSetIdentityArgs']] identity: The managed identity for the disk encryption set. It should be given permission on the key vault before it can be used to encrypt disks.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DiskEncryptionSetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        disk encryption set resource.

        :param str resource_name: The name of the resource.
        :param DiskEncryptionSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DiskEncryptionSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active_key: Optional[pulumi.Input[pulumi.InputType['KeyForDiskEncryptionSetArgs']]] = None,
                 disk_encryption_set_name: Optional[pulumi.Input[str]] = None,
                 encryption_type: Optional[pulumi.Input[Union[str, 'DiskEncryptionSetType']]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['EncryptionSetIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = DiskEncryptionSetArgs.__new__(DiskEncryptionSetArgs)

            __props__.__dict__["active_key"] = active_key
            __props__.__dict__["disk_encryption_set_name"] = disk_encryption_set_name
            __props__.__dict__["encryption_type"] = encryption_type
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["previous_keys"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:compute:DiskEncryptionSet"), pulumi.Alias(type_="azure-native:compute/v20190701:DiskEncryptionSet"), pulumi.Alias(type_="azure-native:compute/v20191101:DiskEncryptionSet"), pulumi.Alias(type_="azure-native:compute/v20200501:DiskEncryptionSet"), pulumi.Alias(type_="azure-native:compute/v20200630:DiskEncryptionSet"), pulumi.Alias(type_="azure-native:compute/v20201201:DiskEncryptionSet"), pulumi.Alias(type_="azure-native:compute/v20210401:DiskEncryptionSet"), pulumi.Alias(type_="azure-native:compute/v20210801:DiskEncryptionSet")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DiskEncryptionSet, __self__).__init__(
            'azure-native:compute/v20200930:DiskEncryptionSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DiskEncryptionSet':
        """
        Get an existing DiskEncryptionSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DiskEncryptionSetArgs.__new__(DiskEncryptionSetArgs)

        __props__.__dict__["active_key"] = None
        __props__.__dict__["encryption_type"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["previous_keys"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return DiskEncryptionSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="activeKey")
    def active_key(self) -> pulumi.Output[Optional['outputs.KeyForDiskEncryptionSetResponse']]:
        """
        The key vault key which is currently used by this disk encryption set.
        """
        return pulumi.get(self, "active_key")

    @property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of key used to encrypt the data of the disk.
        """
        return pulumi.get(self, "encryption_type")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.EncryptionSetIdentityResponse']]:
        """
        The managed identity for the disk encryption set. It should be given permission on the key vault before it can be used to encrypt disks.
        """
        return pulumi.get(self, "identity")

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
    @pulumi.getter(name="previousKeys")
    def previous_keys(self) -> pulumi.Output[Sequence['outputs.KeyForDiskEncryptionSetResponse']]:
        """
        A readonly collection of key vault keys previously used by this disk encryption set while a key rotation is in progress. It will be empty if there is no ongoing key rotation.
        """
        return pulumi.get(self, "previous_keys")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The disk encryption set provisioning state.
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

