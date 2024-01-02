import requests, random
from flask import Flask, redirect, url_for, render_template
from bs4 import BeautifulSoup


def get_all_links(url):
    content = requests.get(url).content
    soup = BeautifulSoup(content, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        if link.has_attr('href'):
            href = link['href']
            if href and not href.startswith('#') and href.startswith('https://barbend.com'):
                links.append(href)
    return links

app = Flask(__name__)
@app.route("/")
def home():
    url = 'https://barbend.com'
    links = get_all_links(url)
    print(random.choice(links))
    return render_template("index.html", content=random.choice(links))

if __name__ == "__main__":
    app.run()
    