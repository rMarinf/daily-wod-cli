import click

from src.cli.controller import CLIController

cli_controller = CLIController()


@click.command()
@click.option('--day', '-d', help='Select the day of WOD (format:yyyy/mm/dd)')
@click.option('--show-content', '-sc', help='Show info in tty or telegram channel (default: tty)', default='tty')
def cli(day, show_content):
    """Get the WOD from Crossfit Web"""
    result = cli_controller.get(day, show_content)
    click.echo(result)
