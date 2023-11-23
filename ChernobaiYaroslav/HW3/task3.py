var1 = input("Enter the first value: ")
var2 = input("Enter the second value: ")
var1 = var1 + var2
var2 = var1[:len(var1) - len(var2)]
var1 = var1[len(var2):]
print(f"\nReversed values: \nReversed first value: {var1}.\nReversed second value: {var2}.")