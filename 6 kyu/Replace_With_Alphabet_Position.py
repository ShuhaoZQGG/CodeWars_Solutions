from string import ascii_lowercase
import string

def alphabet_position(text):
    alphabet = string.ascii_lowercase
    text = text.lower()       
    output = ' '.join(str(ord(char)-96) for char in text.lower() if char.isalpha())
    return output