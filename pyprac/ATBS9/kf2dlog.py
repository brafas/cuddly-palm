#! python3

import zipfile, os

def backupToZip(folder):
    folder = os.path.abspath(folder) #Make sure folder is absolute

    
    #
    # num = 1
    # while True:
    #     zipFilename = os.path.basename(folder) + '_' + str(num) + '.zip'
    #     if not os.path.exists(zipFilename):
    #         break
    #     num += 1