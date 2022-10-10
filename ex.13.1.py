import string


def sentence_modification(file):
    punct = list(string.punctuation)
    white = list(string.whitespace)
    for elem in punct:
        white.append(elem)
    all_to_delete = white
    all_to_delete.remove(' ')
    for d in range(0, 10):
        all_to_delete.append(str(d))
    fin = open(file)
    words_lst = []
    for line in fin:
        line = line.lower()
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


    print(words_lst)
    print(' '.join(words_lst))
    return words_lst


if __name__ == '__main__':
    sentence_modification('file1.txt')