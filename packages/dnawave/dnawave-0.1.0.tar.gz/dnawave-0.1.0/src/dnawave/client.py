import requests
from typing import Optional, Dict, Any
from dnawave.auth import Auth
from dnawave.exceptions import DNAWaveError, AuthenticationError
from dnawave.utils import build_url

class DNAWaveClient:
    def __init__(self, api_key: str, base_url: str = "https://platform.dnawave.ca/api/"):
        self.base_url = base_url
        self.auth = Auth(api_key)

    def _request(self, method: str, path: str, params: Optional[Dict] = None, data: Optional[Dict] = None) -> Dict:
        url = build_url(self.base_url, path, params)
        
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self.auth.get_headers(),
                json=data if data else None
            )
            
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                raise AuthenticationError("Invalid API key")
            raise DNAWaveError(f"HTTP {e.response.status_code}: {e.response.text}")
        except requests.exceptions.RequestException as e:
            raise DNAWaveError(f"Request failed: {str(e)}")

    def get(self, path: str, params: Optional[Dict] = None) -> Dict:
        return self._request("GET", path, params=params)

    def post(self, path: str, data: Dict) -> Dict:
        return self._request("POST", path, data=data)

    def put(self, path: str, data: Dict) -> Dict:
        return self._request("PUT", path, data=data)

    def delete(self, path: str, params: Optional[Dict] = None) -> Dict:
        return self._request("DELETE", path, params=params)