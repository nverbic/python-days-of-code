'''
    Day 30
    Create a function that finds the second smallest element in a list.

    Output:
    Sorted list:
    [2, 2, 2, 3, 7, 8, 8, 8, 10, 10]

    The second smallest number in the array is: 3
'''

import random

def second_smallest_num(num_list):
    ''' Find the second-smallest element in an array '''
    sec_smallest_num = None

    # Sort the list
    num_list.sort()

    # Loop the list backwards
    for i in range(len(num_list)):
        # Check if the compared items have different values
        if num_list[i] != num_list[i+1]:
            sec_smallest_num = num_list[i+1]
            break
    return sec_smallest_num

if __name__ == "__main__":
    # Array of random integers
    numbers_list = [random.randint(1, 10) for _ in range(10)]

    # Find the second smallest number
    second_smallest_number = second_smallest_num(numbers_list)

    print(f"Sorted list:\n{numbers_list}\n")
    if second_smallest_number:
        print(f"The second smallest number in the array is: {second_smallest_number}\n")
    else:
        print("All numbers in the array are the same.\n")
