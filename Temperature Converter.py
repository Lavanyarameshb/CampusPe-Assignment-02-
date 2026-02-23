# Question 7: Temperature Converter

while True:

    print("\n===== TEMPERATURE CONVERTER =====")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9 / 5) + 32
            print("Result:", fahrenheit, "F")

        elif choice == 2:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5 / 9
            print("Result:", celsius, "C")

        elif choice == 3:
            celsius = float(input("Enter temperature in Celsius: "))
            kelvin = celsius + 273.15
            print("Result:", kelvin, "K")

        elif choice == 4:
            kelvin = float(input("Enter temperature in Kelvin: "))
            celsius = kelvin - 273.15
            print("Result:", celsius, "C")

        elif choice == 5:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            kelvin = (fahrenheit - 32) * 5 / 9 + 273.15
            print("Result:", kelvin, "K")

        elif choice == 6:
            kelvin = float(input("Enter temperature in Kelvin: "))
            fahrenheit = (kelvin - 273.15) * 9 / 5 + 32
            print("Result:", fahrenheit, "F")

        elif choice == 7:
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please select between 1 to 7.")

    except:
        print("Invalid input! Please enter correct numbers.")