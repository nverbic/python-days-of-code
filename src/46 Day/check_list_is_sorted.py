'''
    Day 45
    Write a function to check if a given list is sorted

    Output:
    Check if the list is sorted
    [87, 21, 68, 99, 79, 86, 91, 84, 75, 29]
    List is not sorted

    Check if the list is sorted
    [69, 15, 39, 18, 26, 86, 17, 44, 67, 51]
    List is not sorted

    Check if the list is sorted
    [11, 26, 41, 53, 49, 74, 36, 23, 3, 59] 
    List is not sorted

    Check if the list is sorted
    [1, 17, 19, 25, 37, 75, 83, 87, 88, 94]
    List is sorted

    Check if the list is sorted
    [4, 15, 56, 59, 70, 76, 82, 82, 94, 95]
    List is sorted

    Check if the list is sorted
    [28, 33, 35, 38, 38, 41, 65, 84, 92, 97]
    List is sorted
'''

import random

def is_list_sorted(list_arg):
    ''' Check is list sorted '''
     # Compare original list with the sorted list
    if list_arg == sorted(list_arg):
        return True
    return False

if __name__ == "__main__":
    for i in range(6):
        if i < 3:
            # Test with unsorted list of integers
            random_list = [random.randint(1, 100) for i in range(10)]
        else:
            # Test with sorted list of integers
            random_list = sorted([random.randint(1, 100) for i in range(10)])

        print(f"Check if the list is sorted\n{random_list}")

        # Check the list is sorted
        is_sorted = is_list_sorted(random_list)

        if is_sorted:
            print("List is sorted\n")
        else:
            print("List is not sorted\n")
