# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global factor."""
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global factor."""
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

try:
    # Prompt user for temperature
    temp_input = input("Enter the temperature value: ")

    # Check if numeric
    if not temp_input.replace('.', '', 1).isdigit():
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    temperature = float(temp_input)

    # Prompt user for scale
    scale = input("Is this temperature in Celsius (C) or Fahrenheit (F)? ").strip().upper()

    if scale == "C":
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {result}°F")

    elif scale == "F":
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is equal to {result}°C")

    else:
        print("Invalid scale. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

except ValueError as e:
    print(e)
