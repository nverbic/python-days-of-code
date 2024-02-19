'''
    Day 40
    Write a function to find the largest common divisor of two numbers using a function

    Prime factors of 24: [2, 2, 2, 3]
    Prime factors of 32: [2, 2, 2, 2, 2]
    Largest common divisior of 24 and 32 is: 8
'''
import random

def get_prime_factors(number):
    '''Return a list of the number's prime factors'''
    prime_factors = []

    if number != 1:
        i = 2
        # First divide with 2
        while number > 1 :
            if  number % i == 0:
                number = number / i
                prime_factors.append(i)
            else:
                break
        # Set i to 3 and increment by 2 to test only odd numbers. All composite odd numbers
        # are tested but only prime factors are removed from the number. This is because the composite
        # numbers are composed from prime factors (2,3,5,7,11,13,17,19 etc) which are removed from
        # the number before trying the composite number.
        i = 3
        while number > 1 and i <= number:
            if  number % i == 0:
                number = number / i
                prime_factors.append(i)
            else:
                i = i + 2
    return prime_factors

def largest_common_divisor(num1, num2):
    ''' Find the largest common divisor '''
    # Get prime factors
    prime_factors_1 = get_prime_factors(num1)
    prime_factors_2 = get_prime_factors(num2)
    print(f"Prime factors of {num1}: {prime_factors_1}")
    print(f"Prime factors of {num2}: {prime_factors_2}")

    # Find common numbers in the lists
    common_prime_numbers = set(prime_factors_1) & set(prime_factors_2)

    common_numbers_list = []

    # If the number is present in both lists it will be used to calculate the largest common divisor
    for item in common_prime_numbers:
        while ((item in prime_factors_1) and (item in prime_factors_2)):
            common_numbers_list.append(item)
            prime_factors_1.remove(item)
            prime_factors_2.remove(item)

    # Find the largest common divisor
    largest_divisor = 1
    for num in common_numbers_list:
        largest_divisor *= num

    return largest_divisor

if __name__ == '__main__':
    number1 = random.randint(2, 40)
    number2 = random.randint(2, 40)
    largest_common_div = largest_common_divisor(number1, number2)
    print(f"Largest common divisior of {number1} and {number2} is: {largest_common_div}")
