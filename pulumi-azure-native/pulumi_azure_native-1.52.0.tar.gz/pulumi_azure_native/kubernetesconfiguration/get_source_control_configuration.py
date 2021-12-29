# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetSourceControlConfigurationResult',
    'AwaitableGetSourceControlConfigurationResult',
    'get_source_control_configuration',
    'get_source_control_configuration_output',
]

@pulumi.output_type
class GetSourceControlConfigurationResult:
    """
    The SourceControl Configuration object returned in Get & Put response.
    """
    def __init__(__self__, compliance_status=None, configuration_protected_settings=None, enable_helm_operator=None, helm_operator_properties=None, id=None, name=None, operator_instance_name=None, operator_namespace=None, operator_params=None, operator_scope=None, operator_type=None, provisioning_state=None, repository_public_key=None, repository_url=None, ssh_known_hosts_contents=None, system_data=None, type=None):
        if compliance_status and not isinstance(compliance_status, dict):
            raise TypeError("Expected argument 'compliance_status' to be a dict")
        pulumi.set(__self__, "compliance_status", compliance_status)
        if configuration_protected_settings and not isinstance(configuration_protected_settings, dict):
            raise TypeError("Expected argument 'configuration_protected_settings' to be a dict")
        pulumi.set(__self__, "configuration_protected_settings", configuration_protected_settings)
        if enable_helm_operator and not isinstance(enable_helm_operator, bool):
            raise TypeError("Expected argument 'enable_helm_operator' to be a bool")
        pulumi.set(__self__, "enable_helm_operator", enable_helm_operator)
        if helm_operator_properties and not isinstance(helm_operator_properties, dict):
            raise TypeError("Expected argument 'helm_operator_properties' to be a dict")
        pulumi.set(__self__, "helm_operator_properties", helm_operator_properties)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if operator_instance_name and not isinstance(operator_instance_name, str):
            raise TypeError("Expected argument 'operator_instance_name' to be a str")
        pulumi.set(__self__, "operator_instance_name", operator_instance_name)
        if operator_namespace and not isinstance(operator_namespace, str):
            raise TypeError("Expected argument 'operator_namespace' to be a str")
        pulumi.set(__self__, "operator_namespace", operator_namespace)
        if operator_params and not isinstance(operator_params, str):
            raise TypeError("Expected argument 'operator_params' to be a str")
        pulumi.set(__self__, "operator_params", operator_params)
        if operator_scope and not isinstance(operator_scope, str):
            raise TypeError("Expected argument 'operator_scope' to be a str")
        pulumi.set(__self__, "operator_scope", operator_scope)
        if operator_type and not isinstance(operator_type, str):
            raise TypeError("Expected argument 'operator_type' to be a str")
        pulumi.set(__self__, "operator_type", operator_type)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if repository_public_key and not isinstance(repository_public_key, str):
            raise TypeError("Expected argument 'repository_public_key' to be a str")
        pulumi.set(__self__, "repository_public_key", repository_public_key)
        if repository_url and not isinstance(repository_url, str):
            raise TypeError("Expected argument 'repository_url' to be a str")
        pulumi.set(__self__, "repository_url", repository_url)
        if ssh_known_hosts_contents and not isinstance(ssh_known_hosts_contents, str):
            raise TypeError("Expected argument 'ssh_known_hosts_contents' to be a str")
        pulumi.set(__self__, "ssh_known_hosts_contents", ssh_known_hosts_contents)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="complianceStatus")
    def compliance_status(self) -> 'outputs.ComplianceStatusResponse':
        """
        Compliance Status of the Configuration
        """
        return pulumi.get(self, "compliance_status")

    @property
    @pulumi.getter(name="configurationProtectedSettings")
    def configuration_protected_settings(self) -> Optional[Mapping[str, str]]:
        """
        Name-value pairs of protected configuration settings for the configuration
        """
        return pulumi.get(self, "configuration_protected_settings")

    @property
    @pulumi.getter(name="enableHelmOperator")
    def enable_helm_operator(self) -> Optional[bool]:
        """
        Option to enable Helm Operator for this git configuration.
        """
        return pulumi.get(self, "enable_helm_operator")

    @property
    @pulumi.getter(name="helmOperatorProperties")
    def helm_operator_properties(self) -> Optional['outputs.HelmOperatorPropertiesResponse']:
        """
        Properties for Helm operator.
        """
        return pulumi.get(self, "helm_operator_properties")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="operatorInstanceName")
    def operator_instance_name(self) -> Optional[str]:
        """
        Instance name of the operator - identifying the specific configuration.
        """
        return pulumi.get(self, "operator_instance_name")

    @property
    @pulumi.getter(name="operatorNamespace")
    def operator_namespace(self) -> Optional[str]:
        """
        The namespace to which this operator is installed to. Maximum of 253 lower case alphanumeric characters, hyphen and period only.
        """
        return pulumi.get(self, "operator_namespace")

    @property
    @pulumi.getter(name="operatorParams")
    def operator_params(self) -> Optional[str]:
        """
        Any Parameters for the Operator instance in string format.
        """
        return pulumi.get(self, "operator_params")

    @property
    @pulumi.getter(name="operatorScope")
    def operator_scope(self) -> Optional[str]:
        """
        Scope at which the operator will be installed.
        """
        return pulumi.get(self, "operator_scope")

    @property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> Optional[str]:
        """
        Type of the operator
        """
        return pulumi.get(self, "operator_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the resource provider.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="repositoryPublicKey")
    def repository_public_key(self) -> str:
        """
        Public Key associated with this SourceControl configuration (either generated within the cluster or provided by the user).
        """
        return pulumi.get(self, "repository_public_key")

    @property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> Optional[str]:
        """
        Url of the SourceControl Repository.
        """
        return pulumi.get(self, "repository_url")

    @property
    @pulumi.getter(name="sshKnownHostsContents")
    def ssh_known_hosts_contents(self) -> Optional[str]:
        """
        Base64-encoded known_hosts contents containing public SSH keys required to access private Git instances
        """
        return pulumi.get(self, "ssh_known_hosts_contents")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Top level metadata https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/common-api-contracts.md#system-metadata-for-all-azure-resources
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetSourceControlConfigurationResult(GetSourceControlConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSourceControlConfigurationResult(
            compliance_status=self.compliance_status,
            configuration_protected_settings=self.configuration_protected_settings,
            enable_helm_operator=self.enable_helm_operator,
            helm_operator_properties=self.helm_operator_properties,
            id=self.id,
            name=self.name,
            operator_instance_name=self.operator_instance_name,
            operator_namespace=self.operator_namespace,
            operator_params=self.operator_params,
            operator_scope=self.operator_scope,
            operator_type=self.operator_type,
            provisioning_state=self.provisioning_state,
            repository_public_key=self.repository_public_key,
            repository_url=self.repository_url,
            ssh_known_hosts_contents=self.ssh_known_hosts_contents,
            system_data=self.system_data,
            type=self.type)


def get_source_control_configuration(cluster_name: Optional[str] = None,
                                     cluster_resource_name: Optional[str] = None,
                                     cluster_rp: Optional[str] = None,
                                     resource_group_name: Optional[str] = None,
                                     source_control_configuration_name: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSourceControlConfigurationResult:
    """
    The SourceControl Configuration object returned in Get & Put response.
    API Version: 2021-03-01.


    :param str cluster_name: The name of the kubernetes cluster.
    :param str cluster_resource_name: The Kubernetes cluster resource name - either managedClusters (for AKS clusters) or connectedClusters (for OnPrem K8S clusters).
    :param str cluster_rp: The Kubernetes cluster RP - either Microsoft.ContainerService (for AKS clusters) or Microsoft.Kubernetes (for OnPrem K8S clusters).
    :param str resource_group_name: The name of the resource group.
    :param str source_control_configuration_name: Name of the Source Control Configuration.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['clusterResourceName'] = cluster_resource_name
    __args__['clusterRp'] = cluster_rp
    __args__['resourceGroupName'] = resource_group_name
    __args__['sourceControlConfigurationName'] = source_control_configuration_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:kubernetesconfiguration:getSourceControlConfiguration', __args__, opts=opts, typ=GetSourceControlConfigurationResult).value

    return AwaitableGetSourceControlConfigurationResult(
        compliance_status=__ret__.compliance_status,
        configuration_protected_settings=__ret__.configuration_protected_settings,
        enable_helm_operator=__ret__.enable_helm_operator,
        helm_operator_properties=__ret__.helm_operator_properties,
        id=__ret__.id,
        name=__ret__.name,
        operator_instance_name=__ret__.operator_instance_name,
        operator_namespace=__ret__.operator_namespace,
        operator_params=__ret__.operator_params,
        operator_scope=__ret__.operator_scope,
        operator_type=__ret__.operator_type,
        provisioning_state=__ret__.provisioning_state,
        repository_public_key=__ret__.repository_public_key,
        repository_url=__ret__.repository_url,
        ssh_known_hosts_contents=__ret__.ssh_known_hosts_contents,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_source_control_configuration)
def get_source_control_configuration_output(cluster_name: Optional[pulumi.Input[str]] = None,
                                            cluster_resource_name: Optional[pulumi.Input[str]] = None,
                                            cluster_rp: Optional[pulumi.Input[str]] = None,
                                            resource_group_name: Optional[pulumi.Input[str]] = None,
                                            source_control_configuration_name: Optional[pulumi.Input[str]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSourceControlConfigurationResult]:
    """
    The SourceControl Configuration object returned in Get & Put response.
    API Version: 2021-03-01.


    :param str cluster_name: The name of the kubernetes cluster.
    :param str cluster_resource_name: The Kubernetes cluster resource name - either managedClusters (for AKS clusters) or connectedClusters (for OnPrem K8S clusters).
    :param str cluster_rp: The Kubernetes cluster RP - either Microsoft.ContainerService (for AKS clusters) or Microsoft.Kubernetes (for OnPrem K8S clusters).
    :param str resource_group_name: The name of the resource group.
    :param str source_control_configuration_name: Name of the Source Control Configuration.
    """
    ...
