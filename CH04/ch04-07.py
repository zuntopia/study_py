def foo(num, char, text="Pythoneer"):
    print(num)
    print(char)
    print(text)

"""
def bar(num, text="Pythoneer", char):
    print(num)
    print(char)
    print(text)
"""

if __name__=='__main__':
    foo(10, "A", "Pythonista")
    print()
    foo(20, "B")
    print()
    # foo(num=30, "C")
    foo(40, "Pythonista", "D")
    print()
