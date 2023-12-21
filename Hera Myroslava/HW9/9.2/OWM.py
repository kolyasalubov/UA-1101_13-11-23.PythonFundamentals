from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather(city):
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather
        weather_info = f"Status: {w.detailed_status}\nWind: {w.wind()}\nHumidity: {w.humidity}%\nTemperature: {w.temperature('celsius')['temp']}°C\nClouds: {w.clouds}%"
        return weather_info
    except:
        return "Error: City not found"