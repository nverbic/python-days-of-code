'''
    Day 35
    Write a simple unit test for a function that adds two numbers

    Output:
    15 + 33 = 48
    40.5 + 24.81 = 65.31
    Note: Addition of strings is not supported in this method
    a + b = None
'''
import random

def add_numbers(num1, num2):
    ''' Add two numbers '''
    res = None
    try:
        if type(num1) == str and type(num2) == str:
            print("Note: Addition of strings is not supported in this method")
            return res
        res = num1 + num2
    except TypeError as e:
        print(f"Error {num1} + {num2}: {e}")
    return res


if __name__ == "__main__":
    # integer
    num_int_1 = random.randint(0, 50)
    num_int_2 = random.randint(0, 50)
    result = add_numbers(num_int_1, num_int_2)
    print(f"{num_int_1} + {num_int_2} = {result}")
    # float
    num_float_1 = round(random.uniform(0, 50), 2)
    num_float_2 = round(random.uniform(0, 50), 2)
    result = add_numbers(num_float_1, num_float_2)
    print(f"{num_float_1} + {num_float_2} = {result}")
    # strings
    char_1 = "a"
    char_2 = "b"
    result = add_numbers(char_1, char_2)
    print(f"{char_1} + {char_2} = {result}")
