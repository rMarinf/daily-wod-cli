import pytest

from src.cli.controller import CLIController


class TestCLIController:
    cli_controller = CLIController()
    test_data = [
        ('foo', '2020/09/21', 'foo'),
        ('foo', '2020-09-21', 'Invalid date format'),
    ]

    @pytest.mark.parametrize("mock_response, day, expected", test_data)
    def test_get(self, mock_response, day, expected, mocker):
        mocker.patch(
            'src.crawler.WODCrawler.get_wod',
            return_value=mock_response
        )

        result = self.cli_controller.get(day)

        assert result == expected
