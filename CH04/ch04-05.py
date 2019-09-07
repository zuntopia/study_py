def foo(*args):
    for i in range(len(args)):
        print(i)

def bar(**kwargs):
    print(type(kwargs))
    for k, v in kwargs.iteritems():
        print(k, v)

if __name__=='__main__':
    foo(1, 2, 3)
    foo('a', 'b')
    bar(apple=1, banana=2, cherry=3)