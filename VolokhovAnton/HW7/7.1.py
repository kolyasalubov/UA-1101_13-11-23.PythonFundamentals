def find_largest_number(a, b):
    """
    This function takes 2 arguments:
    a (int or float): First number
    b (int or float): Second number
    Returns:
    int or float: The largest number among two numbers given.
    """
    try:
        a = float(a)  # Convert input to float
        b = float(b)  # Convert input to float
    except ValueError:
        print("Invalid entry. Please enter a valid int or float number.")
        return None  # Return None in case of invalid input
    
    return max(a, b)

# Retrieve user input
a, b = input("Enter the first number: "), input("Enter the second number: ")

# Call the function and print the result
result = find_largest_number(a, b)
if result is not None:
    print(f"The largest number is: {result}")
