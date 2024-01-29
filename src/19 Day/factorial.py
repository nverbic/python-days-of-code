'''
    Day 19:
    Write a function to calculate the factorial of a number.

    Output:
    The factorial (using iteration) of 18 is:
    6402373705728000
    The factorial (using math.factorial()) of 18 is:
    6402373705728000

'''
import random
import math

def calc_factorial_math(num):
    ''' Calculate the factorial using math library '''
    return math.factorial(num)

def calc_factorial_iterate(num):
    ''' Calculate the factorial using iteration '''
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact

if __name__ == "__main__":
    num = random.randint(10, 20)
    fact_iter = calc_factorial_iterate(num)
    fact_math = calc_factorial_math(num)
    print(f"The factorial (using iteration) of {num} is:\n{fact_iter}")
    print(f"The factorial (using math.factorial()) of {num} is:\n{fact_math}")
