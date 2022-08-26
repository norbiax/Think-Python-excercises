#!/usr/bin/python
import string


def rotate_word(str, rate):
    alphabet = string.ascii_lowercase
    # print(alphabet)
    new_letters = []
    for c in str:
        # print(alphabet.find(c))
        new_index = alphabet.find(c) + rate
        # print(new_index)
        if new_index > (len(alphabet) - 1):
            new_index = (alphabet.find(c) - (len(alphabet))) + rate
            # print(new_index)
        # print(c)
        # print(alphabet[new_index])
        new_letters.append(alphabet[new_index])
    new_word = ''.join(new_letters)
    return new_word


def make_word_dict(t):
    """Creates dict with words from text file as keys
       :param t: test file
       :return: dict
    """
    d = dict()
    fin = open(t)
    for line in fin:
        word = line.strip().lower()
        d[word] = None
    return d


def rotate_pairs(t):
    """
    Finds rotate pairs in list
    :param t: list
    :return: dict
    """
    d = make_word_dict(t)
    rot_words_dict = {}
    for i in d:
        for j in range(1, 14):
            rot_i = rotate_word(i, j)
            if rot_i in d:
                rot_words_dict[i] = (j, rot_i)
                #print(i, j, rot_i)
    return rot_words_dict

if __name__ == '__main__':
    print(rotate_pairs('words.txt'))
