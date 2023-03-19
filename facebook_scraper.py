#!/usr/bin/python3
import re
import requests
from bs4 import BeautifulSoup

# specify the url
quote_page = 'https://www.google.com/'

# query the website and return the html to the variable 'page'
page = requests.get(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page.content, 'html.parser')

links = soup.find_all('a')
for link in links:
    if 'setprefs' in link.get('href'):
        print(link.text)
# regex = re.compile('.*Google offered in:*')
# price_box = soup.find('div', attrs={'class': regex})
# price = price_box
# print(price)
