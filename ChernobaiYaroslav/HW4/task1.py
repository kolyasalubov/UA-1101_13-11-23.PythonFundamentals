celsiusTemperature = int(input("Enter the temperature in Celsius: "))
if celsiusTemperature < -237.15:
    print("Error: Temperature below absolute zero (-273.15\u2103 )")
else:
    print(f"{celsiusTemperature}\u2103  is equivalent to {int(celsiusTemperature * 9 / 5 + 32)}\u2109")