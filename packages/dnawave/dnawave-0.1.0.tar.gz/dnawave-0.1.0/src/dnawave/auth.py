class Auth:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_headers(self) -> dict:
        return {
            "Authorization": f"{self.api_key}",
            "Content-Type": "application/json"
        }