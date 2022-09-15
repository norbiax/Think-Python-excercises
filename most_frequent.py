import string

def most_frequent1(sentence):
    alphabet = string.ascii_lowercase
    print(alphabet)
    dictonary = dict()
    sentence_lower = sentence.replace(' ','').lower()
    for i in sentence_lower:
        if i in alphabet:
            count_i = sentence_lower.count(i)
            dictonary[i] = count_i

    return dictonary

print(most_frequent1('Ala ma ko%$3ta a kot ma DOM//;;;)'))

