''' #13 day challenge:
    Write a program to shuffle the elements of a list randomly

    Output:
    Original list:
    [9, 2, 9, 7, 8, 6, 2, 3, 9, 5]

    Shuffled with random.shuffle:
    [9, 7, 9, 2, 2, 6, 5, 8, 9, 3]
    Shuffled with random.sample:
    [8, 6, 9, 3, 2, 9, 5, 2, 7, 9]
    Shuffled with numpy.random.shuffle:
    [5, 7, 9, 2, 9, 9, 8, 6, 3, 2]

    Performances measured on a list of 100000 items, running code 1000 times.

    Total execution time using random.shuffle: 91.7363224 seconds
    Average time per execution: 0.0917363224 seconds

    Total execution time using random.sample: 94.4629884 seconds
    Average time per execution: 0.0944629884 seconds

    Total execution time using numpy.random.shuffle: 56.1840821 seconds
    Average time per execution: 0.0561840821 seconds
'''

import random
import timeit
import numpy as np

PREFORMANCE_SAMPLE = 100000
NUMBER_OF_RUNS = 1000

def shuffle(my_list):
    ''' Use random.shuffle '''
    random.shuffle(my_list)
    return my_list

def shuffle_sample(my_list):
    ''' Use random.sample '''
    shuffled_list = random.sample(my_list, len(my_list))
    return shuffled_list

def shuffle_numpy(my_list):
    ''' Use numpy.random.shuffle '''
    np.random.shuffle(my_list)
    return my_list

def wrapper_shuffle():
    my_list = [random.randint(0, 10) for _ in range(PREFORMANCE_SAMPLE)]
    return shuffle(my_list)

def wrapper_shuffle_sample():
    my_list = [random.randint(0, 10) for _ in range(PREFORMANCE_SAMPLE)]
    return shuffle_sample(my_list)

def wrapper_shuffle_numpy():
    my_list = [random.randint(0, 10) for _ in range(PREFORMANCE_SAMPLE)]
    return shuffle_numpy(my_list)

def measure_performance():
    ''' Measure the performance '''
    execution_time_shuffle = round(timeit.timeit(wrapper_shuffle, number=NUMBER_OF_RUNS), 10)
    average_time_shuffle = execution_time_shuffle / NUMBER_OF_RUNS
    execution_time_sample = round(timeit.timeit(wrapper_shuffle_sample, number=NUMBER_OF_RUNS), 10)
    average_time_sample = execution_time_sample / NUMBER_OF_RUNS
    execution_time_numpy = round(timeit.timeit(wrapper_shuffle_numpy, number=NUMBER_OF_RUNS), 10)
    average_time_numpy = execution_time_numpy / NUMBER_OF_RUNS

    print(f"\nPerformances measured on a list of {PREFORMANCE_SAMPLE} items, " \
          f"running code {NUMBER_OF_RUNS} times.\n")
    print(f"Total execution time using random.shuffle: {execution_time_shuffle} seconds")
    print(f"Average time per execution: {average_time_shuffle} seconds\n")
    print(f"Total execution time using random.sample: {execution_time_sample} seconds")
    print(f"Average time per execution: {average_time_sample} seconds\n")
    print(f"Total execution time using numpy.random.shuffle: {execution_time_numpy} seconds")
    print(f"Average time per execution: {average_time_numpy} seconds\n")

if __name__ == "__main__":
    my_list = [random.randint(0, 10) for _ in range(10)]
    print(f"Original list:\n{my_list}\n")
    result = shuffle(my_list)
    print(f"Shuffled with random.shuffle:\n{result}")
    result = shuffle_sample(my_list)
    print(f"Shuffled with random.sample:\n{result}")
    result = shuffle_numpy(my_list)
    print(f"Shuffled with numpy.random.shuffle:\n{result}")
    measure_performance()
