class BirdeyeFetcher(DataFetcher):
    BASE_URL = "https://api.birdeye.so/v1"

    def fetch_data(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        """Fetch data from Birdeye API."""
        if params is None:
            params = {}
        headers = {"X-API-KEY": self.api_key}
        url = f"{self.BASE_URL}/{endpoint}"
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching data from Birdeye: {e}")
            return None