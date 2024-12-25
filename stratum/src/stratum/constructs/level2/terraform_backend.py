"""
Module terraform_backend

This module defines the TerraformBackendL2 class, which is responsible for creating
and managing Azure resource groups and storage accounts with specific configurations
for use as a backend for Terraform state storage.

Classes:
    TerraformBackendL2: A level 2 construct that creates and manages an Azure resource group
                        and a locked storage account for Terraform state storage.
"""

from constructs import Construct

from stratum.constants import AzureLocation, AzureResource
from stratum.constructs.level0.resource_group import ResourceGroupL0
from stratum.constructs.level1.storage_account_locked import StorageAccountLockedL1


class TerraformBackendL2(Construct):
    """
    A level 2 construct that creates and manages an Azure resource group and a locked storage account
    for Terraform state storage.

    Attributes:
        resource_group_l0 (ResourceGroupL0): The resource group level 0 construct.
        storage_account_locked_l1 (StorageAccountLockedL1): The storage account locked level 1 construct.
    """

    def __init__(
        self,
        scope: Construct,
        id: str,
        *,
        resource_group_name: str,
        storage_account_name: str,
        env: str,
        location: AzureLocation,
        sequence_number="01",
        account_replication_type: str = "LRS",
        account_kind: str = "StorageV2",
        account_tier: str = "Standard",
        cross_tenant_replication_enabled: bool = False,
        access_tier: str = "Hot",
        shared_access_key_enabled=False,
        public_network_access_enabled=True,
        is_hns_enabled=False,
        local_user_enabled=False,
        infrastructure_encryption_enabled=True,
        sftp_enabled: bool = False,
        delete_retention_days=7,
    ) -> None:
        """
        Initializes the TerraformBackendL2 construct.

        Args:
            scope (Construct): The scope in which this construct is defined.
            id (str): The scoped construct ID.
            resource_group_name (str): The name of the resource group.
            storage_account_name (str): The name of the storage account.
            env (str): The environment name.
            location (AzureLocation): The Azure location.
            sequence_number (str, optional): The sequence number. Defaults to "01".
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

        self._resource_group_l0 = ResourceGroupL0(
            self,
            f"{AzureResource.RESOURCE_GROUP.abbreviation}_{resource_group_name}_{env}_{location.abbreviation}_{sequence_number}",
            name=resource_group_name,
            env=env,
            location=location,
            sequence_number=sequence_number,
        )

        self._storage_account_locked_l1 = StorageAccountLockedL1(
            self,
            f"{AzureResource.STORAGE_ACCOUNT.abbreviation}_{storage_account_name}_{env}_{location.abbreviation}_{sequence_number}",
            name=storage_account_name,
            env=env,
            location=location,
            sequence_number=sequence_number,
            resource_group_name=self.resource_group_l0.resource_group.name,
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
            delete_retention_days=delete_retention_days,
        )

    @property
    def resource_group_l0(self) -> ResourceGroupL0:
        """Gets the resource group level 0 construct."""
        return self._resource_group_l0

    @property
    def storage_account_locked_l1(self) -> StorageAccountLockedL1:
        """Gets the storage account locked level 1 construct."""
        return self._storage_account_locked_l1
