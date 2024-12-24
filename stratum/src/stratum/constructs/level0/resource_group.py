from cdktf_cdktf_provider_azurerm.resource_group import ResourceGroup
from constructs import Construct

from stratum.constants import AzureLocation, AzureResource


class ResourceGroupL0(Construct):
    def __init__(
        self, scope: Construct, id: str,
        *,
        name: str,
        env: str,
        location: AzureLocation,
        sequence_number: str
    ) -> None:
        super().__init__(scope, id)
        self._resource_group = ResourceGroup(
            self, f"{AzureResource.RESOURCE_GROUP.abbreviation}_{name}_{env}_{location.abbreviation}_{sequence_number}",
            name=f"{AzureResource.RESOURCE_GROUP.abbreviation}-{name}-{env}-{location.abbreviation}-{sequence_number}",
            location=location.full_name
        )

    @property
    def resource_group(self) -> ResourceGroup:
        return self._resource_group
