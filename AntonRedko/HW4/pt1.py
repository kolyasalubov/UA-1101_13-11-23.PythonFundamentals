temp_input = float(input("Enter temperature in Celsius: "))

if temp_input < -273.15:
    print("Temperature below absolute zero!")
else:
    fahren_heit = (temp_input*9/5) + 32
    print(f"{temp_input}°С is equivalent to {fahren_heit}°F")
