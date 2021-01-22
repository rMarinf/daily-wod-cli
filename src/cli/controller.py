from datetime import date, datetime

from src.crawler import WODCrawler


class CLIController:

    def __init__(self):
        self.crawler = WODCrawler()

    def get(self, day):
        try:
            day = date.today() if day is None else datetime.strptime(day, '%Y/%m/%d')
            day_str = day.strftime("%y%m%d")
        except ValueError:
            return 'Invalid date format'

        return self.crawler.get_wod(day_str)

