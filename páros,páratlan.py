a = int(input('Give a number: '))
while a != 0:
    if a%2 == 0:
        print('{} is even.'.format(a))
    else:
        print('{} is odd.'.format(a))
    a = int(input('Give a number: '))
