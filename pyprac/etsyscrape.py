import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.etsy.com/search?q=furry")
# page.raise_for_status() # raises an exception if the can't load it.
page_soup = BeautifulSoup(page.text, "html.parser")

# function returns true if tag has the attribute class. If it has the attr id, then it returns false
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')


#This creates a a bs4.element.Results object.
#Essentially a list of bs4.element.Tag objects.
listing_card = page_soup.find_all("div", class_="v2-listing-card__info")


print(type(listing_card[1]))

for l in listing_card:
    title = l.find('p', class_="text-gray", recursive=False)
    priceSym =  l.find('span', class_="currency-symbol")
    priceVal = l.find('span', class_="currency-value")
    price = priceSym.get_text() + priceVal.get_text()
    print(price)
    #print(title.get_text())
print("returned: " + str(len(listing_card)))
#print(listing_card[1].get_text())
#print(listing_price.get_text())

# WRITE OUTPUT
'''
def list_prettify(list):
    for i in list:
        return str(i)
text_file = open("listingcard.html", "w")
output = ''.join(map(list_prettify, listing_card))
text_file.write(output)
text_file.close()
'''


''' ITERATE THROUGH FIND_ALL

for l in listings:
    price = l.find(class_="n-listing-card__price")
    print(price.get_text())
'''
# Should make a seperate module to write to a CSV.
''' WRITE COMMA SEPERATED FILE
with open('index.csv', 'a') as csv_file:
    writer=csv.writer(csv_file)
    writer.writerow([name, price, datetime.now()])
'''