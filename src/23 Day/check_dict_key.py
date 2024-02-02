'''
    Day 23
    Write a program that checks if a key exists in a dictionary.

    Output:
    Key "Darcy" found in the dictionary.
    Key "Arcy" is not found in the dictionary.
'''
from collections import Counter
import re

def check_dictionary_key(search_dict, search_key):
    ''' Search the dictionary for the desired key '''
    found_key = search_key in search_dict
    return found_key

if __name__ == "__main__":
    book_content = ""
    INPUT_FILE_PATH = ".\\src\\23 Day\\Pride and prejudice.txt"
    with open(INPUT_FILE_PATH, 'r', encoding='utf-8') as input_file:
        book_content = input_file.read()

    if book_content != "":
        # Find all the words
        words_in_book = re.findall(r"([a-z0-9'-]+)", book_content, re.IGNORECASE)

        # Create Counter object
        count_words = Counter(words_in_book)

        # Create dictionary with words:count items
        dict_count_words = dict(count_words)

        # Define keys to search for
        search_keys = ["Darcy", "Arcy"]

        # Check if keys exist in the dictionary
        for item in search_keys:
            result = check_dictionary_key(dict_count_words, item)
            if result:
                print(f"Key \"{item}\" found in the dictionary.")
            else:
                print(f"Key \"{item}\" is not found in the dictionary.")
