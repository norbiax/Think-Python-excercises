import string
from operator import itemgetter


def most_frequent1(sentence):
    '''
    Retrieves a string and returns tuples with letters and their number in the sentence
    :param sentence: string - part of text
    :return: list of tuples
    '''
    alphabet = string.ascii_lowercase
    lst = []
    sentence_lower = sentence.replace(' ', '').lower()
    for i in sentence_lower:
        if i in alphabet:
            count_i = sentence_lower.count(i)
            tup_i = (count_i, i)
            lst.append(tup_i)
    ss_lst = list(set(lst))
    ss_lst.sort(key=itemgetter(0), reverse=True)

    return ss_lst


def words_dict(file):
    '''
    ......
    :param file:
    :param sentence:
    :return:
    '''
    fin = open(file)
    list_of_words = []
    words_collection = dict()
    for line in fin:
        word = line.strip()
        list_of_words.append(word)
    # print(list_of_words)
    for word in list_of_words:
        words_collection[word] = most_frequent1(word)

    return words_collection


def find_keys_by_values(dic, val_to_find):
    keys_lst = []
    for key, value in dic.items():
        if value == val_to_find:
            keys_lst.append(key)
    return keys_lst


def anagrams_sets(collection):
    sets = []
    for key, value in collection.items():
        anagrams = find_keys_by_values(collection, value)
        # print(anagrams)
        if len(anagrams) > 1 and anagrams not in sets:
            sets.append(anagrams)
    for anagrams in sets:
        print(anagrams)


if __name__ == '__main__':
    anagrams_sets(words_dict('words.txt'))
