from src.config.settings import settings
from src.data_sources.alpha_vantage import AlphaVantageFetcher
from src.data_sources.cryptoquant import CryptoQuantFetcher
from src.data_sources.birdeye import BirdeyeFetcher
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    # Initialize fetchers
    alpha_vantage_fetcher = AlphaVantageFetcher(settings.ALPHA_VANTAGE_API_KEY)
    crypto_quant_fetcher = CryptoQuantFetcher(settings.CRYPTOQUANT_API_KEY)
    birdeye_fetcher = BirdeyeFetcher(settings.BIRDEYE_API_KEY)

    # Fetch data
    alpha_vantage_data = alpha_vantage_fetcher.fetch_data("TIME_SERIES_INTRADAY", {"symbol": "IBM", "interval": "5min"})
    logger.info("Alpha Vantage Data: %s", json.dumps(alpha_vantage_data, indent=2))

    crypto_quant_data = crypto_quant_fetcher.fetch_data("market/exchange-flows", {"market": "binance"})
    logger.info("CryptoQuant Data: %s", json.dumps(crypto_quant_data, indent=2))

    birdeye_data = birdeye_fetcher.fetch_data("defi/overview")
    logger.info("Birdeye Data: %s", json.dumps(birdeye_data, indent=2))