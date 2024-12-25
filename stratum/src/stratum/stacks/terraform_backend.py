"""
Module terraform_backend

This module defines the TerraformBackendStack class, which initializes the Terraform stack
with a local backend and an Azure provider, and creates a TerraformBackendL2 construct.

Classes:
    TerraformBackendStack: A Terraform stack that sets up the local backend, Azure provider,
                           and TerraformBackendL2 construct.
"""

from cdktf import LocalBackend, TerraformStack
from cdktf_cdktf_provider_azurerm.provider import AzurermProvider
from constructs import Construct

from stratum.constants import AzureLocation
from stratum.constructs.level2.terraform_backend import TerraformBackendL2


class TerraformBackendStack(TerraformStack):
    """
    A Terraform stack that sets up the local backend, Azure provider, and TerraformBackendL2 construct.

    Attributes:
        azure_provider (AzurermProvider): The Azure provider for Terraform.
        resource_group (TerraformBackendL2): The TerraformBackendL2 construct.
    """

    def __init__(self, scope: Construct, id_: str) -> None:
        """
        Initializes the TerraformBackendStack.

        Args:
            scope (Construct): The scope in which this construct is defined.
            id (str): The scoped construct ID.
        """
        super().__init__(scope, id_)

        LocalBackend(
            self,
            path="init.tfstate",
        )

        self._azure_provider = AzurermProvider(
            self,
            "AzureResourceManagerProvider",
            storage_use_azuread=True,
            features=[{}],
        )

        self.resource_group = TerraformBackendL2(
            self,
            id_,
            resource_group_name="init",
            storage_account_name="init",
            env="prod",
            location=AzureLocation.GERMANY_WEST_CENTRAL,
            sequence_number="01",
        )
