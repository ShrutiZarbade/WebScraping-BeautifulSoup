import requests
from bs4 import BeautifulSoup
from model.db_query import Query
db_obj = Query()

headers = {
    "User-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/79.0.3945.130 Safari/537.36'}


def pagination(webpage, page_num):
    url = webpage + str(page_num)
    response = requests.get(str(url), headers=headers)

    all_data = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        soup_title = soup.find_all("h2", {"class": "title"})
        soup_para = soup.find_all("div", {"class": "post-content image-caption-format-1"})

        for x in range(len(soup_para)):

            link = soup_title[x].a['href']
            title = soup_title[x].a['title']
            para = soup_para[x].p.text.strip()

            all_data.append((title, link, para,))
            print(all_data)

        db_obj.insert_many(data=all_data, table_name="pagination")

        if page_num < 19:
            page_num = page_num + 1
            pagination(webpage, page_num)


pagination('https://www.opencodez.com/page/', 0)
