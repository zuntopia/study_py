import sys

def foo(a, b):
   return a + b

if __name__ == '__main__':
    # foo(sys.argv[1], sys.argv[2])
    print(foo(1, 2))
    print(foo('a', 'b'))