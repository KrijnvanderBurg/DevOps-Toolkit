from cdktf_cdktf_provider_azurerm.storage_container import StorageContainer
from constructs import Construct

from stratum.constructs.level0.storage_account import StorageAccountL0


class StorageContainerL0(Construct):
    def __init__(
        self, scope: Construct, id: str,
        *,
        name: str,
        storage_account_l0: StorageAccountL0,
        container_access_type: str
    ) -> None:
        super().__init__(scope, id)
        self._storage_container = StorageContainer(
            self, f"{storage_account_l0.storage_account.id}_{name}",
            name=name,
            storage_account_id=storage_account_l0.storage_account.id,
            container_access_type=container_access_type
        )

    @property
    def storage_container(self) -> StorageContainer:
        return self._storage_container
