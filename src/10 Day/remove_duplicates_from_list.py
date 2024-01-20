'''  #10 day challenge:
    Write a program to remove duplicates from a list. 
    
    Output:
    Initial list:
    [0, 1, 1, 4, 5, 7, 9, 11, 11, 11, 12, 14, 15, 15, 18, 19, 19, 20, 20, 20]
    Duplicates removed using for loop:
    [0, 1, 4, 5, 7, 9, 11, 12, 14, 15, 18, 19, 20]
    Duplicates removed using set():
    [0, 1, 4, 5, 7, 9, 11, 12, 14, 15, 18, 19, 20]
    '''

import random

def remove_duplicates(original_list):
    ''' Remove duplicates from a list using for loop '''
    duplicates_removed = []

    for item in original_list:
        if item not in duplicates_removed:
            duplicates_removed.append(item)

    return duplicates_removed

def remove_duplicates_using_set(original_list):
    ''' Remove duplicates from a list using set '''
    duplicates_removed = list(set(original_list))
    return duplicates_removed

if __name__ == '__main__':
    random_list = [random.randint(0, 20) for _ in range(20)]
    random_list.sort()

    print(f"Initial list:\n{random_list}")
    duplicates_removed_list_1 = remove_duplicates(random_list)
    print(f"Duplicates removed using for loop:\n{duplicates_removed_list_1}")
    duplicates_removed_list_2 = remove_duplicates_using_set(random_list)
    print(f"Duplicates removed using set():\n{duplicates_removed_list_2}")
