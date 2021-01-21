from click.testing import CliRunner
from cli import cli


class TestCLI:

    def test_cli(self, requests_mock):
        with open('test/integration/mocks/response.html', 'r') as html_response_file:
            html_response = html_response_file.read()
            runner = CliRunner()
            requests_mock.get('https://www.crossfit.com/210121', text=html_response)
            result = runner.invoke(cli)
            assert result.exit_code == 0
            assert '210121' in result.output
            assert 'Rest Day' in result.output
