'''
    Day 43
    Write a program that removes all whitespaces from a given string.

    Output characters from ebook from 1000 to 1400:
    SWICKPRESS:--CHARLESWHITTINGHAMANDCO.TOOKSCOURT,CHANCERYLANE,LONDON.
    [Illustration:_ToJ.ComynsCarrinacknowledgmentofallIowetohisfriendshi
    pandadvice,theseillustrationsaregratefullyinscribed__HughThomson_]PR
    EFACE.[Illustration]_WaltWhitmanhassomewhereafineandjustdistinctionb
    etween“lovingbyallowance”and“lovingwithpersonallove.”Thisdistinction
    appliestobooksaswellastomenandwomen;andinthecaseofthenotvery
'''
import re

def remove_whitespaces(text):
    ''' Remove whitespaces from the text'''
    text_without_whitespaces = ""

    # Remove all whitespaces from the text ('', \t, \n, \r, \v, \f)
    pattern = r"\s+"
    text_without_whitespaces = re.sub(pattern, "", text)
    return text_without_whitespaces

if __name__ == "__main__":
    INPUT_FILE = ".\\src\\43 Day\\Pride and prejudice.txt"
    OUTPUT_FILE = ".\\src\\43 Day\\Text_without_whitespaces.txt"

    with open(INPUT_FILE, 'r', encoding='utf-8') as input_file:
        e_book = input_file.read()

    # Remove whitespaces
    ebook_without_whitespaces = remove_whitespaces(e_book)
    
    # Print part of the ebook without whitespaces
    print(ebook_without_whitespaces[1000:1400])

    # Save the text without the whitespaces
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as output_file:
        output_file.write(ebook_without_whitespaces)
