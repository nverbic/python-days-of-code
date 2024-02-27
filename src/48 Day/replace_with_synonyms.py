'''
    Day 48
    Create a program that replaces specific words in a text with their synonyms.

    Output:
    Text:
    Mr. Darcy is not to be laughed at! cried Elizabeth. That is an uncommon advantage,
    and uncommon I hope it will continue, for it would be a great loss to me to have
    many such acquaintance. I dearly love a laugh.

    Text with synonyms
    Mr. Darcy is not to be laughed at! shout Elizabeth. That is an rare advantage,
    and rare I hope it will continue, for it would be a bang-up loss to me to have
    many such acquaintance. I dearly love a joke. 
'''

import nltk
from nltk.corpus import wordnet
import re

#nltk.download('wordnet')

def find_synonyms(words_list):
    ''' Find synonyms of the words.
        Return the pairs {word:synonym} in a dictionary'''
    synonyms = {}

    for word in words_list:

        # Find a list of synonyms
        synsets = wordnet.synsets(word)
        if synsets:
            # Remember word capitalization
            is_capitalized = word.isupper()
            word_lower = word.lower()
            for item in synsets:
                synonym =  item.lemmas()[0].name()
                # Check that the word is not the same as the current synonym
                if synonym.lower() != word_lower:
                    if is_capitalized:
                        synonym = synonym.capitalize()
                    synonyms[word] = synonym
                    break
        else:
            synonyms[word] = word

    return synonyms


def replace_words(text, words_to_replace):
    ''' Replace words in text with synonyms '''
    # Define a regular expression pattern to match words
    pattern = r'\b\w+\b'

    synonyms_dict = find_synonyms(words_to_replace)

    # Define a function to replace each match with the corresponding replacement word
    def replace(match):
        word = match.group()
        # If word not found in synonyms_dict, return the original word
        return synonyms_dict.get(word, word)

    # Use re.sub() to perform the replacement
    return re.sub(pattern, replace, text)


if __name__ == "__main__":
    text_sample = "Mr. Darcy is not to be laughed at! cried Elizabeth. That is an "\
    "uncommon advantage, and uncommon I hope it will continue, for it would "\
    "be a great loss to me to have many such acquaintance. I dearly love a laugh."
    words_to_replace = ['cried', 'uncommon', 'advantage', 'great', 'acquaintance', 'laugh']
    print(f"Text:\n{text_sample}")
    text_with_synonyms = replace_words(text_sample, words_to_replace)
    print(f"Text with synonyms:\n{text_with_synonyms}")
