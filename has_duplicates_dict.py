#!/usr/bin/python

def has_duplicates(t):
    '''
    Returns True if list has a duplicates
    :param t: list
    :return: bool if there are duplicates or dict without duplicates
    '''
    d = dict()
    for i in t:
        if i not in d:
            d[i] = 1
        else:
            return True
    return d

if __name__ == '__main__':
    print(has_duplicates(['a', 'b', 'c', 'a']))
