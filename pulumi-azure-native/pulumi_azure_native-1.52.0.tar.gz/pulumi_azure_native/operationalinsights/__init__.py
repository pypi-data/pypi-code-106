# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .cluster import *
from .data_export import *
from .data_source import *
from .get_cluster import *
from .get_data_export import *
from .get_data_source import *
from .get_linked_service import *
from .get_linked_storage_account import *
from .get_machine_group import *
from .get_query import *
from .get_query_pack import *
from .get_saved_search import *
from .get_shared_keys import *
from .get_storage_insight_config import *
from .get_workspace import *
from .linked_service import *
from .linked_storage_account import *
from .machine_group import *
from .query import *
from .query_pack import *
from .saved_search import *
from .storage_insight_config import *
from .workspace import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.operationalinsights.v20150320 as __v20150320
    v20150320 = __v20150320
    import pulumi_azure_native.operationalinsights.v20151101preview as __v20151101preview
    v20151101preview = __v20151101preview
    import pulumi_azure_native.operationalinsights.v20190801preview as __v20190801preview
    v20190801preview = __v20190801preview
    import pulumi_azure_native.operationalinsights.v20190901preview as __v20190901preview
    v20190901preview = __v20190901preview
    import pulumi_azure_native.operationalinsights.v20200301preview as __v20200301preview
    v20200301preview = __v20200301preview
    import pulumi_azure_native.operationalinsights.v20200801 as __v20200801
    v20200801 = __v20200801
    import pulumi_azure_native.operationalinsights.v20201001 as __v20201001
    v20201001 = __v20201001
    import pulumi_azure_native.operationalinsights.v20210601 as __v20210601
    v20210601 = __v20210601
else:
    v20150320 = _utilities.lazy_import('pulumi_azure_native.operationalinsights.v20150320')
    v20151101preview = _utilities.lazy_import('pulumi_azure_native.operationalinsights.v20151101preview')
    v20190801preview = _utilities.lazy_import('pulumi_azure_native.operationalinsights.v20190801preview')
    v20190901preview = _utilities.lazy_import('pulumi_azure_native.operationalinsights.v20190901preview')
    v20200301preview = _utilities.lazy_import('pulumi_azure_native.operationalinsights.v20200301preview')
    v20200801 = _utilities.lazy_import('pulumi_azure_native.operationalinsights.v20200801')
    v20201001 = _utilities.lazy_import('pulumi_azure_native.operationalinsights.v20201001')
    v20210601 = _utilities.lazy_import('pulumi_azure_native.operationalinsights.v20210601')

