# Question 12: Multiplication Table Generator

try:
    number = int(input("Enter number: "))
    range_end = int(input("Enter range (end): "))

    print("\nMultiplication Table of", number)

    counter = 1

    while counter <= range_end:
        result = number * counter
        print(number, "x", counter, "=", result)
        counter = counter + 1

except:
    print("Invalid input! Please enter correct numbers.")