import os
# from os.path import expanduser
import zipfile
from zipfile import ZipFile
from pathlib import Path
# homedir = expanduser("~") # Works crossplatform for  < Python 3.4
homedir = str(Path.home()) # For Python 3.5+
projdir = homedir + '/py/cuddly-palm/pyprac/ATBS9/'

ezip = ZipFile(homedir + "/py/cuddly-palm/pyprac/ATBS9/new_zip.zip", 'w') #remember write mode erases all contents of a ZIP file. Use 'a' to append instead.
ezip.write(projdir + 'example_files/spam.txt', compress_type=zipfile.ZIP_DEFLATED) #Which file do you want compressed, and how would you like it compressed.
ezip.close()

