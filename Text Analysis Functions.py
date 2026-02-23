# Question 19: Text Analysis Functions

def count_words(text):
    count = 0
    inside_word = False

    for ch in text:
        if ch != " " and inside_word == False:
            count = count + 1
            inside_word = True
        elif ch == " ":
            inside_word = False

    return count

def count_vowels(text):
    count = 0

    for ch in text:
        if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or
            ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
            count = count + 1

    return count

def count_consonants(text):
    count = 0

    for ch in text:
        if ((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
            if not (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or
                    ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
                count = count + 1

    return count

def reverse_text(text):
    reversed_text = ""
    length = 0

    for ch in text:
        length = length + 1

    index = length - 1

    while index >= 0:
        reversed_text = reversed_text + text[index]
        index = index - 1

    return reversed_text

def is_palindrome(text):
    reversed_version = reverse_text(text)

    if text == reversed_version:
        return True
    else:
        return False
    
def remove_vowels(text):
    result = ""

    for ch in text:
        if not (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or
                ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
            result = result + ch

    return result

def longest_word(text):
    current_word = ""
    longest = ""

    for ch in text:
        if ch != " ":
            current_word = current_word + ch
        else:
            if len(current_word) > len(longest):
                longest = current_word
            current_word = ""
    if len(current_word) > len(longest):
        longest = current_word

    return longest

def word_frequency(text):

    printed_words = ""

    current_word = ""

    print("Word Frequency:")

    for ch in text + " ":
        if ch != " ":
            current_word = current_word + ch
        else:
            already_printed = False
            temp = ""
            for c in printed_words:
                temp = temp + c

            if current_word != "" and current_word not in printed_words:

                count = 0
                temp_word = ""

                for letter in text + " ":
                    if letter != " ":
                        temp_word = temp_word + letter
                    else:
                        if temp_word == current_word:
                            count = count + 1
                        temp_word = ""

                print(current_word, ":", count)
                printed_words = printed_words + current_word + " "

            current_word = ""
def analyze_text(text):

    print("\n=== TEXT ANALYSIS ===")

    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))

    if is_palindrome(text):
        print("Palindrome: Yes")
    else:
        print("Palindrome: No")

    print("Without vowels:", remove_vowels(text))

    longest = longest_word(text)
    print("Longest word:", longest)

    word_frequency(text)

user_text = input("Enter text: ")
analyze_text(user_text)