import requests
import flask
from bs4 import BeautifulSoup

def get_all_links(url):
    content = requests.get(url).content
    soup = BeautifulSoup(content, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        if link.has_attr('href'):
            href = link['href']
            if href and not href.startswith('#'):
                links.append(href)
    return links

if __name__ == '__main__':
    url = 'https://barbend.com'
    links = get_all_links(url)
    print(links)