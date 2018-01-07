#!/usr/bin/env python

# import modules used here -- sys is a very standard one
import sys

def repeat(s, exclaim):
	"""
	This is an example of a function docstring.
	Triple Quotes are a feature unique to python.
	"""
	# Variables defined in a function are local to that function.
	result = s * 3 # or s+s+s. * 3 is also faster due to the fact it's only one calculation.
	if exclaim:
		result = result + '!!!'
	return result

# Gather our code in a main() function
def main():
	print repeat('Yay', False)
	print repeat('Woo Hoo', True)
# Standard boilerplate to call the main() function to begin
# the program.
'''
if __name__ == '__main__':
    main()
'''
