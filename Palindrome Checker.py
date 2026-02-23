# Question 17: Palindrome Checker

try:
    user_input = input("Enter word/number: ")
    lowercase_text = ""

    for character in user_input:
        if character >= 'A' and character <= 'Z':
            lowercase_character = chr(ord(character) + 32)
            lowercase_text = lowercase_text + lowercase_character
        else:
            lowercase_text = lowercase_text + character

    print("\nOriginal:", user_input)
    reversed_text = ""
    index = 0

    length = 0
    for character in lowercase_text:
        length = length + 1

    index = length - 1

    while index >= 0:
        reversed_text = reversed_text + lowercase_text[index]
        index = index - 1

    print("Reversed:", reversed_text)
    
    if lowercase_text == reversed_text:
        print("Result: PALINDROME")
    else:
        print("Result: NOT PALINDROME")

except:
    print("Invalid input!")