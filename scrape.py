import requests
from bs4 import BeautifulSoup


def scrape():
    news_url = 'https://www.bbc.com/news'
    basic_url = 'https://www.bbc.com'
    urls_all = []
    urls = []

    response = requests.get(news_url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    articles = soup.find_all('a', {'class': "gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor"})

    # Create full urls
    for i in range(len(articles)):
        url = articles[i]['href']
        if url.startswith(basic_url):
            urls_all.append(url)
        else:
            urls_all.append(basic_url + url)

    #URL filtering with news
    for link in urls_all:
        if link[:24] == 'https://www.bbc.com/news':
            urls.append(link)

    return urls
