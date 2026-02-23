# Question 20: Number System Functions

def factorial(n):
    if n < 0:
        return "Not defined for negative numbers"
    if n == 0:
        return 1

    result = 1
    counter = 1
    while counter <= n:
        result = result * counter
        counter = counter + 1
    return result

def is_prime(n):
    if n <= 1:
        return False
    divisor = 2
    while divisor < n:
        if n % divisor == 0:
            return False
        divisor = divisor + 1
    return True


def fibonacci(n):
    if n <= 0:
        return "Invalid position"
    if n == 1:
        return 0
    if n == 2:
        return 1

    first = 0
    second = 1
    count = 3

    while count <= n:
        next_number = first + second
        first = second
        second = next_number
        count = count + 1

    return second

def sum_of_digits(n):
    total = 0
    if n < 0:
        n = -n

    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10

    return total

def reverse_number(n):
    reversed_num = 0
    is_negative = False

    if n < 0:
        is_negative = True
        n = -n

    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10

    if is_negative:
        return -reversed_num
    else:
        return reversed_num

def is_armstrong(n):
    original = n
    total = 0

    if n < 0:
        return False

    while n > 0:
        digit = n % 10
        total = total + (digit * digit * digit)
        n = n // 10

    if total == original:
        return True
    else:
        return False

def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def is_perfect_number(n):
    if n <= 1:
        return False

    total = 0
    divisor = 1

    while divisor < n:
        if n % divisor == 0:
            total = total + divisor
        divisor = divisor + 1

    if total == n:
        return True
    else:
        return False

def math_menu():

    while True:
        print("\n===== NUMBER SYSTEM MENU =====")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Check")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number")
        print("10. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 10:
                print("Exiting program...")
                break

            if choice == 1:
                num = int(input("Enter number: "))
                print("Factorial:", factorial(num))

            elif choice == 2:
                num = int(input("Enter number: "))
                print("Is Prime:", is_prime(num))

            elif choice == 3:
                num = int(input("Enter position: "))
                print("Fibonacci number:", fibonacci(num))

            elif choice == 4:
                num = int(input("Enter number: "))
                print("Sum of digits:", sum_of_digits(num))

            elif choice == 5:
                num = int(input("Enter number: "))
                print("Reversed number:", reverse_number(num))

            elif choice == 6:
                num = int(input("Enter number: "))
                print("Is Armstrong:", is_armstrong(num))

            elif choice == 7:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print("GCD:", gcd(a, b))

            elif choice == 8:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print("LCM:", lcm(a, b))

            elif choice == 9:
                num = int(input("Enter number: "))
                print("Is Perfect Number:", is_perfect_number(num))

            else:
                print("Invalid choice.")

        except:
            print("Invalid input! Please enter valid numbers.")

math_menu()