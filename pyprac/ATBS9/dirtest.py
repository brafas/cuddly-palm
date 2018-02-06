import os

path = os.path.abspath(os.pardir)
print(path)
'''
path = os.path.abspath("..") #+ os.sep # If using split(), a os.sep will return as a '' list entry.
# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk(path):
    path = root.split(os.sep) # Splits the path given by os.walk when in the root folder by the os.sep, \\ etc...
    print(path)
    print((len(path) - 1) * '---', os.path.basename(root))
    for file in files:
        print(len(path) * '---', file)
'''