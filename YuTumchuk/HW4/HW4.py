users_input=input("Please enter temperature in Celsius: ")
if int(users_input)<-273.15:
    print(f"Error: Temperature below absolute zero (-273,15{chr(176)}C)")
else:
    temp_in_Fahrenheit=(int(users_input)*9/5)+32
    print (f"{users_input}{chr(176)}C is equivalent to {int(temp_in_Fahrenheit)}{chr(176)}F")