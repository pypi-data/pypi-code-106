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

__all__ = ['DataFlowArgs', 'DataFlow']

@pulumi.input_type
class DataFlowArgs:
    def __init__(__self__, *,
                 factory_name: pulumi.Input[str],
                 properties: pulumi.Input[Union['FlowletArgs', 'MappingDataFlowArgs', 'WranglingDataFlowArgs']],
                 resource_group_name: pulumi.Input[str],
                 data_flow_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DataFlow resource.
        :param pulumi.Input[str] factory_name: The factory name.
        :param pulumi.Input[Union['FlowletArgs', 'MappingDataFlowArgs', 'WranglingDataFlowArgs']] properties: Data flow properties.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] data_flow_name: The data flow name.
        """
        pulumi.set(__self__, "factory_name", factory_name)
        pulumi.set(__self__, "properties", properties)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if data_flow_name is not None:
            pulumi.set(__self__, "data_flow_name", data_flow_name)

    @property
    @pulumi.getter(name="factoryName")
    def factory_name(self) -> pulumi.Input[str]:
        """
        The factory name.
        """
        return pulumi.get(self, "factory_name")

    @factory_name.setter
    def factory_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "factory_name", value)

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Input[Union['FlowletArgs', 'MappingDataFlowArgs', 'WranglingDataFlowArgs']]:
        """
        Data flow properties.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: pulumi.Input[Union['FlowletArgs', 'MappingDataFlowArgs', 'WranglingDataFlowArgs']]):
        pulumi.set(self, "properties", value)

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
    @pulumi.getter(name="dataFlowName")
    def data_flow_name(self) -> Optional[pulumi.Input[str]]:
        """
        The data flow name.
        """
        return pulumi.get(self, "data_flow_name")

    @data_flow_name.setter
    def data_flow_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_flow_name", value)


class DataFlow(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_flow_name: Optional[pulumi.Input[str]] = None,
                 factory_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union[pulumi.InputType['FlowletArgs'], pulumi.InputType['MappingDataFlowArgs'], pulumi.InputType['WranglingDataFlowArgs']]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Data flow resource type.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] data_flow_name: The data flow name.
        :param pulumi.Input[str] factory_name: The factory name.
        :param pulumi.Input[Union[pulumi.InputType['FlowletArgs'], pulumi.InputType['MappingDataFlowArgs'], pulumi.InputType['WranglingDataFlowArgs']]] properties: Data flow properties.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DataFlowArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Data flow resource type.

        :param str resource_name: The name of the resource.
        :param DataFlowArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DataFlowArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_flow_name: Optional[pulumi.Input[str]] = None,
                 factory_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union[pulumi.InputType['FlowletArgs'], pulumi.InputType['MappingDataFlowArgs'], pulumi.InputType['WranglingDataFlowArgs']]]] = None,
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
            __props__ = DataFlowArgs.__new__(DataFlowArgs)

            __props__.__dict__["data_flow_name"] = data_flow_name
            if factory_name is None and not opts.urn:
                raise TypeError("Missing required property 'factory_name'")
            __props__.__dict__["factory_name"] = factory_name
            if properties is None and not opts.urn:
                raise TypeError("Missing required property 'properties'")
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:datafactory:DataFlow")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DataFlow, __self__).__init__(
            'azure-native:datafactory/v20180601:DataFlow',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DataFlow':
        """
        Get an existing DataFlow resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DataFlowArgs.__new__(DataFlowArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["type"] = None
        return DataFlow(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        Etag identifies change in the resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Any]:
        """
        Data flow properties.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The resource type.
        """
        return pulumi.get(self, "type")

