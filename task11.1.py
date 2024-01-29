def check_even_odd(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    
    if age % 2 == 0:
        return "Even"
    else:
        return "Odd"

try:
    user_age = int(input("Enter your age: "))
    result = check_even_odd(user_age)
    print(f"The entered age is {result}.")
except ValueError as ve:
    print(f"Error: {ve}")

