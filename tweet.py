import requests
from bs4 import BeautifulSoup
from model.db_query import Query
db_obj = Query()

url = "https://twitter.com/explore"

result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')
data = soup.select('#div.class=css-1dbjc4n r-my5ep6 r-qklmqi r-1adg311')
print(data,'=======>>>data')