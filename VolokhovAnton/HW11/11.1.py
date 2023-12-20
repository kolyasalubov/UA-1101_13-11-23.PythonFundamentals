def check_age():
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age % 2 == 0:
        print("Even age")
    else:
        print("Odd age")

try:
    check_age()
except ValueError as e:
    print(e)
