def sum(a, b):
    return a + b

if __name__=='__main__':
    a = 3
    b = 4
    print(sum(a, b))
    l_sum = lambda x, y: x + y
    print(l_sum(a, b))

    print([x for x in range(5)])
    l_print = lambda x: [a for a in range(x)]
    print(l_print(5))