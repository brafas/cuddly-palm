import os

# Return Human Readable file sizes, displayed next to the file name/path.
# Sort by size.
def human_Read(bytes):
    byteStr = str(bytes)
    numInts = len(byteStr)

    if bytes < 1000:
        return byteStr + ' bytes'
    elif 1000 <= bytes < 999999:
        return str(int(bytes/10e2)) + " KB"
        # return str(round(bytes, -(numInts - 2)))[:2] + " KB"
    elif numInts >= 7 and numInts < 10:
        return str(int(bytes/10e5)) + " MB"
        # byteStr = str(round(bytes, -(numInts - 3)))
        # return byteStr + ' mB'

# TODO: Put results in a list, sort by actual value, return in human readable format. Dict might work better.
# f = open("sizes.txt", 'w')

def getsize():
    path = 'F:\\Chrome Downloads 2016\\ham\\'

    for fold, subfolds, files in os.walk(path):
        for filename in files:
            # print(str(os.path.getsize(path + filename)) + ' Bytes')
            result = human_Read(os.path.getsize(path + filename))
            print(result)
            #f.write(str(os.path.getsize(path + filename)) + '\n')

getsize()

# f.close()

# 1000 = 1 kb
# 1,000,000 = 1 mb, 1000 kb
# 1,000,000 and 999,999,999

'''
Bytes should show 3 integers

Kilobytes should show 2
'''