import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.etsy.com/search?q=furry")
page_soup = BeautifulSoup(page.text, "html.parser")
soup_tag = page_soup.body  # Tag, this contains all the text located within specified elements matching.
soup_tagattr = soup_tag.attrs  # returns the attributes of the tag as a dictionary.
# you can also call soup_tag['class'] or ['id'] if you want to print just that attr info.
# soup_tag.string returns the text within the tag. Not recursive.
# print(soup_tag.string)
#print(soup_tag['class'])

#  print(page_soup.find_all(_class="prolist display-inline-block listing-link logged"))
#print(page_soup.find_all('div'))

'''
<div class="js-merch-stash-check-listing block-grid-item v2-listing-card position-relative">
        
    '''

# function returns true if tag has the attribute class. If it has the attr id, then it returns false

def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')


listing_card = page_soup.find("div", class_="v2-listing-card")
listing_price = listing_card.find("p", class_="n-listing-card__price")

print(listing_card.prettify())
print(listing_price.get_text())

''' WRITE OUTPUT

text_file = open("listingcard.txt", "w")
text_file.write(listing_card.prettify())
text_file.close()
'''

'''
listingName = listings[0].find(class_="v2-listing-card__info")
# print(listingName.get_text())
# print(listings[0])
'''

''' ITERATE THROUGH FIND_ALL

for l in listings:
    price = l.find(class_="n-listing-card__price")
    print(price.get_text())
'''

''' WRITE COMMA SEPERATED FILE
with open('index.csv', 'a') as csv_file:
    writer=csv.writer(csv_file)
    writer.writerow([name, price, datetime.now()])
'''