'''
    Day 36
    Write a Python program to check if two strings are anagram

    Output:
    "dormitory" and "dirty room" are anagrams
    "debit card" and "bad credit" are anagrams
    "Eleven plus two" and "Twelve plus one" are anagrams
    "A decimal point" and "I'm a dot in place" are anagrams
    "Vacation time" and "I am not active" are anagrams
    "+Clint-Eastwood!" and "old west action" are anagrams
    "Lala land" and "Clara land" are NOT anagrams
    "Finding Nemo" and "Look! It's Nemo!" are NOT anagrams
'''
import re

def check_anagrams(str1, str2):
    ''' Check if the str1 and str2 are anagrams '''

    # Regular expression to extract only letters and numbers from the string
    pattern = re.compile(r'[a-z0-9]+')

    # Remove spaces
    alphanumeric_str1 = str1.replace(" ", "").lower()
    alphanumeric_str2 = str2.replace(" ", "").lower()

    # Use findall() to extract alphanumeric characters
    alphanumeric_list1 = pattern.findall(alphanumeric_str1)
    alphanumeric_list2 = pattern.findall(alphanumeric_str2)

    # Join the extracted characters(strings) back into one string
    alphanumeric_str1 = ''.join(alphanumeric_list1)
    alphanumeric_str2 = ''.join(alphanumeric_list2)

    # Sort the characters alphabetically
    alphanumeric_str1 = ''.join(sorted(alphanumeric_str1))
    alphanumeric_str2 = ''.join(sorted(alphanumeric_str2))

    if alphanumeric_str1 == alphanumeric_str2:
        return True

    return False


if __name__ == "__main__":
    anagrams = {'dormitory': 'dirty room',
                'debit card': 'bad credit',
                'Eleven plus two': 'Twelve plus one',
                'A decimal point': 'I\'m a dot in place',
                'Vacation time': 'I am not active',
                '+Clint-Eastwood!': 'old west action',
                'Lala land': 'Clara land',
                'Finding Nemo': 'Look! It\'s Nemo!'
                }

    for key, value in anagrams.items():
        if check_anagrams(key, value):
            print(f"\"{key}\" and \"{value}\" are anagrams")
        else:
            print(f"\"{key}\" and \"{value}\" are NOT anagrams")
