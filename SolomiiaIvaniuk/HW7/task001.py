def compareNums(num1: float, num2: float) -> float:
    """
    This function takes two arguments with int or float type.
    It compares them and returns the bigger one.
    """

    if num1 > num2:
        return num1
    else:
        return num2


number1 = input("Enter first number: ")
number2 = input("Enter second number: ")
result = ((number1,number2),"bigger")
print(result)







