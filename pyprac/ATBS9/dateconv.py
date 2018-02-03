import shutil, os, re

datepattern = re.compile(r"""^(.*?) # Creates a Regular Expression object, all teext before the date
                         ((0|1)?\d)-  # one or two digits for the month
                         ((0|1|2|3)?\d)-  # one or two digits for the day
                         ((19|20)\d\d)  # four digits for the year
                         (.*?)$  # all text after the date
                         """, re.VERBOSE)

# TODO: Loop over the files in the working dir
# TODO: Skip files without a date
# TODO: Get the different parts of the filenamee.
# TODO: Form the European-style filenanme.
# TODO: Get the full, absolute file paths.
# TODO: Rename the files

