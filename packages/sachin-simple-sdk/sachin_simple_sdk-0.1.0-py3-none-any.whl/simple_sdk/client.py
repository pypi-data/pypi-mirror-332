import requests
from .exceptions import APIError

class SimpleSDK:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    def get_data(self, endpoint: str):
        """Fetch data from the given endpoint."""
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)

    def post_data(self, endpoint: str, data: dict):
        """Send a POST request."""
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=data, headers=self.headers)
        return self._handle_response(response)

    def _handle_response(self, response):
        """Handle API response and raise errors if necessary."""
        if response.status_code >= 400:
            raise APIError(response.json().get("error", "Unknown error"), response.status_code)
        return response.json()
