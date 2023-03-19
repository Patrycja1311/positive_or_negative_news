import pandas as pd
from analyze import analyze_articles


articles = analyze_articles()


def create_data_frame():
    df = pd.DataFrame(articles)
    return df
