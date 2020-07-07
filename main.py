import requests
from bs4 import BeautifulSoup
from database import Connection

connection = Connection()

r = requests.get('https://g1.globo.com/')

html_data = r.text
html = BeautifulSoup(html_data, 'html.parser')

finder = html.find_all(class_='feed-post-link gui-color-primary gui-color-hover')

titles: list = []
links: list = []
for i in finder:
  titles.append(i.get_text())
  links.append(i.get('href'))


connection.add(titles, links)
