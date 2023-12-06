number = int(input('Enter number to calculate her factorial '))

if number in [0,1]:
    result = 1
else:
    result = 1
    for i in range(1, number):
        result = result + i * result

print(result)