'''
    Day 59
    Create a function that checks if a number is a perfect square

    Output:
    Number 1 is perfect square: True
    Number 2 is perfect square: False
    Number 3 is perfect square: False
    Number 4 is perfect square: True
    Number 5 is perfect square: False
    Number 6 is perfect square: False
    Number 7 is perfect square: False
    Number 8 is perfect square: False
    Number 9 is perfect square: True
'''

import math

def is_perfect_square(num):
    ''' Check if number is perfect square '''
    result = math.sqrt(num)
    return result.is_integer()

if __name__ == "__main__":
    for num in range(1, 10):
        print(f"Number {num} is perfect square: {is_perfect_square(num)}")
