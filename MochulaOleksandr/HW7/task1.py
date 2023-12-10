def highest_number(number1,number2):
 """This function returns the highest value"""
 if number1 > number2:
  return number1
 elif number2 > number1:
  return number2
 else:
  return False
 

print(highest_number(15,10))
