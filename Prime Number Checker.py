# Question 15: Prime Number Checker
try:
    # PART 1: Check single number
    number = int(input("Enter a number: "))

    if number <= 1:
        print(number, "is NOT a prime number")

    elif number == 2:
        print(number, "is a PRIME number")

    else:
        divisor = 2
        is_prime = True

        while divisor < number:
            if number % divisor == 0:
                is_prime = False
                break
            divisor = divisor + 1

        if is_prime == True:
            print(number, "is a PRIME number")
        else:
            print(number, "is NOT a prime number")
    # PART 2: Prime numbers in range
    start = int(input("\nEnter start range: "))
    end = int(input("Enter end range: "))

    print("Prime numbers in given range:")

    current = start

    while current <= end:

        if current > 1:
            divisor = 2
            is_prime = True

            while divisor < current:
                if current % divisor == 0:
                    is_prime = False
                    break
                divisor = divisor + 1

            if is_prime == True:
                print(current, end=" ")

        current = current + 1

except:
    print("Invalid input! Please enter valid integers.")