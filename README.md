# COALESCE APP

A Python application to fetch financial data from **Alpha Vantage** (stock data), **CryptoQuant** (crypto analytics), and **Birdeye** (DeFi data). Built with modularity and extensibility in mind.

---

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running the Project](#running-the-project)
- [Server Check](#server-check)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Features

- **Multiple Data Sources**: Fetch data from Alpha Vantage, CryptoQuant, and Birdeye APIs.
- **Error Handling**: Retries with exponential backoff for failed requests.
- **Logging**: Detailed logging for debugging and monitoring.
- **Configuration**: Secure API key management via `.env` file.
- **Modular Design**: Easy to add new data sources.

---

## Prerequisites

- Python 3.8+
- `pip` (Python package manager)
- API keys from:
  - [Alpha Vantage](https://www.alphavantage.co/)
  - [CryptoQuant](https://cryptoquant.com/)
  - [Birdeye](https://birdeye.so/)

---

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/agnivad/CoalesceApp.git
   cd CoalesceApp

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   # For Linux/Mac:
   source venv/bin/activate
   # For Windows:
   venv\Scripts\activate

3. **Install dependencies**:
   pip install -r requirements.txt

4. **Set up API keys**:
    Create a .env file in the root directory:
    ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
    CRYPTOQUANT_API_KEY=your_cryptoquant_api_key
    BIRDEYE_API_KEY=your_birdeye_api_key

5. **Fetch data from all APIs**:
    python src/main.py

6. **Troubleshooting**:
    If you get ModuleNotFoundError, add the src/ directory to PYTHONPATH:
    export PYTHONPATH=$(pwd)/src  # Linux/Mac
    set PYTHONPATH=%cd%\src      # Windows

7. **You can update main.py to fetch different types of data by using various combinations of supported endpoints and parameters, Below are examples:**.
alpha_vantage_params = {"from_currency": "BTC", "to_currency": "USD"}
alpha_vantage_data = alpha_vantage_fetcher.fetch_data(
    endpoint="CURRENCY_EXCHANGE_RATE",
    params=alpha_vantage_params,
)

Future Improvements
Asynchronous Requests: Use asyncio and aiohttp for faster concurrent API calls.
Rate Limiting: Implement rate limiting to respect API usage policies.
Data Validation: Validate API responses with Pydantic or JSON Schema.
Unit Tests: Add comprehensive tests for all fetchers and edge cases.
Docker Support: Containerize the application for deployment.
Monitoring: Add Prometheus/Grafana for API health monitoring.

