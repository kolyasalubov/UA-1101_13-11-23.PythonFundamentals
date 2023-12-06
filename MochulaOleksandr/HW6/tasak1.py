even =[]
odd = []
numbers = []

x = 1
while x <= 10:
    if x%2 == False:
        even.append(x)
    elif x%3 == False:
        odd.append(x)
    else:
        numbers.append(x)
    x+=1
print(f"This are even numbers:{even}, this are odd numbers:{odd}, this are the other numbers:{numbers}\n")    
