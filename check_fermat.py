def check_fermat(a, b, c, n):
    if n > 2:
        if a**n + b**n == c**n:
            print('Hell! Fermat was wrong!')
        else:
            print("No, it doesn't work")
    else:
        print('n is <= 2, condition is not met')

    