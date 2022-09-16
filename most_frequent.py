import string
from operator import itemgetter


def most_frequent1(sentence):
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
    for i in ss_lst:
        print(i[1], round((i[0])/len(sentence_lower)*100, 2), '%')

    return ss_lst


print(most_frequent1("""Letter frequency is the number of times letters of the alphabet appear on average in written 
                    language. Letter frequency analysis dates back to the Arab mathematician Al-Kindi (c. 801–873 AD), 
                    who formally developed the method to break ciphers. Letter frequency analysis gained importance in 
                    Europe with the development of movable type in 1450 AD, where one must estimate the amount of type 
                    required for each letterform. Linguists use letter frequency analysis as a rudimentary technique for 
                    language identification, where it is particularly effective as an indication of whether an unknown 
                    writing system is alphabetic, syllabic, or ideographic."""))
