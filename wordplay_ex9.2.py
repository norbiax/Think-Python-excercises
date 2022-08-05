#!/usr/bin/python

fin = open('words.txt')
line = fin.readline()
with open(r"words.txt", 'r') as fp:
    lines = len(fp.readlines())


def has_no_e():
    collection = []
    for line in fin:
        word = line.strip()
        if 'e' not in word:
            collection.append(word)
            print(word)
    print("Percentage of words without 'e': ", round((len(collection)/lines * 100), 2), '%')


if __name__ == "__main__":
    has_no_e()
