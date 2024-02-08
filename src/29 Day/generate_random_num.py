'''
    Day 29
    Create a function that generates a random number between a given range

    Output:

    Randomly generated number (random.randint()) in range 0, 100:
    31
    Randomly generated number (random.uniform()) in range 0, 100:
    42.73
'''

import random

def generate_random_num(range_arg):
    ''' Generate random number using random.randint() '''
    random_num = random.randint(range_arg[0], range_arg[1])
    return random_num

def generate_random_num_unifrom(range_arg):
    ''' Generate random number using random.uniform() '''
    random_num = round(random.uniform(range_arg[0], range_arg[1]), 2)
    return random_num

if __name__ == "__main__":
    range_of_nums = [0, 100]
    print(f"Randomly generated number (random.randint()) in range {range_of_nums[0]}, {range_of_nums[1]}:\n" \
          f"{generate_random_num(range_of_nums)}")
    print(f"Randomly generated number (random.uniform()) in range {range_of_nums[0]}, {range_of_nums[1]}:\n" \
          f"{generate_random_num_unifrom(range_of_nums)}")
