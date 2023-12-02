# Defining function
def c_to_f(celsius):
    ABSOLUTE_ZERO_C = -273.15 # 
    if celsius < ABSOLUTE_ZERO_C:
        print(f"Error: Temperature below absolute zero ({ABSOLUTE_ZERO_C}°C)")
    else:
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equivalent to {fahrenheit}°F")

# Getting user input
t_in_celsius = float(input("Enter the temperature in Celsius: "))
c_to_f(t_in_celsius)

