'''
    Day 45
    Write a function to check if a number is a prime number

    Output examples:
    The number 14 is not prime
    The number 5 is prime
    The number 17 is prime
    The number 8 is not prime
    The number 18 is not prime
'''

import random
from math import sqrt


def is_prime_number(number):
    ''' Check whether number is prime or not ''' 
    # Corner case (1 is not prime nor composite number)
    if (number <= 1):
        return False

    # Check from 2 to sqrt(n)
    for i in range(2, int(sqrt(number))+1):
        if (number % i == 0):
            return False
    return True


if __name__ == "__main__":
    # Random number
    random_number = random.randint(1, 20)

    # Check if the number is prime
    is_prime = is_prime_number(random_number)

    if is_prime:
        print(f"The number {random_number} is prime")
    else:
        print(f"The number {random_number} is not prime")
