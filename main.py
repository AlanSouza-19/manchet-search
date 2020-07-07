import requests
from bs4 import BeautifulSoup
import sqlite3
from time import sleep
# import asyncio


def addNewManchet(a:list, b: list):
  connection = sqlite3.connect('database.sqlite')
  cursor = connection.cursor()
  z = zip(a, b)

  for title, link in z:
    title = title.replace("'", "")
    cursor.execute(f"INSERT INTO manchets (title, link) VALUES ('{title}', '{link}')")
  
  connection.commit()
  connection.close()


r = requests.get('https://g1.globo.com/')

html_data = r.text
html = BeautifulSoup(html_data, 'html.parser')

finder = html.find_all(class_='feed-post-link gui-color-primary gui-color-hover')

titles: list = []
links: list = []
for i in finder:
  titles.append(i.get_text())
  links.append(i.get('href'))


addNewManchet(titles, links)
