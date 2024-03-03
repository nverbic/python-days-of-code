'''
    Day 52
    Create a program that checks if a string is a palindrome

    Output:
    "He lived as a devil, eh?" is a palindrome: True
    "Never odd or even." is a palindrome: True
    "Sir, I demand, I am a maid named Iris." is a palindrome: True
    "rotator" is a palindrome: True
    "I am not a palindrome" is a palindrome: False
'''

class PalindromeChecker():
    def __init__(self, text:str) -> None:
        self.text = text

    def sanitize_text(self):
        ''' Remove spaces and convert to lowercase '''
        sanitized_text = [char.lower() for char in self.text if char.isalnum()]
        return sanitized_text

    def is_palindrome(self):
        ''' Check if the text is a palindrome '''
        sanitized_text = self.sanitize_text()
        if sanitized_text == sanitized_text[::-1]:
            return True
        return False

if __name__ == "__main__":
    list_of_strings = ["He lived as a devil, eh?",
                        "Never odd or even.",
                        "Sir, I demand, I am a maid named Iris.",
                        "rotator",
                        "I am not a palindrome"]

    for item in list_of_strings:
        print(f"\"{item}\" is a palindrome: {PalindromeChecker(item).is_palindrome()}")
