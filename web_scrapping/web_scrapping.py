import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')

for i in range(len(authors)):
    print(quotes[i].text)
    print(authors[i].text)
    quote_tags = tags[i].find_all('a', class_='tag')
    for quote_tag in quote_tags:
        print(quote_tag.text)
