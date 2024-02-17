'''
    Day 38
    Write a program to flatten a nested list
    
    Output:
    Nested list:
    [[1, 2, 3], [4, 5], [6, 7, 8, [5, 7, 8, [4, 6, 8]]]]
    Flatten list:
    [1, 2, 3, 4, 5, 6, 7, 8, 5, 7, 8, 4, 6, 8]
    '''

def flatten_nested_list(nested_list):
    ''' Flatten nested list '''
    flattened_list = []
    for item in nested_list:
        if type(item) == list: 
            flattened_list.extend(flatten_nested_list(item))
        else:
            # append item if it is not an iterable
            flattened_list.append(item)
    return flattened_list

if __name__ == "__main__":
    nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, [5, 7, 8, [4, 6, 8]]]]
    print(f"Nested list:\n{nested_list}")
    res = flatten_nested_list(nested_list)
    print(f"Flatten list:\n{res}")

