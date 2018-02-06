#!python3
import os

# Return Human Readable file sizes, displayed next to the file name/path.
# Sort by size.

path = os.path.abspath(os.curdir) #+ os.sep # If using split(), a os.sep will return as a '' list entry.
bytes_list = []

def human_Read(bytes):
    byteStr = str(bytes)
    numInts = len(byteStr)

    if bytes < 1000:
        return byteStr + ' bytes'
    elif 1000 <= bytes < 999999:
        return str(round(bytes/10e2, 1)) + " KB"
    elif numInts >= 7 and numInts < 10:
        return str(int(bytes/10e5)) + " MB"

# f = open("sizes.txt", 'w')


for folder, subfolders, files, in os.walk(path):
    pathBase = os.path.basename(folder)
    for filename in files:
        newPath =(os.path.abspath(folder) + os.sep + filename) #Should return the correct directory recursively.
        bytesize = os.path.getsize(newPath)
        result = human_Read(os.path.getsize(newPath))
        bytes_list.append((newPath, bytesize, result))

def hiByte(item):
    return item[1] # using this as a key for sorted() will return the 2nd item in the tuple.

def sumBytes():
    bytesSum = 0
    for x in bytes_list:
        bytesSum += x[1]
    print('Total folder size: ' + human_Read(bytesSum)) #Sum of all files.
    bigFile = sorted(bytes_list, key=hiByte, reverse=True)[0]
    print('The largest file is: ' + os.path.basename(bigFile[0]) + ' at '+ str(bigFile[2])) #Print the largest file name and size

def extCount():
    count = 0
    for base in bytes_list:
        if os.path.basename(base[0]).endswith(".py"):
            count +=1
        #os.path.splitext(path)
    print(str(count) + ' .py files')


bytes_list = sorted(bytes_list, key=hiByte, reverse=True)
for i in bytes_list:
    print(i)
sumBytes()
extCount()
# f.close()

# 1000 = 1 kb
# 1,000,000 = 1 mb, 1000 kb
# 1,000,000 and 999,999,999

'''
Bytes should show 3 integers

Kilobytes should show 2
'''