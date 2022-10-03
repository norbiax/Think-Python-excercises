

def words_list(file):
    '''
    Opens a text file and creates a list with words
    :param file: txt file
    :return: list
    '''
    fin = open(file)
    list_of_words = []
    for line in fin:
        word = line.strip()
        list_of_words.append(word)

    return list_of_words

def subwords_checking(word, lst):
    length = len(word)
    subwords_lst = []
    for i in range(0, length):
        new_word = word[:i] + word[i+1:]
        subwords_lst.append(new_word)
    for sub_word in subwords_lst:
        if sub_word in lst:
            subwords_checking(word, lst)
    return None

subwords_checking('ada')