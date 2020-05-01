import requests
import bs4
url = "https://www.TimesofIndia.com/"
result = requests.get(url)
if result.status_code:
    # print(result.text)
    bs = bs4.BeautifulSoup(result.text, "html.parser")
    find_text = bs.find_all('a')
    # formatted_text= find_text.prettify()
    print(find_text)
    # with open('temp.html', 'w') as f:
    #     f.write(formatted_text)
else:
    print("this website is not for scraping")
