user_tempetature = float (input ('Enter your temperature in C°: '))
F = (user_tempetature * 9/5) + 32

if -273.15 <= user_tempetature :
  print(f'{user_tempetature} is equivalent to {F}')
else:
  print(f'Error! Temperature below absolute zero (-273.15).')
