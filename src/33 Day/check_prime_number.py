'''
    Day 33
    Write a test case for a function that checks if a number is prime

    Output examples:
    The number 19 is prime
    The number 10 is not prime
'''

import random
from math import sqrt


def is_prime_number(number):
    ''' Check whether a number is prime or not ''' 
    # Corner case (1 is not prime nor composite number)
    if (number <= 1):
        return False

    # Check from 2 to sqrt(n)
    for i in range(2, int(sqrt(number))+1):
        if (number % i == 0):
            return False
    return True


if __name__ == "__main__":
    number = random.randint(1, 20)
    is_prime = is_prime_number(number)
    if is_prime:
        print(f"The number {number} is prime")
    else:
        print(f"The number {number} is not prime")
