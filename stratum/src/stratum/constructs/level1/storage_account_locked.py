"""
Module storage_account_locked

This module defines the StorageAccountLockedL1 class, which is responsible for creating
and managing a locked Azure storage account with specific configurations.

Classes:
    StorageAccountLockedL1: A level 1 construct that creates and manages a locked Azure storage account.
"""

from cdktf_cdktf_provider_azurerm.management_lock import ManagementLock
from cdktf_cdktf_provider_azurerm.storage_account import (
    StorageAccount,
    StorageAccountBlobProperties,
    StorageAccountBlobPropertiesDeleteRetentionPolicy,
)
from constructs import Construct

from stratum.constants import AzureLocation, AzureResource


class StorageAccountLockedL1(Construct):
    """
    A level 1 construct that creates and manages a locked Azure storage account.

    Attributes:
        storage_account (StorageAccount): The Azure storage account.
        management_lock (ManagementLock): The management lock applied to the storage account.
    """

    def __init__(
        self,
        scope: Construct,
        id: str,
        *,
        name: str,
        env: str,
        location: AzureLocation,
        sequence_number: str,
        resource_group_name: str,
        account_replication_type: str = "LRS",
        account_kind: str = "StorageV2",
        account_tier: str = "Standard",
        cross_tenant_replication_enabled: bool = False,
        access_tier: str = "Hot",
        shared_access_key_enabled: bool = False,
        public_network_access_enabled: bool = True,
        is_hns_enabled: bool = False,
        local_user_enabled: bool = False,
        infrastructure_encryption_enabled: bool = True,
        sftp_enabled: bool = False,
        delete_retention_days: int = 7,
    ) -> None:
        """
        Initializes the StorageAccountLockedL1 construct.

        Args:
            scope (Construct): The scope in which this construct is defined.
            id (str): The scoped construct ID.
            name (str): The name of the storage account.
            env (str): The environment name.
            location (AzureLocation): The Azure location.
            sequence_number (str): The sequence number.
            resource_group_name (str): The name of the resource group.
            account_replication_type (str, optional): The replication type of the storage account. Defaults to "LRS".
            account_kind (str, optional): The kind of the storage account. Defaults to "StorageV2".
            account_tier (str, optional): The tier of the storage account. Defaults to "Standard".
            cross_tenant_replication_enabled (bool, optional): Whether cross-tenant replication is enabled. Defaults to False.
            access_tier (str, optional): The access tier of the storage account. Defaults to "Hot".
            shared_access_key_enabled (bool, optional): Whether shared access key is enabled. Defaults to False.
            public_network_access_enabled (bool, optional): Whether public network access is enabled. Defaults to True.
            is_hns_enabled (bool, optional): Whether hierarchical namespace is enabled. Defaults to False.
            local_user_enabled (bool, optional): Whether local user is enabled. Defaults to False.
            infrastructure_encryption_enabled (bool, optional): Whether infrastructure encryption is enabled. Defaults to True.
            sftp_enabled (bool, optional): Whether SFTP is enabled. Defaults to False.
            delete_retention_days (int, optional): The number of days to retain deleted items. Defaults to 7.
        """
        super().__init__(scope, id)

        self._storage_account = StorageAccount(
            self,
            f"{AzureResource.STORAGE_ACCOUNT.abbreviation}_{name}_{env}_{location.abbreviation}_{sequence_number}",
            name=f"{AzureResource.STORAGE_ACCOUNT.abbreviation}{name}{env}{location.abbreviation}{sequence_number}",
            location=location,
            resource_group_name=resource_group_name,
            account_replication_type=account_replication_type,
            account_kind=account_kind,
            account_tier=account_tier,
            cross_tenant_replication_enabled=cross_tenant_replication_enabled,
            access_tier=access_tier,
            shared_access_key_enabled=shared_access_key_enabled,
            public_network_access_enabled=public_network_access_enabled,
            is_hns_enabled=is_hns_enabled,
            local_user_enabled=local_user_enabled,
            infrastructure_encryption_enabled=infrastructure_encryption_enabled,
            sftp_enabled=sftp_enabled,
            blob_properties=StorageAccountBlobProperties(
                delete_retention_policy=StorageAccountBlobPropertiesDeleteRetentionPolicy(
                    days=delete_retention_days,
                )
            ),
        )

        # Add a management lock to the storage account
        self._management_lock = ManagementLock(
            self,
            f"{AzureResource.STORAGE_ACCOUNT.abbreviation}{name}{env}{location.abbreviation}{sequence_number}_{AzureResource.MANAGEMENT_LOCK.abbreviation}",
            name=f"{self.storage_account.name}-{AzureResource.MANAGEMENT_LOCK.abbreviation}",
            scope=self.storage_account.id,
            lock_level="CanNotDelete",
        )

    @property
    def storage_account(self) -> StorageAccount:
        """Gets the Azure storage account."""
        return self._storage_account

    @property
    def management_lock(self) -> ManagementLock:
        """Gets the management lock applied to the storage account."""
        return self._management_lock
