'''
    Day 20
    Write a function that takes a list of numbers and returns a new list containing only the even numbers.
    
    Output:
    List of numbers:
    [6, 26, 37, 46, 49, 57, 58, 60, 60, 61, 66, 71, 73, 74, 76, 78, 88, 90, 93, 94]

    Even numbers:
    [6, 26, 46, 58, 60, 60, 66, 74, 76, 78, 88, 90, 94]
    '''

import random

def get_even_numbers(numbers_list):
    ''' From the list of numbers create a new list containing only even numbers'''
    even_num = []

    for item in numbers_list:
        if not item % 2:
            even_num.append(item)
    return even_num

if __name__ == "__main__":
    random_numbers = [random.randint(1, 100) for _ in range(20)]
    random_numbers.sort()
    even_numbers = get_even_numbers(random_numbers)
    print(f"List of numbers:\n{random_numbers}\n")
    print(f"Even numbers:\n{even_numbers}\n")
