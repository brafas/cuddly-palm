import os

# Return Human Readable file sizes, displayed next to the file name/path.
# Sort by size.

path = os.path.abspath('.') + '\\'
bytes_list = []

def human_Read(bytes):
    byteStr = str(bytes)
    numInts = len(byteStr)

    if bytes < 1000:
        return byteStr + ' bytes'
    elif 1000 <= bytes < 999999:
        return str(round(bytes/10e2, 1)) + " KB"
        # return str(round(bytes, -(numInts - 2)))[:2] + " KB"
    elif numInts >= 7 and numInts < 10:
        return str(int(bytes/10e5)) + " MB"
        # byteStr = str(round(bytes, -(numInts - 3)))
        # return byteStr + ' mB'

# f = open("sizes.txt", 'w')


for folder, subfolders, files, in os.walk(path):
    for filename in files:
        bytesize = os.path.getsize(path+filename)
        result = human_Read(os.path.getsize(path+filename))
        bytes_list.append((path + filename, bytesize, result))

def hiByte(item):
    return item[1] # using this as a key for sorted() will return the 2nd item in the tuple.

def sumBytes():
    bytesSum = 0
    for x in bytes_list:
        bytesSum += x[1]
    print('Total folder size: ' + human_Read(bytesSum)) #Sum of all files.
    bigFile = sorted(bytes_list, key=hiByte, reverse=True)[0]
    print('The largest file is: ' +  os.path.basename(bigFile[0]) + ' at '+ str(bigFile[2])) #Print the largest file name and size

bytes_list = sorted(bytes_list, key=hiByte, reverse=True)
print(bytes_list)
sumBytes()
# f.close()

# 1000 = 1 kb
# 1,000,000 = 1 mb, 1000 kb
# 1,000,000 and 999,999,999

'''
Bytes should show 3 integers

Kilobytes should show 2
'''
