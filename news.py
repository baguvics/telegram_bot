import requests
from bs4 import BeautifulSoup
import random


def news_app():
    url = 'https://news.vtomske.ru/c/tomsk'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all("a", "news-small")
    try:
        news = random.choice(headlines)
        news_data = news.text.strip()
    except IndexError:
        print("No elements in news sequence")
        news_data = "Ошибка на сервере(("
    return news_data
