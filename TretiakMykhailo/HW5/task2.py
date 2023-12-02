n = 50
fibonacci = [0, 1]
while True:
    num = fibonacci[-1]  + fibonacci[-2]
    if fibonacci[-1] == n:
        break
    elif num > n:
        break
    
    fibonacci.append(num)
    
print(fibonacci)