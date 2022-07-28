import math

def mysqrt(a):
    x = a + 1
    while True:
        #print(x)
        y = (x + a/x) / 2
        if y == x:
            break
        x = y
    return y

def test_mysqrt_root():
    print('a', '   ', 'mysqrt(a)', '    ', 'math.sqrt(a) ', 'diff')
    print('-', '   ', '---------', '    ', '------------ ', '----')
    a = 1.0
    while a < 10:
        print(a, ' ', round(mysqrt(a), 11), (13-len(str(round(mysqrt(a), 11))))*' ',
              round(math.sqrt(a), 11),
              (13 - len(str(round(math.sqrt(a), 11)))) * ' ',
              abs(mysqrt(a)-math.sqrt(a)))
        a += 1

test_mysqrt_root()