# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetBackendResult',
    'AwaitableGetBackendResult',
    'get_backend',
    'get_backend_output',
]

@pulumi.output_type
class GetBackendResult:
    """
    Backend details.
    """
    def __init__(__self__, credentials=None, description=None, id=None, name=None, properties=None, protocol=None, proxy=None, resource_id=None, title=None, tls=None, type=None, url=None):
        if credentials and not isinstance(credentials, dict):
            raise TypeError("Expected argument 'credentials' to be a dict")
        pulumi.set(__self__, "credentials", credentials)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if protocol and not isinstance(protocol, str):
            raise TypeError("Expected argument 'protocol' to be a str")
        pulumi.set(__self__, "protocol", protocol)
        if proxy and not isinstance(proxy, dict):
            raise TypeError("Expected argument 'proxy' to be a dict")
        pulumi.set(__self__, "proxy", proxy)
        if resource_id and not isinstance(resource_id, str):
            raise TypeError("Expected argument 'resource_id' to be a str")
        pulumi.set(__self__, "resource_id", resource_id)
        if title and not isinstance(title, str):
            raise TypeError("Expected argument 'title' to be a str")
        pulumi.set(__self__, "title", title)
        if tls and not isinstance(tls, dict):
            raise TypeError("Expected argument 'tls' to be a dict")
        pulumi.set(__self__, "tls", tls)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if url and not isinstance(url, str):
            raise TypeError("Expected argument 'url' to be a str")
        pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter
    def credentials(self) -> Optional['outputs.BackendCredentialsContractResponse']:
        """
        Backend Credentials Contract Properties
        """
        return pulumi.get(self, "credentials")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Backend Description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.BackendPropertiesResponse':
        """
        Backend Properties contract
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def protocol(self) -> str:
        """
        Backend communication protocol.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter
    def proxy(self) -> Optional['outputs.BackendProxyContractResponse']:
        """
        Backend Proxy Contract Properties
        """
        return pulumi.get(self, "proxy")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[str]:
        """
        Management Uri of the Resource in External System. This url can be the Arm Resource Id of Logic Apps, Function Apps or Api Apps.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter
    def title(self) -> Optional[str]:
        """
        Backend Title.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def tls(self) -> Optional['outputs.BackendTlsPropertiesResponse']:
        """
        Backend TLS Properties
        """
        return pulumi.get(self, "tls")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type for API Management resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def url(self) -> str:
        """
        Runtime Url of the Backend.
        """
        return pulumi.get(self, "url")


class AwaitableGetBackendResult(GetBackendResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBackendResult(
            credentials=self.credentials,
            description=self.description,
            id=self.id,
            name=self.name,
            properties=self.properties,
            protocol=self.protocol,
            proxy=self.proxy,
            resource_id=self.resource_id,
            title=self.title,
            tls=self.tls,
            type=self.type,
            url=self.url)


def get_backend(backendid: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                service_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBackendResult:
    """
    Backend details.


    :param str backendid: Identifier of the Backend entity. Must be unique in the current API Management service instance.
    :param str resource_group_name: The name of the resource group.
    :param str service_name: The name of the API Management service.
    """
    __args__ = dict()
    __args__['backendid'] = backendid
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20180101:getBackend', __args__, opts=opts, typ=GetBackendResult).value

    return AwaitableGetBackendResult(
        credentials=__ret__.credentials,
        description=__ret__.description,
        id=__ret__.id,
        name=__ret__.name,
        properties=__ret__.properties,
        protocol=__ret__.protocol,
        proxy=__ret__.proxy,
        resource_id=__ret__.resource_id,
        title=__ret__.title,
        tls=__ret__.tls,
        type=__ret__.type,
        url=__ret__.url)


@_utilities.lift_output_func(get_backend)
def get_backend_output(backendid: Optional[pulumi.Input[str]] = None,
                       resource_group_name: Optional[pulumi.Input[str]] = None,
                       service_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBackendResult]:
    """
    Backend details.


    :param str backendid: Identifier of the Backend entity. Must be unique in the current API Management service instance.
    :param str resource_group_name: The name of the resource group.
    :param str service_name: The name of the API Management service.
    """
    ...
