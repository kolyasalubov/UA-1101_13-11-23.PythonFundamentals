celsius_temp = float(input("Enter the temperature in Celsius: "))
if celsius_temp >= -273.15:
    fahrenheit_temp = (celsius_temp * 9 / 5) + 32
    print(f"{celsius_temp}°C is equivalent to {fahrenheit_temp}°F")
else:
    print("Error: temperature below absolute zero ")