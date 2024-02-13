'''
    Day 34
    Write a Python program to merge two dictionaries

    Output:
    First dictionary:
    {'key 1': 5, 'key 2': 12, 'key 3': 10, 'key 4': 9, 'key 5': 6,
     'key 6': 18, 'key 7': 14, 'key 8': 3, 'key 9': 3, 'key 10': 10}

    Second dictionary:
    {'key 8': 17, 'key 9': 5, 'key 10': 8, 'key 11': 6, 'key 12': 15,
     'key 13': 15, 'key 14': 11, 'key 15': 12, 'key 16': 8, 'key 17': 18}

    Merged dictionaries:
    {'key 1': 5, 'key 2': 12, 'key 3': 10, 'key 4': 9, 'key 5': 6, 'key 6': 18,
     'key 7': 14, 'key 8': 17, 'key 9': 5, 'key 10': 8, 'key 11': 6, 'key 12': 15,
      key 13': 15, 'key 14': 11, 'key 15': 12, 'key 16': 8, 'key 17': 18}
'''

import random

def merge_dictionaries(dict1, dict2):
    ''' Merge two dictionaries using update() method '''
    dict1.update(dict2)

def create_dictionary(dictionary_size, start_key_value):
    ''' Create a dictionary of random numbers '''
    new_dict = {}

    for i in range(dictionary_size):
        key = f"key {start_key_value + i}"
        new_dict[key] =  random.randint(1, 20)

    return new_dict


if __name__ == "__main__":
    # Create a dictionary that has 10 values and keys are starting from 1 (key 0 to key 10)
    dict_1 = create_dictionary(10, 1)

    # Create a dictionary that has 10 values and keys are starting from 1 (key 8 to key 17)
    dict_2 = create_dictionary(10, 8)
    print(f"First dictionary:\n{dict_1}\n")
    print(f"Second dictionary:\n{dict_2}\n")

    # Merge dictionaries
    merge_dictionaries(dict_1, dict_2)

    # Merged dictionary has 17 values becasue if both dictionaries contain the same key and
    # different values, then the final output will overwrite the value of the latter dictionary.
    print(f"Merged dictionaries:\n{dict_1}")
