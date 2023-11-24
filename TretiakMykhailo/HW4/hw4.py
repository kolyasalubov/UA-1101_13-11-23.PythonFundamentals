temp_C = int(input("Температура в Celsius: "))
temp_F = (temp_C * 9/5) + 32
if temp_C < -273.15:
    print(f"[!] {temp_C} - неможлива температура")
else:
    print(f"Температура в Fahrenheit: {temp_F}")
