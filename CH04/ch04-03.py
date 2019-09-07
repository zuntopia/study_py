import sys

def bar():
   print("FooBar")

if __name__ == '__main__':
    bar()
    bar(1, 2)
    print(bar(1, 2))