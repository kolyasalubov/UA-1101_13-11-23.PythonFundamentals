celsius_temp = float(input('Enter the value for temperature in °C: '))

if celsius_temp > -273.15:
    fahrenheit_temp = (celsius_temp * 9/5) + 32
    print(f'{celsius_temp} is equivalent to {fahrenheit_temp}°F')
else:
    print('Error: Temperature below absolute zero(-273.15°C)')

