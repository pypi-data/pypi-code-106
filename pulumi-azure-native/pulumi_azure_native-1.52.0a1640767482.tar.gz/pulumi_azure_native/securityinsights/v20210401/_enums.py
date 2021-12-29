# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'IncidentClassification',
    'IncidentClassificationReason',
    'IncidentSeverity',
    'IncidentStatus',
    'Source',
    'ThreatIntelligenceResourceInnerKind',
]


class IncidentClassification(str, Enum):
    """
    The reason the incident was closed
    """
    UNDETERMINED = "Undetermined"
    """
    Incident classification was undetermined
    """
    TRUE_POSITIVE = "TruePositive"
    """
    Incident was true positive
    """
    BENIGN_POSITIVE = "BenignPositive"
    """
    Incident was benign positive
    """
    FALSE_POSITIVE = "FalsePositive"
    """
    Incident was false positive
    """


class IncidentClassificationReason(str, Enum):
    """
    The classification reason the incident was closed with
    """
    SUSPICIOUS_ACTIVITY = "SuspiciousActivity"
    """
    Classification reason was suspicious activity
    """
    SUSPICIOUS_BUT_EXPECTED = "SuspiciousButExpected"
    """
    Classification reason was suspicious but expected
    """
    INCORRECT_ALERT_LOGIC = "IncorrectAlertLogic"
    """
    Classification reason was incorrect alert logic
    """
    INACCURATE_DATA = "InaccurateData"
    """
    Classification reason was inaccurate data
    """


class IncidentSeverity(str, Enum):
    """
    The severity of the incident
    """
    HIGH = "High"
    """
    High severity
    """
    MEDIUM = "Medium"
    """
    Medium severity
    """
    LOW = "Low"
    """
    Low severity
    """
    INFORMATIONAL = "Informational"
    """
    Informational severity
    """


class IncidentStatus(str, Enum):
    """
    The status of the incident
    """
    NEW = "New"
    """
    An active incident which isn't being handled currently
    """
    ACTIVE = "Active"
    """
    An active incident which is being handled
    """
    CLOSED = "Closed"
    """
    A non-active incident
    """


class Source(str, Enum):
    """
    The source of the watchlist
    """
    LOCAL_FILE = "Local file"
    REMOTE_STORAGE = "Remote storage"


class ThreatIntelligenceResourceInnerKind(str, Enum):
    """
    The kind of the entity.
    """
    INDICATOR = "indicator"
    """
    Entity represents threat intelligence indicator in the system.
    """
