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
    'GetAutomationAccountResult',
    'AwaitableGetAutomationAccountResult',
    'get_automation_account',
    'get_automation_account_output',
]

@pulumi.output_type
class GetAutomationAccountResult:
    """
    Definition of the automation account type.
    """
    def __init__(__self__, automation_hybrid_service_url=None, creation_time=None, description=None, disable_local_auth=None, encryption=None, etag=None, id=None, identity=None, last_modified_by=None, last_modified_time=None, location=None, name=None, private_endpoint_connections=None, public_network_access=None, sku=None, state=None, system_data=None, tags=None, type=None):
        if automation_hybrid_service_url and not isinstance(automation_hybrid_service_url, str):
            raise TypeError("Expected argument 'automation_hybrid_service_url' to be a str")
        pulumi.set(__self__, "automation_hybrid_service_url", automation_hybrid_service_url)
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if disable_local_auth and not isinstance(disable_local_auth, bool):
            raise TypeError("Expected argument 'disable_local_auth' to be a bool")
        pulumi.set(__self__, "disable_local_auth", disable_local_auth)
        if encryption and not isinstance(encryption, dict):
            raise TypeError("Expected argument 'encryption' to be a dict")
        pulumi.set(__self__, "encryption", encryption)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if last_modified_by and not isinstance(last_modified_by, str):
            raise TypeError("Expected argument 'last_modified_by' to be a str")
        pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_time and not isinstance(last_modified_time, str):
            raise TypeError("Expected argument 'last_modified_time' to be a str")
        pulumi.set(__self__, "last_modified_time", last_modified_time)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if private_endpoint_connections and not isinstance(private_endpoint_connections, list):
            raise TypeError("Expected argument 'private_endpoint_connections' to be a list")
        pulumi.set(__self__, "private_endpoint_connections", private_endpoint_connections)
        if public_network_access and not isinstance(public_network_access, bool):
            raise TypeError("Expected argument 'public_network_access' to be a bool")
        pulumi.set(__self__, "public_network_access", public_network_access)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="automationHybridServiceUrl")
    def automation_hybrid_service_url(self) -> Optional[str]:
        """
        URL of automation hybrid service which is used for hybrid worker on-boarding.
        """
        return pulumi.get(self, "automation_hybrid_service_url")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> str:
        """
        Gets the creation time.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Gets or sets the description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[bool]:
        """
        Indicates whether requests using non-AAD authentication are blocked
        """
        return pulumi.get(self, "disable_local_auth")

    @property
    @pulumi.getter
    def encryption(self) -> Optional['outputs.EncryptionPropertiesResponse']:
        """
        Encryption properties for the automation account
        """
        return pulumi.get(self, "encryption")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        Gets or sets the etag of the resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource Id for the resource
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.IdentityResponse']:
        """
        Identity for the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[str]:
        """
        Gets or sets the last modified by.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> str:
        """
        Gets the last modified time.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The Azure Region where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Optional[Sequence['outputs.PrivateEndpointConnectionResponse']]:
        """
        List of Automation operations supported by the Automation resource provider.
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[bool]:
        """
        Indicates whether traffic on the non-ARM endpoint (Webhook/Agent) is allowed from the public internet
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.SkuResponse']:
        """
        Gets or sets the SKU of account.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        Gets status of account.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Resource system metadata.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetAutomationAccountResult(GetAutomationAccountResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAutomationAccountResult(
            automation_hybrid_service_url=self.automation_hybrid_service_url,
            creation_time=self.creation_time,
            description=self.description,
            disable_local_auth=self.disable_local_auth,
            encryption=self.encryption,
            etag=self.etag,
            id=self.id,
            identity=self.identity,
            last_modified_by=self.last_modified_by,
            last_modified_time=self.last_modified_time,
            location=self.location,
            name=self.name,
            private_endpoint_connections=self.private_endpoint_connections,
            public_network_access=self.public_network_access,
            sku=self.sku,
            state=self.state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_automation_account(automation_account_name: Optional[str] = None,
                           resource_group_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAutomationAccountResult:
    """
    Definition of the automation account type.


    :param str automation_account_name: The name of the automation account.
    :param str resource_group_name: Name of an Azure Resource group.
    """
    __args__ = dict()
    __args__['automationAccountName'] = automation_account_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:automation/v20210622:getAutomationAccount', __args__, opts=opts, typ=GetAutomationAccountResult).value

    return AwaitableGetAutomationAccountResult(
        automation_hybrid_service_url=__ret__.automation_hybrid_service_url,
        creation_time=__ret__.creation_time,
        description=__ret__.description,
        disable_local_auth=__ret__.disable_local_auth,
        encryption=__ret__.encryption,
        etag=__ret__.etag,
        id=__ret__.id,
        identity=__ret__.identity,
        last_modified_by=__ret__.last_modified_by,
        last_modified_time=__ret__.last_modified_time,
        location=__ret__.location,
        name=__ret__.name,
        private_endpoint_connections=__ret__.private_endpoint_connections,
        public_network_access=__ret__.public_network_access,
        sku=__ret__.sku,
        state=__ret__.state,
        system_data=__ret__.system_data,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_automation_account)
def get_automation_account_output(automation_account_name: Optional[pulumi.Input[str]] = None,
                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAutomationAccountResult]:
    """
    Definition of the automation account type.


    :param str automation_account_name: The name of the automation account.
    :param str resource_group_name: Name of an Azure Resource group.
    """
    ...
