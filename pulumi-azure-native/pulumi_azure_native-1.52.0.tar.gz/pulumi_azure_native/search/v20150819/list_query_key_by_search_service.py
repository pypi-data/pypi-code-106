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
    'ListQueryKeyBySearchServiceResult',
    'AwaitableListQueryKeyBySearchServiceResult',
    'list_query_key_by_search_service',
    'list_query_key_by_search_service_output',
]

@pulumi.output_type
class ListQueryKeyBySearchServiceResult:
    """
    Response containing the query API keys for a given Azure Cognitive Search service.
    """
    def __init__(__self__, value=None):
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Sequence['outputs.QueryKeyResponse']:
        """
        The query keys for the Azure Cognitive Search service.
        """
        return pulumi.get(self, "value")


class AwaitableListQueryKeyBySearchServiceResult(ListQueryKeyBySearchServiceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListQueryKeyBySearchServiceResult(
            value=self.value)


def list_query_key_by_search_service(resource_group_name: Optional[str] = None,
                                     search_service_name: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListQueryKeyBySearchServiceResult:
    """
    Response containing the query API keys for a given Azure Cognitive Search service.


    :param str resource_group_name: The name of the resource group within the current subscription. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str search_service_name: The name of the Azure Cognitive Search service associated with the specified resource group.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['searchServiceName'] = search_service_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:search/v20150819:listQueryKeyBySearchService', __args__, opts=opts, typ=ListQueryKeyBySearchServiceResult).value

    return AwaitableListQueryKeyBySearchServiceResult(
        value=__ret__.value)


@_utilities.lift_output_func(list_query_key_by_search_service)
def list_query_key_by_search_service_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                            search_service_name: Optional[pulumi.Input[str]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListQueryKeyBySearchServiceResult]:
    """
    Response containing the query API keys for a given Azure Cognitive Search service.


    :param str resource_group_name: The name of the resource group within the current subscription. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str search_service_name: The name of the Azure Cognitive Search service associated with the specified resource group.
    """
    ...
