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

__all__ = ['FileServicePropertiesArgs', 'FileServiceProperties']

@pulumi.input_type
class FileServicePropertiesArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 cors: Optional[pulumi.Input['CorsRulesArgs']] = None,
                 file_services_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a FileServiceProperties resource.
        :param pulumi.Input[str] account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input['CorsRulesArgs'] cors: Specifies CORS rules for the File service. You can include up to five CorsRule elements in the request. If no CorsRule elements are included in the request body, all CORS rules will be deleted, and CORS will be disabled for the File service.
        :param pulumi.Input[str] file_services_name: The name of the file Service within the specified storage account. File Service Name must be "default"
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if cors is not None:
            pulumi.set(__self__, "cors", cors)
        if file_services_name is not None:
            pulumi.set(__self__, "file_services_name", file_services_name)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group within the user's subscription. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def cors(self) -> Optional[pulumi.Input['CorsRulesArgs']]:
        """
        Specifies CORS rules for the File service. You can include up to five CorsRule elements in the request. If no CorsRule elements are included in the request body, all CORS rules will be deleted, and CORS will be disabled for the File service.
        """
        return pulumi.get(self, "cors")

    @cors.setter
    def cors(self, value: Optional[pulumi.Input['CorsRulesArgs']]):
        pulumi.set(self, "cors", value)

    @property
    @pulumi.getter(name="fileServicesName")
    def file_services_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the file Service within the specified storage account. File Service Name must be "default"
        """
        return pulumi.get(self, "file_services_name")

    @file_services_name.setter
    def file_services_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file_services_name", value)


class FileServiceProperties(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 cors: Optional[pulumi.Input[pulumi.InputType['CorsRulesArgs']]] = None,
                 file_services_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The properties of File services in storage account.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        :param pulumi.Input[pulumi.InputType['CorsRulesArgs']] cors: Specifies CORS rules for the File service. You can include up to five CorsRule elements in the request. If no CorsRule elements are included in the request body, all CORS rules will be deleted, and CORS will be disabled for the File service.
        :param pulumi.Input[str] file_services_name: The name of the file Service within the specified storage account. File Service Name must be "default"
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FileServicePropertiesArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The properties of File services in storage account.

        :param str resource_name: The name of the resource.
        :param FileServicePropertiesArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FileServicePropertiesArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 cors: Optional[pulumi.Input[pulumi.InputType['CorsRulesArgs']]] = None,
                 file_services_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = FileServicePropertiesArgs.__new__(FileServicePropertiesArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["cors"] = cors
            __props__.__dict__["file_services_name"] = file_services_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:storage:FileServiceProperties"), pulumi.Alias(type_="azure-native:storage/v20190601:FileServiceProperties"), pulumi.Alias(type_="azure-native:storage/v20200801preview:FileServiceProperties"), pulumi.Alias(type_="azure-native:storage/v20210101:FileServiceProperties"), pulumi.Alias(type_="azure-native:storage/v20210201:FileServiceProperties"), pulumi.Alias(type_="azure-native:storage/v20210401:FileServiceProperties"), pulumi.Alias(type_="azure-native:storage/v20210601:FileServiceProperties")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(FileServiceProperties, __self__).__init__(
            'azure-native:storage/v20190401:FileServiceProperties',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'FileServiceProperties':
        """
        Get an existing FileServiceProperties resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FileServicePropertiesArgs.__new__(FileServicePropertiesArgs)

        __props__.__dict__["cors"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        return FileServiceProperties(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def cors(self) -> pulumi.Output[Optional['outputs.CorsRulesResponse']]:
        """
        Specifies CORS rules for the File service. You can include up to five CorsRule elements in the request. If no CorsRule elements are included in the request body, all CORS rules will be deleted, and CORS will be disabled for the File service.
        """
        return pulumi.get(self, "cors")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

