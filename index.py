import requests
from bs4 import BeautifulSoup as bs

url = 'https://barbend.com'
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_image = soup.find('h2', class_='wp-block-post-title')
print(profile_image)