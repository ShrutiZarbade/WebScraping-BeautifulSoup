import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')
soup_page = soup.find_all("span", {"itemprop": "text"})