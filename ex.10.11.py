#!/usr/bin/python
def create_words_list(file):
    ''' Creates a words list from a text file
    :param lst:
    file: text file
    :return:
    words list
    '''
    fin = open(file)
    list_of_words = []

    for line in fin:
        word = line.strip()

        list_of_words.append(word)

    return list_of_words


def reversed_pairs(file):
    '''Creates a reversed pairs list
    :param lst:
    lst: words list
    :return:
    reversed pairs list
    '''
    lst = create_words_list(file)
    list_of_reversed_pairs = []
    for word in lst:
        if word[::-1] in lst and word[::-1] != word:
            list_of_reversed_pairs.append(str(word) + '-' + str(word[::-1]))
            lst.remove(word[::-1])
    return list_of_reversed_pairs


if __name__ == '__main__':
    print(reversed_pairs('words.txt'))
