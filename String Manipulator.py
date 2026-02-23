# Question 3: String Manipulator

sentence = input("Enter a sentence: ")

print("\nOriginal:", sentence)
count_with_spaces = 0

for character in sentence:
    count_with_spaces = count_with_spaces + 1

print("Characters (with spaces):", count_with_spaces)
count_without_spaces = 0

for character in sentence:
    if character != " ":
        count_without_spaces = count_without_spaces + 1

print("Characters (without spaces):", count_without_spaces)

word_count = 0
inside_word = False

for character in sentence:
    if character != " " and inside_word == False:
        word_count = word_count + 1
        inside_word = True
    elif character == " ":
        inside_word = False

print("Words:", word_count)

uppercase_sentence = ""

for character in sentence:
    
    if character >= 'a' and character <= 'z':
        uppercase_character = chr(ord(character) - 32)
        uppercase_sentence = uppercase_sentence + uppercase_character
    else:
        uppercase_sentence = uppercase_sentence + character

print("UPPERCASE:", uppercase_sentence)


lowercase_sentence = ""

for character in sentence:
    # Check if character is uppercase letter
    if character >= 'A' and character <= 'Z':
        lowercase_character = chr(ord(character) + 32)
        lowercase_sentence = lowercase_sentence + lowercase_character
    else:
        lowercase_sentence = lowercase_sentence + character

print("lowercase:", lowercase_sentence)

title_sentence = ""
make_upper = True

for character in sentence:
    if make_upper and character >= 'a' and character <= 'z':
        title_sentence = title_sentence + chr(ord(character) - 32)
        make_upper = False
    elif character == " ":
        title_sentence = title_sentence + character
        make_upper = True
    else:
        title_sentence = title_sentence + character
        make_upper = False

print("Title Case:", title_sentence)

first_word = ""

for character in sentence:
    if character != " ":
        first_word = first_word + character
    else:
        break

print("First word:", first_word)

last_word = ""
temp_word = ""

for character in sentence:
    if character != " ":
        temp_word = temp_word + character
    else:
        last_word = temp_word
        temp_word = ""

# After loop ends, last word will be in temp_word
last_word = temp_word

print("Last word:", last_word)


reversed_sentence = ""
index = count_with_spaces - 1

while index >= 0:
    reversed_sentence = reversed_sentence + sentence[index]
    index = index - 1

print("Reversed:", reversed_sentence)