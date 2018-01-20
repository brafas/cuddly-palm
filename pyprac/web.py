#! python3
import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line
    # sys.argv variable stores a list of the program's filename and command line arguments.
    # if len(sys.argv) > 1 then an argument has been provided
    address = ' '.join(sys.argv[1:]) # Joins all of the arguments into a single string.
else:
    address = pyperclip.paste()

webbrowser.open('http://www.google.com/maps/place/' + address)
