import requests
from bs4 import BeautifulSoup
import json
from scrape import scrape
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


urls = scrape()


def analyze_articles():
    analyzer = SentimentIntensityAnalyzer()
    list_article = []

    for i in range(len(urls)):
        article_url = urls[i]

        response = requests.get(article_url)
        content = response.content
        soup = BeautifulSoup(content, 'html.parser')

        #Search information from HTML
        title = soup.find('title').get_text()[:-11]
        descriptions = soup.find_all('p', {'class': "ssrcss-1q0x1qg-Paragraph eq5iqo00"})
        article_description = ''.join([descriptions[i].get_text() for i in range(len(descriptions))])
        sentiment = analyzer.polarity_scores(article_description)

        #Judging sentiment
        if sentiment['compound'] < -0.5:
          article_dict = {
              'title': title,
              'link': article_url,
              'description': article_description,
              'sentiment': 'negative'
          }
        else:
          article_dict = {
              'title': title,
              'link': article_url,
              'description': article_description,
              'sentiment': 'neutral/positive'
          }

        list_article.append(article_dict)

    print(f'Total number of analyzed articles: {len(list_article)}')

    with open('articles.json', 'w') as f:
        json.dump(list_article, f)

    print("JSON file saved successfully")

    return list_article

