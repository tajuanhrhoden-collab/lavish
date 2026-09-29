import os

from telegram import Bot

from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID


def send_telegram_alert(message: str):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        raise ValueError("TELEGRAM_TOKEN and TELEGRAM_CHAT_ID must be configured")

    bot = Bot(token=TELEGRAM_TOKEN)
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
