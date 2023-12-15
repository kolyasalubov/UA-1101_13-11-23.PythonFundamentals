# OWM.py

from pyowm import OWM

def get_weather_forecast():
    owm = OWM("your-api-key")
    observation = owm.weather_at_place("Kyiv")
    weather = observation.get_weather()
    return weather

# Tk_OWM.py

import tkinter as tk

def show_weather_forecast():
    weather = get_weather_forecast()
    label = tk.Label(text=weather)
    label.pack()

root = tk.Tk()
button = tk.Button(text="Show Weather Forecast", command=show_weather_forecast)
button.pack()

root.mainloop()
