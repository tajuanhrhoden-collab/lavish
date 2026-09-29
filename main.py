import time

import schedule

from config import CHECK_INTERVAL_HOURS, REQUIRED_ENV_VARS, SYMBOLS, TELEGRAM_TOKEN, TELEGRAM_CHAT_ID
from market_data import fetch_history
from signals import calculate_sma, detect_signal, get_signal_message
from telegram_bot import send_telegram_alert


def validate_config():
    missing = [name for name in REQUIRED_ENV_VARS if not globals().get(name)]
    if missing:
        raise ValueError(
            "Missing required environment variables: " + ", ".join(missing)
        )


def run_signal_check():
    for symbol in SYMBOLS:
        try:
            closes = fetch_history(symbol)
            if not closes or len(closes) < 200:
                continue

            short_sma = calculate_sma(closes, 50)
            long_sma = calculate_sma(closes, 200)
            signal = detect_signal(closes)

            if signal == "HOLD":
                continue

            message = get_signal_message(symbol, signal, short_sma, long_sma)
            send_telegram_alert(message)
            print(f"Sent {symbol}: {message}")
        except Exception as exc:
            print(f"Error checking {symbol}: {exc}")


def main():
    validate_config()
    run_signal_check()
    schedule.every(CHECK_INTERVAL_HOURS).hours.do(run_signal_check)

    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    main()
