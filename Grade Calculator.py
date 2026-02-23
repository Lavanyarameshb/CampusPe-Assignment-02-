# Question 6: Grade Calculator

try:
    subject1 = int(input("Enter marks for Subject 1: "))
    subject2 = int(input("Enter marks for Subject 2: "))
    subject3 = int(input("Enter marks for Subject 3: "))
    subject4 = int(input("Enter marks for Subject 4: "))
    subject5 = int(input("Enter marks for Subject 5: "))

    if (subject1 < 0 or subject1 > 100 or
        subject2 < 0 or subject2 > 100 or
        subject3 < 0 or subject3 > 100 or
        subject4 < 0 or subject4 > 100 or
        subject5 < 0 or subject5 > 100):

        print("Marks should be between 0 and 100.")

    else:
        print("\nMarks Entered:")
        print("Subject 1:", subject1)
        print("Subject 2:", subject2)
        print("Subject 3:", subject3)
        print("Subject 4:", subject4)
        print("Subject 5:", subject5)

        total_marks = subject1 + subject2 + subject3 + subject4 + subject5
        print("\nTotal Marks:", total_marks, "/ 500")

        percentage = (total_marks / 500) * 100
        print("Percentage:", percentage, "%")

        if percentage >= 90:
            grade = "A+ (Outstanding)"
        elif percentage >= 80:
            grade = "A (Excellent)"
        elif percentage >= 70:
            grade = "B (Good)"
        elif percentage >= 60:
            grade = "C (Average)"
        elif percentage >= 50:
            grade = "D (Pass)"
        else:
            grade = "F (Fail)"

        print("Grade:", grade)

        if (subject1 >= 40 and subject2 >= 40 and
            subject3 >= 40 and subject4 >= 40 and
            subject5 >= 40):
            print("Result: PASS")
        else:
            print("Result: FAIL")

except:
    print("Invalid input! Please enter valid marks.")