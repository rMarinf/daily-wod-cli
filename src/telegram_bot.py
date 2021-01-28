import telegram

from src.constants import TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID


class TelegramBot:

    def __init__(self):
        self._bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

    def send_wod(self, message):
        try:
            message = self._bot.send_message(chat_id=TELEGRAM_CHANNEL_ID, text=message)
            if message.message_id:
                return 'Go to @DailyWOD channel to see the WOD =)'
        except telegram.error.BadRequest:
            return 'Error when we send the message to Telegram channel'

        return 'An unexpected error occurred :('
