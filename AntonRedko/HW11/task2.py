import datetime


class DayOfWeek:
    def __init__(self):
        self.number = 0

    def get_number(self):
        self.number = input("Enter a number: ")
        if not self.number.isdigit():
            raise ValueError("Input must be a positive integer")
        self.number = int(self.number)
        if self.number < 1:
            raise ValueError("Number must be greater than 0")

    def check_day(self):
        days = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
        if self.number <= 7:
            print(f"{self.number} corresponds to {days[self.number-1]}")
        else:
            day = datetime.datetime(2023, 12, self.number-7).strftime("%A")
            print(f"{self.number} corresponds to {day}")


day_of_week = DayOfWeek()
try:
    day_of_week.get_number()
    day_of_week.check_day()
except ValueError as e:
    print(e)
