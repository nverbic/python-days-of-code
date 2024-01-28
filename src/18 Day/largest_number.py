''' 
    Day 18:
    Create a program to find the largest among three numbers. 
    
    Output:
    [61, 38, 18]
    Find the largest number, using iterate: 61

    [6, 1, 66]
    Find the largest number, using iterate: 66

    [82, 76, 46]
    Find the largest number, using iterate: 82

    [52, 61, 32]
    Find the largest number, using iterate: 61

    [27, 93, 57]
    Find the largest number, using iterate: 93

    [98, 30, 51]
    Find the largest number, using list sort: 98

    [24, 88, 62]
    Find the largest number, using list sort: 88

    [49, 34, 45]
    Find the largest number, using list sort: 49

    [84, 9, 29]
    Find the largest number, using list sort: 84

    [72, 66, 100]
    Find the largest number, using list sort: 100
'''

import random

def largest_number_sort(numbers):
    ''' Find the largest among three numbers, use sort() '''
    numbers.sort()
    return numbers[len(numbers)-1]

def largest_number_iterate(numbers):
    ''' Find the largest among three numbers, use iterate '''
    largest_num = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] > largest_num:
            largest_num = numbers[i]

    return largest_num


if __name__ == "__main__":
    # Solution with for loop (iterative)
    for i in range(5):
        numbers_iter = [random.randint(1, 100) for x in range(3)]
        print(f"\n{numbers_iter}")
        largest_num = largest_number_iterate(numbers_iter)
        print(f"Find the largest number, using iterate: {largest_num}")

    # Solution with list sort() method
    for i in range(5):
        numbers_sort = [random.randint(1, 100) for x in range(3)]
        print(f"\n{numbers_sort}")
        largest_num = largest_number_sort(numbers_sort)
        print(f"Find the largest number, using list sort: {largest_num}")
    