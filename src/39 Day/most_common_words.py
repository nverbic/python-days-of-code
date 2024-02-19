'''
    Day 39
    Write a program to find the most common words in a text file

    Output:
    Total number of words in the online book Alice's Adventures in Wonderland, by Lewis Carroll is: 

    The first 50 most common words in the book Alice's Adventures in Wonderland, by Lewis Carol:
    the : 1834
    and : 935
    to : 807
    a : 694
    of : 634
    it : 543
    she : 541
    said : 462
    you : 440
    in : 432
    i : 411
    alice : 386
    was : 359
    that : 295
    as : 273
    her : 248
    with : 228
    at : 225
    on : 204
    all : 199
    this : 179
    for : 179
    had : 178
    but : 174
    not : 173
    be : 164
    or : 154
    so : 153
    very : 145
    what : 137
    they : 132
    is : 130
    little : 129
    he : 123
    if : 118
    out : 114
    one : 105
    down : 103
    about : 102
    up : 101
    no : 100
    gutenberg : 97
    do : 97
    his : 96
    then : 94
    project : 88
    them : 88
    know : 88
    have : 87
    were : 85
'''
from collections import Counter
import re

def most_common_words(text):
    ''' Find the most common words in the text '''
    words = re.findall(r"([a-z0-9-'’]+)", text, re.IGNORECASE)

    # Convert each word to lowercase
    words_lower_case = [word.lower() for word in words]
    print(f"Total number of all words in the online book Alice's Adventures in Wonderland, by Lewis Carol is: {len(words_lower_case)}\n")

    count_words = Counter(words_lower_case)

    print("The first 50 most common words in the book Alice's Adventures in Wonderland, by Lewis Carol:")
    for word, count in count_words.most_common(50):
        print(f"{word} : {count}")

if __name__ == "__main__":
    INPUT_FILE_PATH = ".\\src\\39 Day\\Alices Adventures In Wonderland.txt"
    with open(INPUT_FILE_PATH, 'r', encoding='utf-8') as input_file:
        e_book = input_file.read()
    most_common_words(e_book)
