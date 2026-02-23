# Question 11: Number Pattern Printer

print("Choose Pattern:")
print("1. Pattern 1")
print("2. Pattern 2")
print("3. Pattern 3")
print("4. Pattern 4")

try:
    choice = int(input("Enter pattern number: "))
    height = int(input("Enter height: "))
    # Pattern 1
    if choice == 1:
        row = 1
        while row <= height:
            number = 1
            while number <= row:
                print(number, end=" ")
                number = number + 1
            print()
            row = row + 1
    # Pattern 2
    elif choice == 2:
        row = 1
        while row <= height:
            count = 1
            while count <= row:
                print(row, end=" ")
                count = count + 1
            print()
            row = row + 1
    # Pattern 3
    elif choice == 3:
        row = height
        while row >= 1:
            number = row
            while number >= 1:
                print(number, end=" ")
                number = number - 1
            print()
            row = row - 1
    # Pattern 4
    elif choice == 4:
        row = 1
        while row <= height:
            number = 1
            while number <= row:
                print(number, end="")
                number = number + 1
            number = row - 1
            while number >= 1:
                print(number, end="")
                number = number - 1

            print()
            row = row + 1

    else:
        print("Invalid pattern choice.")

except:
    print("Invalid input! Please enter correct numbers.")