''' #7 day challenge:
    Write a program to check if a number is positive, negative, or zero.


    Output:
    Categorize a list of numbers to positive, negative or zero:
    [-7, -7, -6, -4, -2, -2, 0, 0, 0, 0, 1, 1, 5, 5, 7, 9, 10, 10, 10, 10]

    Positive:
    [1, 1, 5, 5, 7, 9, 10, 10, 10, 10]

    Negative :
    [-7, -7, -6, -4, -2, -2]

    Zero:
    [0, 0, 0, 0]
'''
import random

def categorize_numbers(numbers):
    ''' From the list create sublists with positive, negative and zero values '''
    categories = {'positive': [],
                  'negative' : [],
                  'zero' : []}

    for num in numbers:
        if num > 0:
            categories['positive'].append(num)
        elif num < 0:
            categories['negative'].append(num)
        else:
            categories['zero'].append(num)

    return categories

if __name__ == "__main__":
    numbers = [random.randint(-10, 10) for _ in range(20)]
    categories = categorize_numbers(numbers)
    print(f"Categorize a list of numbers to positive, negative or zero:\n {numbers}\n")
    print(f"Positive:\n{categories['positive']}\n")
    print(f"Negative:\n{categories['negative']}\n")
    print(f"Zero:\n{categories['zero']}\n")
