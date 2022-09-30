def print_upper_words(words, must_start_with):
    """Prints all caps version of words list,
    excluding word that don't start with letters in must_start_with"""

    for word in words:
        for char in must_start_with:
            if word[0] == char:
                print(word)
        

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})