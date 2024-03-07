'''
    Day 57
    Create a function that returns the key with the maximum value in a dictionary

    Output:
    key : value => key 1 : 3
    key : value => key 2 : 34
    key : value => key 3 : 15
    key : value => key 4 : 37
    key : value => key 5 : 32
    key : value => key 6 : 8
    key : value => key 7 : 24
    key : value => key 8 : 11
    key : value => key 9 : 35
    key : value => key 10 : 11

    Max value:
    key : value => ('key 4', 37)
'''

import random

def create_dictionary(dictionary_size, start_key_value):
    ''' Create a dictionary of random numbers '''
    new_dict = {}

    for i in range(dictionary_size):
        key = f"key {start_key_value + i}"
        new_dict[key] =  random.randint(1, 50)

    return new_dict


def dict_find_max_value(dictionary_arg):
    '''  Find the dictionary key with the maximum value '''
    max_key, max_value = next(iter(dictionary_arg.items()))

    for key, value in dictionary_arg.items():
        if value > max_value:
            max_key, max_value = key, value

    return max_key

if __name__ == "__main__":
    # Create a dictionary of 10 random values
    dict_1 = create_dictionary(10, 1)

    # Find the key with the maximum value
    key_of_max_value = dict_find_max_value(dict_1)

    for key, value in dict_1.items():
        print(f"key : value => {key} : {value}")
    print(f"\nMax value:\nkey : value => {key_of_max_value, dict_1[key_of_max_value]}\n")
