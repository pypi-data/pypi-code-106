# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'KnownDataCollectionRuleResourceKind',
    'KnownDataFlowStreams',
    'KnownExtensionDataSourceStreams',
    'KnownPerfCounterDataSourceStreams',
    'KnownSyslogDataSourceFacilityNames',
    'KnownSyslogDataSourceLogLevels',
    'KnownSyslogDataSourceStreams',
    'KnownWindowsEventLogDataSourceStreams',
]


class KnownDataCollectionRuleResourceKind(str, Enum):
    """
    The kind of the resource.
    """
    LINUX = "Linux"
    WINDOWS = "Windows"


class KnownDataFlowStreams(str, Enum):
    MICROSOFT_EVENT = "Microsoft-Event"
    MICROSOFT_INSIGHTS_METRICS = "Microsoft-InsightsMetrics"
    MICROSOFT_PERF = "Microsoft-Perf"
    MICROSOFT_SYSLOG = "Microsoft-Syslog"
    MICROSOFT_WINDOWS_EVENT = "Microsoft-WindowsEvent"


class KnownExtensionDataSourceStreams(str, Enum):
    MICROSOFT_EVENT = "Microsoft-Event"
    MICROSOFT_INSIGHTS_METRICS = "Microsoft-InsightsMetrics"
    MICROSOFT_PERF = "Microsoft-Perf"
    MICROSOFT_SYSLOG = "Microsoft-Syslog"
    MICROSOFT_WINDOWS_EVENT = "Microsoft-WindowsEvent"


class KnownPerfCounterDataSourceStreams(str, Enum):
    MICROSOFT_PERF = "Microsoft-Perf"
    MICROSOFT_INSIGHTS_METRICS = "Microsoft-InsightsMetrics"


class KnownSyslogDataSourceFacilityNames(str, Enum):
    AUTH = "auth"
    AUTHPRIV = "authpriv"
    CRON = "cron"
    DAEMON = "daemon"
    KERN = "kern"
    LPR = "lpr"
    MAIL = "mail"
    MARK = "mark"
    NEWS = "news"
    SYSLOG = "syslog"
    USER = "user"
    UUCP = "uucp"
    LOCAL0 = "local0"
    LOCAL1 = "local1"
    LOCAL2 = "local2"
    LOCAL3 = "local3"
    LOCAL4 = "local4"
    LOCAL5 = "local5"
    LOCAL6 = "local6"
    LOCAL7 = "local7"
    ASTERISK = "*"


class KnownSyslogDataSourceLogLevels(str, Enum):
    DEBUG = "Debug"
    INFO = "Info"
    NOTICE = "Notice"
    WARNING = "Warning"
    ERROR = "Error"
    CRITICAL = "Critical"
    ALERT = "Alert"
    EMERGENCY = "Emergency"
    ASTERISK = "*"


class KnownSyslogDataSourceStreams(str, Enum):
    MICROSOFT_SYSLOG = "Microsoft-Syslog"


class KnownWindowsEventLogDataSourceStreams(str, Enum):
    MICROSOFT_WINDOWS_EVENT = "Microsoft-WindowsEvent"
    MICROSOFT_EVENT = "Microsoft-Event"
