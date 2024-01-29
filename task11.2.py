def get_day_of_week(number):
    days_of_week = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
    
    try:
        day_number = int(number)
        if day_number < 1 or day_number > 7:
            raise ValueError("Invalid day number. Enter a number between 1 and 7.")
        
        return days_of_week[day_number]
    except ValueError as ve:
        return f"Error: {ve}"

try:
    user_input = input("Enter a number (1-7) to get the corresponding day of the week: ")
    result = get_day_of_week(user_input)
    print(result)
except NameError:
    print("Error: 'result' is not defined. Make sure to run the program in a complete script or use a different environment.")
