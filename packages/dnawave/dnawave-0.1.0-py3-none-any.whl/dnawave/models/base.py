from typing import Optional, Dict, Any, ClassVar, List
from dnawave.client import DNAWaveClient

class BaseModel:
    _client: Optional[DNAWaveClient] = None
    _endpoint: ClassVar[str] = ""
    _list_key: ClassVar[str] = ""  # Add this to handle nested responses

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self._data = kwargs

    @classmethod
    def set_client(cls, client: DNAWaveClient):
        cls._client = client

    @classmethod
    def list(cls, **params) -> list:
        if not cls._client:
            raise DNAWaveError("Client not initialized")
        response = cls._client.get(cls._endpoint, params=params)
        
        # Handle nested response structure
        items = response.get(cls._list_key, []) if cls._list_key else response
        return [cls(**item) for item in items]

    @classmethod
    def get(cls, id: str) -> 'BaseModel':
        if not cls._client:
            raise DNAWaveError("Client not initialized")
        response = cls._client.get(f"{cls._endpoint}/{id}")
        return cls(**response)

    def save(self) -> 'BaseModel':
        if not self._client:
            raise DNAWaveError("Client not initialized")
        
        data = {k: v for k, v in self._data.items() if v is not None}
        
        if self.id:
            response = self._client.put(f"{self._endpoint}/{self.id}", data=data)
        else:
            response = self._client.post(self._endpoint, data=data)
        
        self._data.update(response)
        self.id = response.get('id')
        return self

    def delete(self) -> None:
        if not self._client:
            raise DNAWaveError("Client not initialized")
        if not self.id:
            raise DNAWaveError("Cannot delete without ID")
        self._client.delete(f"{self._endpoint}/{self.id}")

    def __getattr__(self, name):
        return self._data.get(name)

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self._data.get('name')})"