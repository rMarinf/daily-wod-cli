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

        # TODO: Better error handling
        if show_content == 'telegram':
            telegram_bot = TelegramBot()
            telegram_bot.send_wod(message)
            return 'Go to @DailyWOD channel to see the WOD =)'

        return message

