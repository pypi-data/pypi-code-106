# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'BackendEnabledState',
    'DynamicCompressionEnabled',
    'EnforceCertificateNameCheckEnabledState',
    'FrontDoorEnabledState',
    'FrontDoorForwardingProtocol',
    'FrontDoorHealthProbeMethod',
    'FrontDoorProtocol',
    'FrontDoorQuery',
    'FrontDoorRedirectProtocol',
    'FrontDoorRedirectType',
    'HeaderActionType',
    'HealthProbeEnabled',
    'MatchProcessingBehavior',
    'RoutingRuleEnabledState',
    'RulesEngineMatchVariable',
    'RulesEngineOperator',
    'SessionAffinityEnabledState',
    'Transform',
]


class BackendEnabledState(str, Enum):
    """
    Whether to enable use of this backend. Permitted values are 'Enabled' or 'Disabled'
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class DynamicCompressionEnabled(str, Enum):
    """
    Whether to use dynamic compression for cached content
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class EnforceCertificateNameCheckEnabledState(str, Enum):
    """
    Whether to enforce certificate name check on HTTPS requests to all backend pools. No effect on non-HTTPS requests.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class FrontDoorEnabledState(str, Enum):
    """
    Operational status of the Front Door load balancer. Permitted values are 'Enabled' or 'Disabled'
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class FrontDoorForwardingProtocol(str, Enum):
    """
    Protocol this rule will use when forwarding traffic to backends.
    """
    HTTP_ONLY = "HttpOnly"
    HTTPS_ONLY = "HttpsOnly"
    MATCH_REQUEST = "MatchRequest"


class FrontDoorHealthProbeMethod(str, Enum):
    """
    Configures which HTTP method to use to probe the backends defined under backendPools.
    """
    GET = "GET"
    HEAD = "HEAD"


class FrontDoorProtocol(str, Enum):
    """
    Accepted protocol schemes.
    """
    HTTP = "Http"
    HTTPS = "Https"


class FrontDoorQuery(str, Enum):
    """
    Treatment of URL query terms when forming the cache key.
    """
    STRIP_NONE = "StripNone"
    STRIP_ALL = "StripAll"
    STRIP_ONLY = "StripOnly"
    STRIP_ALL_EXCEPT = "StripAllExcept"


class FrontDoorRedirectProtocol(str, Enum):
    """
    The protocol of the destination to where the traffic is redirected
    """
    HTTP_ONLY = "HttpOnly"
    HTTPS_ONLY = "HttpsOnly"
    MATCH_REQUEST = "MatchRequest"


class FrontDoorRedirectType(str, Enum):
    """
    The redirect type the rule will use when redirecting traffic.
    """
    MOVED = "Moved"
    FOUND = "Found"
    TEMPORARY_REDIRECT = "TemporaryRedirect"
    PERMANENT_REDIRECT = "PermanentRedirect"


class HeaderActionType(str, Enum):
    """
    Which type of manipulation to apply to the header.
    """
    APPEND = "Append"
    DELETE = "Delete"
    OVERWRITE = "Overwrite"


class HealthProbeEnabled(str, Enum):
    """
    Whether to enable health probes to be made against backends defined under backendPools. Health probes can only be disabled if there is a single enabled backend in single enabled backend pool.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class MatchProcessingBehavior(str, Enum):
    """
    If this rule is a match should the rules engine continue running the remaining rules or stop. If not present, defaults to Continue.
    """
    CONTINUE_ = "Continue"
    STOP = "Stop"


class RoutingRuleEnabledState(str, Enum):
    """
    Whether to enable use of this rule. Permitted values are 'Enabled' or 'Disabled'
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class RulesEngineMatchVariable(str, Enum):
    """
    Match Variable
    """
    IS_MOBILE = "IsMobile"
    REMOTE_ADDR = "RemoteAddr"
    REQUEST_METHOD = "RequestMethod"
    QUERY_STRING = "QueryString"
    POST_ARGS = "PostArgs"
    REQUEST_URI = "RequestUri"
    REQUEST_PATH = "RequestPath"
    REQUEST_FILENAME = "RequestFilename"
    REQUEST_FILENAME_EXTENSION = "RequestFilenameExtension"
    REQUEST_HEADER = "RequestHeader"
    REQUEST_BODY = "RequestBody"
    REQUEST_SCHEME = "RequestScheme"


class RulesEngineOperator(str, Enum):
    """
    Describes operator to apply to the match condition.
    """
    ANY = "Any"
    IP_MATCH = "IPMatch"
    GEO_MATCH = "GeoMatch"
    EQUAL = "Equal"
    CONTAINS = "Contains"
    LESS_THAN = "LessThan"
    GREATER_THAN = "GreaterThan"
    LESS_THAN_OR_EQUAL = "LessThanOrEqual"
    GREATER_THAN_OR_EQUAL = "GreaterThanOrEqual"
    BEGINS_WITH = "BeginsWith"
    ENDS_WITH = "EndsWith"


class SessionAffinityEnabledState(str, Enum):
    """
    Whether to allow session affinity on this host. Valid options are 'Enabled' or 'Disabled'
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class Transform(str, Enum):
    """
    Describes what transforms are applied before matching
    """
    LOWERCASE = "Lowercase"
    UPPERCASE = "Uppercase"
    TRIM = "Trim"
    URL_DECODE = "UrlDecode"
    URL_ENCODE = "UrlEncode"
    REMOVE_NULLS = "RemoveNulls"
