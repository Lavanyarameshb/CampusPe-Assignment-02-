# Question 13: Sum and Average Calculator

try:
    count = int(input("How many numbers? "))

    if count <= 0:
        print("Count must be greater than 0.")
    else:
        total_sum = 0
        counter = 1

        first_number = float(input("Enter number 1: "))
        total_sum = total_sum + first_number
        maximum = first_number
        minimum = first_number

        counter = 2

        while counter <= count:
            number = float(input("Enter number " + str(counter) + ": "))

            total_sum = total_sum + number

            if number > maximum:
                maximum = number

            if number < minimum:
                minimum = number

            counter = counter + 1

        average = total_sum / count

        print("\nSum:", total_sum)
        print("Average:", average)
        print("Maximum:", maximum)
        print("Minimum:", minimum)

except:
    print("Invalid input! Please enter correct numbers.")