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

__all__ = ['VirtualMachineScaleSetVMArgs', 'VirtualMachineScaleSetVM']

@pulumi.input_type
class VirtualMachineScaleSetVMArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 vm_scale_set_name: pulumi.Input[str],
                 additional_capabilities: Optional[pulumi.Input['AdditionalCapabilitiesArgs']] = None,
                 availability_set: Optional[pulumi.Input['SubResourceArgs']] = None,
                 diagnostics_profile: Optional[pulumi.Input['DiagnosticsProfileArgs']] = None,
                 hardware_profile: Optional[pulumi.Input['HardwareProfileArgs']] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 license_type: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_profile: Optional[pulumi.Input['NetworkProfileArgs']] = None,
                 os_profile: Optional[pulumi.Input['OSProfileArgs']] = None,
                 plan: Optional[pulumi.Input['PlanArgs']] = None,
                 storage_profile: Optional[pulumi.Input['StorageProfileArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a VirtualMachineScaleSetVM resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] vm_scale_set_name: The name of the VM scale set where the extension should be create or updated.
        :param pulumi.Input['AdditionalCapabilitiesArgs'] additional_capabilities: Specifies additional capabilities enabled or disabled on the virtual machine in the scale set. For instance: whether the virtual machine has the capability to support attaching managed data disks with UltraSSD_LRS storage account type.
        :param pulumi.Input['SubResourceArgs'] availability_set: Specifies information about the availability set that the virtual machine should be assigned to. Virtual machines specified in the same availability set are allocated to different nodes to maximize availability. For more information about availability sets, see [Manage the availability of virtual machines](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-manage-availability?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json). <br><br> For more information on Azure planned maintenance, see [Planned maintenance for virtual machines in Azure](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-planned-maintenance?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json) <br><br> Currently, a VM can only be added to availability set at creation time. An existing VM cannot be added to an availability set.
        :param pulumi.Input['DiagnosticsProfileArgs'] diagnostics_profile: Specifies the boot diagnostic settings state. <br><br>Minimum api-version: 2015-06-15.
        :param pulumi.Input['HardwareProfileArgs'] hardware_profile: Specifies the hardware settings for the virtual machine.
        :param pulumi.Input[str] instance_id: The instance ID of the virtual machine.
        :param pulumi.Input[str] license_type: Specifies that the image or disk that is being used was licensed on-premises. This element is only used for images that contain the Windows Server operating system. <br><br> Possible values are: <br><br> Windows_Client <br><br> Windows_Server <br><br> If this element is included in a request for an update, the value must match the initial value. This value cannot be updated. <br><br> For more information, see [Azure Hybrid Use Benefit for Windows Server](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json) <br><br> Minimum api-version: 2015-06-15
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input['NetworkProfileArgs'] network_profile: Specifies the network interfaces of the virtual machine.
        :param pulumi.Input['OSProfileArgs'] os_profile: Specifies the operating system settings for the virtual machine.
        :param pulumi.Input['PlanArgs'] plan: Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use.  In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started ->**. Enter any required information and then click **Save**.
        :param pulumi.Input['StorageProfileArgs'] storage_profile: Specifies the storage settings for the virtual machine disks.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "vm_scale_set_name", vm_scale_set_name)
        if additional_capabilities is not None:
            pulumi.set(__self__, "additional_capabilities", additional_capabilities)
        if availability_set is not None:
            pulumi.set(__self__, "availability_set", availability_set)
        if diagnostics_profile is not None:
            pulumi.set(__self__, "diagnostics_profile", diagnostics_profile)
        if hardware_profile is not None:
            pulumi.set(__self__, "hardware_profile", hardware_profile)
        if instance_id is not None:
            pulumi.set(__self__, "instance_id", instance_id)
        if license_type is not None:
            pulumi.set(__self__, "license_type", license_type)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if network_profile is not None:
            pulumi.set(__self__, "network_profile", network_profile)
        if os_profile is not None:
            pulumi.set(__self__, "os_profile", os_profile)
        if plan is not None:
            pulumi.set(__self__, "plan", plan)
        if storage_profile is not None:
            pulumi.set(__self__, "storage_profile", storage_profile)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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
    @pulumi.getter(name="vmScaleSetName")
    def vm_scale_set_name(self) -> pulumi.Input[str]:
        """
        The name of the VM scale set where the extension should be create or updated.
        """
        return pulumi.get(self, "vm_scale_set_name")

    @vm_scale_set_name.setter
    def vm_scale_set_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "vm_scale_set_name", value)

    @property
    @pulumi.getter(name="additionalCapabilities")
    def additional_capabilities(self) -> Optional[pulumi.Input['AdditionalCapabilitiesArgs']]:
        """
        Specifies additional capabilities enabled or disabled on the virtual machine in the scale set. For instance: whether the virtual machine has the capability to support attaching managed data disks with UltraSSD_LRS storage account type.
        """
        return pulumi.get(self, "additional_capabilities")

    @additional_capabilities.setter
    def additional_capabilities(self, value: Optional[pulumi.Input['AdditionalCapabilitiesArgs']]):
        pulumi.set(self, "additional_capabilities", value)

    @property
    @pulumi.getter(name="availabilitySet")
    def availability_set(self) -> Optional[pulumi.Input['SubResourceArgs']]:
        """
        Specifies information about the availability set that the virtual machine should be assigned to. Virtual machines specified in the same availability set are allocated to different nodes to maximize availability. For more information about availability sets, see [Manage the availability of virtual machines](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-manage-availability?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json). <br><br> For more information on Azure planned maintenance, see [Planned maintenance for virtual machines in Azure](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-planned-maintenance?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json) <br><br> Currently, a VM can only be added to availability set at creation time. An existing VM cannot be added to an availability set.
        """
        return pulumi.get(self, "availability_set")

    @availability_set.setter
    def availability_set(self, value: Optional[pulumi.Input['SubResourceArgs']]):
        pulumi.set(self, "availability_set", value)

    @property
    @pulumi.getter(name="diagnosticsProfile")
    def diagnostics_profile(self) -> Optional[pulumi.Input['DiagnosticsProfileArgs']]:
        """
        Specifies the boot diagnostic settings state. <br><br>Minimum api-version: 2015-06-15.
        """
        return pulumi.get(self, "diagnostics_profile")

    @diagnostics_profile.setter
    def diagnostics_profile(self, value: Optional[pulumi.Input['DiagnosticsProfileArgs']]):
        pulumi.set(self, "diagnostics_profile", value)

    @property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(self) -> Optional[pulumi.Input['HardwareProfileArgs']]:
        """
        Specifies the hardware settings for the virtual machine.
        """
        return pulumi.get(self, "hardware_profile")

    @hardware_profile.setter
    def hardware_profile(self, value: Optional[pulumi.Input['HardwareProfileArgs']]):
        pulumi.set(self, "hardware_profile", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        The instance ID of the virtual machine.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies that the image or disk that is being used was licensed on-premises. This element is only used for images that contain the Windows Server operating system. <br><br> Possible values are: <br><br> Windows_Client <br><br> Windows_Server <br><br> If this element is included in a request for an update, the value must match the initial value. This value cannot be updated. <br><br> For more information, see [Azure Hybrid Use Benefit for Windows Server](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json) <br><br> Minimum api-version: 2015-06-15
        """
        return pulumi.get(self, "license_type")

    @license_type.setter
    def license_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "license_type", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[pulumi.Input['NetworkProfileArgs']]:
        """
        Specifies the network interfaces of the virtual machine.
        """
        return pulumi.get(self, "network_profile")

    @network_profile.setter
    def network_profile(self, value: Optional[pulumi.Input['NetworkProfileArgs']]):
        pulumi.set(self, "network_profile", value)

    @property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> Optional[pulumi.Input['OSProfileArgs']]:
        """
        Specifies the operating system settings for the virtual machine.
        """
        return pulumi.get(self, "os_profile")

    @os_profile.setter
    def os_profile(self, value: Optional[pulumi.Input['OSProfileArgs']]):
        pulumi.set(self, "os_profile", value)

    @property
    @pulumi.getter
    def plan(self) -> Optional[pulumi.Input['PlanArgs']]:
        """
        Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use.  In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started ->**. Enter any required information and then click **Save**.
        """
        return pulumi.get(self, "plan")

    @plan.setter
    def plan(self, value: Optional[pulumi.Input['PlanArgs']]):
        pulumi.set(self, "plan", value)

    @property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[pulumi.Input['StorageProfileArgs']]:
        """
        Specifies the storage settings for the virtual machine disks.
        """
        return pulumi.get(self, "storage_profile")

    @storage_profile.setter
    def storage_profile(self, value: Optional[pulumi.Input['StorageProfileArgs']]):
        pulumi.set(self, "storage_profile", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class VirtualMachineScaleSetVM(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_capabilities: Optional[pulumi.Input[pulumi.InputType['AdditionalCapabilitiesArgs']]] = None,
                 availability_set: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 diagnostics_profile: Optional[pulumi.Input[pulumi.InputType['DiagnosticsProfileArgs']]] = None,
                 hardware_profile: Optional[pulumi.Input[pulumi.InputType['HardwareProfileArgs']]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 license_type: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_profile: Optional[pulumi.Input[pulumi.InputType['NetworkProfileArgs']]] = None,
                 os_profile: Optional[pulumi.Input[pulumi.InputType['OSProfileArgs']]] = None,
                 plan: Optional[pulumi.Input[pulumi.InputType['PlanArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_profile: Optional[pulumi.Input[pulumi.InputType['StorageProfileArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vm_scale_set_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Describes a virtual machine scale set virtual machine.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AdditionalCapabilitiesArgs']] additional_capabilities: Specifies additional capabilities enabled or disabled on the virtual machine in the scale set. For instance: whether the virtual machine has the capability to support attaching managed data disks with UltraSSD_LRS storage account type.
        :param pulumi.Input[pulumi.InputType['SubResourceArgs']] availability_set: Specifies information about the availability set that the virtual machine should be assigned to. Virtual machines specified in the same availability set are allocated to different nodes to maximize availability. For more information about availability sets, see [Manage the availability of virtual machines](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-manage-availability?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json). <br><br> For more information on Azure planned maintenance, see [Planned maintenance for virtual machines in Azure](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-planned-maintenance?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json) <br><br> Currently, a VM can only be added to availability set at creation time. An existing VM cannot be added to an availability set.
        :param pulumi.Input[pulumi.InputType['DiagnosticsProfileArgs']] diagnostics_profile: Specifies the boot diagnostic settings state. <br><br>Minimum api-version: 2015-06-15.
        :param pulumi.Input[pulumi.InputType['HardwareProfileArgs']] hardware_profile: Specifies the hardware settings for the virtual machine.
        :param pulumi.Input[str] instance_id: The instance ID of the virtual machine.
        :param pulumi.Input[str] license_type: Specifies that the image or disk that is being used was licensed on-premises. This element is only used for images that contain the Windows Server operating system. <br><br> Possible values are: <br><br> Windows_Client <br><br> Windows_Server <br><br> If this element is included in a request for an update, the value must match the initial value. This value cannot be updated. <br><br> For more information, see [Azure Hybrid Use Benefit for Windows Server](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json) <br><br> Minimum api-version: 2015-06-15
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[pulumi.InputType['NetworkProfileArgs']] network_profile: Specifies the network interfaces of the virtual machine.
        :param pulumi.Input[pulumi.InputType['OSProfileArgs']] os_profile: Specifies the operating system settings for the virtual machine.
        :param pulumi.Input[pulumi.InputType['PlanArgs']] plan: Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use.  In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started ->**. Enter any required information and then click **Save**.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[pulumi.InputType['StorageProfileArgs']] storage_profile: Specifies the storage settings for the virtual machine disks.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] vm_scale_set_name: The name of the VM scale set where the extension should be create or updated.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VirtualMachineScaleSetVMArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Describes a virtual machine scale set virtual machine.

        :param str resource_name: The name of the resource.
        :param VirtualMachineScaleSetVMArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VirtualMachineScaleSetVMArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_capabilities: Optional[pulumi.Input[pulumi.InputType['AdditionalCapabilitiesArgs']]] = None,
                 availability_set: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 diagnostics_profile: Optional[pulumi.Input[pulumi.InputType['DiagnosticsProfileArgs']]] = None,
                 hardware_profile: Optional[pulumi.Input[pulumi.InputType['HardwareProfileArgs']]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 license_type: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_profile: Optional[pulumi.Input[pulumi.InputType['NetworkProfileArgs']]] = None,
                 os_profile: Optional[pulumi.Input[pulumi.InputType['OSProfileArgs']]] = None,
                 plan: Optional[pulumi.Input[pulumi.InputType['PlanArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_profile: Optional[pulumi.Input[pulumi.InputType['StorageProfileArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vm_scale_set_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = VirtualMachineScaleSetVMArgs.__new__(VirtualMachineScaleSetVMArgs)

            __props__.__dict__["additional_capabilities"] = additional_capabilities
            __props__.__dict__["availability_set"] = availability_set
            __props__.__dict__["diagnostics_profile"] = diagnostics_profile
            __props__.__dict__["hardware_profile"] = hardware_profile
            __props__.__dict__["instance_id"] = instance_id
            __props__.__dict__["license_type"] = license_type
            __props__.__dict__["location"] = location
            __props__.__dict__["network_profile"] = network_profile
            __props__.__dict__["os_profile"] = os_profile
            __props__.__dict__["plan"] = plan
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["storage_profile"] = storage_profile
            __props__.__dict__["tags"] = tags
            if vm_scale_set_name is None and not opts.urn:
                raise TypeError("Missing required property 'vm_scale_set_name'")
            __props__.__dict__["vm_scale_set_name"] = vm_scale_set_name
            __props__.__dict__["instance_view"] = None
            __props__.__dict__["latest_model_applied"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["resources"] = None
            __props__.__dict__["sku"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["vm_id"] = None
            __props__.__dict__["zones"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:compute:VirtualMachineScaleSetVM"), pulumi.Alias(type_="azure-native:compute/v20171201:VirtualMachineScaleSetVM"), pulumi.Alias(type_="azure-native:compute/v20180401:VirtualMachineScaleSetVM"), pulumi.Alias(type_="azure-native:compute/v20180601:VirtualMachineScaleSetVM"), pulumi.Alias(type_="azure-native:compute/v20190301:VirtualMachineScaleSetVM"), pulumi.Alias(type_="azure-native:compute/v20190701:VirtualMachineScaleSetVM"), pulumi.Alias(type_="azure-native:compute/v20191201:VirtualMachineScaleSetVM"), pulumi.Alias(type_="azure-native:compute/v20200601:VirtualMachineScaleSetVM"), pulumi.Alias(type_="azure-native:compute/v20201201:VirtualMachineScaleSetVM"), pulumi.Alias(type_="azure-native:compute/v20210301:VirtualMachineScaleSetVM"), pulumi.Alias(type_="azure-native:compute/v20210401:VirtualMachineScaleSetVM"), pulumi.Alias(type_="azure-native:compute/v20210701:VirtualMachineScaleSetVM")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VirtualMachineScaleSetVM, __self__).__init__(
            'azure-native:compute/v20181001:VirtualMachineScaleSetVM',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VirtualMachineScaleSetVM':
        """
        Get an existing VirtualMachineScaleSetVM resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VirtualMachineScaleSetVMArgs.__new__(VirtualMachineScaleSetVMArgs)

        __props__.__dict__["additional_capabilities"] = None
        __props__.__dict__["availability_set"] = None
        __props__.__dict__["diagnostics_profile"] = None
        __props__.__dict__["hardware_profile"] = None
        __props__.__dict__["instance_id"] = None
        __props__.__dict__["instance_view"] = None
        __props__.__dict__["latest_model_applied"] = None
        __props__.__dict__["license_type"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_profile"] = None
        __props__.__dict__["os_profile"] = None
        __props__.__dict__["plan"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resources"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["storage_profile"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["vm_id"] = None
        __props__.__dict__["zones"] = None
        return VirtualMachineScaleSetVM(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="additionalCapabilities")
    def additional_capabilities(self) -> pulumi.Output[Optional['outputs.AdditionalCapabilitiesResponse']]:
        """
        Specifies additional capabilities enabled or disabled on the virtual machine in the scale set. For instance: whether the virtual machine has the capability to support attaching managed data disks with UltraSSD_LRS storage account type.
        """
        return pulumi.get(self, "additional_capabilities")

    @property
    @pulumi.getter(name="availabilitySet")
    def availability_set(self) -> pulumi.Output[Optional['outputs.SubResourceResponse']]:
        """
        Specifies information about the availability set that the virtual machine should be assigned to. Virtual machines specified in the same availability set are allocated to different nodes to maximize availability. For more information about availability sets, see [Manage the availability of virtual machines](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-manage-availability?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json). <br><br> For more information on Azure planned maintenance, see [Planned maintenance for virtual machines in Azure](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-planned-maintenance?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json) <br><br> Currently, a VM can only be added to availability set at creation time. An existing VM cannot be added to an availability set.
        """
        return pulumi.get(self, "availability_set")

    @property
    @pulumi.getter(name="diagnosticsProfile")
    def diagnostics_profile(self) -> pulumi.Output[Optional['outputs.DiagnosticsProfileResponse']]:
        """
        Specifies the boot diagnostic settings state. <br><br>Minimum api-version: 2015-06-15.
        """
        return pulumi.get(self, "diagnostics_profile")

    @property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(self) -> pulumi.Output[Optional['outputs.HardwareProfileResponse']]:
        """
        Specifies the hardware settings for the virtual machine.
        """
        return pulumi.get(self, "hardware_profile")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[str]:
        """
        The virtual machine instance ID.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter(name="instanceView")
    def instance_view(self) -> pulumi.Output['outputs.VirtualMachineScaleSetVMInstanceViewResponse']:
        """
        The virtual machine instance view.
        """
        return pulumi.get(self, "instance_view")

    @property
    @pulumi.getter(name="latestModelApplied")
    def latest_model_applied(self) -> pulumi.Output[bool]:
        """
        Specifies whether the latest model has been applied to the virtual machine.
        """
        return pulumi.get(self, "latest_model_applied")

    @property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies that the image or disk that is being used was licensed on-premises. This element is only used for images that contain the Windows Server operating system. <br><br> Possible values are: <br><br> Windows_Client <br><br> Windows_Server <br><br> If this element is included in a request for an update, the value must match the initial value. This value cannot be updated. <br><br> For more information, see [Azure Hybrid Use Benefit for Windows Server](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json) <br><br> Minimum api-version: 2015-06-15
        """
        return pulumi.get(self, "license_type")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> pulumi.Output[Optional['outputs.NetworkProfileResponse']]:
        """
        Specifies the network interfaces of the virtual machine.
        """
        return pulumi.get(self, "network_profile")

    @property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> pulumi.Output[Optional['outputs.OSProfileResponse']]:
        """
        Specifies the operating system settings for the virtual machine.
        """
        return pulumi.get(self, "os_profile")

    @property
    @pulumi.getter
    def plan(self) -> pulumi.Output[Optional['outputs.PlanResponse']]:
        """
        Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use.  In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started ->**. Enter any required information and then click **Save**.
        """
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state, which only appears in the response.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def resources(self) -> pulumi.Output[Sequence['outputs.VirtualMachineExtensionResponse']]:
        """
        The virtual machine child extension resources.
        """
        return pulumi.get(self, "resources")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output['outputs.SkuResponse']:
        """
        The virtual machine SKU.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> pulumi.Output[Optional['outputs.StorageProfileResponse']]:
        """
        Specifies the storage settings for the virtual machine disks.
        """
        return pulumi.get(self, "storage_profile")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> pulumi.Output[str]:
        """
        Azure VM unique ID.
        """
        return pulumi.get(self, "vm_id")

    @property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Sequence[str]]:
        """
        The virtual machine zones.
        """
        return pulumi.get(self, "zones")

