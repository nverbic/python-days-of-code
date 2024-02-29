'''
    Day 50
    Create a program that finds the intersection and union of two sets

    Output:
    Set a:
    {'me', 'the', 'music', 'to', 'dance'}

    Set b:
    {'me', 'the', 'around', 'dance', 'moon', 'all'}

    Set c:
    {'me', 'the', 'around', 'dance', 'room', 'all'}

    Union of sets:
    {'me', 'the', 'music', 'around', 'dance', 'to', 'room', 'moon', 'all'}

    Intersection of sets:
    {'me', 'the', 'dance'}
'''

if __name__ == "__main__":
    song_lyrics_1 = "Dance me to the music"
    song_lyrics_2 = "Dance me all around the moon"
    song_lyrics_3 = "Dance me all around the room"

    # Create set from a list of words
    a = set((song_lyrics_1.lower().split()))
    b = set((song_lyrics_2.lower().split()))
    c = set((song_lyrics_3.lower().split()))

    # Print sets
    print(f"Set a:\n{a}\n")
    print(f"Set b:\n{b}\n")
    print(f"Set c:\n{c}\n")

    # Union returns a new set with elements from the set and all others.
    abc_union = a.union(b, c)
    print(f"Union of sets:\n{abc_union}\n")

    # Intersection returns a new set with elements common to the set and all others.
    abc_intersection = a.intersection(b,c)
    print(f"Intersection of sets:\n{abc_intersection}")
