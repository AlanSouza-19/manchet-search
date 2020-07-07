import requests
from bs4 import BeautifulSoup

r = requests.get('https://g1.globo.com/')

html_data = r.text
html = BeautifulSoup(html_data, 'html.parser')

finder = html.find_all(class_='feed-post-link gui-color-primary gui-color-hover')

for i in finder:
  print(i.get_text(), i.get('href'))
  print()
