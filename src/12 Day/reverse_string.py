''' #12 day challenge:
    Write a program to reverse a given string.

    Output:
    Original: MY NAME IS PETER PARKER.
    Reversed: YM EMAN SI RETEP REKRAP

    Original: YOUR FRIENDLY NEIGHBORHOOD SPIDER-MAN.
    Reversed: RUOY YLDNEIRF DOOHROBHGIEN NAM-REDIPS

    Original: WITH GREAT POWER, THERE MUST ALSO COME GREAT RESPONSIBILITY!
    Reversed: HTIW TAERG ,REWOP EREHT TSUM OSLA EMOC TAERG YTILIBISNOPSER

    Original: ANYONE CAN WEAR THE MASK.
    Reversed: ENOYNA NAC RAEW EHT KSAM

    Original: I BELIEVE THERE'S A HERO IN ALL OF US.
    Reversed: I EVEILEB S'EREHT A OREH NI LLA FO SU

    Original: WHO AM I?
    Reversed: OHW MA I

'''
def reverse_text(text):
    ''' Reverse text '''
    lines_reversed = []
    end_punctuation = ".?!"

    for line in text:
        # Remove end punctuation
        if line[-1] in end_punctuation:
            line = line[:-1]
        # Create the list of words
        words = line.split()
        # Reverse the individual words in the sentence
        reversed_words = [word[::-1] for word in words]
        # Join the words in the sentence
        lines_reversed.append(' '.join(reversed_words))

    return lines_reversed

if __name__ == "__main__":
    FILE_PATH = ".\\src\\12 Day\\SpiderMan_quote.txt"

    with open(FILE_PATH, 'r', encoding='utf-8') as fp:
        lines = [line.strip().upper() for line in fp ]

    lines_reversed = reverse_text(lines)

    for i in range(len(lines)):
        print(f"Original: {lines[i]}")
        print(f"Reversed: {lines_reversed[i]}\n")

