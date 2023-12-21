from pyowm import OWM
from API import KEY


def get_weather(place_inp):
    observation = mgr.weather_at_place(place_inp)
    w = observation.weather
    return f"""
        Weather in {place_inp} right now:\n\
        {w.detailed_status}\n
        Cloudiness: {w.clouds}\n\
        Wind speed: {w.wind()['speed']}\n\
        Wind direction: {w.wind()['deg']} degrees\n\
        Humidity: {w.humidity}\n\
        Temperature: {w.temperature('celsius')['temp']}° C\n\
        Feels like: {w.temperature('celsius')['feels_like']}° C\n\
        Rain: {list(w.rain.keys())[0] if w.rain else '-'} {list(w.rain.values())[0] if w.rain else ''}
        
"""

owm = OWM(KEY)
mgr = owm.weather_manager()