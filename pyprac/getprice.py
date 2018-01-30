import requests
from bs4 import BeautifulSoup

pageUrl = "https://www.etsy.com/search?q=furry&explicit=1&order=date_desc"
etsypage = requests.get(pageUrl)

soup = BeautifulSoup(etsypage.text, "html.parser")

cardinfo = soup.find_all("div", class_="v2-listing-card__info")

# Write cardinfo results
file_html = open("cardinfo.html", "w")
output = cardinfo
file_html.write(str(output))
priceList = []

def getPrice():
    for elem in cardinfo:
        priceSym = elem.find("span", class_="currency-symbol")
        priceVal = elem.find("span", class_="currency-value")
        price = priceSym.get_text() + priceVal.get_text()
        priceList.append(price)
    print(priceList)
    print(str(len(priceList)) + " Entries.")

'''
def list_prettify(list):
    for i in list:
        return str(i)
text_file = open("listingcard.html", "w")
output = ''.join(map(list_prettify, listing_card))
text_file.write(output)
text_file.close()
'''
getPrice()
#make a function getprice(amnt)
# make it return amnt results. And how many available.