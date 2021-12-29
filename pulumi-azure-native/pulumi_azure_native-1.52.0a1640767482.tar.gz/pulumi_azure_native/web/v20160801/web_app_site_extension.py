# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['WebAppSiteExtensionArgs', 'WebAppSiteExtension']

@pulumi.input_type
class WebAppSiteExtensionArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 site_extension_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a WebAppSiteExtension resource.
        :param pulumi.Input[str] name: Site name.
        :param pulumi.Input[str] resource_group_name: Name of the resource group to which the resource belongs.
        :param pulumi.Input[str] site_extension_id: Site extension name.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if site_extension_id is not None:
            pulumi.set(__self__, "site_extension_id", site_extension_id)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Site name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group to which the resource belongs.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="siteExtensionId")
    def site_extension_id(self) -> Optional[pulumi.Input[str]]:
        """
        Site extension name.
        """
        return pulumi.get(self, "site_extension_id")

    @site_extension_id.setter
    def site_extension_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "site_extension_id", value)


class WebAppSiteExtension(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 site_extension_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Site Extension Information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Site name.
        :param pulumi.Input[str] resource_group_name: Name of the resource group to which the resource belongs.
        :param pulumi.Input[str] site_extension_id: Site extension name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WebAppSiteExtensionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Site Extension Information.

        :param str resource_name: The name of the resource.
        :param WebAppSiteExtensionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WebAppSiteExtensionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 site_extension_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = WebAppSiteExtensionArgs.__new__(WebAppSiteExtensionArgs)

            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["site_extension_id"] = site_extension_id
            __props__.__dict__["authors"] = None
            __props__.__dict__["comment"] = None
            __props__.__dict__["description"] = None
            __props__.__dict__["download_count"] = None
            __props__.__dict__["extension_url"] = None
            __props__.__dict__["feed_url"] = None
            __props__.__dict__["icon_url"] = None
            __props__.__dict__["installation_args"] = None
            __props__.__dict__["installed_date_time"] = None
            __props__.__dict__["kind"] = None
            __props__.__dict__["license_url"] = None
            __props__.__dict__["local_is_latest_version"] = None
            __props__.__dict__["local_path"] = None
            __props__.__dict__["project_url"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["published_date_time"] = None
            __props__.__dict__["summary"] = None
            __props__.__dict__["title"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["version"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:web:WebAppSiteExtension"), pulumi.Alias(type_="azure-native:web/v20180201:WebAppSiteExtension"), pulumi.Alias(type_="azure-native:web/v20181101:WebAppSiteExtension"), pulumi.Alias(type_="azure-native:web/v20190801:WebAppSiteExtension"), pulumi.Alias(type_="azure-native:web/v20200601:WebAppSiteExtension"), pulumi.Alias(type_="azure-native:web/v20200901:WebAppSiteExtension"), pulumi.Alias(type_="azure-native:web/v20201001:WebAppSiteExtension"), pulumi.Alias(type_="azure-native:web/v20201201:WebAppSiteExtension"), pulumi.Alias(type_="azure-native:web/v20210101:WebAppSiteExtension"), pulumi.Alias(type_="azure-native:web/v20210115:WebAppSiteExtension"), pulumi.Alias(type_="azure-native:web/v20210201:WebAppSiteExtension")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(WebAppSiteExtension, __self__).__init__(
            'azure-native:web/v20160801:WebAppSiteExtension',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WebAppSiteExtension':
        """
        Get an existing WebAppSiteExtension resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WebAppSiteExtensionArgs.__new__(WebAppSiteExtensionArgs)

        __props__.__dict__["authors"] = None
        __props__.__dict__["comment"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["download_count"] = None
        __props__.__dict__["extension_url"] = None
        __props__.__dict__["feed_url"] = None
        __props__.__dict__["icon_url"] = None
        __props__.__dict__["installation_args"] = None
        __props__.__dict__["installed_date_time"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["license_url"] = None
        __props__.__dict__["local_is_latest_version"] = None
        __props__.__dict__["local_path"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["project_url"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["published_date_time"] = None
        __props__.__dict__["summary"] = None
        __props__.__dict__["title"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["version"] = None
        return WebAppSiteExtension(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def authors(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of authors.
        """
        return pulumi.get(self, "authors")

    @property
    @pulumi.getter
    def comment(self) -> pulumi.Output[Optional[str]]:
        """
        Site Extension comment.
        """
        return pulumi.get(self, "comment")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Detailed description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="downloadCount")
    def download_count(self) -> pulumi.Output[Optional[int]]:
        """
        Count of downloads.
        """
        return pulumi.get(self, "download_count")

    @property
    @pulumi.getter(name="extensionUrl")
    def extension_url(self) -> pulumi.Output[Optional[str]]:
        """
        Extension URL.
        """
        return pulumi.get(self, "extension_url")

    @property
    @pulumi.getter(name="feedUrl")
    def feed_url(self) -> pulumi.Output[Optional[str]]:
        """
        Feed URL.
        """
        return pulumi.get(self, "feed_url")

    @property
    @pulumi.getter(name="iconUrl")
    def icon_url(self) -> pulumi.Output[Optional[str]]:
        """
        Icon URL.
        """
        return pulumi.get(self, "icon_url")

    @property
    @pulumi.getter(name="installationArgs")
    def installation_args(self) -> pulumi.Output[Optional[str]]:
        """
        Installer command line parameters.
        """
        return pulumi.get(self, "installation_args")

    @property
    @pulumi.getter(name="installedDateTime")
    def installed_date_time(self) -> pulumi.Output[Optional[str]]:
        """
        Installed timestamp.
        """
        return pulumi.get(self, "installed_date_time")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="licenseUrl")
    def license_url(self) -> pulumi.Output[Optional[str]]:
        """
        License URL.
        """
        return pulumi.get(self, "license_url")

    @property
    @pulumi.getter(name="localIsLatestVersion")
    def local_is_latest_version(self) -> pulumi.Output[Optional[bool]]:
        """
        <code>true</code> if the local version is the latest version; <code>false</code> otherwise.
        """
        return pulumi.get(self, "local_is_latest_version")

    @property
    @pulumi.getter(name="localPath")
    def local_path(self) -> pulumi.Output[Optional[str]]:
        """
        Local path.
        """
        return pulumi.get(self, "local_path")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="projectUrl")
    def project_url(self) -> pulumi.Output[Optional[str]]:
        """
        Project URL.
        """
        return pulumi.get(self, "project_url")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        Provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publishedDateTime")
    def published_date_time(self) -> pulumi.Output[Optional[str]]:
        """
        Published timestamp.
        """
        return pulumi.get(self, "published_date_time")

    @property
    @pulumi.getter
    def summary(self) -> pulumi.Output[Optional[str]]:
        """
        Summary description.
        """
        return pulumi.get(self, "summary")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[Optional[str]]:
        """
        Site extension title.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[str]]:
        """
        Version information.
        """
        return pulumi.get(self, "version")

