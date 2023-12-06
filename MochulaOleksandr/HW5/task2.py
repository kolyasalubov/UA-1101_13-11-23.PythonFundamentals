numbers = [0,1]
n = 0
y = 1
while numbers[y] <= 8:
    numbers.append(numbers[n]+numbers[y])
    n += 1
    y += 1
print(numbers,"etc.")
