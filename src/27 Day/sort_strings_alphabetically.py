'''
    Day 27
    Create a program that sorts a list of strings alphabetically.

    Output:

    Unsorted list of strings (first 20):
    The
    Project
    Gutenberg
    eBook
    of
    Alice's
    Adventures
    in
    Wonderland
    This
    ebook
    is
    for
    the
    use
    anyone
    anywhere
    United
    States
    and

    List sorted alphabetically (first 20):
    -
    0
    000
    1
    11
    1500
    2
    20
    2001
    2008
    2021
    27
    3
    30
    4
    5
    50
    501
    596-1887
    6

    Unsorted list of strings (first 20):
    The Project Gutenberg eBook of Alice's Adventures in Wonderland

    This ebook is for the use of anyone anywhere in the United States and
    most other parts of the world at no cost and with almost no restrictions
    whatsoever. You may copy it, give it away or re-use it under the terms
    of the Project Gutenberg License included with this ebook or online
    at www.gutenberg.org. If you are not located in the United States,
    you will have to check the laws of the country where you are located
    before using this eBook.

    Title: Alice's Adventures in Wonderland


    Author: Lewis Carroll

    Release date: June 27, 2008 [eBook #11]
    Most recently updated: March 30, 2021

    Language: English


    List sorted alphabetically (first 20):
    ($1 to $5,000) are particularly important to maintaining tax exempt
    (Alice began to say “I once tasted—” but checked herself hastily, and
    (Before she had this fit)
    (Dinah was the cat.) “I hope they’ll remember her saucer of milk at
    (In which the cook and the baby joined):
    (We know it to be true):
    (and she tried to curtsey as she spoke—fancy _curtseying_ as you’re
    (for when she looked down at her feet, they seemed to be almost out of
    (or any other work associated in any way with the phrase “Project
    (she had kept a piece of it in her pocket) till she was about a foot
    (she knew) to the confused clamour of the busy farm-yard—while the
    (she was obliged to say “creatures,” you see, because some of them were
    (trademark/copyright) agreement. If you do not agree to abide by all
    (www.gutenberg.org), you must, at no additional cost, fee or expense
    (“I only wish it was,” the March Hare said to itself in a whisper.)
    *      *      *      *      *      *
    *      *      *      *      *      *
    *      *      *      *      *      *
    *      *      *      *      *      *      *
    *      *      *      *      *      *      *

'''

import re
from collections import Counter

INPUT_FILE_PATH = ".\\src\\27 Day\\Alices Adventures In Wonderland.txt"
SORTED_WORDS_FILE_PATH = ".\\src\\27 Day\\Sorted_Words.txt"
SORTED_LINES_FILE_PATH = ".\\src\\27 Day\\Sorted_Lines.txt"

def get_list_of_words(text):
    ''' Get a list of words from the text
    '''
    # Get all the words from the text
    words = re.findall(r"([a-z0-9'-]+)", text, re.IGNORECASE)

    # Create Counter object for the words used in the text
    words_counter = Counter(words)

    # Get the list of words from the Counter object (without duplicates)
    return(list(words_counter.keys()))


def sort_list_alphabetically(list_of_strings, file_path):
    ''' Sort the list alphabetically
    '''
    # Print the first 20 lines of text
    print("\nUnsorted list of strings (first 20):")
    for i in range(0, 20):
        print(list_of_strings[i])

    # Sort list alphabet.
    list_of_strings.sort()

    # Iterate over a copy of the list while modifying the original list
    for item in list_of_strings[:]:
        # Remove empty items which are at the beginning of the sorted list
        if item == "":
            list_of_strings.remove(item)
        else:
            break

    # Print the first 20 lines of text after sorting
    print("\nList sorted alphabetically (first 20):")
    for i in range(0, 20):
        print(list_of_strings[i])

    with open(file_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(item + '\n' for item in list_of_strings)


def sort_list_of_words():
    ''' Sort a list of words from the text alphabetically 
    '''
    with open(INPUT_FILE_PATH, 'r', encoding='utf-8') as input_file:
        text = input_file.read()

    # Get a list of words from the file
    words_list = get_list_of_words(text)

    # Sort the list alphabetically
    sort_list_alphabetically(words_list, SORTED_WORDS_FILE_PATH)


def sort_list_of_text_lines():
    ''' Sort a list of lines from the text alphabetically
     '''
    # Read the input file (as a string and as a list of strings)
    with open(INPUT_FILE_PATH, 'r', encoding='utf-8') as input_file:
        text_lines = input_file.readlines()

    # Prepare the list: remove leading whitepsaces from the list
    text_lines = [line.strip() for line in text_lines]

    # Sort the list alphabetically
    sort_list_alphabetically(text_lines, SORTED_LINES_FILE_PATH)


if __name__ == "__main__":
    sort_list_of_words()
    sort_list_of_text_lines()
