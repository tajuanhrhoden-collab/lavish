def calculate_sma(values, window):
    if len(values) < window:
        return None
    return sum(values[-window:]) / window


def detect_signal(closes):
    if len(closes) < 200:
        return "HOLD"

    short_sma = calculate_sma(closes, 50)
    long_sma = calculate_sma(closes, 200)
    previous_short = calculate_sma(closes[:-1], 50)
    previous_long = calculate_sma(closes[:-1], 200)

    if previous_short is None or previous_long is None:
        return "HOLD"

    if short_sma > long_sma and previous_short <= previous_long:
        return "BUY"
    if short_sma < long_sma and previous_short >= previous_long:
        return "SELL"

    return "HOLD"


def get_signal_message(symbol: str, signal: str, short_sma: float, long_sma: float):
    return (
        f"{symbol} - {signal} signal\n"
        f"50-day MA: {short_sma:.2f}\n"
        f"200-day MA: {long_sma:.2f}"
    )
