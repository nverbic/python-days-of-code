''' #9 day challenge:
    Write a program to check if a number is even or odd.


    Output:
    Categorize a list of numbers to even and odd numbers lists:
    [33, 97, 39, 70, 37, 34, 31, 94, 17, 22, 68, 6, 23, 32, 12, 68, 40, 26, 92, 14]

    Even:
    [70, 34, 94, 22, 68, 6, 32, 12, 68, 40, 26, 92, 14]

    Odd:
    [33, 97, 39, 37, 31, 17, 23]
'''
import random

def categorize_even_odd_numbers(numbers):
    ''' From the list create sublists with even and odd values '''
    categories = {'even': [],
                  'odd' : []}

    for num in numbers:
        if num % 2:
            categories['odd'].append(num)
        else:
            categories['even'].append(num)

    return categories

if __name__ == "__main__":
    numbers = [random.randint(0, 100) for _ in range(20)]
    categories = categorize_even_odd_numbers(numbers)
    print(f"Categorize a list of numbers to even and odd numbers lists:\n{numbers}\n")
    print(f"Even:\n{categories['even']}\n")
    print(f"Odd:\n{categories['odd']}\n")
