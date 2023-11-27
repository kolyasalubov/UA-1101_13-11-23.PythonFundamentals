n1 = int(input("Enter number"))
n2 = int(input("Enter number"))
n3 = int(input("Enter number"))
n4 = int(input("Enter number"))

numbers = [n1, n2, n3, n4]

print(f"product {n1*n2*n3*n4}")
print(f"reverse sorted {sorted(numbers, reverse=True)}")
print(f"ascending sorted {sorted(numbers)}")
