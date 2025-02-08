# CoalesceApp
Financial Data Fetcher
The Financial Data Fetcher is a Python application that fetches financial data from multiple APIs, including Alpha Vantage, CryptoQuant, and Birdeye. It is designed to be modular, extensible, and easy to use.

Features
Multiple Data Sources: Fetch data from Alpha Vantage (stock data), CryptoQuant (crypto analytics), and Birdeye (DeFi data).

Caching: Uses lru_cache to cache API responses and reduce redundant requests.

Error Handling: Implements retries with exponential backoff for failed requests.

Logging: Provides detailed logging for debugging and monitoring.

Configuration Management: Uses environment variables to securely manage API keys.

Modular Design: Easy to add new data sources or extend functionality.
