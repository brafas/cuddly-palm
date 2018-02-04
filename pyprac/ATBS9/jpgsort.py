import os, shutil

def copyjpg(folder):
    folder = os.path.abspath(folder)
    # abspath is now F:\Chrome Downloads 2016

    for fold, subfolders, files in os.walk(folder):
        for filename in files:
            if filename.endswith('.jpg'):
                shutil.copy(os.path.join(fold + '\\' + filename), folder + '\\imagesbackup')

copyjpg('F:\\Chrome Downloads 2016')