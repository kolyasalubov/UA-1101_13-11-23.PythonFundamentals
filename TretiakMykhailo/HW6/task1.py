# Task 1
even = []
odd = []
other = []
for i in range(1, 11):
    if i%2==0:
        even.append(i)
    elif i%3==0:
        odd.append(i)
    elif i%2 and i%3:
        other.append(i)
        
print(f"Even: {even}")
print(f"Odd: {odd}")
print(f"Numbers that are not divisible by 2 and 3: {other}")