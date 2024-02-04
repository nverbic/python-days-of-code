''''
    Day 25:
    Create a program to concatenate two lists.

    Output:
    Length of list_1: 1000000
    Length of list_2: 1000000
    Length of concatenated lists (using += operator): 2000000
    Length of list_1: 2000000
    Length of list_2: 1000000
    Length of concatenated lists (using itertools chain()): 3000000

'''

from itertools import chain

def concatenate_lists(list_1, list_2):
    ''' Concatenate two lists using += operator'''
    list_1 += list_2

def concatenate_lists_chain(list_1, list_2):
    ''' Concatenate two lists using chain() '''
    concatenated_list = list(chain(list_1, list_2))
    return concatenated_list

if __name__ == "__main__":
    list_1 = [i for i in range(10**6)]
    list_2 = [i for i in range(10**6, 2*10**6)]

    print(f"Length of list_1: {len(list_1)}")
    print(f"Length of list_2: {len(list_2)}")

    # Concatenate lists using += operator
    concatenate_lists(list_1, list_2)
    print(f"Length of concatenated lists (using += operator): {len(list_1)}")

    print(f"Length of list_1: {len(list_1)}")
    print(f"Length of list_2: {len(list_2)}")

    # Concatenate lists using itertools chain() method
    concatenated_list = concatenate_lists_chain(list_1, list_2)
    print(f"Length of concatenated lists (using itertools chain()): {len(concatenated_list)}")
