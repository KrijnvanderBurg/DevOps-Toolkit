from cdktf import LocalBackend, TerraformStack
from cdktf_cdktf_provider_azurerm.provider import AzurermProvider
from constructs import Construct

from stratum.constants import AzureLocation
from stratum.constructs.level2.terraform_backend import TerraformBackendL2


class TerraformBackendStack(TerraformStack):
    def __init__(
            self, scope: Construct, id: str
    ) -> None:
        super().__init__(scope, id)

        LocalBackend(
            self,
            path="init.tfstate"
        )

        self._azure_provider = AzurermProvider(
            self, "AzureResourceManagerProvider",
            storage_use_azuread=True,
            features=[{}],
        )

        self.resource_group = TerraformBackendL2(
            self, id,
            resource_group_name="init",
            storage_account_name="init",
            env="prod",
            location=AzureLocation.GERMANY_WEST_CENTRAL,
            sequence_number="01"
        )
