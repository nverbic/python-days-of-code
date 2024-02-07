'''
    Day 28
    Create a program that removes the nth element from a list.

    1. use the built-in del statement (imperative way)
    2. use the built-in pop() method
    3. use the built-in remove() method
    4. use slicing (pythonic way)
    5. use a list comprehension (pythonic way)
    6. use the built-in filter() function (functional way)
    7. use shifting and overwriting in-place (imperative way)

    Output:
    Original list
    [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]

    1. Use del() to remove the element with the index 5:
    [100, 101, 102, 103, 104, 106, 107, 108, 109]

    2. Use pop() to remove the element with the index 5:
    [100, 101, 102, 103, 104, 106, 107, 108, 109]

    3. Use remove() to remove the element with the index 5:
    [100, 101, 102, 103, 104, 106, 107, 108, 109]

    4. Use slicing to remove the element with the index 5:
    [100, 101, 102, 103, 104, 106, 107, 108, 109]

    5. Use list comprehension to remove the element with the index 5:
    [100, 101, 102, 103, 104, 106, 107, 108, 109]
'''

import random

def remove_elem_del(list_object, remove_index):
    ''' Remove elem using del() method '''
    del list_object[remove_index]

def remove_elem_pop(list_object, remove_index):
    '''Remove elem using pop() method '''
    list_object.pop(remove_index)

def remove_elem(list_object, remove_index):
    '''Remove elem using remove() method '''
    list_object.remove(remove_index)

def remove_elem_slicing(list_object, remove_index):
    '''Remove elem using slicing '''
    new_list = list_object[:remove_index] + list_object[remove_index+1:]
    return new_list

def remove_elem_list_comprehension(list_object, remove_index):
    '''Remove elem using list comprehension '''
    new_list = [list_object[i] for i in range(len(list_object)) if i != remove_index]
    return new_list


if __name__ == '__main__':
    # Create list
    numbers = list(range(100, 110))

    # Get random index
    item_index = random.randint(0, 10-1)
    print(f"Original list\n{numbers}")

    # Use shallow copy if the called method changes the original list
    numbers_copy = numbers.copy()
    # Remove element using del
    remove_elem_del(numbers_copy, item_index)
    print(f"\n1. Use del() to remove the element with the index {item_index}:\n{numbers_copy}")

    # Use shallow copy if the called method changes the original list
    numbers_copy = numbers.copy()
    # Remove element using pop
    remove_elem_pop(numbers_copy, item_index)
    print(f"\n2. Use pop() to remove the element with the index {item_index}:\n{numbers_copy}")

    # Use shallow copy if the called method changes the original list
    numbers_copy = numbers.copy()
    # Remove element using pop
    remove_elem_pop(numbers_copy, item_index)
    print(f"\n3. Use remove() to remove the element with the index {item_index}:\n{numbers_copy}")

    # Remove element using slicing
    returned_list = remove_elem_slicing(numbers, item_index)
    print(f"\n4. Use slicing to remove the element with the index {item_index}:\n{returned_list}")

    # Remove element using list comprehension
    returned_list = remove_elem_list_comprehension(numbers, item_index)
    print(f"\n5. Use list comprehension to remove the element with the index {item_index}:\n{returned_list}")
