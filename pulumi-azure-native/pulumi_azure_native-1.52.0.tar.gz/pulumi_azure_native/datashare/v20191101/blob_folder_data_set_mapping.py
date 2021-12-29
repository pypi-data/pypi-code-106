# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['BlobFolderDataSetMappingArgs', 'BlobFolderDataSetMapping']

@pulumi.input_type
class BlobFolderDataSetMappingArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 container_name: pulumi.Input[str],
                 data_set_id: pulumi.Input[str],
                 kind: pulumi.Input[str],
                 prefix: pulumi.Input[str],
                 resource_group: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 share_subscription_name: pulumi.Input[str],
                 storage_account_name: pulumi.Input[str],
                 subscription_id: pulumi.Input[str],
                 data_set_mapping_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a BlobFolderDataSetMapping resource.
        :param pulumi.Input[str] account_name: The name of the share account.
        :param pulumi.Input[str] container_name: Container that has the file path.
        :param pulumi.Input[str] data_set_id: The id of the source data set.
        :param pulumi.Input[str] kind: Kind of data set mapping.
               Expected value is 'BlobFolder'.
        :param pulumi.Input[str] prefix: Prefix for blob folder
        :param pulumi.Input[str] resource_group: Resource group of storage account.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] share_subscription_name: The name of the share subscription which will hold the data set sink.
        :param pulumi.Input[str] storage_account_name: Storage account name of the source data set.
        :param pulumi.Input[str] subscription_id: Subscription id of storage account.
        :param pulumi.Input[str] data_set_mapping_name: The name of the data set mapping to be created.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "container_name", container_name)
        pulumi.set(__self__, "data_set_id", data_set_id)
        pulumi.set(__self__, "kind", 'BlobFolder')
        pulumi.set(__self__, "prefix", prefix)
        pulumi.set(__self__, "resource_group", resource_group)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "share_subscription_name", share_subscription_name)
        pulumi.set(__self__, "storage_account_name", storage_account_name)
        pulumi.set(__self__, "subscription_id", subscription_id)
        if data_set_mapping_name is not None:
            pulumi.set(__self__, "data_set_mapping_name", data_set_mapping_name)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        The name of the share account.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="containerName")
    def container_name(self) -> pulumi.Input[str]:
        """
        Container that has the file path.
        """
        return pulumi.get(self, "container_name")

    @container_name.setter
    def container_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "container_name", value)

    @property
    @pulumi.getter(name="dataSetId")
    def data_set_id(self) -> pulumi.Input[str]:
        """
        The id of the source data set.
        """
        return pulumi.get(self, "data_set_id")

    @data_set_id.setter
    def data_set_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "data_set_id", value)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        Kind of data set mapping.
        Expected value is 'BlobFolder'.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def prefix(self) -> pulumi.Input[str]:
        """
        Prefix for blob folder
        """
        return pulumi.get(self, "prefix")

    @prefix.setter
    def prefix(self, value: pulumi.Input[str]):
        pulumi.set(self, "prefix", value)

    @property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> pulumi.Input[str]:
        """
        Resource group of storage account.
        """
        return pulumi.get(self, "resource_group")

    @resource_group.setter
    def resource_group(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="shareSubscriptionName")
    def share_subscription_name(self) -> pulumi.Input[str]:
        """
        The name of the share subscription which will hold the data set sink.
        """
        return pulumi.get(self, "share_subscription_name")

    @share_subscription_name.setter
    def share_subscription_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "share_subscription_name", value)

    @property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> pulumi.Input[str]:
        """
        Storage account name of the source data set.
        """
        return pulumi.get(self, "storage_account_name")

    @storage_account_name.setter
    def storage_account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "storage_account_name", value)

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> pulumi.Input[str]:
        """
        Subscription id of storage account.
        """
        return pulumi.get(self, "subscription_id")

    @subscription_id.setter
    def subscription_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "subscription_id", value)

    @property
    @pulumi.getter(name="dataSetMappingName")
    def data_set_mapping_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the data set mapping to be created.
        """
        return pulumi.get(self, "data_set_mapping_name")

    @data_set_mapping_name.setter
    def data_set_mapping_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_set_mapping_name", value)


class BlobFolderDataSetMapping(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 container_name: Optional[pulumi.Input[str]] = None,
                 data_set_id: Optional[pulumi.Input[str]] = None,
                 data_set_mapping_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 prefix: Optional[pulumi.Input[str]] = None,
                 resource_group: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 share_subscription_name: Optional[pulumi.Input[str]] = None,
                 storage_account_name: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A Blob folder data set mapping.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the share account.
        :param pulumi.Input[str] container_name: Container that has the file path.
        :param pulumi.Input[str] data_set_id: The id of the source data set.
        :param pulumi.Input[str] data_set_mapping_name: The name of the data set mapping to be created.
        :param pulumi.Input[str] kind: Kind of data set mapping.
               Expected value is 'BlobFolder'.
        :param pulumi.Input[str] prefix: Prefix for blob folder
        :param pulumi.Input[str] resource_group: Resource group of storage account.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] share_subscription_name: The name of the share subscription which will hold the data set sink.
        :param pulumi.Input[str] storage_account_name: Storage account name of the source data set.
        :param pulumi.Input[str] subscription_id: Subscription id of storage account.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BlobFolderDataSetMappingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A Blob folder data set mapping.

        :param str resource_name: The name of the resource.
        :param BlobFolderDataSetMappingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BlobFolderDataSetMappingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 container_name: Optional[pulumi.Input[str]] = None,
                 data_set_id: Optional[pulumi.Input[str]] = None,
                 data_set_mapping_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 prefix: Optional[pulumi.Input[str]] = None,
                 resource_group: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 share_subscription_name: Optional[pulumi.Input[str]] = None,
                 storage_account_name: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = BlobFolderDataSetMappingArgs.__new__(BlobFolderDataSetMappingArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            if container_name is None and not opts.urn:
                raise TypeError("Missing required property 'container_name'")
            __props__.__dict__["container_name"] = container_name
            if data_set_id is None and not opts.urn:
                raise TypeError("Missing required property 'data_set_id'")
            __props__.__dict__["data_set_id"] = data_set_id
            __props__.__dict__["data_set_mapping_name"] = data_set_mapping_name
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = 'BlobFolder'
            if prefix is None and not opts.urn:
                raise TypeError("Missing required property 'prefix'")
            __props__.__dict__["prefix"] = prefix
            if resource_group is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group'")
            __props__.__dict__["resource_group"] = resource_group
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if share_subscription_name is None and not opts.urn:
                raise TypeError("Missing required property 'share_subscription_name'")
            __props__.__dict__["share_subscription_name"] = share_subscription_name
            if storage_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'storage_account_name'")
            __props__.__dict__["storage_account_name"] = storage_account_name
            if subscription_id is None and not opts.urn:
                raise TypeError("Missing required property 'subscription_id'")
            __props__.__dict__["subscription_id"] = subscription_id
            __props__.__dict__["data_set_mapping_status"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:datashare:BlobFolderDataSetMapping"), pulumi.Alias(type_="azure-native:datashare/v20181101preview:BlobFolderDataSetMapping"), pulumi.Alias(type_="azure-native:datashare/v20200901:BlobFolderDataSetMapping"), pulumi.Alias(type_="azure-native:datashare/v20201001preview:BlobFolderDataSetMapping"), pulumi.Alias(type_="azure-native:datashare/v20210801:BlobFolderDataSetMapping")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(BlobFolderDataSetMapping, __self__).__init__(
            'azure-native:datashare/v20191101:BlobFolderDataSetMapping',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'BlobFolderDataSetMapping':
        """
        Get an existing BlobFolderDataSetMapping resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BlobFolderDataSetMappingArgs.__new__(BlobFolderDataSetMappingArgs)

        __props__.__dict__["container_name"] = None
        __props__.__dict__["data_set_id"] = None
        __props__.__dict__["data_set_mapping_status"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["prefix"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resource_group"] = None
        __props__.__dict__["storage_account_name"] = None
        __props__.__dict__["subscription_id"] = None
        __props__.__dict__["type"] = None
        return BlobFolderDataSetMapping(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="containerName")
    def container_name(self) -> pulumi.Output[str]:
        """
        Container that has the file path.
        """
        return pulumi.get(self, "container_name")

    @property
    @pulumi.getter(name="dataSetId")
    def data_set_id(self) -> pulumi.Output[str]:
        """
        The id of the source data set.
        """
        return pulumi.get(self, "data_set_id")

    @property
    @pulumi.getter(name="dataSetMappingStatus")
    def data_set_mapping_status(self) -> pulumi.Output[str]:
        """
        Gets the status of the data set mapping.
        """
        return pulumi.get(self, "data_set_mapping_status")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Kind of data set mapping.
        Expected value is 'BlobFolder'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the azure resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def prefix(self) -> pulumi.Output[str]:
        """
        Prefix for blob folder
        """
        return pulumi.get(self, "prefix")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the data set mapping.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> pulumi.Output[str]:
        """
        Resource group of storage account.
        """
        return pulumi.get(self, "resource_group")

    @property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> pulumi.Output[str]:
        """
        Storage account name of the source data set.
        """
        return pulumi.get(self, "storage_account_name")

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> pulumi.Output[str]:
        """
        Subscription id of storage account.
        """
        return pulumi.get(self, "subscription_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the azure resource
        """
        return pulumi.get(self, "type")

