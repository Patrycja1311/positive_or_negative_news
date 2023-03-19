from analyze import analyze_articles
from data_set import create_data_frame
from scrape import scrape


if __name__ == '__main__':
    scrape()
    analyze_articles()
    create_data_frame()
