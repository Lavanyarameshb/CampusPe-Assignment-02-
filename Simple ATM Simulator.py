# Question 10: Simple ATM Simulator

balance = 10000  

while True:

    print("\n===== ATM SIMULATOR =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Current Balance: ₹", balance)

        elif choice == 2:
            deposit_amount = float(input("Enter amount to deposit: "))

            if deposit_amount > 0:
                balance = balance + deposit_amount
                print("Deposit successful!")
                print("New Balance: ₹", balance)
            else:
                print("Deposit amount must be greater than 0.")

        elif choice == 3:
            withdraw_amount = float(input("Enter amount to withdraw: "))

            if withdraw_amount <= 0:
                print("Withdrawal amount must be greater than 0.")

            elif withdraw_amount > balance:
                print("Insufficient balance!")

            elif balance - withdraw_amount < 500:
                print("Minimum balance of ₹500 must remain in account.")

            else:
                balance = balance - withdraw_amount
                print("Withdrawal successful!")
                print("New Balance: ₹", balance)

        elif choice == 4:
            print("Thank you for using ATM!")
            break

        else:
            print("Invalid choice. Please select 1 to 4.")

    except:
        print("Invalid input! Please enter correct values.")