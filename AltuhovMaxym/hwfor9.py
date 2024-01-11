from random import randint

number = randint(1, 100)


def randomizer():
    print(f'Guess a number between 1 and 100')

    counter = 1

    while counter < 11:

        guess_number = int(input(f'Attempt № {counter}. Enter your number: '))

        if guess_number == number:
            print(f'Great job!')
            break

        elif guess_number < number:
            print('Your number is less, try again.')
            counter += 1

        elif guess_number > number:
            print('Your number is more, try again.')
            counter += 1

        if counter == 11:
            print("Loser")


randomizer()



from pyowm import OWM
import tkinter as tk

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
HEIGHT = 350
WIDTH = 450


def weather_response(city_name):

    try:
        label.config(text="")
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
        return "City error"


def get_weather():
    label["text"] = ""
    for iterat in weather_response(entry_field.get()):
        print(iterat)
        label['text'] += f"{iterat}\n"


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
label["text"] = "Hello user"
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()

import pygame

FPS = 60

WIDTH_DISPLAY = 500
HEIGHT_DISPLAY = 500

COORD_X = 50
COORD_Y = 50
WIDTH_RECTANGLE = 40
HEIGHT_RECTANGLE = 60
DELTA_STEP = 5

BLACK_COLOR = (0, 0, 0)
RED_COLOR = (250, 0, 0)

pygame.init()

gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)

pygame.display.set_caption("My first game")

run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and COORD_X > 0:
        COORD_X = COORD_X - DELTA_STEP
    if keys[pygame.K_RIGHT] and COORD_X + WIDTH_RECTANGLE < pygame.display.get_window_size()[0]:
        COORD_X = COORD_X + DELTA_STEP
    if keys[pygame.K_UP] and COORD_Y > 0:
        COORD_Y = COORD_Y - DELTA_STEP
    if keys[pygame.K_DOWN] and COORD_Y + HEIGHT_RECTANGLE < pygame.display.get_window_size()[1]:
        COORD_Y = COORD_Y + DELTA_STEP

    gameDisplay.fill(BLACK_COLOR)

    pygame.draw.rect(gameDisplay, RED_COLOR, [COORD_X,
                                              COORD_Y,
                                              WIDTH_RECTANGLE,
                                              HEIGHT_RECTANGLE])
    pygame.display.update()
    clock.tick(FPS)


