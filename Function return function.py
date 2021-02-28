def test(y):
    return lambda x : y+x

def test1(f=None):
    return 1 if not f else f(1)

def test3(f=None):
    return 3 if not f else f(3)



print(test1(test(test3())))