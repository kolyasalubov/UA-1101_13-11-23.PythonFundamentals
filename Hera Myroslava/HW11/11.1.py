def user_age(age):
    if age < 0:
        raise ValueError ("Enter the correct number.")
    
    if age % 2 == 0:
        print("Your age is even.")
    else:
        print("Your age is odd.")

def main():
    try:
        age = int(input("Enter your age: "))
        user_age(age)
    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()