import requests

class OysterTwitterSDK:
    def __init__(self, base_url="http://127.0.0.1:8000"):
        """Initialize the Oyster Twitter SDK with base URL."""
        self.base_url = base_url.rstrip('/')

    def generate_keys_and_tokens(self):
        """
        Generate access tokens and API keys.
        Note: This operation can take 15-20 minutes.
        
        Returns:
            dict: Response from the API
        """
        try:
            response = requests.post(f"{self.base_url}/generate_keys_and_access_tokens")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to generate keys and tokens: {str(e)}")

    def fetch_keys_and_tokens(self):
        """
        Fetch existing access tokens and API keys.
        
        Returns:
            dict: Response containing keys and tokens
        """
        try:
            response = requests.get(f"{self.base_url}/fetch_keys_and_tokens")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch keys and tokens: {str(e)}")

    def verify_encumbrance(self):
        """
        Verify encumbrance status.
        
        Returns:
            dict: Response containing verification results
        """
        try:
            response = requests.get(f"{self.base_url}/verify_encumbrance")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to verify encumbrance: {str(e)}")

# Export OysterTwitterSDK
__all__ = ['OysterTwitterSDK']