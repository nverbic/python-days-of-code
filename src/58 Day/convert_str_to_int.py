'''
    Day 58
    Create a function that converts a string to an integer and handles ValueError

    Output:
    Converted string "1979", <class 'str'> to an integer 1979, <class 'int'>
    Error: Cannot convert string "Convert text", <class 'str'> to an integer. 
    Error: Cannot convert string "A", <class 'str'> to an integer.
    Error: Cannot convert string "2 + 5", <class 'str'> to an integer.
    Evaluate string expression "1979", <class 'str'> to an integer 1979, <class 'int'>
    Error: Cannot evaluate string expression "Convert text", <class 'str'> to an integer.
    Error: Cannot evaluate string expression "A", <class 'str'> to an integer.
    Evaluate string expression "2 + 5", <class 'str'> to an integer 7, <class 'int'>
'''

def str_to_int(str_input):
    ''' Convert a string to an integer using method int() '''
    try:
        int_value = int(str_input)
        print(f"Converted string \"{str_input}\", {type(str_input)} to an integer "\
              f"{int_value}, {type(int_value)}")
        return int_value
    except ValueError:
        print(f"Error: Cannot convert string \"{str_input}\", {type(str_input)} to an integer. ")
        return None


def str_to_int_eval(str_input):
    ''' Convert a string to an integer using method eval() '''
    try:
        int_value = eval(str_input)
        print(f"Evaluate string expression \"{str_input}\", {type(str_input)} to an integer "\
              f"{int_value}, {type(int_value)}")
        return int_value
    except Exception:
        print(f"Error: Cannot evaluate string expression \"{str_input}\", "\
              f"{type(str_input)} to an integer. ")
        return None


if __name__ == "__main__":
    test_string_1 = "1979"
    test_string_2 = "Convert text"
    test_string_3 = "A"
    test_string_4 = "2 + 5"

    # Convert to integer using int()
    str_to_int(test_string_1)
    str_to_int(test_string_2)
    str_to_int(test_string_3)
    str_to_int(test_string_4)

    # Convert to integer using eval()
    str_to_int_eval(test_string_1)
    str_to_int_eval(test_string_2)
    str_to_int_eval(test_string_3)
    str_to_int_eval(test_string_4)
