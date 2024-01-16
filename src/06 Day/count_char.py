''' #6 day challenge:
   Write a program to count the occurrences of a specific character in a string.


    Output:
    I got that feeling
    That bad feeling that you don't know
    I don't even know her
    But I hope that
    She comforts you tonight
    Nobody here that keeps you in the shade
    And ever owned you
    Some sentimental tears or someone else's girl
    That drips away
    But I somehow slowly love you
    And wanna keep you the same
    Well, I somehow slowly know you
    And wanna keep you away

    Count characters in the text using String count() method:
    {'a': 19, 'n': 21, 's': 14, 't': 23, 'y': 13, 'z': 0}

    Count characters in the text using regex findall() method:
    {'a': 19, 'n': 21, 's': 14, 't': 23, 'y': 13, 'z': 0}
'''
import re

def count_occurrences_regex(text, char_list):
    ''' Count the number of specific characters in text'''
    char_count = {}

    # Use regular expressions findall() method
    for char in char_list:
        char_count[char]  = len(re.findall(re.escape(char), text))

    return char_count


def count_occurrences(text, char_list):
    ''' Count the number of specific characters in text'''
    char_count = {}

    # Use String count() method
    for char in char_list:
        char_count[char] = text.count(char)

    return char_count

if __name__ == "__main__":
    file_path = ".\\src\\06 Day\\Massive_Attack.txt"
    text = ""
    char_list = ['a', 'n', 's', 't', 'y', 'z']

    with open(file_path, 'r', encoding='utf-8') as input_file:
        text = input_file.read()

    if text != "":
        print(f"\n{text}\n")
        occurrences = count_occurrences(text, char_list)
        print(f"Count characters in the text using String count() method:\n {occurrences}\n")
        occurrences = count_occurrences(text, char_list)
        print(f"Count characters in the text using regex findall() method:\n {occurrences}\n")
    else:
        print("The file is empty.")
