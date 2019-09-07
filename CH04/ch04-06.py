def foo(a, b):
    return a + b
    return a * b

def bar(a, b):
    return a + b, a * b

if __name__=='__main__':
    print(foo(5, 10))
    print(bar(5, 10))