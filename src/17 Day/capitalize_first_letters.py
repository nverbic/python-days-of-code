''''
    Day 17:
    Create a program that capitalizes the first letter of each word in a sentence

    Input (part of the book):
    The Project Gutenberg eBook of Alice's Adventures in Wonderland
    
    This ebook is for the use of anyone anywhere in the United States and
    most other parts of the world at no cost and with almost no restrictions
    whatsoever. You may copy it, give it away or re-use it under the terms
    of the Project Gutenberg License included with this ebook or online
    at www.gutenberg.org. If you are not located in the United States,
    you will have to check the laws of the country where you are located
    before using this eBook.

    Title: Alice's Adventures in Wonderland


    Author: Lewis Carroll

    Release date: June 27, 2008 [eBook #11]
                    Most recently updated: March 30, 2021

    Language: English

    Credits: Arthur DiBianca and David Widger


    *** START OF THE PROJECT GUTENBERG EBOOK ALICE'S ADVENTURES IN WONDERLAND ***
    [Illustration]

    Output:
    The Project Gutenberg EBook Of Alice's Adventures In Wonderland
        
    This Ebook Is For The Use Of Anyone Anywhere In The United States And
    Most Other Parts Of The World At No Cost And With Almost No Restrictions
    Whatsoever. You May Copy It, Give It Away Or Re-use It Under The Terms
    Of The Project Gutenberg License Included With This Ebook Or Online
    At Www.gutenberg.org. If You Are Not Located In The United States,
    You Will Have To Check The Laws Of The Country Where You Are Located
    Before Using This EBook.

    Title: Alice's Adventures In Wonderland


    Author: Lewis Carroll

    Release Date: June 27, 2008 [eBook #11]
                    Most Recently Updated: March 30, 2021

    Language: English

    Credits: Arthur DiBianca And David Widger


    *** START OF THE PROJECT GUTENBERG EBOOK ALICE'S ADVENTURES IN WONDERLAND ***
    [Illustration]
'''
import re

def capitalize_first_letters(text_lines):
    ''' Capitalize first letters of the text '''
    # Save text with capitalized letters to a new file
    output_file_path = ".\\src\\17 Day\\Capitalized.txt"
    capitalized_text = []

    for line in text_lines:
        # Split the words in the line. Use regex to preserve spacing.
        words = re.split(r'(\s+)', line)

        # Capitalized words
        capitalized_line = ""

        # TODO: Capitalize letter that next to quotation mark
        for word in words:
            if (word != ''):
                # Do not use capitalize() because it converts the first letter
                # of word to upper case and remaining to lower case.
                # The code below just capitalizes the first letters of the words and
                # other letters remain the same as in the original file.
                capitalized_line += word[0].upper() + word[1:]
        capitalized_text.append(capitalized_line)

    # Save to output file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for line in capitalized_text:
            output_file.write(line)

if __name__ == "__main__":
    INPUT_FILE_PATH = ".\\src\\17 Day\\Alices Adventures In Wonderland.txt"
    with open(INPUT_FILE_PATH, 'r', encoding='utf-8') as input_file:
        text_lines = input_file.readlines()
    capitalize_first_letters(text_lines)
