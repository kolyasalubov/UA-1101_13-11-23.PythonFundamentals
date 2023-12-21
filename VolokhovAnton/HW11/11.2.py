def get_day_of_week(number):
    if number == 1:
        return "Monday"
    elif number == 2:
        return "Tuesday"
    elif number == 3:
        return "Wednesday"
    elif number == 4:
        return "Thursday"
    elif number == 5:
        return "Friday"
    elif number == 6:
        return "Saturday"
    elif number == 7:
        return "Sunday"
    else:
        return None  # Return None for invalid input


try:
    number = int(input("Enter a number (1-7): "))
    day_of_week = get_day_of_week(number)
    if day_of_week:
        print(f"The day of the week is {day_of_week}")
    else:
        print("Invalid input")
except ValueError:
    print("Invalid input")
