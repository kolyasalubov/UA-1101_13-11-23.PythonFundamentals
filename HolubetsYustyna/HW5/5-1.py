# Create a list that contains elements of integer type, then use the loop to change 
# the type of these elements to a floating type. (Hint: use the built-in float () function)

import random

rand_int_li = random.sample(range(0, 1000), 50)

rand_flt_li = [float(num) for num in rand_int_li]

print(rand_flt_li)
