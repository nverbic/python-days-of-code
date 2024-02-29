'''
    Day 49
    Create a program that implements the bubble sort algorithm

    Output:
    Unsorted list:
    [9, 96, 87, 91, 6, 53, 80, 52, 97, 63, 72, 1, 21, 37, 57, 32, 59, 42, 95, 88]
    Sorted list:
    [1, 6, 9, 21, 32, 37, 42, 52, 53, 57, 59, 63, 72, 80, 87, 88, 91, 95, 96, 97]
'''
import random

def bubble_sort(unsorted_list):
    ''' Bubble sort algorithm '''
    swaped_positions = False

    while True:
        swaped_positions = False
        for i in range(0, len(unsorted_list)-1):
            if unsorted_list[i] > unsorted_list[i+1]:
                unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]
                swaped_positions = True
        if swaped_positions is False:
            break

if __name__ == "__main__":
    radnom_list = [random.randint(0, 100) for i in range(20)]
    print(f"Unsorted list:\n{radnom_list}")
    bubble_sort(radnom_list)
    print(f"Sorted list:\n{radnom_list}")
