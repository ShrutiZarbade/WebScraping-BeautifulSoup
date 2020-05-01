import requests
from bs4 import BeautifulSoup
from model.db_query import Query
db_obj = Query()

url = "https://twitter.com/TheOnion"
data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')
timeline = soup.select('#timeline li.stream-item')
all_tweet = []
for tweet in timeline:
    tweet_id = tweet['data-item-id']
    tweet_text = tweet.select('p.tweet-text')[0].get_text()
    all_tweet.append((tweet_id, tweet_text))
    data = all_tweet
    table_name = "twitter"
    db_obj.insert_many(data=data, table_name=table_name)




