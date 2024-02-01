''''
    Day 22
    Create a program to find the second-largest element in a list

    Output:
    [9, 114, 137, 168, 170, 200, 243, 304, 304, 316, 
     326, 337, 361, 581, 671, 744, 818, 881, 948, 977]
    The second largest number in the array is: 948
'''

import random

def second_largest_num(num_list):
    ''' Find the second-largest element in an array '''
    sec_largest_num = None

    # Sort the list
    num_list.sort()

    # Loop the list backwards
    for i in range(len(num_list)-1,-1,-1):
        # Check if the compared items have different values
        if num_list[i] != num_list[i-1]:
            sec_largest_num = num_list[i-1]
            break
    return sec_largest_num

if __name__ == "__main__":
    # Array of random integers
    numbers_list = [random.randint(1, 1000) for _ in range(20)]

    # Find the second largest number
    second_largest_number = second_largest_num(numbers_list)

    print(f"{numbers_list}")
    if second_largest_number:
        print(f"The second largest number in the array is: {second_largest_number}")
    else:
        print("All numbers in the array are the same.")
