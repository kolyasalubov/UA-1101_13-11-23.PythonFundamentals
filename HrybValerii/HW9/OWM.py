from pyowm import OWM
from pyowm.commons.exceptions import NotFoundError

API_KEY = 'ef2206ff5da67de63306d0b143e20872'


owm = OWM(API_KEY)
mgr = owm.weather_manager()


def weather_info(input_city):
    try:
        observation = mgr.weather_at_place(input_city)
    except NotFoundError:
        return f"Sorry, we couldn't find weather information for '{input_city}'. " \
                        f"Please check the city name and try again."
    w = observation.weather
    speed_wind = w.wind()
    humidity = w.humidity
    temperature = w.temperature('celsius')

    return (f'''In {input_city} the weather status is {w.detailed_status}.
The wind speed is {speed_wind['speed']} km/hour.
Air humidity is {humidity}.
Temperature is {temperature['temp']}.
The maximal recorded temperature is {temperature['temp_max']}.
The minimal temperature of the air is {temperature['temp_min']}.
{f'In the last 3h {w.rain["3h"]} mms of rain have fallen.' 
    if w.rain.get('3h') else 'No data about the rain'}
Cloud index is {w.clouds}''')








