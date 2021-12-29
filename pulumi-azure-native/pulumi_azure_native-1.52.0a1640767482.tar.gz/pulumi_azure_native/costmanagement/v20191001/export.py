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

__all__ = ['ExportArgs', 'Export']

@pulumi.input_type
class ExportArgs:
    def __init__(__self__, *,
                 definition: pulumi.Input['QueryDefinitionArgs'],
                 delivery_info: pulumi.Input['ExportDeliveryInfoArgs'],
                 scope: pulumi.Input[str],
                 export_name: Optional[pulumi.Input[str]] = None,
                 format: Optional[pulumi.Input[Union[str, 'FormatType']]] = None,
                 schedule: Optional[pulumi.Input['ExportScheduleArgs']] = None):
        """
        The set of arguments for constructing a Export resource.
        :param pulumi.Input['QueryDefinitionArgs'] definition: Has definition for the export.
        :param pulumi.Input['ExportDeliveryInfoArgs'] delivery_info: Has delivery information for the export.
        :param pulumi.Input[str] scope: The scope associated with query and export operations. This includes '/subscriptions/{subscriptionId}/' for subscription scope, '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope and '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for Department scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope, '/providers/Microsoft.Management/managementGroups/{managementGroupId} for Management Group scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for billingProfile scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}' for invoiceSection scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}' specific for partners, 'providers/Microsoft.CostManagement/ExternalSubscriptions/{externalSubscriptionId}' for linked account and 'providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountId}' for consolidated account
        :param pulumi.Input[str] export_name: Export Name.
        :param pulumi.Input[Union[str, 'FormatType']] format: The format of the export being delivered.
        :param pulumi.Input['ExportScheduleArgs'] schedule: Has schedule information for the export.
        """
        pulumi.set(__self__, "definition", definition)
        pulumi.set(__self__, "delivery_info", delivery_info)
        pulumi.set(__self__, "scope", scope)
        if export_name is not None:
            pulumi.set(__self__, "export_name", export_name)
        if format is not None:
            pulumi.set(__self__, "format", format)
        if schedule is not None:
            pulumi.set(__self__, "schedule", schedule)

    @property
    @pulumi.getter
    def definition(self) -> pulumi.Input['QueryDefinitionArgs']:
        """
        Has definition for the export.
        """
        return pulumi.get(self, "definition")

    @definition.setter
    def definition(self, value: pulumi.Input['QueryDefinitionArgs']):
        pulumi.set(self, "definition", value)

    @property
    @pulumi.getter(name="deliveryInfo")
    def delivery_info(self) -> pulumi.Input['ExportDeliveryInfoArgs']:
        """
        Has delivery information for the export.
        """
        return pulumi.get(self, "delivery_info")

    @delivery_info.setter
    def delivery_info(self, value: pulumi.Input['ExportDeliveryInfoArgs']):
        pulumi.set(self, "delivery_info", value)

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Input[str]:
        """
        The scope associated with query and export operations. This includes '/subscriptions/{subscriptionId}/' for subscription scope, '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope and '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for Department scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope, '/providers/Microsoft.Management/managementGroups/{managementGroupId} for Management Group scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for billingProfile scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}' for invoiceSection scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}' specific for partners, 'providers/Microsoft.CostManagement/ExternalSubscriptions/{externalSubscriptionId}' for linked account and 'providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountId}' for consolidated account
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: pulumi.Input[str]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter(name="exportName")
    def export_name(self) -> Optional[pulumi.Input[str]]:
        """
        Export Name.
        """
        return pulumi.get(self, "export_name")

    @export_name.setter
    def export_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "export_name", value)

    @property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input[Union[str, 'FormatType']]]:
        """
        The format of the export being delivered.
        """
        return pulumi.get(self, "format")

    @format.setter
    def format(self, value: Optional[pulumi.Input[Union[str, 'FormatType']]]):
        pulumi.set(self, "format", value)

    @property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input['ExportScheduleArgs']]:
        """
        Has schedule information for the export.
        """
        return pulumi.get(self, "schedule")

    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input['ExportScheduleArgs']]):
        pulumi.set(self, "schedule", value)


class Export(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 definition: Optional[pulumi.Input[pulumi.InputType['QueryDefinitionArgs']]] = None,
                 delivery_info: Optional[pulumi.Input[pulumi.InputType['ExportDeliveryInfoArgs']]] = None,
                 export_name: Optional[pulumi.Input[str]] = None,
                 format: Optional[pulumi.Input[Union[str, 'FormatType']]] = None,
                 schedule: Optional[pulumi.Input[pulumi.InputType['ExportScheduleArgs']]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A export resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['QueryDefinitionArgs']] definition: Has definition for the export.
        :param pulumi.Input[pulumi.InputType['ExportDeliveryInfoArgs']] delivery_info: Has delivery information for the export.
        :param pulumi.Input[str] export_name: Export Name.
        :param pulumi.Input[Union[str, 'FormatType']] format: The format of the export being delivered.
        :param pulumi.Input[pulumi.InputType['ExportScheduleArgs']] schedule: Has schedule information for the export.
        :param pulumi.Input[str] scope: The scope associated with query and export operations. This includes '/subscriptions/{subscriptionId}/' for subscription scope, '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope and '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for Department scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope, '/providers/Microsoft.Management/managementGroups/{managementGroupId} for Management Group scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for billingProfile scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}' for invoiceSection scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}' specific for partners, 'providers/Microsoft.CostManagement/ExternalSubscriptions/{externalSubscriptionId}' for linked account and 'providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountId}' for consolidated account
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ExportArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A export resource.

        :param str resource_name: The name of the resource.
        :param ExportArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ExportArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 definition: Optional[pulumi.Input[pulumi.InputType['QueryDefinitionArgs']]] = None,
                 delivery_info: Optional[pulumi.Input[pulumi.InputType['ExportDeliveryInfoArgs']]] = None,
                 export_name: Optional[pulumi.Input[str]] = None,
                 format: Optional[pulumi.Input[Union[str, 'FormatType']]] = None,
                 schedule: Optional[pulumi.Input[pulumi.InputType['ExportScheduleArgs']]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
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
            __props__ = ExportArgs.__new__(ExportArgs)

            if definition is None and not opts.urn:
                raise TypeError("Missing required property 'definition'")
            __props__.__dict__["definition"] = definition
            if delivery_info is None and not opts.urn:
                raise TypeError("Missing required property 'delivery_info'")
            __props__.__dict__["delivery_info"] = delivery_info
            __props__.__dict__["export_name"] = export_name
            __props__.__dict__["format"] = format
            __props__.__dict__["schedule"] = schedule
            if scope is None and not opts.urn:
                raise TypeError("Missing required property 'scope'")
            __props__.__dict__["scope"] = scope
            __props__.__dict__["name"] = None
            __props__.__dict__["tags"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:costmanagement:Export"), pulumi.Alias(type_="azure-native:costmanagement/v20190101:Export"), pulumi.Alias(type_="azure-native:costmanagement/v20190901:Export"), pulumi.Alias(type_="azure-native:costmanagement/v20191101:Export"), pulumi.Alias(type_="azure-native:costmanagement/v20200601:Export"), pulumi.Alias(type_="azure-native:costmanagement/v20201201preview:Export"), pulumi.Alias(type_="azure-native:costmanagement/v20210101:Export"), pulumi.Alias(type_="azure-native:costmanagement/v20211001:Export")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Export, __self__).__init__(
            'azure-native:costmanagement/v20191001:Export',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Export':
        """
        Get an existing Export resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ExportArgs.__new__(ExportArgs)

        __props__.__dict__["definition"] = None
        __props__.__dict__["delivery_info"] = None
        __props__.__dict__["format"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["schedule"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Export(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def definition(self) -> pulumi.Output['outputs.QueryDefinitionResponse']:
        """
        Has definition for the export.
        """
        return pulumi.get(self, "definition")

    @property
    @pulumi.getter(name="deliveryInfo")
    def delivery_info(self) -> pulumi.Output['outputs.ExportDeliveryInfoResponse']:
        """
        Has delivery information for the export.
        """
        return pulumi.get(self, "delivery_info")

    @property
    @pulumi.getter
    def format(self) -> pulumi.Output[Optional[str]]:
        """
        The format of the export being delivered.
        """
        return pulumi.get(self, "format")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def schedule(self) -> pulumi.Output[Optional['outputs.ExportScheduleResponse']]:
        """
        Has schedule information for the export.
        """
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Mapping[str, str]]:
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

