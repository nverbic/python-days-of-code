'''
    Day 41
    Write a program that uses recursion to generate all permutations of a list

    Output:
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
'''

def list_permutations(list_arg):
    ''' Find all permutations of the list '''

    # If only one elem in the list, return list
    if len(list_arg) == 1:
        return [list_arg]

    permutations = []

    for i, item in enumerate(list_arg):
        # Create new list without current item
        list_without_item = list_arg[:i] + list_arg[i+1:]

        # Generate permutations where current item is the first
        # item in the list
        for permutation in list_permutations(list_without_item):
            permutations.append([item] + permutation)
    return permutations


if __name__ == "__main__":
    radnom_list = [1,2,3]
    print(list_permutations(radnom_list))
