DAYS = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday",
        5: "Friday", 6: "Saturday", 7: "Sunday"}


def get_day(num_of_day: int) -> str:
    return DAYS.get(num_of_day, "No day")


def main():
    try:
        user_input = int(input("Enter number from 1 to 7: "))
        if user_input > 8 or user_input <= 0:
            raise ValueError("Number must be from 1 to 7")
        day = get_day(user_input)

    except ValueError as error:
        print(f"Value Error: {error}")

    except Exception as error:
        print(f"Error: {error}")

    else:
        print(f"{user_input}: {day}")

    finally:
        print("Bye!")


if __name__ == '__main__':
    main()
