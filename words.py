def print_upper_words (list, must_start_with):
    for word in list:
        for letter in must_start_with:
            if word[0].upper() == letter.upper():
                print(word.upper())
                break

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],must_start_with={"h", "y"})