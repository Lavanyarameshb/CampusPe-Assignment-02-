# Question 8: Leap Year Checker

try:
    year_input = input("Enter a year: ")
    year = int(year_input)

    print("\nChecking year:", year)
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year, "is a LEAP year")
                print("Reason: Divisible by 4, 100 and 400.")
            else:
                print(year, "is NOT a leap year")
                print("Reason: Divisible by 100 but NOT divisible by 400.")
        else:
            print(year, "is a LEAP year")
            print("Reason: Divisible by 4 but NOT divisible by 100.")
    else:
        print(year, "is NOT a leap year")
        print("Reason: Not divisible by 4.")

except:
    print("Invalid input! Please enter a valid year.")