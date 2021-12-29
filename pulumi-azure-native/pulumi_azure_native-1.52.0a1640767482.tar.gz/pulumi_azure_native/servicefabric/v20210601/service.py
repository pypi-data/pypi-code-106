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

__all__ = ['ServiceArgs', 'Service']

@pulumi.input_type
class ServiceArgs:
    def __init__(__self__, *,
                 application_name: pulumi.Input[str],
                 cluster_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 service_kind: pulumi.Input[Union[str, 'ServiceKind']],
                 correlation_scheme: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceCorrelationDescriptionArgs']]]] = None,
                 default_move_cost: Optional[pulumi.Input[Union[str, 'MoveCost']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 partition_description: Optional[pulumi.Input[Union['NamedPartitionSchemeDescriptionArgs', 'SingletonPartitionSchemeDescriptionArgs', 'UniformInt64RangePartitionSchemeDescriptionArgs']]] = None,
                 placement_constraints: Optional[pulumi.Input[str]] = None,
                 service_dns_name: Optional[pulumi.Input[str]] = None,
                 service_load_metrics: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceLoadMetricDescriptionArgs']]]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 service_package_activation_mode: Optional[pulumi.Input[Union[str, 'ArmServicePackageActivationMode']]] = None,
                 service_placement_policies: Optional[pulumi.Input[Sequence[pulumi.Input['ServicePlacementPolicyDescriptionArgs']]]] = None,
                 service_type_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Service resource.
        :param pulumi.Input[str] application_name: The name of the application resource.
        :param pulumi.Input[str] cluster_name: The name of the cluster resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Union[str, 'ServiceKind']] service_kind: The kind of service (Stateless or Stateful).
        :param pulumi.Input[Sequence[pulumi.Input['ServiceCorrelationDescriptionArgs']]] correlation_scheme: A list that describes the correlation of the service with other services.
        :param pulumi.Input[Union[str, 'MoveCost']] default_move_cost: Specifies the move cost for the service.
        :param pulumi.Input[str] location: It will be deprecated in New API, resource location depends on the parent resource.
        :param pulumi.Input[Union['NamedPartitionSchemeDescriptionArgs', 'SingletonPartitionSchemeDescriptionArgs', 'UniformInt64RangePartitionSchemeDescriptionArgs']] partition_description: Describes how the service is partitioned.
        :param pulumi.Input[str] placement_constraints: The placement constraints as a string. Placement constraints are boolean expressions on node properties and allow for restricting a service to particular nodes based on the service requirements. For example, to place a service on nodes where NodeType is blue specify the following: "NodeColor == blue)".
        :param pulumi.Input[str] service_dns_name: Dns name used for the service. If this is specified, then the service can be accessed via its DNS name instead of service name.
        :param pulumi.Input[Sequence[pulumi.Input['ServiceLoadMetricDescriptionArgs']]] service_load_metrics: The service load metrics is given as an array of ServiceLoadMetricDescription objects.
        :param pulumi.Input[str] service_name: The name of the service resource in the format of {applicationName}~{serviceName}.
        :param pulumi.Input[Union[str, 'ArmServicePackageActivationMode']] service_package_activation_mode: The activation Mode of the service package
        :param pulumi.Input[Sequence[pulumi.Input['ServicePlacementPolicyDescriptionArgs']]] service_placement_policies: A list that describes the correlation of the service with other services.
        :param pulumi.Input[str] service_type_name: The name of the service type
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Azure resource tags.
        """
        pulumi.set(__self__, "application_name", application_name)
        pulumi.set(__self__, "cluster_name", cluster_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_kind", service_kind)
        if correlation_scheme is not None:
            pulumi.set(__self__, "correlation_scheme", correlation_scheme)
        if default_move_cost is not None:
            pulumi.set(__self__, "default_move_cost", default_move_cost)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if partition_description is not None:
            pulumi.set(__self__, "partition_description", partition_description)
        if placement_constraints is not None:
            pulumi.set(__self__, "placement_constraints", placement_constraints)
        if service_dns_name is not None:
            pulumi.set(__self__, "service_dns_name", service_dns_name)
        if service_load_metrics is not None:
            pulumi.set(__self__, "service_load_metrics", service_load_metrics)
        if service_name is not None:
            pulumi.set(__self__, "service_name", service_name)
        if service_package_activation_mode is not None:
            pulumi.set(__self__, "service_package_activation_mode", service_package_activation_mode)
        if service_placement_policies is not None:
            pulumi.set(__self__, "service_placement_policies", service_placement_policies)
        if service_type_name is not None:
            pulumi.set(__self__, "service_type_name", service_type_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> pulumi.Input[str]:
        """
        The name of the application resource.
        """
        return pulumi.get(self, "application_name")

    @application_name.setter
    def application_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "application_name", value)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[str]:
        """
        The name of the cluster resource.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_name", value)

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
    @pulumi.getter(name="serviceKind")
    def service_kind(self) -> pulumi.Input[Union[str, 'ServiceKind']]:
        """
        The kind of service (Stateless or Stateful).
        """
        return pulumi.get(self, "service_kind")

    @service_kind.setter
    def service_kind(self, value: pulumi.Input[Union[str, 'ServiceKind']]):
        pulumi.set(self, "service_kind", value)

    @property
    @pulumi.getter(name="correlationScheme")
    def correlation_scheme(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ServiceCorrelationDescriptionArgs']]]]:
        """
        A list that describes the correlation of the service with other services.
        """
        return pulumi.get(self, "correlation_scheme")

    @correlation_scheme.setter
    def correlation_scheme(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceCorrelationDescriptionArgs']]]]):
        pulumi.set(self, "correlation_scheme", value)

    @property
    @pulumi.getter(name="defaultMoveCost")
    def default_move_cost(self) -> Optional[pulumi.Input[Union[str, 'MoveCost']]]:
        """
        Specifies the move cost for the service.
        """
        return pulumi.get(self, "default_move_cost")

    @default_move_cost.setter
    def default_move_cost(self, value: Optional[pulumi.Input[Union[str, 'MoveCost']]]):
        pulumi.set(self, "default_move_cost", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        It will be deprecated in New API, resource location depends on the parent resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="partitionDescription")
    def partition_description(self) -> Optional[pulumi.Input[Union['NamedPartitionSchemeDescriptionArgs', 'SingletonPartitionSchemeDescriptionArgs', 'UniformInt64RangePartitionSchemeDescriptionArgs']]]:
        """
        Describes how the service is partitioned.
        """
        return pulumi.get(self, "partition_description")

    @partition_description.setter
    def partition_description(self, value: Optional[pulumi.Input[Union['NamedPartitionSchemeDescriptionArgs', 'SingletonPartitionSchemeDescriptionArgs', 'UniformInt64RangePartitionSchemeDescriptionArgs']]]):
        pulumi.set(self, "partition_description", value)

    @property
    @pulumi.getter(name="placementConstraints")
    def placement_constraints(self) -> Optional[pulumi.Input[str]]:
        """
        The placement constraints as a string. Placement constraints are boolean expressions on node properties and allow for restricting a service to particular nodes based on the service requirements. For example, to place a service on nodes where NodeType is blue specify the following: "NodeColor == blue)".
        """
        return pulumi.get(self, "placement_constraints")

    @placement_constraints.setter
    def placement_constraints(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "placement_constraints", value)

    @property
    @pulumi.getter(name="serviceDnsName")
    def service_dns_name(self) -> Optional[pulumi.Input[str]]:
        """
        Dns name used for the service. If this is specified, then the service can be accessed via its DNS name instead of service name.
        """
        return pulumi.get(self, "service_dns_name")

    @service_dns_name.setter
    def service_dns_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_dns_name", value)

    @property
    @pulumi.getter(name="serviceLoadMetrics")
    def service_load_metrics(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ServiceLoadMetricDescriptionArgs']]]]:
        """
        The service load metrics is given as an array of ServiceLoadMetricDescription objects.
        """
        return pulumi.get(self, "service_load_metrics")

    @service_load_metrics.setter
    def service_load_metrics(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceLoadMetricDescriptionArgs']]]]):
        pulumi.set(self, "service_load_metrics", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the service resource in the format of {applicationName}~{serviceName}.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="servicePackageActivationMode")
    def service_package_activation_mode(self) -> Optional[pulumi.Input[Union[str, 'ArmServicePackageActivationMode']]]:
        """
        The activation Mode of the service package
        """
        return pulumi.get(self, "service_package_activation_mode")

    @service_package_activation_mode.setter
    def service_package_activation_mode(self, value: Optional[pulumi.Input[Union[str, 'ArmServicePackageActivationMode']]]):
        pulumi.set(self, "service_package_activation_mode", value)

    @property
    @pulumi.getter(name="servicePlacementPolicies")
    def service_placement_policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ServicePlacementPolicyDescriptionArgs']]]]:
        """
        A list that describes the correlation of the service with other services.
        """
        return pulumi.get(self, "service_placement_policies")

    @service_placement_policies.setter
    def service_placement_policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ServicePlacementPolicyDescriptionArgs']]]]):
        pulumi.set(self, "service_placement_policies", value)

    @property
    @pulumi.getter(name="serviceTypeName")
    def service_type_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the service type
        """
        return pulumi.get(self, "service_type_name")

    @service_type_name.setter
    def service_type_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_type_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Azure resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Service(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_name: Optional[pulumi.Input[str]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 correlation_scheme: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceCorrelationDescriptionArgs']]]]] = None,
                 default_move_cost: Optional[pulumi.Input[Union[str, 'MoveCost']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 partition_description: Optional[pulumi.Input[Union[pulumi.InputType['NamedPartitionSchemeDescriptionArgs'], pulumi.InputType['SingletonPartitionSchemeDescriptionArgs'], pulumi.InputType['UniformInt64RangePartitionSchemeDescriptionArgs']]]] = None,
                 placement_constraints: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_dns_name: Optional[pulumi.Input[str]] = None,
                 service_kind: Optional[pulumi.Input[Union[str, 'ServiceKind']]] = None,
                 service_load_metrics: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceLoadMetricDescriptionArgs']]]]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 service_package_activation_mode: Optional[pulumi.Input[Union[str, 'ArmServicePackageActivationMode']]] = None,
                 service_placement_policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServicePlacementPolicyDescriptionArgs']]]]] = None,
                 service_type_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        The service resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_name: The name of the application resource.
        :param pulumi.Input[str] cluster_name: The name of the cluster resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceCorrelationDescriptionArgs']]]] correlation_scheme: A list that describes the correlation of the service with other services.
        :param pulumi.Input[Union[str, 'MoveCost']] default_move_cost: Specifies the move cost for the service.
        :param pulumi.Input[str] location: It will be deprecated in New API, resource location depends on the parent resource.
        :param pulumi.Input[Union[pulumi.InputType['NamedPartitionSchemeDescriptionArgs'], pulumi.InputType['SingletonPartitionSchemeDescriptionArgs'], pulumi.InputType['UniformInt64RangePartitionSchemeDescriptionArgs']]] partition_description: Describes how the service is partitioned.
        :param pulumi.Input[str] placement_constraints: The placement constraints as a string. Placement constraints are boolean expressions on node properties and allow for restricting a service to particular nodes based on the service requirements. For example, to place a service on nodes where NodeType is blue specify the following: "NodeColor == blue)".
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_dns_name: Dns name used for the service. If this is specified, then the service can be accessed via its DNS name instead of service name.
        :param pulumi.Input[Union[str, 'ServiceKind']] service_kind: The kind of service (Stateless or Stateful).
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceLoadMetricDescriptionArgs']]]] service_load_metrics: The service load metrics is given as an array of ServiceLoadMetricDescription objects.
        :param pulumi.Input[str] service_name: The name of the service resource in the format of {applicationName}~{serviceName}.
        :param pulumi.Input[Union[str, 'ArmServicePackageActivationMode']] service_package_activation_mode: The activation Mode of the service package
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServicePlacementPolicyDescriptionArgs']]]] service_placement_policies: A list that describes the correlation of the service with other services.
        :param pulumi.Input[str] service_type_name: The name of the service type
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Azure resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServiceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The service resource.

        :param str resource_name: The name of the resource.
        :param ServiceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServiceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_name: Optional[pulumi.Input[str]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 correlation_scheme: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceCorrelationDescriptionArgs']]]]] = None,
                 default_move_cost: Optional[pulumi.Input[Union[str, 'MoveCost']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 partition_description: Optional[pulumi.Input[Union[pulumi.InputType['NamedPartitionSchemeDescriptionArgs'], pulumi.InputType['SingletonPartitionSchemeDescriptionArgs'], pulumi.InputType['UniformInt64RangePartitionSchemeDescriptionArgs']]]] = None,
                 placement_constraints: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_dns_name: Optional[pulumi.Input[str]] = None,
                 service_kind: Optional[pulumi.Input[Union[str, 'ServiceKind']]] = None,
                 service_load_metrics: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceLoadMetricDescriptionArgs']]]]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 service_package_activation_mode: Optional[pulumi.Input[Union[str, 'ArmServicePackageActivationMode']]] = None,
                 service_placement_policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServicePlacementPolicyDescriptionArgs']]]]] = None,
                 service_type_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = ServiceArgs.__new__(ServiceArgs)

            if application_name is None and not opts.urn:
                raise TypeError("Missing required property 'application_name'")
            __props__.__dict__["application_name"] = application_name
            if cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_name'")
            __props__.__dict__["cluster_name"] = cluster_name
            __props__.__dict__["correlation_scheme"] = correlation_scheme
            __props__.__dict__["default_move_cost"] = default_move_cost
            __props__.__dict__["location"] = location
            __props__.__dict__["partition_description"] = partition_description
            __props__.__dict__["placement_constraints"] = placement_constraints
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["service_dns_name"] = service_dns_name
            if service_kind is None and not opts.urn:
                raise TypeError("Missing required property 'service_kind'")
            __props__.__dict__["service_kind"] = service_kind
            __props__.__dict__["service_load_metrics"] = service_load_metrics
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["service_package_activation_mode"] = service_package_activation_mode
            __props__.__dict__["service_placement_policies"] = service_placement_policies
            __props__.__dict__["service_type_name"] = service_type_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:servicefabric:Service"), pulumi.Alias(type_="azure-native:servicefabric/v20170701preview:Service"), pulumi.Alias(type_="azure-native:servicefabric/v20190301:Service"), pulumi.Alias(type_="azure-native:servicefabric/v20190301preview:Service"), pulumi.Alias(type_="azure-native:servicefabric/v20190601preview:Service"), pulumi.Alias(type_="azure-native:servicefabric/v20191101preview:Service"), pulumi.Alias(type_="azure-native:servicefabric/v20200301:Service"), pulumi.Alias(type_="azure-native:servicefabric/v20201201preview:Service")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Service, __self__).__init__(
            'azure-native:servicefabric/v20210601:Service',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Service':
        """
        Get an existing Service resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServiceArgs.__new__(ServiceArgs)

        __props__.__dict__["correlation_scheme"] = None
        __props__.__dict__["default_move_cost"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["partition_description"] = None
        __props__.__dict__["placement_constraints"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["service_dns_name"] = None
        __props__.__dict__["service_kind"] = None
        __props__.__dict__["service_load_metrics"] = None
        __props__.__dict__["service_package_activation_mode"] = None
        __props__.__dict__["service_placement_policies"] = None
        __props__.__dict__["service_type_name"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Service(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="correlationScheme")
    def correlation_scheme(self) -> pulumi.Output[Optional[Sequence['outputs.ServiceCorrelationDescriptionResponse']]]:
        """
        A list that describes the correlation of the service with other services.
        """
        return pulumi.get(self, "correlation_scheme")

    @property
    @pulumi.getter(name="defaultMoveCost")
    def default_move_cost(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the move cost for the service.
        """
        return pulumi.get(self, "default_move_cost")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        Azure resource etag.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        It will be deprecated in New API, resource location depends on the parent resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Azure resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partitionDescription")
    def partition_description(self) -> pulumi.Output[Optional[Any]]:
        """
        Describes how the service is partitioned.
        """
        return pulumi.get(self, "partition_description")

    @property
    @pulumi.getter(name="placementConstraints")
    def placement_constraints(self) -> pulumi.Output[Optional[str]]:
        """
        The placement constraints as a string. Placement constraints are boolean expressions on node properties and allow for restricting a service to particular nodes based on the service requirements. For example, to place a service on nodes where NodeType is blue specify the following: "NodeColor == blue)".
        """
        return pulumi.get(self, "placement_constraints")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The current deployment or provisioning state, which only appears in the response
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="serviceDnsName")
    def service_dns_name(self) -> pulumi.Output[Optional[str]]:
        """
        Dns name used for the service. If this is specified, then the service can be accessed via its DNS name instead of service name.
        """
        return pulumi.get(self, "service_dns_name")

    @property
    @pulumi.getter(name="serviceKind")
    def service_kind(self) -> pulumi.Output[str]:
        """
        The kind of service (Stateless or Stateful).
        """
        return pulumi.get(self, "service_kind")

    @property
    @pulumi.getter(name="serviceLoadMetrics")
    def service_load_metrics(self) -> pulumi.Output[Optional[Sequence['outputs.ServiceLoadMetricDescriptionResponse']]]:
        """
        The service load metrics is given as an array of ServiceLoadMetricDescription objects.
        """
        return pulumi.get(self, "service_load_metrics")

    @property
    @pulumi.getter(name="servicePackageActivationMode")
    def service_package_activation_mode(self) -> pulumi.Output[Optional[str]]:
        """
        The activation Mode of the service package
        """
        return pulumi.get(self, "service_package_activation_mode")

    @property
    @pulumi.getter(name="servicePlacementPolicies")
    def service_placement_policies(self) -> pulumi.Output[Optional[Sequence['outputs.ServicePlacementPolicyDescriptionResponse']]]:
        """
        A list that describes the correlation of the service with other services.
        """
        return pulumi.get(self, "service_placement_policies")

    @property
    @pulumi.getter(name="serviceTypeName")
    def service_type_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the service type
        """
        return pulumi.get(self, "service_type_name")

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
        Azure resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Azure resource type.
        """
        return pulumi.get(self, "type")

