# Chapter 04: 입/출력

## 1. 함수를 이용한 입/출력
> 이 장은 합수를 다루는 것을 설명합니다.  
> 이 장에서 우리는 다음과 같이 명칭을 정합니다.

```python
def 함수(매개변수1, 매개변수2, ...):
    실행
def function(parameter1, parameter2, ...):
    runnable

함수(인수1, 인수2, ...)
function(argument1, argument2, ...)
```

### python은 함수를 지원하고, 별도의 타입 선언은 필요하지 않습니다.

* 일반적인 함수를 생성할 수 있습니다.

```python ch04-01.py
def foo(a, b):
   return a + b

if __name__ == '__main__':
    print(foo(1, 2))
    print(foo('a', 'b'))
```

* return 이 있는 경우만 return을 합니다.
  * return 이 없으면 함수 내부 실행 후 종료합니다.

```python ch04-02.py
def bar(a, b):
   print(a + b)

if __name__ == '__main__':
    bar(1, 2)
    print(bar(1, 2))
```

* 매개변수 없이도 실행 가능합니다.

```python ch04-03.py
def bar():
   print("FooBar")

if __name__ == '__main__':
    bar()
    bar(1, 2)
    print(bar(1, 2))
```

* 함수의 인자를 지정할 수 있습니다.

```python ch04-04.py
def foo(a, b):
   print(a+b)

if __name__ == '__main__':
    foo(a=1, b=2)
    foo(a=1, b=2, c=3)
```

* ch04-04는 정해진 변수와 맞는 인자만 지정 가능합니다.
  * 파이썬에서는 *argc, **argv 와 같은 매개변수 처리가 가능합니다.

```python ch04-05.py
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
```

* 함수의 반환은 한번만 가능하다

```python ch04-06.py
def foo(a, b):
    return a + b

    # this will not be returned.
    return a * b

def bar(a, b):
    return a + b, a * b

if __name__=='__main__':
    foo(5, 10)
    bar(5, 10)
```

* 함수에 미리 값을 지정할 수 있습니다.
  * 미리 정하는 경우, 매개변수의 순서, 인수의 순서가 모두 중요합니다.

```python 04-07.py
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
```

* 함수 내의 변수는 함수 내에서만 유효합니다.
  * 함수 밖에서 영향을 주기 위해서는 미리 선언하거나, global 예약어를 필요로 합니다.

```python py04-08.py
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
```

* Lambda는 함수를 한줄로 표현할 수 있습니다.
  * 제한된 용도로 사용

```python ch04-09.py
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

```

## User 가 직접 수행하는 입/출력
* input()을 이용하여 입력이 가능합니다.
```python ch04-11.py
result = input("type here: ")
print(result+" world")
```

* input() 으로 들어오는 값은 string 입니다. 다른 타입으로는 형변환이 필요합니다.
```python ch04-12.py
result = input("type number: ")
print(result)
print(type(result))
print(result+1)
```

* print() 는 화면에 출력하는 역할을 합니다.
  > python2 에서는 print(var), print var 모두 가능했지만, python3에서는 print(var)만 가능합니다.
  * print함수 내부에서 ,로 분리된 경우만 띄어쓰기 지원이 됩니다.
  * 또는 함수 종료에 대한 지정을 통해서 한줄로 출력이 가능합니다.
```python ch04-13.py
print("hello" "world")
print("hello"+"world")
print("hello", "world")

for i in range(0,5):
    print (i)
for i in range(6,10):
    print(i, end=" ")
```

## File 을 이용한 입/출력
> file 입/출력 시 파일의 목적이나 손상 등을 방지하기 위해 다음 형태를 이용합니다.

|Read|Write|Append|
|-|-|-|
|r|w|a|

* python에서는 open() 을 통해 파일 소켓을 열고, 반환값으로 cursor를 가져옵니다. 그리고 close() 를 통해 닫을 수 있습니다.
* 절대경로를 지정하지 않으면 헌재 위치를 기준으로 상대경로로 적용됩니다.
```python ch04-21.py
import os
my_file=open(os.getcwd()+'/CH04/fileio/newfile1', 'w')
my_file.close()
```

* 파일에 쓸 때는 cursor의 write() 함수를 이용합니다.
  * `\n`을 명시적으로 입력하지 않으면 줄바꿈이 되지 않습니다.
```python ch04-22.py
import os
f = open(os.getcwd()+'/CH04/fileio/newfile2', 'w')
for i in range(1,5):
    f.write("line %s\n", i)

for j in range(6,10):
    f.write("line %s ", j)
f.close()
```

* 파일을 읽을 때는 'r' 를 이용합니다.
  * 줄 단위로 읽을 때는 readline() 을 씁니다.
  * 전체를 줄 단위로 미리 읽을 때는 readlines() 를 씁니다.
  * 전체를 한번에 버퍼에 넣을 때는 read() 를 씁니다.
```python ch04-23.py
import os
# Readline
f1 = open(os.getcwd()+'/CH04/fileio/newfile2', 'r')
## 잘못된 사용
for line in f1.readline():
    print(line)
f1.close()
## 올바른 사용
f1_1 = open(os.getcwd()+'/CH04/fileio/newfile2', 'r')
each_line = f1_1.readline()
while each_line:
    print(each_line)
    each_line=f1_1.readline()
#Readlines
f2 = open(os.getcwd()+'/CH04/fileio/newfile2', 'r')
all_lines = f2.readlines()
f2.close()
for f2l in all_lines:
    print(f2l)
#Read
f3 = open(os.getcwd()+'/CH04/fileio/newfile2', 'r')
print(f3.read())
f3.close()
```

* 파일의 제일 뒤에 추가를 할 때  'a'를 씁니다.
```python ch04-24.py
import os
f = open(os.getcwd()+'/CH04/fileio/newfile2', 'a')
f.write('added line')
f.close()
```

* `with`를 이용해서 편하게 이용할 수 있습니다.
  * `with`는 내부의 종료를 보장하는 경우 사용합니다.
```python ch04-25.py
import os
with open(os.getcwd()+'/CH04/fileio/withfile', 'w') as f:
    f.write("Pythoneer")
```
> with는 현재 수행 단계 완료 시, 리소스 회수를 보장합니다. 이를 통해 파일 뿐 아니라 DB 컨넥션 등에서도 회수를 보장할 수 있습니다.