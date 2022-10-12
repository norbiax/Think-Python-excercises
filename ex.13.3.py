#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string
from operator import itemgetter


def sentence_modification(file, first_line, last_line):
    """
    Reads a file, breaks each line within the given range into words, removes whitespace and punctuation, and converts
    to lowercase. Displays the 20 most commonly used words in the book.
    :param last_line: number
    :param first_line: number
    :param file: txt file
    :return: list
    """
    punct = list(string.punctuation)
    white = list(string.whitespace)
    for elem in punct:
        white.append(elem)
    all_to_delete = white
    all_to_delete.remove(' ')
    all_to_delete.append('”')
    all_to_delete.append('“')
    for d in range(0, 10):
        all_to_delete.append(str(d))
    fin = open(file, encoding="utf8")
    words_lst = []
    # lines to read
    line_numbers = [first_line, last_line]
    for i, line in enumerate(fin):
        line = line.lower()
        # read from first_line to the last_line
        if i in range(first_line, last_line + 1):
            for char in all_to_delete:
                if char in all_to_delete:
                    line = line.replace(char, '')
            words = line.split(' ')
            to_remove = ['']
            for word in list(words):
                if word in to_remove:
                    words.remove(word)

            for elem in words:
                words_lst.append(elem)

        elif i > last_line:
            # don't read after last_line to save time
            break
    total_word_number = len(words_lst)
    d = {}
    for i in words_lst:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    # print(words_lst)
    # print(total_word_number)
    # print(d)
    # print(' '.join(words_lst))

    t = d.items()
    ss_lst = list(set(t))
    ss_lst.sort(key=itemgetter(1), reverse=True)

    top_20 = []
    for i in ss_lst:
        count = 0
        if len(top_20) < 20:
            top_20.append(i)
            print(i)
            count += 1

    # print(ss_lst)

    return top_20


if __name__ == '__main__':
    sentence_modification('gut.txt', 324, 6488)
