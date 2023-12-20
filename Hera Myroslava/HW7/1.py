def large_number (a, b):
  return a if a > b else (b if a < b else f"The numbers {a} and {b} are equal")

a = float(input("Enter number a: "))
b = float(input("Enter number b: "))
print (f"The large number is: ", large_number(a, b))