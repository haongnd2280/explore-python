# tests/test_weather.py
from weather_cli.weather import get_weather


def test_get_weather():
    city = "London"
    result = get_weather(city)
    assert isinstance(result, str)
    assert len(result) > 0  # Ensure some data is returned
