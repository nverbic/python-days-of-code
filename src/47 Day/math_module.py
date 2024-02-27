'''
    Day 47
    Create a program that imports the math module and uses its functions.

    Output:
    math.sqrt(4) = 2.0
    math.pow(4,2) = 16.0
    math.exp(4) = 54.598150033144236
    math.log2(4) = 2.0
    math.log(4) = 1.3862943611198906
    math.floor(13.542314652451461) = 13
    Cmath.ceil(13.542314652451461) = 14
    math.lcm((4, 8, 12)) = 24
    math.modf(13.542314652451461) = (0.542314652451461, 13.0)
'''

import math
import random

def calc_square_root(num):
    ''' Return the square root of num. '''
    result = math.sqrt(num)
    print(f"math.sqrt({num}) = {result}")
    return result

def calc_pow(num, exponent):
    ''' Return num raised to the power of exponent. '''
    result = math.pow(num, exponent)
    print(f"math.pow({num},{exponent}) = {result}")
    return result

def calc_exp(num):
    ''' Return e raised to the power num, where e = 2.718281… is the base of natural logarithm. '''
    result = math.exp(num)
    print(f"math.exp({num}) = {result}")
    return result

def calc_log(num):
    ''' Return the natural logarithm of num (to base e). '''
    result = math.log(num)
    print(f"math.log({num}) = {result}")
    return result

def calc_log2(num):
    ''' Return the base-2 logarithm of num (to base e). '''
    result = math.log2(num)
    print(f"math.log2({num}) = {result}")
    return result

def calc_floor(num):
    ''' Return the floor of num, the largest integer less than or equal to num. '''
    result = math.floor(num)
    print(f"math.floor({num}) = {result}")
    return result

def calc_ceil(num):
    ''' Return the ceiling of num, the smallest integer greater than or equal to num. '''
    result = math.ceil(num)
    print(f"Cmath.ceil({num}) = {result}")
    return result

def calc_lcm(*numbers):
    ''' Return the least common multiple of the specified integer arguments '''
    result = math.lcm(*numbers)
    print(f"math.lcm({numbers}) = {result}")
    return result

def calc_modf(num):
    ''' Return the fractional and integer parts of num.  '''
    result = math.modf(num)
    print(f"math.modf({num}) = {result}")
    return result

if __name__ == "__main__":
    rand_num = random.randint(1, 20)
    rand_float = random.uniform(1, 20)
    calc_square_root(rand_num)
    calc_pow(rand_num, 2)
    calc_exp(rand_num)
    calc_log2(rand_num)
    calc_log(rand_num)
    calc_floor(rand_float)
    calc_ceil(rand_float)
    calc_lcm(4,8,12)
    calc_modf(rand_float)
