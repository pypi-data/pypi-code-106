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
    'GetActionGroupResult',
    'AwaitableGetActionGroupResult',
    'get_action_group',
    'get_action_group_output',
]

@pulumi.output_type
class GetActionGroupResult:
    """
    An action group resource.
    """
    def __init__(__self__, arm_role_receivers=None, automation_runbook_receivers=None, azure_app_push_receivers=None, azure_function_receivers=None, email_receivers=None, enabled=None, event_hub_receivers=None, group_short_name=None, id=None, identity=None, itsm_receivers=None, kind=None, location=None, logic_app_receivers=None, name=None, sms_receivers=None, tags=None, type=None, voice_receivers=None, webhook_receivers=None):
        if arm_role_receivers and not isinstance(arm_role_receivers, list):
            raise TypeError("Expected argument 'arm_role_receivers' to be a list")
        pulumi.set(__self__, "arm_role_receivers", arm_role_receivers)
        if automation_runbook_receivers and not isinstance(automation_runbook_receivers, list):
            raise TypeError("Expected argument 'automation_runbook_receivers' to be a list")
        pulumi.set(__self__, "automation_runbook_receivers", automation_runbook_receivers)
        if azure_app_push_receivers and not isinstance(azure_app_push_receivers, list):
            raise TypeError("Expected argument 'azure_app_push_receivers' to be a list")
        pulumi.set(__self__, "azure_app_push_receivers", azure_app_push_receivers)
        if azure_function_receivers and not isinstance(azure_function_receivers, list):
            raise TypeError("Expected argument 'azure_function_receivers' to be a list")
        pulumi.set(__self__, "azure_function_receivers", azure_function_receivers)
        if email_receivers and not isinstance(email_receivers, list):
            raise TypeError("Expected argument 'email_receivers' to be a list")
        pulumi.set(__self__, "email_receivers", email_receivers)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if event_hub_receivers and not isinstance(event_hub_receivers, list):
            raise TypeError("Expected argument 'event_hub_receivers' to be a list")
        pulumi.set(__self__, "event_hub_receivers", event_hub_receivers)
        if group_short_name and not isinstance(group_short_name, str):
            raise TypeError("Expected argument 'group_short_name' to be a str")
        pulumi.set(__self__, "group_short_name", group_short_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, str):
            raise TypeError("Expected argument 'identity' to be a str")
        pulumi.set(__self__, "identity", identity)
        if itsm_receivers and not isinstance(itsm_receivers, list):
            raise TypeError("Expected argument 'itsm_receivers' to be a list")
        pulumi.set(__self__, "itsm_receivers", itsm_receivers)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if logic_app_receivers and not isinstance(logic_app_receivers, list):
            raise TypeError("Expected argument 'logic_app_receivers' to be a list")
        pulumi.set(__self__, "logic_app_receivers", logic_app_receivers)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if sms_receivers and not isinstance(sms_receivers, list):
            raise TypeError("Expected argument 'sms_receivers' to be a list")
        pulumi.set(__self__, "sms_receivers", sms_receivers)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if voice_receivers and not isinstance(voice_receivers, list):
            raise TypeError("Expected argument 'voice_receivers' to be a list")
        pulumi.set(__self__, "voice_receivers", voice_receivers)
        if webhook_receivers and not isinstance(webhook_receivers, list):
            raise TypeError("Expected argument 'webhook_receivers' to be a list")
        pulumi.set(__self__, "webhook_receivers", webhook_receivers)

    @property
    @pulumi.getter(name="armRoleReceivers")
    def arm_role_receivers(self) -> Optional[Sequence['outputs.ArmRoleReceiverResponse']]:
        """
        The list of ARM role receivers that are part of this action group. Roles are Azure RBAC roles and only built-in roles are supported.
        """
        return pulumi.get(self, "arm_role_receivers")

    @property
    @pulumi.getter(name="automationRunbookReceivers")
    def automation_runbook_receivers(self) -> Optional[Sequence['outputs.AutomationRunbookReceiverResponse']]:
        """
        The list of AutomationRunbook receivers that are part of this action group.
        """
        return pulumi.get(self, "automation_runbook_receivers")

    @property
    @pulumi.getter(name="azureAppPushReceivers")
    def azure_app_push_receivers(self) -> Optional[Sequence['outputs.AzureAppPushReceiverResponse']]:
        """
        The list of AzureAppPush receivers that are part of this action group.
        """
        return pulumi.get(self, "azure_app_push_receivers")

    @property
    @pulumi.getter(name="azureFunctionReceivers")
    def azure_function_receivers(self) -> Optional[Sequence['outputs.AzureFunctionReceiverResponse']]:
        """
        The list of azure function receivers that are part of this action group.
        """
        return pulumi.get(self, "azure_function_receivers")

    @property
    @pulumi.getter(name="emailReceivers")
    def email_receivers(self) -> Optional[Sequence['outputs.EmailReceiverResponse']]:
        """
        The list of email receivers that are part of this action group.
        """
        return pulumi.get(self, "email_receivers")

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        """
        Indicates whether this action group is enabled. If an action group is not enabled, then none of its receivers will receive communications.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="eventHubReceivers")
    def event_hub_receivers(self) -> Optional[Sequence['outputs.EventHubReceiverResponse']]:
        """
        The list of event hub receivers that are part of this action group.
        """
        return pulumi.get(self, "event_hub_receivers")

    @property
    @pulumi.getter(name="groupShortName")
    def group_short_name(self) -> str:
        """
        The short name of the action group. This will be used in SMS messages.
        """
        return pulumi.get(self, "group_short_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Azure resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> str:
        """
        Azure resource identity
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="itsmReceivers")
    def itsm_receivers(self) -> Optional[Sequence['outputs.ItsmReceiverResponse']]:
        """
        The list of ITSM receivers that are part of this action group.
        """
        return pulumi.get(self, "itsm_receivers")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Azure resource kind
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="logicAppReceivers")
    def logic_app_receivers(self) -> Optional[Sequence['outputs.LogicAppReceiverResponse']]:
        """
        The list of logic app receivers that are part of this action group.
        """
        return pulumi.get(self, "logic_app_receivers")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Azure resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="smsReceivers")
    def sms_receivers(self) -> Optional[Sequence['outputs.SmsReceiverResponse']]:
        """
        The list of SMS receivers that are part of this action group.
        """
        return pulumi.get(self, "sms_receivers")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Azure resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="voiceReceivers")
    def voice_receivers(self) -> Optional[Sequence['outputs.VoiceReceiverResponse']]:
        """
        The list of voice receivers that are part of this action group.
        """
        return pulumi.get(self, "voice_receivers")

    @property
    @pulumi.getter(name="webhookReceivers")
    def webhook_receivers(self) -> Optional[Sequence['outputs.WebhookReceiverResponse']]:
        """
        The list of webhook receivers that are part of this action group.
        """
        return pulumi.get(self, "webhook_receivers")


class AwaitableGetActionGroupResult(GetActionGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetActionGroupResult(
            arm_role_receivers=self.arm_role_receivers,
            automation_runbook_receivers=self.automation_runbook_receivers,
            azure_app_push_receivers=self.azure_app_push_receivers,
            azure_function_receivers=self.azure_function_receivers,
            email_receivers=self.email_receivers,
            enabled=self.enabled,
            event_hub_receivers=self.event_hub_receivers,
            group_short_name=self.group_short_name,
            id=self.id,
            identity=self.identity,
            itsm_receivers=self.itsm_receivers,
            kind=self.kind,
            location=self.location,
            logic_app_receivers=self.logic_app_receivers,
            name=self.name,
            sms_receivers=self.sms_receivers,
            tags=self.tags,
            type=self.type,
            voice_receivers=self.voice_receivers,
            webhook_receivers=self.webhook_receivers)


def get_action_group(action_group_name: Optional[str] = None,
                     resource_group_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetActionGroupResult:
    """
    An action group resource.


    :param str action_group_name: The name of the action group.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['actionGroupName'] = action_group_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:insights/v20210901:getActionGroup', __args__, opts=opts, typ=GetActionGroupResult).value

    return AwaitableGetActionGroupResult(
        arm_role_receivers=__ret__.arm_role_receivers,
        automation_runbook_receivers=__ret__.automation_runbook_receivers,
        azure_app_push_receivers=__ret__.azure_app_push_receivers,
        azure_function_receivers=__ret__.azure_function_receivers,
        email_receivers=__ret__.email_receivers,
        enabled=__ret__.enabled,
        event_hub_receivers=__ret__.event_hub_receivers,
        group_short_name=__ret__.group_short_name,
        id=__ret__.id,
        identity=__ret__.identity,
        itsm_receivers=__ret__.itsm_receivers,
        kind=__ret__.kind,
        location=__ret__.location,
        logic_app_receivers=__ret__.logic_app_receivers,
        name=__ret__.name,
        sms_receivers=__ret__.sms_receivers,
        tags=__ret__.tags,
        type=__ret__.type,
        voice_receivers=__ret__.voice_receivers,
        webhook_receivers=__ret__.webhook_receivers)


@_utilities.lift_output_func(get_action_group)
def get_action_group_output(action_group_name: Optional[pulumi.Input[str]] = None,
                            resource_group_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetActionGroupResult]:
    """
    An action group resource.


    :param str action_group_name: The name of the action group.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
