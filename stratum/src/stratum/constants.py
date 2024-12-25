"""
Module constants

This module defines constants for Azure locations and resources using Enums.

Classes:
    AzureLocation: Enum representing Azure locations with their full names and abbreviations.
    AzureResource: Enum representing Azure resources with their full names and abbreviations.
"""

from enum import Enum


class AzureLocation(Enum):
    """
    Enum representing Azure locations with their full names and abbreviations.
    """

    GERMANY_WEST_CENTRAL = "germany west central", "gwc"

    def __init__(self, full_name: str, abbreviation: str) -> None:
        """
        Initialize the AzureLocation enum.

        Args:
            full_name (str): The full name of the Azure location.
            abbreviation (str): The abbreviation of the Azure location.
        """
        self._full_name = full_name
        self._abbreviation = abbreviation

    @property
    def full_name(self) -> str:
        """
        Get the full name of the Azure location.

        Returns:
            str: The full name of the Azure location.
        """
        return self._full_name

    @property
    def abbreviation(self) -> str:
        """
        Get the abbreviation of the Azure location.

        Returns:
            str: The abbreviation of the Azure location.
        """
        return self._abbreviation


class AzureResource(Enum):
    """
    Enum representing Azure resources with their full names and abbreviations.
    """

    RESOURCE_GROUP = "resource_group", "rg"
    STORAGE_ACCOUNT = "storage_account", "st"
    MANAGEMENT_LOCK = "management_lock", "lock"

    def __init__(self, full_name: str, abbreviation: str) -> None:
        """
        Initialize the AzureResource enum.

        Args:
            full_name (str): The full name of the Azure resource.
            abbreviation (str): The abbreviation of the Azure resource.
        """
        self._full_name = full_name
        self._abbreviation = abbreviation

    @property
    def full_name(self) -> str:
        """
        Get the full name of the Azure resource.

        Returns:
            str: The full name of the Azure resource.
        """
        return self._full_name

    @property
    def abbreviation(self) -> str:
        """
        Get the abbreviation of the Azure resource.

        Returns:
            str: The abbreviation of the Azure resource.
        """
        return self._abbreviation
