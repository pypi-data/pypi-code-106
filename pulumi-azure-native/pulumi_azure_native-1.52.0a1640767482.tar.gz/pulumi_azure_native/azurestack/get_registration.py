# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetRegistrationResult',
    'AwaitableGetRegistrationResult',
    'get_registration',
    'get_registration_output',
]

@pulumi.output_type
class GetRegistrationResult:
    """
    Registration information.
    """
    def __init__(__self__, billing_model=None, cloud_id=None, etag=None, id=None, location=None, name=None, object_id=None, tags=None, type=None):
        if billing_model and not isinstance(billing_model, str):
            raise TypeError("Expected argument 'billing_model' to be a str")
        pulumi.set(__self__, "billing_model", billing_model)
        if cloud_id and not isinstance(cloud_id, str):
            raise TypeError("Expected argument 'cloud_id' to be a str")
        pulumi.set(__self__, "cloud_id", cloud_id)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if object_id and not isinstance(object_id, str):
            raise TypeError("Expected argument 'object_id' to be a str")
        pulumi.set(__self__, "object_id", object_id)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="billingModel")
    def billing_model(self) -> Optional[str]:
        """
        Specifies the billing mode for the Azure Stack registration.
        """
        return pulumi.get(self, "billing_model")

    @property
    @pulumi.getter(name="cloudId")
    def cloud_id(self) -> Optional[str]:
        """
        The identifier of the registered Azure Stack.
        """
        return pulumi.get(self, "cloud_id")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        The entity tag used for optimistic concurrency when modifying the resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        ID of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[str]:
        """
        The object identifier associated with the Azure Stack connecting to Azure.
        """
        return pulumi.get(self, "object_id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Custom tags for the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of Resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetRegistrationResult(GetRegistrationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRegistrationResult(
            billing_model=self.billing_model,
            cloud_id=self.cloud_id,
            etag=self.etag,
            id=self.id,
            location=self.location,
            name=self.name,
            object_id=self.object_id,
            tags=self.tags,
            type=self.type)


def get_registration(registration_name: Optional[str] = None,
                     resource_group: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRegistrationResult:
    """
    Registration information.
    API Version: 2017-06-01.


    :param str registration_name: Name of the Azure Stack registration.
    :param str resource_group: Name of the resource group.
    """
    __args__ = dict()
    __args__['registrationName'] = registration_name
    __args__['resourceGroup'] = resource_group
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:azurestack:getRegistration', __args__, opts=opts, typ=GetRegistrationResult).value

    return AwaitableGetRegistrationResult(
        billing_model=__ret__.billing_model,
        cloud_id=__ret__.cloud_id,
        etag=__ret__.etag,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        object_id=__ret__.object_id,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_registration)
def get_registration_output(registration_name: Optional[pulumi.Input[str]] = None,
                            resource_group: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRegistrationResult]:
    """
    Registration information.
    API Version: 2017-06-01.


    :param str registration_name: Name of the Azure Stack registration.
    :param str resource_group: Name of the resource group.
    """
    ...
