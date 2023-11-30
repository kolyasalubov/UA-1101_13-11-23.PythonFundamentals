tmp_c = float(input('Enter the temperature is Celsius: '))
tmp_f = (tmp_c * 9/5) + 32

if tmp_c < -273.15:
      print('Errror: Trmperature below absolute zero (-273.15°C)')
else:
      print(f'{tmp_c}°C is equivalent to {tmp_f}°F')