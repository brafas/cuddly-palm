import shutil, os, re
os.chdir('F:\\pyfold\\photos')

datePattern = re.compile(r"""^(.*?) # '*' applies to preceeding token. '?' makes the preceeding quantifier lazy
# Creates a Regular Expression object, all teext before the date ~~Start of string (^), Any character except newline (.), 0 or more , 0 or 1
                         ((19|20)\d\d)-
                         ((0|1)?\d)-  # one or two digits for the month. \d One Digit. '?' digit is also optional. 
                         ((0|1|2|3)?\d)  # one or two digits for the day
                         (.*?)$  # all text after the date
                         """, re.VERBOSE)

# ^^^^ Total of 8 groups, count the amount of opening parenthesis.

filelist = os.listdir('.')

for amerForm in filelist:
    mo = datePattern.search(amerForm)

    #Skip files without date
    if mo == None:
        continue #breaks loop

    beforePart = mo.group(1)
    yearPart = mo.group(2)
    monthPart = mo.group(4)
    dayPart = mo.group(6)
    afterPart = mo.group(8)
    dateNew = beforePart + monthPart + '-' + dayPart + '-' + yearPart + afterPart

    absWorkingDir = os.path.abspath('.')
    amerFileName = os.path.join(absWorkingDir, amerForm)
    myWay = os.path.join(absWorkingDir, dateNew)

    print('%s' " is now: " '%s' % (amerFileName, myWay))

# TODO: Loop over the files in the working dir
# TODO: Skip files without a date
# TODO: Get the different parts of the filenamee.
# TODO: Form the European-style filenanme.
# TODO: Get the full, absolute file paths.
# TODO: Rename the files

