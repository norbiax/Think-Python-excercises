#!/usr/bin/python
import string


def rotate_word(str, rate):
    alphabet = string.ascii_lowercase
    print(alphabet)
    new_letters = []
    for c in str:
        #print(alphabet.find(c))
        new_index = alphabet.find(c) + rate
        #print(new_index)
        if new_index > (len(alphabet) - 1):
            new_index = (alphabet.find(c) - (len(alphabet))) + rate
            # print(new_index)
        # print(c)
        # print(alphabet[new_index])
        new_letters.append(alphabet[new_index])
    new_word = ''.join(new_letters)
    return new_word


print(rotate_word('melon', -10))
