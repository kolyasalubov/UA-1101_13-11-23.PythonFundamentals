user = input("Enter number: ")
n = []
for j in range(int(user), 0, -1):
    n.append(j)
    #print(n)
for i in user:
    count = 1
    if int(i) == 0:
        print(1)
    elif int(i) == 1:
        print(1)
    else:
        for last_loop in n:
            count = count * int(last_loop)
print(count)
