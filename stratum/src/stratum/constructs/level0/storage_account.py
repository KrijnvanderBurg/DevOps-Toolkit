from cdktf_cdktf_provider_azurerm.storage_account import (
    StorageAccount,
    StorageAccountBlobProperties,
    StorageAccountBlobPropertiesDeleteRetentionPolicy,
)
from constructs import Construct

from stratum.constants import AzureLocation, AzureResource
from stratum.constructs.level0.resource_group import ResourceGroupL0


class StorageAccountL0(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        *,
        name: str,
        env: str,
        location: AzureLocation,
        sequence_number: str,
        resource_group_l0: ResourceGroupL0,
        account_replication_type: str,
        account_kind: str, account_tier: str,
        cross_tenant_replication_enabled: bool,
        access_tier: str,
        shared_access_key_enabled: bool,
        public_network_access_enabled: bool,
        is_hns_enabled: bool,
        local_user_enabled: bool,
        infrastructure_encryption_enabled: bool,
        sftp_enabled: bool,
        delete_retention_days: int,
    ) -> None:
        super().__init__(scope, id)
        self._storage_account = StorageAccount(
            self, f"{AzureResource.STORAGE_ACCOUNT.abbreviation}_{name}_{env}_{location.abbreviation}_{sequence_number}",
            name=f"{AzureResource.STORAGE_ACCOUNT.abbreviation}-{name}-{env}-{location.abbreviation}-{sequence_number}",
            location=location.full_name,
            resource_group_name=resource_group_l0.resource_group.name,
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

    @property
    def storage_account(self) -> StorageAccount:
        return self._storage_account
