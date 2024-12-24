from constructs import Construct

from stratum.constants import AzureLocation, AzureResource
from stratum.constructs.level0.resource_group import ResourceGroupL0
from stratum.constructs.level1.storage_account_locked import StorageAccountLockedL1


class TerraformBackendL2(Construct):
    def __init__(
        self, scope: Construct, id: str,
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
        delete_retention_days=7
    ) -> None:
        super().__init__(scope, id)

        self._resource_group_l0 = ResourceGroupL0(
            self, f"{AzureResource.RESOURCE_GROUP.abbreviation}_{resource_group_name}_{env}_{location.abbreviation}_{sequence_number}",
            name=resource_group_name,
            env=env,
            location=location,
            sequence_number=sequence_number
        )

        self._storage_account_locked_l1 = StorageAccountLockedL1(
            self, f"{AzureResource.STORAGE_ACCOUNT.abbreviation}_{storage_account_name}_{env}_{location.abbreviation}_{sequence_number}",
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
            delete_retention_days=delete_retention_days
        )

    @property
    def resource_group_l0(self) -> ResourceGroupL0:
        return self._resource_group_l0

    @property
    def storage_account_locked_l1(self) -> StorageAccountLockedL1:
        return self._storage_account_locked_l1
