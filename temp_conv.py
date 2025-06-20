def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("🌡️ Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Choose conversion (1 or 2): ")

try:
    if choice == '1':
        c = float(input("Enter temperature in Celsius: "))
        f = celsius_to_fahrenheit(c)
        print(f"{c}°C = {round(f, 2)}°F")

    elif choice == '2':
        f = float(input("Enter temperature in Fahrenheit: "))
        c = fahrenheit_to_celsius(f)
        print(f"{f}°F = {round(c, 2)}°C")

    else:
        print("❌ Invalid choice. Please enter 1 or 2.")

except ValueError:
    print("❌ Please enter a valid number.")
