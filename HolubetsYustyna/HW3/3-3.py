# interchange values of 2 variables w/o the 3rd one

a = [6, 34]
b = 'bs'
# print(id(a), id(b))

a,b = b,a

print(a, b)
# print(id(a), id(b))