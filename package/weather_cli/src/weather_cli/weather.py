import requests


API_URL = "https://wttr.in/{}?format=%C+%t"

def get_weather(city: str) -> str:
    """Feather weather data for a given city.
    """

    response = requests.get(API_URL.format(city))
    if response.status_code == 200:
        return response.text.strip()
    else:
        return "Error featching weather data"
    
