class AlphaVantageFetcher(DataFetcher):
    BASE_URL = "https://www.alphavantage.co/query"

    def fetch_data(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        """Fetch data from Alpha Vantage API."""
        if params is None:
            params = {}
        params["apikey"] = self.api_key
        url = f"{self.BASE_URL}?function={endpoint}"
        return self._cached_request(url, params)