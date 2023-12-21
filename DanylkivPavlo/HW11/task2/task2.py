def get_weekday(num_str):
    number_of_day = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
    try:
        number = int(num_str)
        if number < 1 or number > 7:
            raise ValueError("Input should be only numbers from 1 to 7 included.")
        return number_of_day[number]

    except ValueError as ve:
        return f"Error! {ve}"


your_number = input("Enter the number: ")
print(get_weekday(your_number))