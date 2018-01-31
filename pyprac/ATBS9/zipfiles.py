import os
from zipfile import ZipFile

ezip = ZipFile("F:\\pyfold\\zip\example.zip")

print(ezip.namelist())