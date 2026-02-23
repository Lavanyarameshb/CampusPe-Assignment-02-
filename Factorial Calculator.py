# Question 14: Factorial Calculator

try:
    number = int(input("Enter a number: "))

    if number < 0:
        print("Factorial is not defined for negative numbers.")

    elif number == 0:
        print("0! = 1")

    else:
        factorial = 1
        counter = number

        print(str(number) + "! =", end=" ")

        while counter >= 1:
            factorial = factorial * counter

            if counter > 1:
                print(counter, "x", end=" ")
            else:
                print(counter, end="")

            counter = counter - 1

        print(" =", factorial)

except:
    print("Invalid input! Please enter a valid integer.")