import json
import re

from click.testing import CliRunner
from datetime import date
from cli import cli


class TestCLI:

    def test_cli_tty(self, requests_mock):
        with open('test/integration/mocks/response.html', 'r') as html_response_file:
            html_response = html_response_file.read()
            runner = CliRunner()
            requests_mock.get('https://www.crossfit.com/210121', text=html_response)
            result = runner.invoke(cli, ['--day', '2021/01/21'])
            assert result.exit_code == 0
            assert '210121' in result.output
            assert 'Rest Day' in result.output

            today_str = date.today().strftime("%y%m%d")
            requests_mock.get('https://www.crossfit.com/{}'.format(today_str), text=html_response)
            result = runner.invoke(cli)
            assert result.exit_code == 0
            assert today_str in result.output
            assert 'Rest Day' in result.output

    def test_cli_telegram(self, requests_mock):
        with open('test/integration/mocks/response.html', 'r') as html_response_file:
            with open('test/integration/mocks/telegram-response.json', 'r') as telegram_file:
                html_response = html_response_file.read()
                telegram_json_data = json.dumps(telegram_file.read())
                runner = CliRunner()
                requests_mock.get('https://www.crossfit.com/210121', text=html_response)
                matcher = re.compile('https://api.telegram.org/bot*')
                requests_mock.get(matcher, json=telegram_json_data)
                result = runner.invoke(cli, ['--day', '2021/01/21', '--show-content', 'telegram'])
                print(result)
                assert result.exit_code == 0
                assert 'Go to @DailyWOD channel to see the WOD =)\n' in result.output

    def test_cli_bad_day(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['--day', '2021-02-22'])
        assert result.exit_code == 0
        assert 'Invalid date format' in result.output
