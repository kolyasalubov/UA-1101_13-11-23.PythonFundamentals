# Print Fibonacci numbers up to the entered number n, using cycles.
# (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)

count_inp = int(input('Enter the number of terms: '))

prv_num_0, prv_num_1 = 0, 1
count = 0

Fibo_li = [prv_num_0, prv_num_1]

while count < count_inp:
    Fibo = prv_num_0 + prv_num_1
    Fibo_li.append(Fibo)
    prv_num_0 = prv_num_1
    prv_num_1 = Fibo
    count += 1

print(Fibo_li)