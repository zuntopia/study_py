b = 10

def foo(x, y):
    a = x * 2
    b = y * 2
    return a, b

def bar(x, y):
    b = x ** 2
    global c
    c = y ** 2
    return b, c

a = 100
def foobar(x, y):
    global a
    a = x + 1
    b = y + 1
    return a, b

if __name__=='__main__':
    a = 5
    print(a, b)
    foo(a, b) # Nothing will be returned
    print(a, b)
    a, b = foo(a, b) # 5 * 2, 10 * 2
    print(a, b)

    c = 10
    print(b, c)
    b, c = bar(b, c) # 20 ** 2, 20 ** 2
    print(b, c)

    a, b = foobar(a, b)
    print(a, b)