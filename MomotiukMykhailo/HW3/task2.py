import numpy
number = 1984

#subtask 1
number_list = list(map(int, str(number)))
multiplication = numpy.prod(number_list)
print('The product of these digits is:', multiplication)

#subtask 2
origin_list = tuple(number_list)
number_list.reverse()

# print('reversed list:', number_list) # for test purposes
# print('origin list:', origin_list) # for test purposes

reversed_number = ''.join(map(str, number_list))
print('Reversed number:', reversed_number)

#subtask 3
asc_list = list(origin_list)
asc_list.sort()
print('Sorted list:', asc_list)
