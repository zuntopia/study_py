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