
def even_odd_age(age: int) -> str:
    if age < 0:
        raise ValueError("Your entered negative number")
    if age % 2:
        return "Odd"
    return "Even"


def main():
    try:
        user_age = int(input("Enter your age: "))
        result = even_odd_age(age=user_age)

    except ValueError as e:
        print(f"Value Error: {e}")

    except Exception as e:
        print(f"Error: {e}")

    else:
        print(f"Your age {user_age} is {result}")

    finally:
        print("Bye!")


if __name__ == '__main__':
    main()
