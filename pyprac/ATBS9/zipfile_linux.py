import os
from os.path import expanduser
from zipfile import ZipFile
from pathlib import Path
# homedir = expanduser("~") # Works crossplatform for  < Python 3.4
homedir = str(Path.home()) # For Python 3.5+

ezip = ZipFile(homedir + "/py/cuddly-palm/pyprac/ATBS9/example.zip")

print(ezip.namelist()) # prints the tree contained in the ZIP file.

zipfo = (ezip.getinfo("spam.txt"))

print(zipfo.file_size)
print(zipfo.compress_size)
print('Compressed size is %sx smaller!' % (round(zipfo.file_size / zipfo.compress_size, 2)))
ezip.close()