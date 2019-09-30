import os
f = open(os.getcwd()+'/CH04/fileio/newfile2', 'w')
for i in range(1,5):
    f.write("line %s\n" % i)

for j in range(6,10):
    f.write("line %s " % j)
f.close()