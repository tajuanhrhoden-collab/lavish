# Python Telegram Trading Signal Bot

A Python Telegram bot that checks crypto and stock prices hourly and sends buy/sell alerts based on the 50-day and 200-day moving average crossover strategy.

## Features
- Checks BTC, ETH, and AAPL hourly
- Uses Binance API for crypto prices
- Uses Yahoo Finance for stock prices
- Detects Golden Cross / Death Cross signals
- Sends Telegram alerts to a configured chat

## Setup

1. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Copy environment example:
   ```bash
   cp .env.example .env
   ```

4. Update `.env` with your values:
   ```env
   TELEGRAM_TOKEN=your_telegram_bot_token
   TELEGRAM_CHAT_ID=your_telegram_chat_id
   BINANCE_API_KEY=your_binance_api_key
   BINANCE_API_SECRET=your_binance_api_secret
   ```

5. Start the bot:
   ```bash
   python main.py
   ```

## Strategy
- 50-day MA crosses above 200-day MA -> BUY
- 50-day MA crosses below 200-day MA -> SELL
- Otherwise -> HOLD

## Notes
- For Binance, you need the API key and secret even if you only want market data.
- For stocks, Yahoo Finance can be used without an API key.
- The bot checks the configured symbols on a scheduled hourly loop.
