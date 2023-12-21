try:
    user_input = int(input("Enter your age: "))
    if user_input < 0:
        raise Exception("Age can't be a negative number!")
    print(f"Your age is even.") if user_input % 2 == 0 \
                                else print(f"Your age is odd.")
except ValueError as e:
    print(f"Error! {e}")