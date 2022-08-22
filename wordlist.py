#!/usr/bin/python
import time


def create_list_with_append():
    fin = open('words.txt')
    list_of_words = []

    for line in fin:
        word = line.strip()
        list_of_words.append(word)

    return list_of_words

def create_list_with_idiom():
    fin = open('words.txt')
    line = fin.readline()
    t = []

    for line in fin:
        word = line.strip()
        t += [word]

    return t

start = time.time()
create_list_with_append()
end = time.time()
print("The time of execution of above program is :", end - start)


start = time.time()
create_list_with_idiom()
end = time.time()
print("The time of execution of above program is :", end - start)