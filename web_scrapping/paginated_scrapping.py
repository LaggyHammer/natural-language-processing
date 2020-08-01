import requests
from bs4 import BeautifulSoup

url = "https://scrapingclub.com/exercise/list_basic/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

count = 1
for i in items:
    item_name = i.find('h4', class_='card-title').text.strip('\n')
    item_price = i.find('h5').text

    print(f'{count}. Item: {item_name}, Price: {item_price}')
    count += 1

pages = soup.find('ul', class_='pagination')
urls = []
links = pages.find_all('a', class_='page-link')
for link in links:
    page_num = int(link.text) if link.text.isdigit() else None
    if page_num is not None:
        urls.append(link.get('href'))

print(urls)
for i in urls:
    new_url = url + i
    response = requests.get(new_url)
    soup = BeautifulSoup(response.text, 'lxml')

    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

    for j in items:
        item_name = j.find('h4', class_='card-title').text.strip('\n')
        item_price = j.find('h5').text

        print(f'{count}. Item: {item_name}, Price: {item_price}')

        count += 1
