import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Random number")

        self.target_number = random.randint(1, 100)
        self.remaining_attempts = 10

        self.label = tk.Label(self.master, text="Guess the number (1-100):")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.master)
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(self.master, text="Guess", command=self.make_guess)
        self.guess_button.pack(pady=10)

        self.message_label = tk.Label(self.master, text=f"Attempts left: {self.remaining_attempts}")
        self.message_label.pack(pady=10)

    def make_guess(self):
        user_guess = self.entry.get()

        try:
            user_guess = int(user_guess)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
            return

        self.remaining_attempts -= 1
        self.message_label.config(text=f"Attempts left: {self.remaining_attempts}")

        if user_guess == self.target_number:
            messagebox.showinfo("Congratulations!", "You guessed the correct number!")
            self.master.destroy()
        elif self.remaining_attempts == 0:
            messagebox.showinfo("Game Over", f"You ran out of attempts. The correct number was {self.target_number}.")
            self.master.destroy()
        elif user_guess < self.target_number:
            messagebox.showinfo("Incorrect", "Try a higher number.")
        elif user_guess > self.target_number:
            messagebox.showinfo("Incorrect", "Try a lower number.")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()