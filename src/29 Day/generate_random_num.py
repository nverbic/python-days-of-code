'''
    Day 29
    Create a function that generates a random number between a given range

    Output:

    Randomly generated number in range 0, 100:
    15
'''

import random

def generate_random_num(range_arg):
    ''' Generate random number using random library '''
    random_num = random.randint(range_arg[0], range_arg[1])
    return random_num

if __name__ == "__main__":
    range_of_nums = [0, 100]
    print(f"Randomly generated number in range {range_of_nums[0]}, {range_of_nums[1]}:\n" \
          f"{generate_random_num(range_of_nums)}")
