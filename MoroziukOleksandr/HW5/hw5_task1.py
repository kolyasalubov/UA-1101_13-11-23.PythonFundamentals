import random

# Generate 5 random numbers between 10 and 30
randomlist = random.sample(range(0, 1000), 20)
print('This is a randomly generated list of integers: ' + str(randomlist))

# This is an empty list of floating point numbers
f_random_list = []

# Scanning a previously randomly generated list and converting integers to floats
for item in randomlist:
    f_random_list.append(float(item))

print(f_random_list)
