def compareNums(num1: float, num2: float) -> float:
    """
    This function takes two arguments with int or float type.
    It compares them and returns the bigger one.
    """

    if num1 > num2:
        return num1
    else:
        return num2

    
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(compareNums(num1, num2), "is bigger.")