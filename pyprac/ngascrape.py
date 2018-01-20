import requests
from bs4 import BeautifulSoup 

'''Scraper for NGA.gov Z Artists
There are 6 pages Total
https://www.nga.gov/Collection/artists.html?const_startLetter=z&pageNumber=1'''

page = requests.get('https://www.nga.gov/Collection/artists.html?const_startLetter=z&pageNumber=1')
soup = BeautifulSoup(page.text, 'html.parser')

print(soup)
artist_name_list = soup.find(class_='returns')
#print(artist_name_list)