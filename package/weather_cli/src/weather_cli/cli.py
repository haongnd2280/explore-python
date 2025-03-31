# src/weather_cli/cli.py
import click
from weather_cli.weather import get_weather


@click.command()
@click.argument("city")
def weather(city):
    """Get the current weather for a CITY."""
    result = get_weather(city)
    click.echo(result)


if __name__ == "__main__":
    weather()
