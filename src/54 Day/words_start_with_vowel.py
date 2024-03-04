'''
    Day 54
    Create a function to find all words in a sentence that start with a vowel

    Output:
    36 words in the text file start with a vowel:
    on
    on
    is
    in
    over
    up
    All
    of
    another
    And
    is
    is
    at
    on
    in
    over
    and
    again
    as
    is
    is
    it's
    I've
    and
    in
    and
    as
    as
    about
    As
    in
    ear
    I'm
    always
    one's
    anywhere
'''
import re

def find_words_starting_with_vowel(text):
    ''' Find the words that start with a vowel '''
    # Pattern for matching the words (include also apostrophe and dash)
    pattern = r'\b[aeiouAEIOU][\w\'-]+\b'

    # Find a list of words that start with a vowel
    list_of_words = re.findall(pattern, text)
    
    return list_of_words

if __name__ == "__main__":
    TEXT_FILE = ".\\src\\54 Day\song_lyrics.txt"

    with open(TEXT_FILE, 'r', encoding='utf-8') as input_file:
        song_lyrics = input_file.read()

    words = find_words_starting_with_vowel(song_lyrics)
    print(f"{len(words)} words in the text file start with a vowel:")
    for word in words:
        print(word)
