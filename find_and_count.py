def find_and_count(word, letter, start):
    index = start
    cnt = 0
    while index < len(word):
        if word[index] == letter:
            cnt += 1
            print('word[', index, ']', sep='')
        index += 1
    return cnt

if __name__ == '__main__':
    (find_and_count('radosny_rabarbar', 'r', 5))