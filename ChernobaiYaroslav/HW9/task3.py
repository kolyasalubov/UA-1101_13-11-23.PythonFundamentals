from pyowm import OWM
import tkinter as tk

#Enter your API key here
API_KEY = ''
# ---------- FREE API KEY examples ---------------------

def get_weather():
    try:
        label_error.config(text = "")
        city = entry_field.get()
        owm = OWM(API_KEY)
        mgr = owm.weather_manager()

        # Search for current weather in London (Great Britain) and get details
        observation = mgr.weather_at_place(city)
        w = observation.weather

        # w.detailed_status         # 'clouds'
        # w.wind()                  # {'speed': 4.6, 'deg': 330}
        # w.humidity                # 87
        # w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
        # w.rain                    # {}
        # w.heat_index              # None
        # w.clouds                  # 75

        label.config(text = (f"""City: {city}\nConditions: {w.detailed_status }.\n\
Temperature is {round(w.temperature('celsius')['temp'], 2)} C.
Wind speed is {w.wind()['speed']} km/hours.\nHumidity of the air is {w.humidity}."""))


    except:
        label_error.config(text = "Oops! There was a problem retrieving \
that information.")
        label.config(text = "")


HEIGHT = 350
WIDTH = 450


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

label_error = tk.Label(root, text ="", font=('Courier', 8))
label_error.place(relx = 0.5, rely = 0.03, anchor ="n")

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 8))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                    text="Get Weather", 
                    bg="gray", fg="white", 
                    font=('Courier', 8), 
                    command= get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)


root.mainloop()