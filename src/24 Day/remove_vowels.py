''''
    Day 24:
    Write a program to remove vowels from a given string.

    Sample from the book:
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

    Output:
    Text without vowels is saved in the file TextWithoutVowels.txt

    Sample of the book without vowels:
    Th Prjct Gtnbrg Bk f lc's dvntrs n Wndrlnd
    
    Ths bk s fr th s f nyn nywhr n th ntd Stts nd
    mst thr prts f th wrld t n cst nd wth lmst n rstrctns
    whtsvr. Y my cpy t, gv t wy r r-s t ndr th trms
    f th Prjct Gtnbrg Lcns ncldd wth ths bk r nln
    t www.gtnbrg.rg. f y r nt lctd n th ntd Stts,
    y wll hv t chck th lws f th cntry whr y r lctd
    bfr sng ths Bk.

    Ttl: lc's dvntrs n Wndrlnd


    thr: Lws Crrll

    Rls dt: Jn 27, 2008 [Bk #11]
                    Mst rcntly pdtd: Mrch 30, 2021

'''
import re

def remove_vowels(text):
    '''  Remove vowels from text '''
    output_file_path = ".\\src\\24 Day\\TextWithoutVowels.txt"

    # Define the pattern
    pattern = re.compile("[aeiouAEIOU]")

    # Replace vowels with empty string
    text_without_vowels = re.sub(pattern, "", text)

    print("\nText without vowels is saved in the file TextWithoutVowels.txt\n")
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(text_without_vowels)

if __name__ == "__main__":
    INPUT_FILE_PATH = ".\\src\\24 Day\\Alices Adventures In Wonderland.txt"
    with open(INPUT_FILE_PATH, 'r', encoding='utf-8') as input_file:
        text = input_file.read()
    remove_vowels(text)
