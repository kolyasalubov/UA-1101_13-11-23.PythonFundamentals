q = input("Enter four-digit natural number: ")
count = 1
for i in q:
    count *= int(i)
print(count)

b = q[3],q[2],q[1],q[0]
print(b)

sorted_number = int("".join(sorted(str(q))))
print(sorted_number)
