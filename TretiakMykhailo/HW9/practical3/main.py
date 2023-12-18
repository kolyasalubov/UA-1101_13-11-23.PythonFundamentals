from pyowm import OWM
import tkinter as tk

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
HEIGHT = 350
WIDTH = 450


def weather_response(city_name):
    try:
        own = OWM(API_KEY)
        ngr = own.weather_manager()

        observation = ngr.weather_at_place(str(city_name))
        w = observation.weather

        result = [w.detailed_status,
                  w.humidity, w.temperature("celsius"),
                  w.rain, w.heat_index, w.clouds]

        print(result)
        return result

    except Exception as error:
        return "Sorry, Unknown city"


def get_weather():
    label["text"] = ""
    for i in weather_response(entry_field.get()):
        print(i)
        label['text'] += f"{i}\n"


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14))
label["text"] = "Hello"
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
