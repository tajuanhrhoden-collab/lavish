from datetime import datetime

from binance import Client
import yfinance as yf

from config import BINANCE_API_KEY, BINANCE_API_SECRET


def get_binance_client():
    return Client(api_key=BINANCE_API_KEY, api_secret=BINANCE_API_SECRET)


def get_crypto_history(symbol: str, days: int = 300):
    client = get_binance_client()
    klines = client.get_historical_klines(
        symbol=symbol,
        interval="1d",
        start_str=f"{days} day ago UTC",
        limit=300,
    )

    closes = []
    for candle in klines:
        if len(candle) >= 5:
            closes.append(float(candle[4]))

    return closes


def get_stock_history(symbol: str, period: str = "365d", interval: str = "1d"):
    data = yf.download(
        tickers=symbol,
        period=period,
        interval=interval,
        progress=False,
        auto_adjust=True,
    )

    if data.empty:
        raise ValueError(f"No data returned for {symbol}")

    return data["Close"].tolist()


def fetch_history(symbol: str):
    if symbol.endswith("USDT") or symbol.endswith("USD"):
        return get_crypto_history(symbol)
    return get_stock_history(symbol)


def format_market_name(symbol: str):
    return symbol.upper()
