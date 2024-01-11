''' #1 day challenge:
    Create a program that swaps the values of two variables.

    Output:
    Swap the values:
    var_1 = 5
    var_2 = 10

    Values swapped:
    var_1 = 10
    var_2 = 5

    Swap again:
    var_1 = 5
    var_2 = 10
'''

def swap_vars(a, b):
    '''' Swap two variables '''
    tmp = a
    a = b
    b = tmp
    return a,b

if __name__ == '__main__':
    var_1 = 5
    var_2 = 10
    print(f"Swap the values:\nvar_1 = {var_1}\nvar_2 = {var_2}")
    var_1, var_2 = swap_vars(var_1, var_2)
    print(f"\nValues swapped:\nvar_1 = {var_1}\nvar_2 = {var_2}")
    var_1, var_2 = var_2, var_1
    print(f"\nSwap again:\nvar_1 = {var_1}\nvar_2 = {var_2}")
