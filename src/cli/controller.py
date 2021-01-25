from datetime import date, datetime

from src.crawler import WODCrawler
from src.telegram_bot import TelegramBot


class CLIController:

    def __init__(self):
        self.crawler = WODCrawler()

    def get(self, day, show_content='tty'):
        try:
            day = date.today() if day is None else datetime.strptime(day, '%Y/%m/%d')
            day_str = day.strftime("%y%m%d")
        except ValueError:
            return 'Invalid date format'

        message = self.crawler.get_wod(day_str)

        if show_content == 'telegram':
            telegram_bot = TelegramBot()
            return telegram_bot.send_wod(message)

        return message

