#!/usr/bin/python
import string

def rotate_word(str, rate):
    alphabet = string.ascii_lowercase
    for c in str:
        new_index = alphabet.find(c) + rate
        #print(new_index)
        if new_index > (len(alphabet)-1):
            new_index = (alphabet.find(c)-(len(alphabet)-1)) + rate
            #print(new_index)
        #print(c)
       # print(alphabet[new_index])
        new_string = str.replace(c, alphabet[new_index])
    return new_string

print(rotate_word('abcdef', 1))
