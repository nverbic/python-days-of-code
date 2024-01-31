'''
    Day 21
    Create a program to remove a specific element from a set.

    Output:
    Set of numbers:
    {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}
    Removed from the set 15:
    {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19}
'''

import random

def remove_item(rand_set, num):
    ''''Remove item from the set '''
    rand_set.discard(num)
    return rand_set

if __name__ == "__main__":
    SET_LENGTH = 20

    # Create set
    random_set = set(range(SET_LENGTH))
    print(f"Set of numbers:\n{random_set}")

    # Get random number from the set range
    item_to_remove = random.randint(0, SET_LENGTH-1)

    # Remove the number
    new_set = remove_item(random_set, item_to_remove)
    print(f"Removed {item_to_remove} from the set:\n{new_set}")
