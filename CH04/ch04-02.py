import sys

def bar(a, b):
   print(a + b)

if __name__ == '__main__':
    # bar(sys.argv[1], sys.argv[2])
    bar(1, 2)
    print(bar(1, 2))
