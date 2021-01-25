import pytest

from src.cli.controller import CLIController


class TestCLIController:
    cli_controller = CLIController()
    test_data = [
        # Show content in tty with a valid date
        ('foo', None, '2020/09/21', 'tty', 'foo'),
        # Show content in tty with a invalid date
        ('foo', None, '2020-09-21', 'tty', 'Invalid date format'),
        # Show content in telegram with a valid date
        ('foo', 'foo', '2020/09/21', 'telegram', 'foo'),
        # Show content in telegram with a valid date
        ('foo', 'foo', '2020-09-21', 'telegram', 'Invalid date format'),
    ]

    @pytest.mark.parametrize("get_wod_mock, send_wod_mock, day, show_content, expected", test_data)
    def test_get(self, get_wod_mock, send_wod_mock, day, show_content, expected, mocker):
        mocker.patch(
            'src.crawler.WODCrawler.get_wod',
            return_value=get_wod_mock
        )

        mocker.patch(
            'src.telegram_bot.TelegramBot.send_wod',
            return_value=send_wod_mock
        )
        result = self.cli_controller.get(day, show_content)

        assert result == expected
