import urllib.parse
from typing import Optional, Dict, Any

def build_url(base_url: str, path: str, params: Optional[Dict[str, Any]] = None) -> str:
    """Build URL with optional query parameters"""
    url = f"{base_url.rstrip('/')}/{path.lstrip('/')}"
    if params:
        query = urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
        if query:
            url = f"{url}?{query}"
    return url