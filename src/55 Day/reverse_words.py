''' 
    Day 55
    Create a function that takes a string and returns the reverse of each word.

    Input file text:
        "Cuisine
        Main article: Roman cuisine

        Spaghetti alla carbonara, a typical Roman dish
        Rome's cuisine has evolved through centuries and periods of social, cultural, and political changes.
        Rome became a major gastronomical centre during the ancient age."

    Output file text:
        "enisiuC
        niaM elcitra: namoR enisiuc

        ittehgapS alla aranobrac, a lacipyt namoR hsid
        emoR's enisiuc sah devlove hguorht seirutnec dna sdoirep fo laicos, larutluc, dna lacitilop segnahc.
        emoR emaceb a rojam lacimonortsag ertnec gnirud eht tneicna ega."
'''

def reverse_words_in_text(string_to_reverse):
    ''' Reverse the words in a string but keep the non-alphanumeric chars
      on their positions '''

    reversed_word = ""
    reversed_words = []
    alphanumeric = ""

    # Split string into list of words
    words = string_to_reverse.split()

    for word in words:
        for char in word:
            if char.isalnum():
                alphanumeric += char
            else:
                # If character is not alphanum., revert the characters that are found so far
                # and after that add also the non-alphanum. character.
                reversed_word += alphanumeric[::-1]
                alphanumeric = ""
                reversed_word += char

        # Append the last alphanumeric characters (if any)
        reversed_word += alphanumeric[::-1]

        # Append the reversed word to the list of words
        reversed_words.append(reversed_word)

        # Reset variables
        reversed_word = ""
        alphanumeric = ""

    # Join the reversed words into string
    reversed_string = ' '.join(reversed_words)
    return reversed_string


if __name__ == "__main__":
    TEXT_FILE = ".\\src\\55 Day\\wikipedia_text.txt"
    REVERSED_FILE = ".\\src\\55 Day\\reversed_text.txt"

    with open(TEXT_FILE, 'r', encoding='utf-8') as input_file:
        with open(REVERSED_FILE, 'w', encoding='utf-8') as output_file:
            for line in input_file:
                reversed_line = reverse_words_in_text(line)
                output_file.write(reversed_line + '\n')
