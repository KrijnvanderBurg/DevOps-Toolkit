"""
Module resource_group

This module defines the ResourceGroupL0 class, which is responsible for creating
and managing an Azure resource group with specific configurations.

Classes:
    ResourceGroupL0: A level 0 construct that creates and manages an Azure resource group.
"""

from cdktf_cdktf_provider_azurerm.resource_group import ResourceGroup
from constructs import Construct

from stratum.constants import AzureLocation, AzureResource


class ResourceGroupL0(Construct):
    """
    A level 0 construct that creates and manages an Azure resource group.

    Attributes:
        resource_group (ResourceGroup): The Azure resource group.
    """

    def __init__(
        self, scope: Construct, id: str, *, name: str, env: str, location: AzureLocation, sequence_number: str
    ) -> None:
        """
        Initializes the ResourceGroupL0 construct.

        Args:
            scope (Construct): The scope in which this construct is defined.
            id (str): The scoped construct ID.
            name (str): The name of the resource group.
            env (str): The environment name.
            location (AzureLocation): The Azure location.
            sequence_number (str): The sequence number.
        """
        super().__init__(scope, id)
        self._resource_group = ResourceGroup(
            self,
            f"{AzureResource.RESOURCE_GROUP.abbreviation}_{name}_{env}_{location.abbreviation}_{sequence_number}",
            name=f"{AzureResource.RESOURCE_GROUP.abbreviation}-{name}-{env}-{location.abbreviation}-{sequence_number}",
            location=location.name,
        )

    @property
    def resource_group(self) -> ResourceGroup:
        """Gets the Azure resource group."""
        return self._resource_group
