''' #5 day challenge:
    Write a program to find the maximum and minimum values in a list.

    Output:
    Generate list of floats using python random module

    The list:
    [13.26, 10.01, 6.37, 17.86, 15.17, 9.11, 9.05, 8.9, 14.72, 17.25]

    Min value using min(): 6.37
    Max value using max(): 17.86
    Min value using numpy min(): 6.37
    Max value using numpy max(): 17.86

    Generate list of floats using numpy random module

    The list:
    [11.48, 5.87, 19.43, 8.67, 14.63, 17.67, 10.93, 3.62, 15.57, 14.9]

    Min value using min(): 3.62
    Max value using max(): 19.43
    Min value using numpy min(): 3.62
    Max value using numpy max(): 19.43
'''
import random
import numpy as np

def min_max_items(list):
    '''Find min and max values in the list '''
    print(f"\nThe list:\n{list}\n")
    print(f"Min value using min(): {min(list)}")
    print(f"Max value using max(): {max(list)}")
    print(f"Min value using numpy min(): {np.min(list)}")
    print(f"Max value using numpy max(): {np.max(list)}")

if __name__ == "__main__":
    print("\nGenerate a list of floats using python random module.")
    # Generate a list
    list = [round(random.uniform(1.0, 20.0), 2) for _ in range(10)]
    # Find min/max
    min_max_items(list)

    print("\nGenerate a list of floats using numpy random module.")
    # Generate a list
    list_np = np.random.uniform(1.0, 20.0, 10)
    # Round to 2 decimal places
    list_np = np.round(list_np, 2).tolist()
    # Find min/max
    min_max_items(list_np)
