# Celcius to Fahrenheit converter

celc_user = float(input('Enter the temperature in Celsius: '))
print('Error: Temperature below absolute zero (-273.15°C) ' if celc_user < -273.15 \
      else f'{celc_user}°C is equivalent to {(celc_user * 9 / 5) + 32}°F')