#!/usr/bin/python

def words_dict(file):
    '''
    Creates a words dict from a text file
    :param file:
    file: text file
    :return:
    words dict
    '''
    count = 0
    fin = open(file)
    #line = fin.readline()
    words_dict = dict()

    for line in fin:
        word = line.strip()
        count += 1
        words_dict[word] = count
    return words_dict

if __name__ == '__main__':
    print(words_dict('words.txt'))
