import tkinter as tk
from OWM import get_weather

HEIGHT = 350
WIDTH = 450


def print_weather():
    try:
        message_weather = get_weather(entry_field.get())
    except:
        message_weather = 'Something went wrong...'

    output_field.configure(state='normal')
    output_field.delete(0.0, tk.END)
    output_field.insert(0.0, message_weather)
    output_field.configure(state='disabled')


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
                   command=lambda: print_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

output_field = tk.Text(lower_frame, font=('Courier', 9), state='disabled')
output_field.place(relx=0, rely=0, relheight=1, relwidth=1)


label = tk.Label(frame, font=('Courier', 14))
label.place(relheight=1, relwidth=0)



root.mainloop()

