############## Task1 ###########################

# from random import randint
#
# tries=10
# number_tobe_guessed = randint(0, 100)
# print("Try to guess number in range from 0 to 100")
# while tries:
#     user_guess=int(input(f"Input any number, {tries} tries remained:"))
#     if user_guess==number_tobe_guessed:
#         print(f"Your number is {user_guess} and you GUESSED! Congrats!!!")
#         break
#     elif user_guess>=number_tobe_guessed:
#         tries -= 1
#         print(f"Your number {user_guess} is greater than target!")
#         if tries==0:
#             print ("Sorry, you lost.")
#             break
#
#     elif user_guess<=number_tobe_guessed:
#         tries -= 1
#         print(f"Your number {user_guess} is lesser than target!")
#         if tries==0:
#             print ("Sorry, you lost.")
#             break

############## Task2 ###########################

# import pygame
#
# FPS = 60
#
# WIDTH_DISPLAY = 500
# HEIGHT_DISPLAY = 500
#
# COORD_X = 50
# COORD_Y = 50
# WIDTH_RECTANGLE = 40
# HEIGHT_RECTANGLE = 60
# DELTA_STEP = 5
#
# BLACK_COLOR = (0, 0, 0)
# RED_COLOR = (250, 0, 0)
#
# pygame.init()
#
# gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)
#
# pygame.display.set_caption("My first game")
#
# run = True
# clock = pygame.time.Clock()
#
# while run:
#     pygame.time.delay(100)
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#
#     keys = pygame.key.get_pressed()
#
#     if keys[pygame.K_LEFT] and COORD_X!=0:
#         COORD_X = COORD_X - DELTA_STEP
#     if keys[pygame.K_RIGHT] and COORD_X!=(WIDTH_DISPLAY-WIDTH_RECTANGLE):
#         COORD_X = COORD_X + DELTA_STEP
#     if keys[pygame.K_UP] and COORD_Y!=0:
#         COORD_Y = COORD_Y - DELTA_STEP
#     if keys[pygame.K_DOWN] and COORD_Y!=(HEIGHT_DISPLAY-HEIGHT_RECTANGLE):
#         COORD_Y = COORD_Y + DELTA_STEP
#
#     gameDisplay.fill(BLACK_COLOR)
#
#     pygame.draw.rect(gameDisplay, RED_COLOR, [COORD_X,
#                                               COORD_Y,
#                                               WIDTH_RECTANGLE,
#                                               HEIGHT_RECTANGLE])
#     pygame.display.update()
#     clock.tick(FPS)

############## Task3 ###########################

from pyowm import OWM
import tkinter as tk
from tkinter import font

API_KEY_OWM = 'ef2206ff5da67de63306d0b143e20872'

HEIGHT = 350
WIDTH = 450


# ---------- FREE API KEY examples ---------------------

def get_weather():
    owm = OWM(API_KEY_OWM)
    mgr = owm.weather_manager()

    # Search for current weather in city, user stated in widget and get details
    city = entry_field.get()
    observation = mgr.weather_at_place(city)
    w = observation.weather
    result = f"Weather in {city}:\n\n" \
             f"Clouds:{w.detailed_status}\n" \
             f"Wind:{w.wind()}\n" \
             f"Humidity:{w.humidity}\n" \
             f"Temperature:{w.temperature('celsius')}\n" \
             f"Rain:{w.rain}\n" \
             f"Heat index:{w.heat_index}\n"
    label.config(text=result)


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

label = tk.Label(lower_frame, font=('Courier', 10), justify="left", anchor="w", wraplength=320)
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
