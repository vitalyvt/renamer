# Move number in the begining of file neme to the end of name befor extention.

from os import listdir
from os import rename

n=0
print('\n', 'Renamer v 0.1', '\n')
fileList = listdir('.')
for fileName in fileList:
    splittedFileName = str.split(fileName,'.')
    if splittedFileName[0].isnumeric():
        splittedFileName.insert(len(splittedFileName)-1,splittedFileName[0])
        del splittedFileName[0]
        newFileName = '.'.join(splittedFileName)
        print('Was: ', FileName,'\n', 'Now: ', newFileName, '\n')
        n += 1
        rename(fileName,newFileName) 
print(n, ' file(s) was renamed', '\n')