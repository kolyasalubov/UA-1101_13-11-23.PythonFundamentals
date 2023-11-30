# Write a script that will calculate the factorial of the entered
# number w/o using recursion 3! = 1*2*3 = 6

num_inp = int(input('Enter a number: '))

num, facto = num_inp, 1
formula_f = ''

while num > 0:
    facto *= num
    formula_f = '*{}{}'.format(num, formula_f)  
    num -= 1

print('{}! = {} = {}'.format(num_inp, formula_f[1:], facto))