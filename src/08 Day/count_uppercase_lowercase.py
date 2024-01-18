''' #8 day challenge:
     Write a function that accepts a string and calculates the number of 
     uppercase and lowercase letters in it.


    Output:
    "It is a curious thing, Harry, but perhaps those who are best suited to power
    are those who have never sought it. Those who, like you, have leadership thrust upon them,
    and take up the mantle because they must, and find to their own surprise
    that they wear it well." — Albus Dumbledore

    Number of uppercase letters in text: 5
    Number of lowercase letters in text: 217
    Number of other characters in text (without spacses): 11
'''

def count_uppercase_lowercase(text):
    ''' Count the number of uppercase and lowercase letters '''
    uppercase_count = 0
    lowercase_count = 0
    other_chars_count = 0

    for char in text:
        if char.isupper():
            uppercase_count += 1
        elif char.isalpha():
            lowercase_count += 1
        else:
            other_chars_count += 1

    print(f"Number of uppercase letters in text: {uppercase_count}")
    print(f"Number of lowercase letters in text: {lowercase_count}")
    print(f"Number of other characters in text (without spacses): {other_chars_count}")

if __name__ == "__main__":
    FILE_PATH = ".\\src\\08 Day\\HarryPotter_quote.txt"
    with open(FILE_PATH, 'r', encoding='utf-8') as input_file:
        text = input_file.read()
        print(f"Text:\n{text}\n")
        text_without_spaces = ''.join(text.split())
        count_uppercase_lowercase(text_without_spaces)
    