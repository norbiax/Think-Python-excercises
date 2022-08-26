#!/usr/bin/python

def has_duplicates(t):
    '''
    Returns True if list has a duplicates
    :param t: list
    :return: bool
    '''
    d = dict()
    for i in t:
        if i not in d:
            d[i] = 1
        else:
            return True
    return False

if __name__ == '__main__':
    t = [1, 2, 3]
    print(has_duplicates(t))
    t.append(1)
    print(has_duplicates(t))
