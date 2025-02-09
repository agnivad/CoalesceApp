from typing import Optional, Dict, Any
from src.fetchers.base_fetcher import DataFetcher


class CryptoQuantFetcher(DataFetcher):
    BASE_URL = "https://api.cryptoquant.com/v1"

    def fetch_data(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        """Fetch data from CryptoQuant API."""
        if params is None:
            params = {}
        params["api_key"] = self.api_key
        url = f"{self.BASE_URL}/{endpoint}"
        return self._cached_request(url, params)