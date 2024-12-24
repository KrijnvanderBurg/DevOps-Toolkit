from enum import Enum


class AzureLocation(Enum):
    GERMANY_WEST_CENTRAL = "germany west central", "gwc"

    def __init__(self, full_name: str, abbreviation: str):
        self._full_name = full_name
        self._abbreviation = abbreviation

    @property
    def full_name(self):
        return self._full_name

    @property
    def abbreviation(self):
        return self._abbreviation


class AzureResource(Enum):
    RESOURCE_GROUP = "resource_group", "rg"
    STORAGE_ACCOUNT = "storage_account", "st"
    MANAGEMENT_LOCK = "management_lock", "lock"

    def __init__(self, full_name: str, abbreviation: str):
        self._full_name = full_name
        self._abbreviation = abbreviation

    @property
    def full_name(self):
        return self._full_name

    @property
    def abbreviation(self):
        return self._abbreviation
