from src.crawler import WODCrawler


class TestWODCrawler:
    crawler = WODCrawler()

    def test_get_wod(self):
        message = self.crawler.get_wod()
        # TODO: Improve test (I need to mock the request to the page)
        assert message != ""
