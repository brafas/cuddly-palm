import os
from zipfile import ZipFile

ezip = ZipFile("F:\\pyfold\\zip\example.zip")

print(ezip.namelist()) # prints the tree contained in the ZIP file.

zipfo = (ezip())