import pytest

from datetime import date

from src.crawler import WODCrawler


class TestWODCrawler:
    crawler = WODCrawler()

    def test_get_wod(self, mocker):
        test_content = 'foo'
        mocker.patch(
            'src.crawler.WODCrawler._get_web_content',
            return_value=test_content
        )
        mocker.patch(
            'src.crawler.WODCrawler._beautify_content',
            return_value=test_content
        )

        formatted_day = date.today().strftime("%y%m%d")
        message = self.crawler.get_wod()
        assert message == "{0}\n\n{1}".format(formatted_day, test_content)

    def test_beautify_content(self):
        test_content = 'foo'
        assert test_content == self.crawler._beautify_content(test_content)

        test_content = 'Beginner option:\n foo'
        assert '\n**********\nBeginner option:\n\n foo' == self.crawler._beautify_content(test_content)
