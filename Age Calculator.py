# Question 4: Age Calculator

try:
    birth_year_input = input("Enter your birth year: ")
    birth_year = int(birth_year_input)

    current_year_input = input("Enter current year: ")
    current_year = int(current_year_input)

    if birth_year > current_year:
        print("Birth year cannot be greater than current year.")
    else:
        age_years = current_year - birth_year
        print("\nYour Age:", age_years, "years")

        age_months = age_years * 12
        print("Age in Months:", age_months)

        age_days = age_years * 365
        print("Age in Days (approx):", age_days)

        age_hours = age_days * 24
        print("Age in Hours:", age_hours)

        age_minutes = age_hours * 60
        print("Age in Minutes:", age_minutes)

        if age_years < 100:
            years_to_100 = 100 - age_years
            print("Years until 100:", years_to_100)
        else:
            print("You are already 100 or more!")

except:
    print("Invalid input! Please enter valid numbers.")