# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'CatalogCollationType',
    'CreateMode',
    'DatabaseLicenseType',
    'DatabaseReadScale',
    'ElasticPoolLicenseType',
    'ReadOnlyEndpointFailoverPolicy',
    'ReadWriteEndpointFailoverPolicy',
    'SampleName',
    'ServerKeyType',
]


class CatalogCollationType(str, Enum):
    """
    Collation of the metadata catalog.
    """
    DATABAS_E_DEFAULT = "DATABASE_DEFAULT"
    SQ_L_LATIN1_GENERAL_CP1_C_I_AS = "SQL_Latin1_General_CP1_CI_AS"


class CreateMode(str, Enum):
    """
    Specifies the mode of database creation.
    
    Default: regular database creation.
    
    Copy: creates a database as a copy of an existing database. sourceDatabaseId must be specified as the resource ID of the source database.
    
    Secondary: creates a database as a secondary replica of an existing database. sourceDatabaseId must be specified as the resource ID of the existing primary database.
    
    PointInTimeRestore: Creates a database by restoring a point in time backup of an existing database. sourceDatabaseId must be specified as the resource ID of the existing database, and restorePointInTime must be specified.
    
    Recovery: Creates a database by restoring a geo-replicated backup. sourceDatabaseId must be specified as the recoverable database resource ID to restore.
    
    Restore: Creates a database by restoring a backup of a deleted database. sourceDatabaseId must be specified. If sourceDatabaseId is the database's original resource ID, then sourceDatabaseDeletionDate must be specified. Otherwise sourceDatabaseId must be the restorable dropped database resource ID and sourceDatabaseDeletionDate is ignored. restorePointInTime may also be specified to restore from an earlier point in time.
    
    RestoreLongTermRetentionBackup: Creates a database by restoring from a long term retention vault. recoveryServicesRecoveryPointResourceId must be specified as the recovery point resource ID.
    
    Copy, Secondary, and RestoreLongTermRetentionBackup are not supported for DataWarehouse edition.
    """
    DEFAULT = "Default"
    COPY = "Copy"
    SECONDARY = "Secondary"
    POINT_IN_TIME_RESTORE = "PointInTimeRestore"
    RESTORE = "Restore"
    RECOVERY = "Recovery"
    RESTORE_EXTERNAL_BACKUP = "RestoreExternalBackup"
    RESTORE_EXTERNAL_BACKUP_SECONDARY = "RestoreExternalBackupSecondary"
    RESTORE_LONG_TERM_RETENTION_BACKUP = "RestoreLongTermRetentionBackup"
    ONLINE_SECONDARY = "OnlineSecondary"


class DatabaseLicenseType(str, Enum):
    """
    The license type to apply for this database. `LicenseIncluded` if you need a license, or `BasePrice` if you have a license and are eligible for the Azure Hybrid Benefit.
    """
    LICENSE_INCLUDED = "LicenseIncluded"
    BASE_PRICE = "BasePrice"


class DatabaseReadScale(str, Enum):
    """
    If enabled, connections that have application intent set to readonly in their connection string may be routed to a readonly secondary replica. This property is only settable for Premium and Business Critical databases.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ElasticPoolLicenseType(str, Enum):
    """
    The license type to apply for this elastic pool.
    """
    LICENSE_INCLUDED = "LicenseIncluded"
    BASE_PRICE = "BasePrice"


class ReadOnlyEndpointFailoverPolicy(str, Enum):
    """
    Failover policy of the read-only endpoint for the failover group.
    """
    DISABLED = "Disabled"
    ENABLED = "Enabled"


class ReadWriteEndpointFailoverPolicy(str, Enum):
    """
    Failover policy of the read-write endpoint for the failover group. If failoverPolicy is Automatic then failoverWithDataLossGracePeriodMinutes is required.
    """
    MANUAL = "Manual"
    AUTOMATIC = "Automatic"


class SampleName(str, Enum):
    """
    The name of the sample schema to apply when creating this database.
    """
    ADVENTURE_WORKS_LT = "AdventureWorksLT"
    WIDE_WORLD_IMPORTERS_STD = "WideWorldImportersStd"
    WIDE_WORLD_IMPORTERS_FULL = "WideWorldImportersFull"


class ServerKeyType(str, Enum):
    """
    The key type like 'ServiceManaged', 'AzureKeyVault'.
    """
    SERVICE_MANAGED = "ServiceManaged"
    AZURE_KEY_VAULT = "AzureKeyVault"
