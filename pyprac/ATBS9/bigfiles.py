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
    fextList = [] # make a list of the file extensions. List of tuples to count how many of each extension?
    fexts = [] # this will be the tuple
    for base in bytes_list:
        base = os.path.basename(base[0]) #act on the first entry in the tuple.
        fname, fext = os.path.splitext(base) # Returns a tuple, the filename and the extension, fext is the extension
        fexts.append(fext)


        #os.path.splitext(path)
    for i in range(len(fexts)): #Look into using enumerate() instead.
        if fexts[i] == fexts[i + 1]:
        #  fix this, list item must match next. Maybe a Row for each different extension returned?
            print(fexts[i] + " matched")
        else:
            newFext = fexts.pop(i+1) #Returns the "unmatched" extension
            print(newFext)
            print("Not match")
    fextList.append(fexts) #Fexts is now a list, let's append it to the main Fext List.
    print(fextList)

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