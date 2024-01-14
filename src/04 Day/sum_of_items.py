''' #4 day challenge:
    Write a program to find the sum of all elements in a list.

    Output:
    The list:
    [9, 9, 1, 7, 10, 5, 10, 10, 4, 10]

    The sum of all elements is 75
'''
import random

def sum_items(list):
    ''' Sum of the items in a list '''
    sum = 0
    for item in list:
        sum = sum + item
    print(f"\nThe list:\n{list}\n")
    print(f"The sum of all elements is {sum}")

if __name__ == "__main__":
    list = [random.randint(1, 10) for _ in range(10)]
    sum_items(list)

