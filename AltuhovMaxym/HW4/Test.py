def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    try:
        celsius = float(input("Enter the temperature in Celsius: "))
        
        if celsius < -273.15:
            print(f"Error: Temperature below absolute zero (-273.15°C)")
        else:
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is equivalent to {fahrenheit}°F")

    except ValueError:
        print("Error: Please enter a valid number for the temperature.")

if __name__ == "__main__":
    main()