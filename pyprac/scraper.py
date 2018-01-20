import requests
from bs4 import BeautifulSoup
url = 'https://assets.digitalocean.com/articles/eng_python/beautiful-soup/mockturtle.html'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser') #run page.text through BS to give you a BeautifulSoup object. This is a parse tree from the parsed page run through Python's built in html.parser
paragraphs = soup.find_all('p') # Returns all pieces of text in <p> tags. This is a list.
classes = soup.find_all(class_='chorus') # Searches for classes
specclass = soup.find_all('p', class_='chorus') #Searches for <p> elements with css class chorus. the argument id= will find html ID targets.

print(paragraphs[1].get_text()) # Prints the 2nd <p> element, get_text() removes the html tags

#  print(soup.prettify()) #Will print the nested data structure in unicode.
'''
print(str(page)) #returns <Response [200]> W3C Status Code Definitions
print(str(page.status_code)) #returns 200
print(page.text) #Text based content of web files. The <html>. page.content for the response in bytes
'''