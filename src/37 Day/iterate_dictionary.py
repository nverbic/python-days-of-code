''' 
    Day 37
    Write a program to iterate through a dictionary and print its keys and values

    Output:
    key 1: 15
    key 2: 17
    key 3: 13
    key 4: 4 
    key 5: 8
    key 6: 19
    key 7: 8
    key 8: 10
    key 9: 20
    key 10: 13
    key 11: 19
    key 12: 10
    key 13: 19
    key 14: 9
    key 15: 13
    key 16: 14
    key 17: 7
    key 18: 3
    key 19: 3
    key 20: 1
'''

import random

def create_dictionary(dictionary_size, start_key_value):
    ''' Create a dictionary of random numbers '''
    new_dict = {}

    for i in range(dictionary_size):
        key = f"key {start_key_value + i}"
        new_dict[key] =  random.randint(1, 20)

    return new_dict

def iterate_dict(dict_to_iterate):
    ''' Iterate through a dictionary and print keys and values '''
    for key, value in dict_to_iterate.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    # Create a dictionary that has 20 values and keys are starting from 1 (key 1 to key 20)
    radnom_dict = create_dictionary(20, 1)

    # Iterate through
    iterate_dict(radnom_dict)
