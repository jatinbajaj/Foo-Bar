
for i in range(1, 1001):
    if i % 3 == 0 and i % 5 == 0:
        print('foo-bar')

    elif i % 3 == 0:
        if i % 10 == 0:
            print(i)
        else:
            print('foo')

    elif i % 5 == 0:
        if i % 10 == 0:
            print(i)
        else:
            print('bar')

    else:
        print(i)







