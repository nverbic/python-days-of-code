''' #3 day challenge:
    Write a function to count the number of vowels in a given string


    Output:
    Here comes the sun, doo-doo-doo-doo
    Here comes the sun, and I say
    It's alright

    The number of vowels in the above text is 26
'''
import re

def count_vowels(text):
    ''' Count the number of vowels in text'''
    vowels = re.findall(r'[a,e,i,o,u]', text)
    return len(vowels)

if __name__ == "__main__":
    file_path = ".\\src\\03 Day\\The_Beatles.txt"
    text = ""
    with open(file_path, 'r', encoding='utf-8') as input_file:
        text = input_file.read()
    if text != "":
        number_of_vowels = count_vowels(text)
        print(f"\n{text}\n\nThe number of vowels in the above text is {number_of_vowels}\n")
    else:
        print("The file is empty.")
