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

__all__ = [
    'GetEntitiesGetTimelineResult',
    'AwaitableGetEntitiesGetTimelineResult',
    'get_entities_get_timeline',
    'get_entities_get_timeline_output',
]

@pulumi.output_type
class GetEntitiesGetTimelineResult:
    """
    The entity timeline result operation response.
    """
    def __init__(__self__, meta_data=None, value=None):
        if meta_data and not isinstance(meta_data, dict):
            raise TypeError("Expected argument 'meta_data' to be a dict")
        pulumi.set(__self__, "meta_data", meta_data)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="metaData")
    def meta_data(self) -> Optional['outputs.TimelineResultsMetadataResponse']:
        """
        The metadata from the timeline operation results.
        """
        return pulumi.get(self, "meta_data")

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence[Any]]:
        """
        The timeline result values.
        """
        return pulumi.get(self, "value")


class AwaitableGetEntitiesGetTimelineResult(GetEntitiesGetTimelineResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEntitiesGetTimelineResult(
            meta_data=self.meta_data,
            value=self.value)


def get_entities_get_timeline(end_time: Optional[str] = None,
                              entity_id: Optional[str] = None,
                              kinds: Optional[Sequence[Union[str, 'EntityTimelineKind']]] = None,
                              number_of_bucket: Optional[int] = None,
                              operational_insights_resource_provider: Optional[str] = None,
                              resource_group_name: Optional[str] = None,
                              start_time: Optional[str] = None,
                              workspace_name: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEntitiesGetTimelineResult:
    """
    The entity timeline result operation response.


    :param str end_time: The end timeline date, so the results returned are before this date.
    :param str entity_id: entity ID
    :param Sequence[Union[str, 'EntityTimelineKind']] kinds: Array of timeline Item kinds.
    :param int number_of_bucket: The number of bucket for timeline queries aggregation.
    :param str operational_insights_resource_provider: The namespace of workspaces resource provider- Microsoft.OperationalInsights.
    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    :param str start_time: The start timeline date, so the results returned are after this date.
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['endTime'] = end_time
    __args__['entityId'] = entity_id
    __args__['kinds'] = kinds
    __args__['numberOfBucket'] = number_of_bucket
    __args__['operationalInsightsResourceProvider'] = operational_insights_resource_provider
    __args__['resourceGroupName'] = resource_group_name
    __args__['startTime'] = start_time
    __args__['workspaceName'] = workspace_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:securityinsights/v20190101preview:getEntitiesGetTimeline', __args__, opts=opts, typ=GetEntitiesGetTimelineResult).value

    return AwaitableGetEntitiesGetTimelineResult(
        meta_data=__ret__.meta_data,
        value=__ret__.value)


@_utilities.lift_output_func(get_entities_get_timeline)
def get_entities_get_timeline_output(end_time: Optional[pulumi.Input[str]] = None,
                                     entity_id: Optional[pulumi.Input[str]] = None,
                                     kinds: Optional[pulumi.Input[Optional[Sequence[Union[str, 'EntityTimelineKind']]]]] = None,
                                     number_of_bucket: Optional[pulumi.Input[Optional[int]]] = None,
                                     operational_insights_resource_provider: Optional[pulumi.Input[str]] = None,
                                     resource_group_name: Optional[pulumi.Input[str]] = None,
                                     start_time: Optional[pulumi.Input[str]] = None,
                                     workspace_name: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEntitiesGetTimelineResult]:
    """
    The entity timeline result operation response.


    :param str end_time: The end timeline date, so the results returned are before this date.
    :param str entity_id: entity ID
    :param Sequence[Union[str, 'EntityTimelineKind']] kinds: Array of timeline Item kinds.
    :param int number_of_bucket: The number of bucket for timeline queries aggregation.
    :param str operational_insights_resource_provider: The namespace of workspaces resource provider- Microsoft.OperationalInsights.
    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    :param str start_time: The start timeline date, so the results returned are after this date.
    :param str workspace_name: The name of the workspace.
    """
    ...
