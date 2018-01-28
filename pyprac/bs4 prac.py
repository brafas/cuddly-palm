import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.etsy.com/search?q=furry&explicit=1&order=date_desc")
# page.raise_for_status() # raises an exception if the can't load it.
page_soup = BeautifulSoup(page.text, "html.parser")
listing_card = page_soup.find_all("div", class_="v2-listing-card__info")

# print(listing_card[0].p)
print(str(listing_card[0].p.string))
