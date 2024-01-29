def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    tmp_c = float(input('Enter the temperature in Celsius: '))

    if tmp_c < -273.15:
        print('Error: Temperature below absolute zero (-273.15°C)')
    else:
        tmp_f = celsius_to_fahrenheit(tmp_c)
        print(f'{tmp_c}°C is equivalent to {tmp_f}°F')

if __name__ == "__main__":
    main()