from tkinter import Tk, Label, Entry, Button, StringVar
from random import randint


class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")

        self.start_number = 1
        self.end_number = 100
        self.tries = 10
        self.random_number = randint(self.start_number, self.end_number)

        self.tries_left = StringVar()
        self.tries_left.set(f"You have {self.tries} tries")

        Label(master, textvariable=self.tries_left).pack()

        self.user_input_entry = Entry(master)
        self.user_input_entry.pack()

        Button(master, text="Submit", command=self.check_guess).pack()

    def check_guess(self):
        user_input = int(self.user_input_entry.get())
        self.tries -= 1

        if user_input == self.random_number:
            result_text = "Congratulations, you won!"
        elif user_input < self.random_number:
            result_text = "The incorrectly guessed number is greater"
        else:
            result_text = "The incorrectly guessed number is less"

        self.tries_left.set(f"{result_text} - You have {self.tries} tries left")

        if self.tries == 0 or user_input == self.random_number:
            self.user_input_entry.config(state='disabled')


if __name__ == "__main__":
    root = Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
