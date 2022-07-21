def is_triangle(a, b, c):
    if a + b < c or a + c < b or b + c < a:
        print('No')
    else:
        print('Yes')

def create_triangle():
    a = int(input('First side: \n'))
    b = int(input('Second side: \n'))
    c = int(input('Third side: \n'))
    is_triangle(a, b, c)

create_triangle()
