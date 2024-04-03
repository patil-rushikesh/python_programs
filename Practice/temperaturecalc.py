def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def my_temp_scale_to_celsius(my_temp):
    # Your conversion logic for MyTempScale to Celsius here
    return (my_temp - 32) * 5/9

def celsius_to_my_temp_scale(celsius):
    # Your conversion logic for Celsius to MyTempScale here
    return (celsius * 9/5) + 32

def my_temp_scale_to_fahrenheit(my_temp):
    # Your conversion logic for MyTempScale to Fahrenheit here
    return my_temp

def fahrenheit_to_my_temp_scale(fahrenheit):
    # Your conversion logic for Fahrenheit to MyTempScale here
    return fahrenheit

def kelvin_to_my_temp_scale(kelvin):
    # Your conversion logic for Kelvin to MyTempScale here
    return (kelvin - 273.15) * 9/5 + 32

def my_temp_scale_to_kelvin(my_temp):
    # Your conversion logic for MyTempScale to Kelvin here
    return (my_temp - 32) * 5/9 + 273.15

def temperature_converter():
    while True:
        print("\nTemperature Conversion Options:")
        print("1. Fahrenheit to Celsius")
        print("2. Celsius to Fahrenheit")
        print("3. Kelvin to Fahrenheit")
        print("4. Kelvin to Celsius")
        print("5. Celsius to Kelvin")
        print("6. Fahrenheit to Kelvin")
        print("7. MyTempScale to Celsius")
        print("8. Celsius to MyTempScale")
        print("9. MyTempScale to Fahrenheit")
        print("10. Fahrenheit to MyTempScale")
        print("11. Kelvin to MyTempScale")
        print("12. MyTempScale to Kelvin")
        print("13. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print("Temperature in Celsius:", fahrenheit_to_celsius(fahrenheit))
        elif choice == "2":
            celsius = float(input("Enter temperature in Celsius: "))
            print("Temperature in Fahrenheit:", celsius_to_fahrenheit(celsius))
        elif choice == "3":
            kelvin = float(input("Enter temperature in Kelvin: "))
            print("Temperature in Fahrenheit:", kelvin_to_fahrenheit(kelvin))
        elif choice == "4":
            kelvin = float(input("Enter temperature in Kelvin: "))
            print("Temperature in Celsius:", kelvin_to_celsius(kelvin))
        elif choice == "5":
            celsius = float(input("Enter temperature in Celsius: "))
            print("Temperature in Kelvin:", celsius_to_kelvin(celsius))
        elif choice == "6":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print("Temperature in Kelvin:", fahrenheit_to_kelvin(fahrenheit))
        elif choice == "7":
            my_temp = float(input("Enter temperature in MyTempScale: "))
            print("Temperature in Celsius:", my_temp_scale_to_celsius(my_temp))
        elif choice == "8":
            celsius = float(input("Enter temperature in Celsius: "))
            print("Temperature in MyTempScale:", celsius_to_my_temp_scale(celsius))
        elif choice == "9":
            my_temp = float(input("Enter temperature in MyTempScale: "))
            print("Temperature in Fahrenheit:", my_temp_scale_to_fahrenheit(my_temp))
        elif choice == "10":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print("Temperature in MyTempScale:", fahrenheit_to_my_temp_scale(fahrenheit))
        elif choice == "11":
            kelvin = float(input("Enter temperature in Kelvin: "))
            print("Temperature in MyTempScale:", kelvin_to_my_temp_scale(kelvin))
        elif choice == "12":
            my_temp = float(input("Enter temperature in MyTempScale: "))
            print("Temperature in Kelvin:", my_temp_scale_to_kelvin(my_temp))
        elif choice == "13":
            print("Exiting temperature converter.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    temperature_converter()
