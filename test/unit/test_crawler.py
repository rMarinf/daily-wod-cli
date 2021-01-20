import pytest

from unittest.mock import Mock
from datetime import date


from src.crawler import WODCrawler


@pytest.fixture
def mock_response(request):
    """
    since we typically test a bunch of different
    requests calls for a service, we are going to do
    a lot of mock responses, so its usually a good idea
    to have a helper function that builds these things
    """
    status = request.node.get_closest_marker("status", 200)
    content = request.node.get_closest_marker("content", 'CONTENT')
    json_data = request.node.get_closest_marker("json")
    raise_for_status = request.node.get_closest_marker("raise_for_status")

    mock_resp = Mock()
    # mock raise_for_status call w/optional error
    mock_resp.raise_for_status = Mock()
    if raise_for_status:
        mock_resp.raise_for_status.side_effect = raise_for_status
    # set status code and content
    mock_resp.status_code = status
    mock_resp.content = content.args[0] if content is not None else content
    # add json data if provided
    if json_data:
        mock_resp.json = Mock(
            return_value=json_data
        )
    return mock_resp

class TestWODCrawler:
    crawler = WODCrawler()
    test_content = 'foo'

    def test_get_wod(self, mocker):
        mocker.patch(
            'src.crawler.WODCrawler._get_web_content',
            return_value=self.test_content
        )
        mocker.patch(
            'src.crawler.WODCrawler._beautify_content',
            return_value=self.test_content
        )

        formatted_day = date.today().strftime("%y%m%d")
        message = self.crawler.get_wod()
        assert message == "{0}\n\n{1}".format(formatted_day, self.test_content)

    @pytest.mark.content(f"""<div class="_6zX5t4v71r1EQ1b1O0nO2 jYZW249J9cFebTPrzuIl0"><p>{test_content}</p></div>""")
    @pytest.mark.status(200)
    def test_get_web_content(self, mocker, mock_response):
        mocker.patch(
            'requests.get',
            return_value=mock_response
        )
        web_content = self.crawler._get_web_content('210101')

        assert web_content == self.test_content

    def test_beautify_content(self):
        assert self.test_content == self.crawler._beautify_content(self.test_content)

        test_content = 'Beginner option:\n foo'
        assert '\n**********\nBeginner option:\n\n foo' == self.crawler._beautify_content(test_content)
