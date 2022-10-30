#Shows the price and the amount of reviews for the product

import requests, re
from bs4 import BeautifulSoup

r = requests.get("https://webscraper.io/test-sites/e-commerce/allinone/product/492").content
soup = BeautifulSoup(r, 'html.parser')
span = soup.find("h4",{"class":"pull-right price"})
price = span.text
span = soup.find("div",{"class":"ratings"})
rate = span.text
print(price)
print(rate)