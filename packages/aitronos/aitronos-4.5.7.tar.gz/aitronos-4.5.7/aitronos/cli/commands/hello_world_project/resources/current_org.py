import json
from pathlib import Path
from typing import Optional, List
from dataclasses import dataclass
from datetime import datetime
import logging

# Set up logging
logger = logging.getLogger(__name__)

@dataclass
class Address:
    """Organization address information."""
    street: Optional[str] = None
    post_code: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    phone_number: Optional[str] = None

    @staticmethod
    def from_json(data: dict) -> "Address":
        """Convert JSON data to Address instance."""
        address = Address()
        fields = {
            "street": "street",
            "post_code": "postCode",
            "city": "city",
            "country": "country",
            "phone_number": "phoneNumber"
        }
        
        for attr, json_key in fields.items():
            if json_key not in data or data[json_key] is None:
                logger.warning(f"Missing or null address field: {json_key}")
            setattr(address, attr, data.get(json_key))
            
        return address


@dataclass
class Organization:
    """Organization data structure."""
    id: Optional[str] = None
    name: Optional[str] = None
    logo: Optional[str] = None
    address: Optional[Address] = None
    members: List[str] = None
    created_at: Optional[datetime] = None
    assistants: List[str] = None
    default_assistant: Optional[str] = None

    def __post_init__(self):
        # Initialize empty lists if None
        if self.members is None:
            self.members = []
        if self.assistants is None:
            self.assistants = []

    @staticmethod
    def from_json(data: dict) -> "Organization":
        """Convert JSON data to Organization instance."""
        org = Organization()
        
        # Basic fields
        fields = {
            "id": "id",
            "name": "name",
            "logo": "logo",
            "default_assistant": "defaultAssistant"
        }
        
        for attr, json_key in fields.items():
            if json_key not in data or data[json_key] is None:
                logger.warning(f"Missing or null organization field: {json_key}")
            setattr(org, attr, data.get(json_key))

        # Address
        if "address" in data and data["address"]:
            org.address = Address.from_json(data["address"])
        else:
            logger.warning("Missing or null address data")
            org.address = Address()

        # Lists
        org.members = data.get("members", [])
        org.assistants = data.get("assistants", [])
        if not org.members:
            logger.warning("No members found in organization data")
        if not org.assistants:
            logger.warning("No assistants found in organization data")

        # Date handling
        try:
            if "createdAt" in data and data["createdAt"]:
                org.created_at = datetime.strptime(data["createdAt"], "%m/%d/%Y %H:%M:%S")
            else:
                logger.warning("Missing creation date")
        except ValueError as e:
            logger.error(f"Failed to parse creation date: {e}")
            org.created_at = None

        return org


class CurrentOrg:
    """
    A singleton-like class for managing the current organization's data.
    Loads organization data from a JSON file and provides access to the organization's profile.
    """

    _instance = None
    _org_data: Optional[Organization] = None

    def __new__(cls):
        """Ensures only one instance of CurrentOrg is created."""
        if cls._instance is None:
            cls._instance = super(CurrentOrg, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        """Loads organization data from a JSON file."""
        # Resolve the JSON file path relative to this file's location
        json_file = Path(__file__).parent / "org_data.json"

        if not json_file.exists():
            raise FileNotFoundError(f"JSON file not found at path: {json_file}")

        try:
            with open(json_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                self._org_data = Organization.from_json(data)
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse JSON file: {e}")
        except Exception as e:
            raise RuntimeError(f"An error occurred while loading organization data: {e}")

    @property
    def org(self) -> Organization:
        """
        Returns the current organization's data.

        :return: An instance of the Organization class populated with data from the JSON file.
        :raises RuntimeError: If organization data has not been initialized.
        """
        if self._org_data is None:
            raise RuntimeError("Organization data has not been initialized.")
        return self._org_data

    def reload(self):
        """Reloads the organization data from the JSON file."""
        self._initialize()


# Example Usage
# if __name__ == "__main__":
#     try:
#         current_org = CurrentOrg()  # Automatically loads org_data.json
#         org_data = current_org.org  # Access the Organization instance
#         print(f"Organization: {org_data.name}")
#         print(f"Members: {len(org_data.members)}")
#         print(f"Assistants: {len(org_data.assistants)}")
#         print(f"Default Assistant: {org_data.default_assistant}")
#     except Exception as e:
#         print(f"An error occurred: {e}") 