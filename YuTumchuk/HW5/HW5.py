######## Task1 #########
# creating arbitrary list consisted of integers
list_int = []
for i in range(7):
    list_int.append(i)
# looping through list
list_float = []
for item in list_int:
    list_float.append(float(item))
# or we can use list comprehension here: list_float=[float(i) for i in list_int]
print(list_float)

######## Task2 #########
n = int(input("Please enter number to which build Fibonacci sequence:"))
fibonacci_sequence = [0, 1]
while fibonacci_sequence[-1] < n:
    new_element = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    if new_element > n:
        break
    else:
        fibonacci_sequence.append(new_element)
print(fibonacci_sequence)

######## Task3 #########
n = int(input("Please enter number to make factorial with:"))
if n < 0:
    while True:
        n = int((input("You entered a negative number, i can't do anything with it, enter positive:")))
        if n >= 0:
            break
res_factorial = 1
for i in range(1, n + 1):
    res_factorial *= i
print(res_factorial)
