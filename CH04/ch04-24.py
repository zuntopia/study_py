import os
f = open(os.getcwd()+'/CH04/fileio/newfile2', 'a')
f.write('\nadded line')
f.close()
fr = open(os.getcwd()+'/CH04/fileio/newfile2', 'r')
print(fr.read())
fr.close()