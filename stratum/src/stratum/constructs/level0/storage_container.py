"""
Module storage_container

This module defines the StorageContainerL0 class, which is responsible for creating
and managing an Azure storage container with specific configurations.

Classes:
    StorageContainerL0: A level 0 construct that creates and manages an Azure storage container.
"""

from cdktf_cdktf_provider_azurerm.storage_container import StorageContainer
from constructs import Construct

from stratum.constructs.level0.storage_account import StorageAccountL0


class StorageContainerL0(Construct):
    """
    A level 0 construct that creates and manages an Azure storage container.

    Attributes:
        storage_container (StorageContainer): The Azure storage container.
    """

    def __init__(
        self, scope: Construct, id: str, *, name: str, storage_account_l0: StorageAccountL0, container_access_type: str
    ) -> None:
        """
        Initializes the StorageContainerL0 construct.

        Args:
            scope (Construct): The scope in which this construct is defined.
            id (str): The scoped construct ID.
            name (str): The name of the storage container.
            storage_account_l0 (StorageAccountL0): The storage account level 0 construct.
            container_access_type (str): The access type of the storage container.
        """
        super().__init__(scope, id)
        self._storage_container = StorageContainer(
            self,
            f"{storage_account_l0.storage_account.id}_{name}",
            name=name,
            storage_account_id=storage_account_l0.storage_account.id,
            container_access_type=container_access_type,
        )

    @property
    def storage_container(self) -> StorageContainer:
        """Gets the Azure storage container."""
        return self._storage_container
