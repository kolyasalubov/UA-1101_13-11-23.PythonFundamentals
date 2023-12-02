C = float(input("Please write Celsius to convert into Fahrenheit \n"))
if C >= -273.15:
    F = (C*9/5)+32
    print (f"Temperature {C} C is equivalent to {F} F")
else:
     print("There is no lower temperature than -273.15")