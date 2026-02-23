# Question 16: Number Guessing Game

import random

play_again = "yes"

while play_again == "yes":

    secret_number = random.randint(1, 100)
    attempts_left = 7
    attempts_used = 0
    guessed_correctly = False

    print("\n=== NUMBER GUESSING GAME ===")
    print("Guess the number between 1 and 100")
    print("You have 7 attempts.")

    while attempts_left > 0:

        try:
            guess = int(input("Enter your guess: "))
            attempts_left = attempts_left - 1
            attempts_used = attempts_used + 1

            if guess == secret_number:
                print("🎉 Congratulations! You guessed correctly.")
                print("Attempts used:", attempts_used)
                guessed_correctly = True
                break

            elif guess < secret_number:
                print("Too Low!")

            else:
                print("Too High!")

            print("Attempts remaining:", attempts_left)

        except:
            print("Invalid input! Please enter a number.")

    if guessed_correctly == False:
        print("\nYou failed to guess the number.")
        print("The correct number was:", secret_number)

    play_again = input("\nDo you want to play again? (yes/no): ")

print("Thank you for playing!")