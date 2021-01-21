import click

from src.cli_controller import CLIController

cli_controller = CLIController()


@click.command()
@click.option('--day', '-d', help='Select the day of WOD (format:yyyy/mm/dd)')
def cli(day):
    """Get the WOD from Crossfit Web"""
    result = cli_controller.get(day)
    click.echo(result)
