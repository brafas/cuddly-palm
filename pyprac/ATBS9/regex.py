import re

print(re.split(r'\s*', 'here are some words')) # The r indicates the string will not be processed like a normal string
#* indicates 0 or more
# \s means one whitespace
# This returns a list, [here, are, some, words]
