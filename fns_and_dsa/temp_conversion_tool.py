FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR= 9/5
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
x=input("Enter the temperature to convert: ")
y=input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if y=='C':
    converted_temp = convert_to_fahrenheit(float(x))
    print(f"{x}°C is {converted_temp:.2f}°F")
elif y=='F':
    converted_temp = convert_to_celsius(float(x))
    print(f"{x}°F is {converted_temp:.2f}°C")    
else:
    print("Invalid temperature. Please enter a numeric value.")





