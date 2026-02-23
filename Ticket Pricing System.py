# Question 9: Ticket Pricing System

try:
    age = int(input("Enter age: "))
    day = input("Enter day of the week: ")
    number_of_tickets = int(input("Enter number of tickets: "))

    if age < 3:
        base_price = 0
        category = "Free"
    elif age >= 3 and age <= 12:
        base_price = 150
        category = "Child"
    elif age >= 13 and age <= 59:
        base_price = 300
        category = "Adult"
    else:
        base_price = 200
        category = "Senior"

    print("\nTicket Category:", category)
    print("Base price per ticket: ₹", base_price)

    total_base = base_price * number_of_tickets

    if (day == "Friday" or day == "Saturday" or day == "Sunday"):
        discount = (total_base * 20) / 100
        print("Weekend Discount (20%): ₹", discount)
    else:
        discount = 0
        print("No Discount")
        
    final_amount = total_base - discount

    print("Price after discount: ₹", final_amount)
    print("Total amount to pay: ₹", final_amount)

except:
    print("Invalid input! Please enter correct values.")