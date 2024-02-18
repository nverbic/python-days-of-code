'''
    Day 39
    Write a program to find the most common words in a text file

    Output:
    Total number of words in the online book Alice's Adventures in Wonderland, by Lewis Carroll is: 

    The first 50 most common words in the book are:
    the : 1700
    and : 866
    to : 800
    a : 676
    of : 611
    I : 546
    it : 543
    she : 513
    said : 458
    in : 417
    you : 413
    Alice : 399
    was : 358
    that : 299
    as : 256
    her : 245
    with : 223
    t : 217
    at : 216
    s : 210
    on : 200
    all : 193
    had : 178
    for : 162
    not : 162
    be : 162
    this : 156
    or : 147
    very : 140
    but : 136
    they : 133
    is : 127
    little : 127
    so : 126
    The : 125
    out : 114
    he : 107
    about : 101
    one : 100
    what : 99
    up : 99
    down : 99
    his : 95
    them : 88
    know : 88
    were : 85
    Project : 84
    Gutenberg : 84
    like : 84
    have : 83
'''
from collections import Counter
import re

def most_common_words(text):
    ''' Find the most common words in the text '''
    words = re.findall(r"([a-z0-9'-]+)", text, re.IGNORECASE)
    print(f"Total number of all words in the online book Alice's Adventures in Wonderland, by Lewis Carol is: {len(words)}\n")

    count_words = Counter(words)

    print("The first 50 most common words in the book Alice's Adventures in Wonderland, by Lewis Carol:")
    for word, count in count_words.most_common(50):
        print(f"{word} : {count}")

if __name__ == "__main__":
    INPUT_FILE_PATH = ".\\src\\39 Day\\Alices Adventures In Wonderland.txt"
    with open(INPUT_FILE_PATH, 'r', encoding='utf-8') as input_file:
        e_book = input_file.read()
    most_common_words(e_book)

