# using loop for

num = int(input("Please enter number n: "))
num1_Fibonacci, num2_Fibonacci = 0, 1

for i in range(num):
    print(num1_Fibonacci, end=" ")
    num1_Fibonacci, num2_Fibonacci = num2_Fibonacci, num1_Fibonacci + num2_Fibonacci
    


# using loop while

num = int(input("\nPlease enter number n: "))
num1_Fibonacci, num2_Fibonacci = 0, 1

while num1_Fibonacci <=num:
    print("The number of Fibonacci series is:", num1_Fibonacci)
    # print(num1_Fibonacci, end=" ")
    num1_Fibonacci, num2_Fibonacci = num2_Fibonacci, num1_Fibonacci + num2_Fibonacci

