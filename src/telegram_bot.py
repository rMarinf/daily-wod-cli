import telegram

from src.constants import TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID


class TelegramBot:

    def __init__(self):
        self.bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

    def send_wod(self, message):
        # TODO: Better error handling
        return self.bot.send_message(chat_id=TELEGRAM_CHANNEL_ID, text=message)
