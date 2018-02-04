#! python3

import zipfile, os

def backupToZip(folder):
    folder = os.path.abspath(folder) #Make sure folder is absolute

    num = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(num) + '.zip' # The basename is the last part of the path
        if not os.path.exists(zipFilename): # If it exists, Stop at break, otherwise, add 1 to num value and continue
            break
        num += 1
        print('Done')

    print('Creating %s' % zipFilename)
    backupZip = zipfile.ZipFile(zipFilename, 'w')
    # Created the zip file, now to add files to it

    for fold, subfolds, files in os.walk(folder):
        print('Adding files in %s' % fold)
        backupZip.write(fold)
        for filename in files:
            print(folder + '\\' + filename)
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(fold, filename))
        backupZip.close()


backupToZip('F:\\pyfold\\photos')