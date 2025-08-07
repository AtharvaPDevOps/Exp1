from temperature import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius
)

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    choice = input("Choose an option: ")
    temp = float(input("Enter the temperature: "))

    if choice == '1':
        print(f"{temp}°C = {celsius_to_fahrenheit(temp):.2f}°F")
    elif choice == '2':
        print(f"{temp}°F = {fahrenheit_to_celsius(temp):.2f}°C")
    elif choice == '3':
        print(f"{temp}°C = {celsius_to_kelvin(temp):.2f}K")
    elif choice == '4':
        print(f"{temp}K = {kelvin_to_celsius(temp):.2f}°C")
    else:
        print("Invalid option.")

if __name__ == '__main__':
    main()

