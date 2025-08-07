from temperature import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius
)

def run_all():
    print("Celsius to Fahrenheit (25°C):", celsius_to_fahrenheit(25))
    print("Fahrenheit to Celsius (77°F):", fahrenheit_to_celsius(77))
    print("Celsius to Kelvin (0°C):", celsius_to_kelvin(0))
    print("Kelvin to Celsius (300K):", kelvin_to_celsius(300))

if __name__ == "__main__":
    run_all()

