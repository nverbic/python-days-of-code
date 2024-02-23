'''
    Day 44
    Write a program that reads an integer from the user and handles invalid inputs

    Output:
    Please enter an integer: 5
    Value is 5

    Please enter an integer: t
    The entered value must be an integer. Please try again.

    Please enter an integer: 6.5
    The entered value must be an integer. Please try again.
'''

def user_input_int():
    ''' Expect user input as integer '''
    try:
        int_number = int(input("Please enter an integer: "))
        print(f"Value is {int_number}")
        return int_number
    except ValueError:
        print("The entered value must be an integer. Please try again.")
        return None

if __name__ == "__main__":
    number = user_input_int()
