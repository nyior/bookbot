# main file
from collections import Counter


def num_of_words(content):
    words_count = len(content.split())
    letters_count  =  count_letters(content)

    print("--- Begin report of books/frankenstein.txt ---\n\n")
    print(f"{words_count} words found in the document")
    
    keys = list(letters_count)
    
    for c in keys:
        if c.isalpha():
            print(f"The {c} character was found {letters_count[c]} times")


def count_letters(content):
    # A pythonic approach
    # col = Counter(content)
    # return dict(col)  

    # A more verbose approach
    chars = {}
    for c in content:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
    

with open("./books/frankenstein.txt") as f:
    file_contents = f.read()
    words_count = num_of_words(file_contents.lower())
    print(words_count)