def the_biggest_number(num1: int, num2: int) -> int:
    """
    Return the biggest number of prowided two numbers

    :param num1: First number to compare
    :param num2: Second number to comopare 

    :return: If number are equal retutn 0 otherwise the bigges number
    :type: int
    """
    res = 0
    if num1 > num2:
        res = num1
    elif num2 > num1:
        res = num2
    else:
        print("The numbers are equal!")
    return res

number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")
result = the_biggest_number(number1,number2)
print(result)