from datetime import datetime

def even_odd_year(age_str):
    try:
        age = int(age_str)
        if age < 0:
            raise ValueError("Age can't be negative")

        current_year = datetime.now().year
        birth_year = current_year - age

        if age % 2 == 0:
            return f"The age {age} is even."
        else:
            return f"The age {age} is odd."
    except ValueError as ve:
        return f"Error: {ve}"

your_age_str = input("Enter your age: ")
result = even_odd_year(your_age_str)
print(result)
