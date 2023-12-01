def lineReturnFromList(numsList: list[int])->str:
    """Return a string from a list consisting of integer values"""
    return " ".join(map(str, numsList))

###############
# Solution №1
###############

# evenNums = []
# oddNumsDivBy3 = []
# numsNotDivBy2And3 = []

# for number in range(1, 11):
    
#     if number%2 == 0:
#         evenNums.append(number)
#     if number%3 == 0:
#         oddNumsDivBy3.append(number)
#     if number%2 != 0 and number%3 != 0:
#         numsNotDivBy2And3.append(number)

# print(f"Even numbers that are divisible by 2: {lineReturnFromList(evenNums)}")
# print(f"Odd numbers, which are divisible by 3: {lineReturnFromList(oddNumsDivBy3)}")
# print(f"Numbers that are not divisible by 2 and 3: {lineReturnFromList(numsNotDivBy2And3)}")



###############
# Solution №2
###############

print(f"Even numbers that are divisible by 2: {lineReturnFromList([number for number in range(1, 11) if number % 2 == 0])}")
print(f"Odd numbers, which are divisible by 3: {lineReturnFromList([number for number in range(1, 11) if number % 3 == 0])}")
print(f"Numbers that are not divisible by 2 and 3: {lineReturnFromList([number for number in range(1, 11) if number % 2 != 0 and number % 3 != 0])}")