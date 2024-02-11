'''
    Day 32
    Create a function that calculates the average of a list of numbers.

    Output:
    List of numbers:
    [1, 4, 2, 7, 6, 9, 7, 3, 3, 8]

    The average value calculated suing sum() and len(): 5.0

    The average value calculated using statistics mean(): 5
'''

import random
import statistics

def calc_average(num_list):
    ''' Calculate the average value of a list of numbers '''
    avg  = sum(num_list)/len(num_list)
    return avg

def calc_average_statistics(num_list):
    ''' Calculate the average value of a list of numbers using statistics library'''
    avg = statistics.mean(num_list)
    return avg


if __name__ == "__main__":
    # Array of random integers
    numbers_list = [random.randint(1, 10) for _ in range(10)]
    print(f"List of numbers:\n{numbers_list}\n")

    # Find the average value
    average_value = calc_average(numbers_list)
    print(f"The average value calculated suing sum() and len(): {average_value}\n")

        # Find the average value, use statistics lib
    average_value_stat = calc_average_statistics(numbers_list)
    print(f"The average value calculated using statistics mean(): {average_value_stat}\n")

