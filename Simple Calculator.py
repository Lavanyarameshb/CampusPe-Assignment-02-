# Question 2: Simple Calculator

try:
    first_number_input = input("Enter first number: ")
    first_number = float(first_number_input)

    second_number_input = input("Enter second number: ")
    second_number = float(second_number_input)

    print("\nResults:")

    # Addition
    addition_result = first_number + second_number
    print(str(first_number) + " + " + str(second_number) + " = " + str(addition_result))

    # Subtraction
    subtraction_result = first_number - second_number
    print(str(first_number) + " - " + str(second_number) + " = " + str(subtraction_result))

    # Multiplication
    multiplication_result = first_number * second_number
    print(str(first_number) + " * " + str(second_number) + " = " + str(multiplication_result))

    # Division (check divide by zero)
    if second_number != 0:
        division_result = first_number / second_number
        print(str(first_number) + " / " + str(second_number) + " = " + str(division_result))
    else:
        print("Division not possible (cannot divide by zero)")

    # Modulus (check divide by zero)
    if second_number != 0:
        modulus_result = first_number % second_number
        print(str(first_number) + " % " + str(second_number) + " = " + str(modulus_result))
    else:
        print("Modulus not possible (cannot divide by zero)")

    # Exponentiation (Power)
    power_result = first_number ** second_number
    print(str(first_number) + " ^ " + str(second_number) + " = " + str(power_result))

except:
    print("Invalid input! Please enter valid numbers.")