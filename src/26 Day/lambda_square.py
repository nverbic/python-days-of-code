''' 
    Day 26
    Create a program that uses a lambda function to square each element of a list. 
    
    Output:
    List:
    [1, 7, 3, 4, 6, 9, 1, 2, 4, 2]
    List of squares:
    [1, 49, 9, 16, 36, 81, 1, 4, 16, 4]
    '''

import random

def square_list_items(input_list):
    ''' Square elements of the list '''
    squared_list = list(map(lambda item: item**2, input_list))
    return squared_list

if __name__ == "__main__":
    numbers_list = [random.randint(1, 10) for _ in range(10)]
    print(f"Input list:\n{numbers_list}")
    squared_list = square_list_items(numbers_list)
    print(f"List of squares:\n{squared_list}")
