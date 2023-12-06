# numbers = [25,54,10,8,1,6]
# x = len(numbers)
# while x > 0:
#     x = x -1
#     numbers[x] = float(numbers[x])
# print(numbers)

numbers = [25,54,10,8,1,6]
x = len(numbers)
y = 0
for y in range(x):
    numbers[y] = float(numbers[y])
print(numbers)
