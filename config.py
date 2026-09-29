import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")
CHECK_INTERVAL_HOURS = int(os.getenv("CHECK_INTERVAL_HOURS", "1"))
RAW_SYMBOLS = os.getenv("SYMBOLS", "BTCUSDT,ETHUSDT,AAPL")
SYMBOLS = [symbol.strip() for symbol in RAW_SYMBOLS.split(",") if symbol.strip()]

REQUIRED_ENV_VARS = [
    "TELEGRAM_TOKEN",
    "TELEGRAM_CHAT_ID",
]
