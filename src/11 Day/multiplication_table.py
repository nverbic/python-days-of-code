''' #11 day challenge:
    Write a program to print the multiplication table of a given number.

    Output:
    Multiplication table of number 5:
    [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
'''
import random

def multiplication_table(number):
    ''' Print the multiplication table of a numbers '''
    multipl_table = []
    for i in range(1, 11):
        multipl_table.append(number * i)
    return multipl_table

if __name__ == "__main__":
    number = random.randint(1, 10)
    multipl_table = multiplication_table(number)
    print(f"Multiplication table of number {number}:\n{multipl_table}\n")
