def most_frequent1(string):
    dictonary = dict()
    for i in string:
        count_i = string.count(i)
        dictonary[i] = count_i

    return dictonary

print(most_frequent1('a la'))

def most_frequent1(string):

