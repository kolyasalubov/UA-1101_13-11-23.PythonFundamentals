tempC = float(input("Enter the temperature in Celsius: "))
if tempC >= -273.15:
    tempF = (tempC * 9 / 5) + 32
    print(tempC,"°C is equivalent to",tempF, "°F")
else:
    print("Error: temperature below absolute zero ")