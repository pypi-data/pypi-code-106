# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from .get_graph_query import *
from .graph_query import *

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.resourcegraph.v20180901preview as __v20180901preview
    v20180901preview = __v20180901preview
    import pulumi_azure_native.resourcegraph.v20200401preview as __v20200401preview
    v20200401preview = __v20200401preview
else:
    v20180901preview = _utilities.lazy_import('pulumi_azure_native.resourcegraph.v20180901preview')
    v20200401preview = _utilities.lazy_import('pulumi_azure_native.resourcegraph.v20200401preview')

