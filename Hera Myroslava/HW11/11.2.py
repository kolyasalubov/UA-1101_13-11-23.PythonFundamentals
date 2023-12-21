def day_of_week(number):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if 1 <= number <= 7:
        return days_of_week[number - 1]
    else:
        return "Invalid input. Please enter a number between 1 and 7."

def main():
    try:
        input_number = int(input("Enter a number (1-7) to get the day of the week: "))
        day = day_of_week(input_number)
        print(f"The day of the week is: {day}")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

if __name__ == "__main__":
    main()