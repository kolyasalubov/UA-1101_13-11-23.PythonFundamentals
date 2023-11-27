temp_cels_user = float(input("Enter temperature in Celsius to convert to Fahrenheit\n"))

min_temp = -273.15

if temp_cels_user < min_temp:
    print(f"Temperature below absolute zero {min_temp}° C")
else:
    F = (temp_cels_user *9/5) + 32
    print(f"{temp_cels_user}° C is equivalent to {F}° F")    