temperature_c = float (input ('Enter your temperature in C°: '))
F  = (temperature_c * 9/5) + 32

if -273.15 <= temperature_c:
  print(f'{temperature_c} is equivalent to {F}')
else:
  print(f'Error! Temperature below absolute zero (-273.15).')
  
  
  

