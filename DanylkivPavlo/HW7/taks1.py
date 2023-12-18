def largest_number(num1,num2):
    """ Function that returns the largest number """
    if num1 > num2:
        print("The first number is bigger")
    elif num1 == num2:
        print("two numbers are equal")
    else:
        print("The second number is bigger")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
largest_number(num1,num2)