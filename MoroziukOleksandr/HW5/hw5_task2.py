# Print Fibonacci numbers up to the entered number n, using cycles. 

num = int(input('Enter the number up to which you want to display the Fibonacci numbers: '))

if num < 0:
    print("Invalid input")
if num == 0:
    print(0)

a, b = 0, 1
while a <= num:
    print(a, end=" ")
    a, b = b, a + b
