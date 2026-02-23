# Question 5: Bill Splitter

try:
    total_bill_input = input("Enter total bill amount: ")
    total_bill = float(total_bill_input)

    number_of_people_input = input("Enter number of people: ")
    number_of_people = int(number_of_people_input)

    tax_percentage_input = input("Enter tax percentage: ")
    tax_percentage = float(tax_percentage_input)

    tip_percentage_input = input("Enter tip percentage: ")
    tip_percentage = float(tip_percentage_input)

    if number_of_people <= 0:
        print("Number of people must be greater than 0.")
    else:
        print("\n=== BILL BREAKDOWN ===")

        subtotal = total_bill
        print("Subtotal: ₹", subtotal)

        tax_amount = (subtotal * tax_percentage) / 100
        print("Tax amount: ₹", tax_amount)

        after_tax = subtotal + tax_amount
        print("After tax: ₹", after_tax)

        tip_amount = (after_tax * tip_percentage) / 100
        print("Tip amount: ₹", tip_amount)

        final_total = after_tax + tip_amount
        print("Total bill: ₹", final_total)

        per_person = final_total / number_of_people
        print("Amount per person: ₹", per_person)

except:
    print("Invalid input! Please enter correct values.")