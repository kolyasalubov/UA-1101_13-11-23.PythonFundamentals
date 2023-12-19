# fibonacci
n = int(input("What is the max value of the sequence do you want? "))
first_num = 0
second_num = 1
sum = 0

while sum <= n:
    print(sum)
    sum = first_num + second_num
    first_num = second_num
    second_num = sum