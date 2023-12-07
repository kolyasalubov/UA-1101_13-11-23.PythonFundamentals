# temperatureC = float(input("What is the temperature in Celsius:"))
# if temperatureC < -273.15:
#   print("This is temperature below absolute zero is not possible")
# else:
#    temperatureF = (temperatureC * 9/5) + 32
#    print(temperatureF)

status_code = int(input("Enter statuscode from server: "))

match status_code:
    case 400:
        print("Bad")
    case 401:
        print("maks")
    case _:
        print("Else")