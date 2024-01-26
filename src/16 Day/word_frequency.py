''''
    Day 16:
    Write a function that counts the frequency of each word in a sentence.

    Output:
    Total number of words in the online book Pride and Prejudice, by Jane Austin is: 131404

    The first 50 most common words in the book are:
    the : 4516
    to : 4310
    of : 3932
    and : 3628
    her : 2189
    I : 2107
    a : 2024
    in : 1944
    was : 1874
    that : 1587
    not : 1492
    she : 1417
    it : 1334
    be : 1272
    his : 1218
    you : 1216
    as : 1180
    had : 1158
    he : 1120
    with : 1108
    for : 1089
    is : 922
    have : 875
    Mr : 806
    at : 781
    him : 773
    by : 706
    but : 704
    on : 704
    s : 677
    all : 647
    Elizabeth : 644
    my : 606
    so : 595
    which : 568
    were : 564
    been : 536
    could : 522
    from : 502
    very : 488
    they : 484
    would : 480
    no : 459
    me : 458
    them : 445
    this : 433
    Darcy : 429
    their : 420
    your : 420
    will : 418

    The usage count of all the words from the book is saved in the file WordsCount.txt
'''
from collections import Counter, OrderedDict
import re

def word_frequency(text):
    OUTPUT_FILE_PATH = ".\\src\\16 Day\\WordsCount.txt"

    words = re.findall(r"([a-z0-9'-]+)", text, re.IGNORECASE)
    print(f"Total number of words in the online book Pride and Prejudice, by Jane Austin is: {len(words)}\n")

    count_words = Counter(words)

    print("The first 50 most common words in the book are:")
    for word, count in count_words.most_common(50):
        print(f"{word} : {count}")

    print("\nThe usage count of all the words from the book is saved in the file WordsCount.txt\n")
    with open(OUTPUT_FILE_PATH, 'w', encoding='utf-8') as output_file:
        for key, value  in count_words.most_common():
            output_file.write(f"{key} : {value}\n")

if __name__ == "__main__":
    INPUT_FILE_PATH = ".\\src\\16 Day\\Pride and prejudice.txt"
    with open(INPUT_FILE_PATH, 'r', encoding='utf-8') as input_file:
        text = input_file.read()
    word_frequency(text)
