'''
    Day 51
    Create a program that counts the occurrences of each word in a text file

    Output:
    Total number of all words in the text file is: 20488

    50 most common words from the text file:
    the : 770
    and : 642
    i : 447
    to : 417
    of : 403
    you : 350
    a : 339
    in : 309
    with : 228
    is : 213
    not : 200
    my : 200
    that : 200
    this : 194
    me : 179
    for : 170
    it : 150
    or : 140
    your : 131
    as : 128
    will : 127
    but : 125
    be : 124
    do : 124
    thou : 116
    so : 116
    all : 107
    have : 105
    love : 104
    lysander : 101
    her : 101
    demetrius : 99
    gutenberg : 98
    hermia : 98
    by : 96
    he : 96
    no : 95
    are : 90
    project : 89
    his : 89
    if : 88
    we : 84
    on : 83
    shall : 74
    what : 73
    helena : 71
    from : 71
    here : 68
    theseus : 67
    thy : 65
'''

from collections import Counter
import re

INPUT_FILE = ".\\src\\51 Day\\A_midsummer_nights_dream.txt"

def word_frequency(text):
    ''' Count the number of occurrences of each word in a text file'''
    text_lower_case = text.lower()

    words_list = re.findall(r"([a-z0-9-'’]+)", text_lower_case)
    print(f"Total number of all words in the text file is: {len(words_list)}\n")

    words_counter = Counter(words_list)

    print("Print the 50 most common words from the text file:")
    for word, count in words_counter.most_common(50):
        print(f"{word} : {count}")


if __name__ == "__main__":
    with open(INPUT_FILE, 'r', encoding='utf-8') as text_file:
        e_book = text_file.read()

    # Count the word's frequency
    word_frequency(e_book)
